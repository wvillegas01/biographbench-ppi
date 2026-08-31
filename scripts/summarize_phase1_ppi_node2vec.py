"""Summarize Phase 1 node2vec-compatible random-walk baseline."""

from __future__ import annotations

import csv
import json
import math
from collections import defaultdict
from pathlib import Path

import numpy as np
from scipy.stats import t, wilcoxon


ROOT = Path(__file__).resolve().parents[1]
NODE2VEC_INPUT = ROOT / "results" / "phase1" / "ppi_node2vec_link_prediction.csv"
CLASSICAL_INPUT = ROOT / "results" / "phase1" / "ppi_link_prediction_baselines.csv"
REPORTS_DIR = ROOT / "reports"


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def mean_ci(values: list[float]) -> dict[str, float]:
    arr = np.asarray(values, dtype=float)
    n = int(arr.size)
    mean = float(np.mean(arr)) if n else float("nan")
    sd = float(np.std(arr, ddof=1)) if n > 1 else 0.0
    half = float(t.ppf(0.975, df=n - 1) * sd / math.sqrt(n)) if n > 1 else float("nan")
    return {"n": n, "mean": mean, "sd": sd, "ci95_low": mean - half, "ci95_high": mean + half}


def paired_diff(reference: dict[int, float], candidate: dict[int, float]) -> dict[str, float]:
    seeds = sorted(set(reference) & set(candidate))
    diff = np.asarray([reference[s] - candidate[s] for s in seeds], dtype=float)
    n = int(diff.size)
    if n < 2:
        return {"n": n, "mean_diff": float(np.mean(diff)) if n else float("nan"), "wilcoxon_p": float("nan"), "cohen_dz": float("nan")}
    try:
        p_value = float(wilcoxon(diff).pvalue)
    except ValueError:
        p_value = 1.0
    sd = float(np.std(diff, ddof=1))
    return {
        "n": n,
        "mean_diff": float(np.mean(diff)),
        "wilcoxon_p": p_value,
        "cohen_dz": float(np.mean(diff) / sd) if sd > 0 else float("inf"),
    }


def main() -> int:
    node_rows = [r for r in read_csv(NODE2VEC_INPUT) if r["split"] == "test"]
    classical_rows = [r for r in read_csv(CLASSICAL_INPUT) if r["split"] == "test"]

    grouped: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    for row in node_rows:
        grouped[(row["dataset"], row["negative_strategy"])].append(row)

    summaries = []
    for (dataset, strategy), rows in sorted(grouped.items()):
        auprc = mean_ci([float(r["auprc"]) for r in rows])
        auroc = mean_ci([float(r["auroc"]) for r in rows])
        summaries.append(
            {
                "dataset": dataset,
                "negative_strategy": strategy,
                "model": "node2vec_walk_logreg",
                "n": auprc["n"],
                "auroc_mean": auroc["mean"],
                "auroc_sd": auroc["sd"],
                "auprc_mean": auprc["mean"],
                "auprc_sd": auprc["sd"],
                "auprc_ci95_low": auprc["ci95_low"],
                "auprc_ci95_high": auprc["ci95_high"],
            }
        )

    values: dict[tuple[str, str, str], dict[int, float]] = defaultdict(dict)
    for row in classical_rows:
        values[(row["dataset"], row["negative_strategy"], row["model"])][int(row["seed"])] = float(row["auprc"])
    for row in node_rows:
        values[(row["dataset"], row["negative_strategy"], "node2vec_walk_logreg")][int(row["seed"])] = float(row["auprc"])

    paired = []
    for summary in summaries:
        dataset = summary["dataset"]
        strategy = summary["negative_strategy"]
        node = values[(dataset, strategy, "node2vec_walk_logreg")]
        for reference_model in ["hist_gradient_boosting", "random_forest", "logistic_regression"]:
            reference = values.get((dataset, strategy, reference_model), {})
            if not reference:
                continue
            paired.append(
                {
                    "dataset": dataset,
                    "negative_strategy": strategy,
                    "reference": reference_model,
                    "candidate": "node2vec_walk_logreg",
                    **paired_diff(reference, node),
                }
            )

    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    output = {"summary": summaries, "paired_tests": paired}
    (REPORTS_DIR / "phase1_ppi_node2vec_statistics.json").write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")

    lines = [
        "# Phase 1 node2vec-compatible Baseline Statistics",
        "",
        "| Dataset | Negatives | n | AUROC mean | AUPRC mean | SD | CI95 low | CI95 high |",
        "|---|---|---:|---:|---:|---:|---:|---:|",
    ]
    for row in summaries:
        lines.append(
            f"| `{row['dataset']}` | `{row['negative_strategy']}` | {row['n']} | "
            f"{row['auroc_mean']:.6f} | {row['auprc_mean']:.6f} | {row['auprc_sd']:.6f} | "
            f"{row['auprc_ci95_low']:.6f} | {row['auprc_ci95_high']:.6f} |"
        )
    lines.extend(["", "## Paired AUPRC Differences: Reference minus node2vec", "", "| Dataset | Negatives | Reference | n | Mean diff | Wilcoxon p | Cohen dz |", "|---|---|---|---:|---:|---:|---:|"])
    for row in paired:
        lines.append(
            f"| `{row['dataset']}` | `{row['negative_strategy']}` | `{row['reference']}` | {row['n']} | "
            f"{row['mean_diff']:.6f} | {row['wilcoxon_p']:.6g} | {row['cohen_dz']:.6f} |"
        )
    (REPORTS_DIR / "phase1_ppi_node2vec_statistics.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {len(summaries)} node2vec summaries and {len(paired)} paired tests.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
