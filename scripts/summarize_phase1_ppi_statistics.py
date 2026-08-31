"""Summarize Phase 1 PPI multi-seed results with uncertainty and paired tests."""

from __future__ import annotations

import csv
import json
import math
from collections import defaultdict
from pathlib import Path

import numpy as np
from scipy.stats import t, wilcoxon


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "results" / "phase1" / "ppi_link_prediction_baselines.csv"
REPORTS_DIR = ROOT / "reports"


def as_float(value: str) -> float:
    return float(value) if value != "" else float("nan")


def read_rows() -> list[dict[str, str]]:
    with INPUT.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def mean_ci(values: list[float]) -> dict[str, float]:
    arr = np.asarray(values, dtype=float)
    arr = arr[np.isfinite(arr)]
    n = int(arr.size)
    if n == 0:
        return {"n": 0, "mean": float("nan"), "sd": float("nan"), "ci95_low": float("nan"), "ci95_high": float("nan")}
    mean = float(np.mean(arr))
    sd = float(np.std(arr, ddof=1)) if n > 1 else 0.0
    if n > 1:
        half = float(t.ppf(0.975, df=n - 1) * sd / math.sqrt(n))
    else:
        half = float("nan")
    return {"n": n, "mean": mean, "sd": sd, "ci95_low": mean - half, "ci95_high": mean + half}


def paired_stats(left: list[float], right: list[float]) -> dict[str, float]:
    left_arr = np.asarray(left, dtype=float)
    right_arr = np.asarray(right, dtype=float)
    mask = np.isfinite(left_arr) & np.isfinite(right_arr)
    diff = left_arr[mask] - right_arr[mask]
    n = int(diff.size)
    if n < 2:
        return {"n": n, "mean_diff": float(np.mean(diff)) if n else float("nan"), "wilcoxon_p": float("nan"), "cohen_dz": float("nan")}
    try:
        p_value = float(wilcoxon(diff).pvalue)
    except ValueError:
        p_value = 1.0
    sd = float(np.std(diff, ddof=1))
    dz = float(np.mean(diff) / sd) if sd > 0 else float("inf")
    return {"n": n, "mean_diff": float(np.mean(diff)), "wilcoxon_p": p_value, "cohen_dz": dz}


def main() -> int:
    rows = [row for row in read_rows() if row["split"] == "test"]

    summary_rows: list[dict[str, object]] = []
    grouped: dict[tuple[str, str, str], list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        grouped[(row["dataset"], row["negative_strategy"], row["model"])].append(row)

    for (dataset, strategy, model), group in sorted(grouped.items()):
        auroc = mean_ci([as_float(row["auroc"]) for row in group])
        auprc = mean_ci([as_float(row["auprc"]) for row in group])
        summary_rows.append(
            {
                "dataset": dataset,
                "negative_strategy": strategy,
                "model": model,
                "n": auprc["n"],
                "auroc_mean": auroc["mean"],
                "auroc_sd": auroc["sd"],
                "auroc_ci95_low": auroc["ci95_low"],
                "auroc_ci95_high": auroc["ci95_high"],
                "auprc_mean": auprc["mean"],
                "auprc_sd": auprc["sd"],
                "auprc_ci95_low": auprc["ci95_low"],
                "auprc_ci95_high": auprc["ci95_high"],
            }
        )

    paired_rows: list[dict[str, object]] = []
    by_context_model: dict[tuple[str, str, str], dict[int, float]] = defaultdict(dict)
    for row in rows:
        by_context_model[(row["dataset"], row["negative_strategy"], row["model"])][int(row["seed"])] = as_float(row["auprc"])

    contexts = sorted({(row["dataset"], row["negative_strategy"]) for row in rows})
    for dataset, strategy in contexts:
        reference = by_context_model.get((dataset, strategy, "hist_gradient_boosting"), {})
        if not reference:
            continue
        for model in sorted({row["model"] for row in rows if row["dataset"] == dataset and row["negative_strategy"] == strategy}):
            if model == "hist_gradient_boosting":
                continue
            candidate = by_context_model[(dataset, strategy, model)]
            seeds = sorted(set(reference) & set(candidate))
            stats = paired_stats([reference[s] for s in seeds], [candidate[s] for s in seeds])
            paired_rows.append(
                {
                    "dataset": dataset,
                    "negative_strategy": strategy,
                    "reference": "hist_gradient_boosting",
                    "candidate": model,
                    "metric": "test_auprc",
                    **stats,
                }
            )

    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    output = {"summary": summary_rows, "paired_tests": paired_rows}
    (REPORTS_DIR / "phase1_ppi_statistics.json").write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")

    lines = [
        "# Phase 1 PPI Statistics",
        "",
        "## Test AUPRC Summary",
        "",
        "| Dataset | Negatives | Model | n | AUPRC mean | SD | CI95 low | CI95 high |",
        "|---|---|---|---:|---:|---:|---:|---:|",
    ]
    for row in summary_rows:
        lines.append(
            f"| `{row['dataset']}` | `{row['negative_strategy']}` | `{row['model']}` | {row['n']} | "
            f"{row['auprc_mean']:.6f} | {row['auprc_sd']:.6f} | {row['auprc_ci95_low']:.6f} | {row['auprc_ci95_high']:.6f} |"
        )
    lines.extend(
        [
            "",
            "## Paired Tests Against HGB",
            "",
            "| Dataset | Negatives | Candidate | n | Mean delta AUPRC | Wilcoxon p | Cohen dz |",
            "|---|---|---|---:|---:|---:|---:|",
        ]
    )
    for row in paired_rows:
        lines.append(
            f"| `{row['dataset']}` | `{row['negative_strategy']}` | `{row['candidate']}` | {row['n']} | "
            f"{row['mean_diff']:.6f} | {row['wilcoxon_p']:.6g} | {row['cohen_dz']:.6f} |"
        )
    (REPORTS_DIR / "phase1_ppi_statistics.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote statistics for {len(summary_rows)} model summaries and {len(paired_rows)} paired tests.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
