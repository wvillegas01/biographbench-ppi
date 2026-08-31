"""Build consolidated MVP status reports for BioGraphBench audit."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPORTS_DIR = ROOT / "reports"
RESULTS_DIR = ROOT / "results" / "raw"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def dataset_matrix() -> list[dict[str, str]]:
    rows = read_csv(REPORTS_DIR / "dataset_audit.csv")
    selected_ids = {
        "string_human_physical_v12",
        "biogrid_human",
        "biogrid_human_physical_no_string_overlap",
        "string_human_physical_no_biogrid_overlap",
        "obnb_biogrid_gobp",
        "openbiolink2020_hq_directed",
    }
    output = []
    for row in rows:
        if row["dataset_id"] not in selected_ids:
            continue
        output.append(
            {
                "dataset_id": row["dataset_id"],
                "task": row["label_type"],
                "graph_type": row["graph_type"],
                "nodes": row["number_of_nodes"],
                "edges_or_classes": row["number_of_edges"] if row["number_of_edges"] not in {"", "Unknown", "NA"} else row["number_of_classes"],
                "download_status": row["download_status"],
                "preprocessing_status": row["preprocessing_status"],
                "eligible": row["eligible"],
                "main_risk": row["exclusion_reason"],
            }
        )
    return output


def model_matrix() -> list[dict[str, str]]:
    output = []
    if (RESULTS_DIR / "link_prediction_heuristics.csv").exists():
        for row in read_csv(RESULTS_DIR / "link_prediction_heuristics.csv"):
            if row["split"] == "test":
                output.append(
                    {
                        "task": "link_prediction",
                        "dataset": row["dataset"],
                        "model": row["model"],
                        "feature_or_input": "train_graph_heuristic",
                        "auroc": row["auroc"],
                        "auprc": row["auprc"],
                        "primary_note": "classical unsupervised heuristic",
                    }
                )
    if (RESULTS_DIR / "link_prediction_supervised.csv").exists():
        for row in read_csv(RESULTS_DIR / "link_prediction_supervised.csv"):
            if row["split"] == "test":
                output.append(
                    {
                        "task": "link_prediction",
                        "dataset": row["dataset"],
                        "model": row["model"],
                        "feature_or_input": row["feature_set"],
                        "auroc": row["auroc"],
                        "auprc": row["auprc"],
                        "primary_note": f"Brier={float(row['brier']):.4f}; ECE10={float(row['ece_10']):.4f}",
                    }
                )
    if (RESULTS_DIR / "node_classification_logreg.csv").exists():
        for row in read_csv(RESULTS_DIR / "node_classification_logreg.csv"):
            if row["split"] == "test":
                output.append(
                    {
                        "task": "node_classification",
                        "dataset": row["dataset"],
                        "model": row["model"],
                        "feature_or_input": row["feature"],
                        "auroc": row["macro_auroc"],
                        "auprc": row["macro_auprc"],
                        "primary_note": f"micro_f1={float(row['micro_f1']):.4f}",
                    }
                )
    if (RESULTS_DIR / "node_classification_gnn.csv").exists():
        for row in read_csv(RESULTS_DIR / "node_classification_gnn.csv"):
            if row["split"] == "test":
                output.append(
                    {
                        "task": "node_classification",
                        "dataset": row["dataset"],
                        "model": row["model"],
                        "feature_or_input": row["feature"],
                        "auroc": row["macro_auroc"],
                        "auprc": row["macro_auprc"],
                        "primary_note": f"micro_f1@0.5={float(row['micro_f1']):.4f}",
                    }
                )
    if (RESULTS_DIR / "node_classification_threshold_tuning.csv").exists():
        for row in read_csv(RESULTS_DIR / "node_classification_threshold_tuning.csv"):
            if row["split"] == "test":
                output.append(
                    {
                        "task": "node_classification_threshold_tuned",
                        "dataset": row["dataset"],
                        "model": row["model"],
                        "feature_or_input": f"{row['feature']} + {row['threshold_strategy']}",
                        "auroc": row["macro_auroc"],
                        "auprc": row["macro_auprc"],
                        "primary_note": f"micro_f1={float(row['micro_f1']):.4f}; recall={float(row['micro_recall']):.4f}",
                    }
                )
    return output


def best_rows(model_rows: list[dict[str, str]]) -> list[dict[str, str]]:
    best: dict[tuple[str, str], dict[str, str]] = {}
    for row in model_rows:
        key = (row["task"], row["dataset"])
        if row["task"] == "node_classification_threshold_tuned":
            current = best.get(key)
            current_f1 = -1.0
            if current is not None and "micro_f1=" in current["primary_note"]:
                try:
                    current_f1 = float(current["primary_note"].split("micro_f1=")[1].split(";")[0])
                except ValueError:
                    current_f1 = -1.0
            try:
                row_f1 = float(row["primary_note"].split("micro_f1=")[1].split(";")[0])
            except ValueError:
                row_f1 = -1.0
            if current is None or row_f1 > current_f1:
                best[key] = row
            continue
        current = best.get(key)
        if current is None or float(row["auprc"]) > float(current["auprc"]):
            best[key] = row
    return list(best.values())


def make_markdown(dataset_rows: list[dict[str, str]], model_rows: list[dict[str, str]]) -> str:
    best = best_rows(model_rows)
    lines = [
        "# BioGraphBench MVP Status Report",
        "",
        "Fecha: 2026-08-05",
        "",
        "## Principio rector",
        "",
        "> BioGraphBench no empieza con modelos; empieza con confianza.",
        "",
        "Este MVP ya tiene una base auditable para dos tareas: link prediction y node classification. Incluye descargas con hashes, inspeccion de datos, filtrado, splits validados, features iniciales, baselines clasicos, modelos supervisados y un GNN piloto.",
        "",
        "## Datasets y estado",
        "",
        "| Dataset | Tarea | Tipo | Nodos | Aristas/clases | Estado | Riesgo principal |",
        "|---|---|---|---:|---:|---|---|",
    ]
    for row in dataset_rows:
        lines.append(
            f"| `{row['dataset_id']}` | `{row['task']}` | `{row['graph_type']}` | "
            f"{row['nodes']} | {row['edges_or_classes']} | `{row['eligible']}` | {row['main_risk']} |"
        )

    lines.extend(
        [
            "",
            "## Mejores resultados iniciales",
            "",
            "| Tarea | Dataset | Modelo | Input/features | AUROC | AUPRC | Nota |",
            "|---|---|---|---|---:|---:|---|",
        ]
    )
    for row in best:
        lines.append(
            f"| `{row['task']}` | `{row['dataset']}` | `{row['model']}` | `{row['feature_or_input']}` | "
            f"{float(row['auroc']):.6f} | {float(row['auprc']):.6f} | {row['primary_note']} |"
        )

    lines.extend(
        [
            "",
            "## Lo que ya esta cubierto",
            "",
            "- Descarga reproducible de STRING, BioGRID, OpenBioLink y OBNB.",
            "- Auditoria de datasets existentes y gap analysis.",
            "- Link prediction en STRING y BioGRID.",
            "- Node classification en OBNB BioGRID+GOBP.",
            "- Splits positivos/negativos sin overlap para PPI.",
            "- Ablaciones de solapamiento STRING/BioGRID.",
            "- Features iniciales para node classification.",
            "- Baselines heuristicas, supervisados y GNN piloto.",
            "- Calibracion basica en link prediction supervisado: Brier, NLL y ECE-10.",
            "- Threshold tuning por tarea para node classification.",
            "",
            "## Hallazgos importantes",
            "",
            "- STRING y BioGRID tienen alto solapamiento biologico: 423,528 pares Entrez compartidos.",
            "- Las heuristicas clasicas en PPI son muy fuertes; cualquier GNN debe compararse contra ellas.",
            "- Los modelos supervisados sobre heuristicas elevan aun mas la vara en link prediction.",
            "- Node classification es mucho mas dificil y desbalanceado; AUPRC y threshold tuning son mas informativos que F1 con umbral 0.5.",
            "- El GCN piloto prueba infraestructura, pero aun no es un resultado final competitivo.",
            "",
            "## Riesgos abiertos",
            "",
            "- OpenBioLink requiere revision semantica de relaciones inversas antes de aceptarlo como KG principal.",
            "- OGB `ogbl-biokg` esta verificado para descarga, pero aun no cargado/procesado localmente.",
            "- Falta robustez, escalabilidad, interpretabilidad y estadistica con multiples semillas.",
            "- Las features biologicas externas no deben incorporarse sin auditoria de licencia y leakage temporal.",
            "- El MVP actual usa una semilla principal; el protocolo final necesita 5-10 semillas segun fase.",
            "",
            "## Decision",
            "",
            "El MVP auditado esta listo para convertirse en un repositorio benchmark inicial. La siguiente fase ya puede moverse desde `Auditoria` hacia una estructura de paquete reproducible, conservando estos reportes como evidencia.",
        ]
    )
    return "\n".join(lines) + "\n"


def make_next_steps() -> str:
    return """# Next Steps

Fecha: 2026-08-05

## Prioridad 1

1. Convertir `Auditoria` en esqueleto de paquete `biographbench`.
2. Congelar entorno: `pyproject.toml`, `requirements-lock.txt` o `environment.yml`.
3. Mover scripts estables a modulos versionados.
4. Crear tests formales para leakage, splits, features y metricas.
5. Ejecutar 5 semillas en baselines principales.

## Prioridad 2

1. Cargar y auditar `ogbl-biokg`.
2. Resolver OpenBioLink inverse-relation review.
3. Implementar GCN/GraphSAGE/APPNP de forma modular.
4. Agregar calibracion posterior: temperature scaling o isotonic cuando aplique.
5. Agregar curvas de robustez iniciales para STRING/BioGRID.

## Prioridad 3

1. Interpretabilidad: GNNExplainer/Integrated Gradients cuando haya GNNs estables.
2. Escalabilidad: fracciones 10/25/50/75/100%.
3. Analisis estadistico con multiples semillas.
4. Figuras reproducibles.
"""


def main() -> int:
    dataset_rows = dataset_matrix()
    model_rows = model_matrix()
    write_csv(
        REPORTS_DIR / "dataset_readiness_matrix.csv",
        dataset_rows,
        ["dataset_id", "task", "graph_type", "nodes", "edges_or_classes", "download_status", "preprocessing_status", "eligible", "main_risk"],
    )
    write_csv(
        REPORTS_DIR / "model_baseline_matrix.csv",
        model_rows,
        ["task", "dataset", "model", "feature_or_input", "auroc", "auprc", "primary_note"],
    )
    (REPORTS_DIR / "mvp_status_report.md").write_text(make_markdown(dataset_rows, model_rows), encoding="utf-8")
    (REPORTS_DIR / "next_steps.md").write_text(make_next_steps(), encoding="utf-8")
    print("Wrote MVP status reports.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
