"""Build manuscript-oriented summaries for Phase 1 PPI results."""

from __future__ import annotations

import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPORTS_DIR = ROOT / "reports"
ARTICLE_DIR = ROOT / "Articulo"
STATS_PATH = REPORTS_DIR / "phase1_ppi_statistics.json"
NODE2VEC_STATS_PATH = REPORTS_DIR / "phase1_ppi_node2vec_statistics.json"


def main() -> int:
    stats = json.loads(STATS_PATH.read_text(encoding="utf-8"))
    summary = stats["summary"]
    node2vec_summary = []
    if NODE2VEC_STATS_PATH.exists():
        node2vec_summary = json.loads(NODE2VEC_STATS_PATH.read_text(encoding="utf-8"))["summary"]

    by_key = {(r["dataset"], r["negative_strategy"], r["model"]): r for r in summary}
    node2vec_by_key = {
        (r["dataset"], r["negative_strategy"]): r for r in node2vec_summary
    }
    datasets = sorted({r["dataset"] for r in summary})
    rows = []
    for dataset in datasets:
        hgb_random = by_key.get((dataset, "random", "hist_gradient_boosting"))
        hgb_degree = by_key.get((dataset, "degree_matched", "hist_gradient_boosting"))
        rf_random = by_key.get((dataset, "random", "random_forest"))
        rf_degree = by_key.get((dataset, "degree_matched", "random_forest"))
        node2vec_random = node2vec_by_key.get((dataset, "random"))
        node2vec_degree = node2vec_by_key.get((dataset, "degree_matched"))
        if not hgb_random or not hgb_degree:
            continue
        random_mean = float(hgb_random["auprc_mean"])
        degree_mean = float(hgb_degree["auprc_mean"])
        drop = random_mean - degree_mean
        rows.append(
            {
                "dataset": dataset,
                "hgb_random_auprc_mean": random_mean,
                "hgb_random_auprc_sd": float(hgb_random["auprc_sd"]),
                "hgb_degree_matched_auprc_mean": degree_mean,
                "hgb_degree_matched_auprc_sd": float(hgb_degree["auprc_sd"]),
                "hgb_absolute_drop": drop,
                "hgb_relative_drop_percent": 100.0 * drop / random_mean,
                "rf_random_auprc_mean": "" if not rf_random else float(rf_random["auprc_mean"]),
                "rf_degree_matched_auprc_mean": "" if not rf_degree else float(rf_degree["auprc_mean"]),
                "node2vec_random_auprc_mean": ""
                if not node2vec_random
                else float(node2vec_random["auprc_mean"]),
                "node2vec_degree_matched_auprc_mean": ""
                if not node2vec_degree
                else float(node2vec_degree["auprc_mean"]),
            }
        )

    ARTICLE_DIR.mkdir(parents=True, exist_ok=True)
    csv_path = ARTICLE_DIR / "phase1_ppi_negative_sampling_impact.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

    lines = [
        "# Phase 1 PPI Negative-Sampling Impact",
        "",
        "All values are test AUPRC means over 10 seeds. Degree-matched negatives preserve an approximate endpoint degree-bin distribution of positive pairs.",
        "",
        "| Dataset | HGB random | HGB degree-matched | Absolute drop | Relative drop | RF random | RF degree-matched |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            f"| `{row['dataset']}` | {row['hgb_random_auprc_mean']:.6f} | "
            f"{row['hgb_degree_matched_auprc_mean']:.6f} | {row['hgb_absolute_drop']:.6f} | "
            f"{row['hgb_relative_drop_percent']:.1f}% | {row['rf_random_auprc_mean']:.6f} | "
            f"{row['rf_degree_matched_auprc_mean']:.6f} |"
        )
    lines.extend(
        [
            "",
            "## Manuscript Takeaway",
            "",
            "Across all four PPI tasks, replacing uniformly sampled random negatives with degree-matched negatives reduced HGB test AUPRC. "
            "The reduction was modest for STRING without BioGRID but substantial for BioGRID tasks, especially BioGRID without STRING. "
            "This directly supports the revised article thesis: high PPI link-prediction performance under balanced random negatives partly reflects topological separability induced by the negative-sampling protocol.",
        ]
    )
    md_path = ARTICLE_DIR / "phase1_ppi_negative_sampling_impact.md"
    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    if node2vec_summary:
        model_lines = [
            "# Phase 1 PPI Model-Family Comparison",
            "",
            "All values are test AUPRC means over 10 seeds. The node2vec-compatible baseline uses auditable random-walk embeddings with a logistic edge decoder.",
            "",
            "| Dataset | Negatives | Logistic regression | Random forest | HGB | node2vec-compatible |",
            "|---|---|---:|---:|---:|---:|",
        ]
        strategies = sorted({r["negative_strategy"] for r in summary})
        for dataset in datasets:
            for strategy in strategies:
                logreg = by_key.get((dataset, strategy, "logistic_regression"))
                rf = by_key.get((dataset, strategy, "random_forest"))
                hgb = by_key.get((dataset, strategy, "hist_gradient_boosting"))
                node2vec = node2vec_by_key.get((dataset, strategy))
                if not all([logreg, rf, hgb, node2vec]):
                    continue
                model_lines.append(
                    f"| `{dataset}` | `{strategy}` | {float(logreg['auprc_mean']):.6f} | "
                    f"{float(rf['auprc_mean']):.6f} | {float(hgb['auprc_mean']):.6f} | "
                    f"{float(node2vec['auprc_mean']):.6f} |"
                )
        model_lines.extend(
            [
                "",
                "## Manuscript Takeaway",
                "",
                "The added random-walk baseline strengthens the comparison because it does not rely only on local handcrafted edge scores. "
                "HGB and RF remain strongest in most STRING and complete BioGRID settings, but node2vec-compatible embeddings become competitive under the harder BioGRID no-STRING degree-matched regime. "
                "This pattern supports a focused PPI article: model rankings are conditional on the graph source and negative-sampling contract, not merely on the nominal task definition.",
            ]
        )
        model_md_path = ARTICLE_DIR / "phase1_ppi_model_family_comparison.md"
        model_md_path.write_text("\n".join(model_lines) + "\n", encoding="utf-8")
        model_csv_path = ARTICLE_DIR / "phase1_ppi_model_family_comparison.csv"
        model_rows = []
        for dataset in datasets:
            for strategy in strategies:
                logreg = by_key.get((dataset, strategy, "logistic_regression"))
                rf = by_key.get((dataset, strategy, "random_forest"))
                hgb = by_key.get((dataset, strategy, "hist_gradient_boosting"))
                node2vec = node2vec_by_key.get((dataset, strategy))
                if not all([logreg, rf, hgb, node2vec]):
                    continue
                model_rows.append(
                    {
                        "dataset": dataset,
                        "negative_strategy": strategy,
                        "logistic_regression_auprc_mean": float(logreg["auprc_mean"]),
                        "random_forest_auprc_mean": float(rf["auprc_mean"]),
                        "hist_gradient_boosting_auprc_mean": float(hgb["auprc_mean"]),
                        "node2vec_compatible_auprc_mean": float(node2vec["auprc_mean"]),
                    }
                )
        with model_csv_path.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(model_rows[0]))
            writer.writeheader()
            writer.writerows(model_rows)
        print(f"Wrote {model_md_path}")
        print(f"Wrote {model_csv_path}")
    print(f"Wrote {csv_path}")
    print(f"Wrote {md_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
