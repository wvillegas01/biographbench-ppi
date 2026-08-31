"""Build a compact baseline summary report."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS_DIR = ROOT / "results" / "raw"
REPORTS_DIR = ROOT / "reports"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def main() -> int:
    link_rows = read_csv(RESULTS_DIR / "link_prediction_heuristics.csv")
    supervised_rows = read_csv(RESULTS_DIR / "link_prediction_supervised.csv")
    node_rows = read_csv(RESULTS_DIR / "node_classification_logreg.csv")
    node_gnn_path = RESULTS_DIR / "node_classification_gnn.csv"
    node_gnn_rows = read_csv(node_gnn_path) if node_gnn_path.exists() else []
    node_threshold_path = RESULTS_DIR / "node_classification_threshold_tuning.csv"
    node_threshold_rows = read_csv(node_threshold_path) if node_threshold_path.exists() else []

    best_link = {}
    for row in link_rows + supervised_rows:
        if row["split"] != "test":
            continue
        current = best_link.get(row["dataset"])
        if current is None or float(row["auprc"]) > float(current["auprc"]):
            best_link[row["dataset"]] = row

    best_node = {}
    for row in node_rows + node_gnn_rows:
        if row["split"] != "test":
            continue
        current = best_node.get(row["dataset"])
        if current is None or float(row["macro_auprc"]) > float(current["macro_auprc"]):
            best_node[row["dataset"]] = row

    best_node_f1 = {}
    for row in node_threshold_rows:
        if row["split"] != "test":
            continue
        current = best_node_f1.get(row["dataset"])
        if current is None or float(row["micro_f1"]) > float(current["micro_f1"]):
            best_node_f1[row["dataset"]] = row

    lines = [
        "# Baseline Summary",
        "",
        "Fecha: 2026-08-05",
        "",
        "## Link Prediction",
        "",
        "| Dataset | Mejor baseline test | AUROC | AUPRC |",
        "|---|---|---:|---:|",
    ]
    for dataset, row in best_link.items():
        lines.append(
            f"| `{dataset}` | `{row['model']}` | {float(row['auroc']):.6f} | {float(row['auprc']):.6f} |"
        )

    lines.extend(
        [
            "",
            "## Node Classification",
            "",
            "| Dataset | Mejor feature test | Macro AUROC | Macro AUPRC | Micro-F1 |",
            "|---|---|---:|---:|---:|",
        ]
    )
    for dataset, row in best_node.items():
        descriptor = row.get("feature") or row.get("model")
        if row.get("model") and row.get("feature"):
            descriptor = f"{row['model']} / {row['feature']}"
        lines.append(
            f"| `{dataset}` | `{descriptor}` | {float(row['macro_auroc']):.6f} | "
            f"{float(row['macro_auprc']):.6f} | {float(row['micro_f1']):.6f} |"
        )

    if best_node_f1:
        lines.extend(
            [
                "",
                "## Node Classification Threshold-Tuned F1",
                "",
                "| Dataset | Mejor modelo test | Micro-F1 | Macro-F1 | Precision | Recall |",
                "|---|---|---:|---:|---:|---:|",
            ]
        )
        for dataset, row in best_node_f1.items():
            lines.append(
                f"| `{dataset}` | `{row['model']}` | {float(row['micro_f1']):.6f} | "
                f"{float(row['macro_f1']):.6f} | {float(row['micro_precision']):.6f} | "
                f"{float(row['micro_recall']):.6f} |"
            )

    lines.extend(
        [
            "",
            "## Lectura",
            "",
            "- Las heuristicas clasicas son fuertes en PPI, especialmente Adamic-Adar y Preferential Attachment segun dataset.",
            "- Los modelos supervisados sobre heuristicas mejoran la vara inicial y ya reportan calibracion basica.",
            "- Esto confirma que cualquier GNN debe compararse contra baselines estructurales y supervisados serios.",
            "- En node classification, `one_hot_log_degree` mejora el control constante, pero sigue siendo debil; eso deja espacio para modelos que usen propagacion/estructura de forma mas rica.",
            "- El GCN piloto mejora macro-AUPRC frente a logistic regression, pero no resuelve aun el desbalance ni el umbral de decision; debe tratarse como prueba inicial de infraestructura, no como resultado final.",
            "- El tuning de umbrales por tarea recupera F1 distinto de cero y expone el trade-off precision/recall; logistic regression queda mejor en micro-F1 test, mientras GCN conserva mejor macro-AUPRC.",
        ]
    )

    (REPORTS_DIR / "baseline_summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {REPORTS_DIR / 'baseline_summary.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
