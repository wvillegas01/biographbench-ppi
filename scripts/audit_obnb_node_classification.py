"""Audit OBNB candidates for node classification.

Candidates:
- BioGRID + GOBP
- STRING + GOBP

The script builds/loads OBNB archived data version obnbdata-0.1.0 and records
graph, label, and split statistics without training models.
"""

from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path

import numpy as np
from obnb.dataset import OpenBiomedNetBench


ROOT = Path(__file__).resolve().parents[1]
OBNB_ROOT = ROOT / "data" / "obnb"
REPORTS_DIR = ROOT / "reports"
VERSION = "obnbdata-0.1.0"

CANDIDATES = [
    ("BioGRID", "GOBP"),
    ("STRING", "GOBP"),
]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def file_info(path: Path) -> dict[str, object]:
    return {
        "path": str(path),
        "size_bytes": path.stat().st_size if path.exists() else 0,
        "sha256": sha256(path) if path.exists() else "",
    }


def audit_candidate(graph_name: str, label_name: str) -> dict[str, object]:
    dataset = OpenBiomedNetBench(
        root=str(OBNB_ROOT),
        graph_name=graph_name,
        label_name=label_name,
        version=VERSION,
        graph_as_feature=False,
    )

    y = dataset.y
    y_mask = dataset.y_mask.astype(bool)
    labels_per_task = np.asarray(dataset.label.sizes)
    positives_per_task = y.sum(axis=0)
    observed_per_task = y_mask.sum(axis=0)
    negatives_per_task = observed_per_task - positives_per_task

    split_counts = {}
    split_positive_counts = {}
    for split, mask in dataset.masks.items():
        split_mask = mask.astype(bool).reshape(-1)
        split_counts[split] = int(split_mask.sum())
        split_positive_counts[split] = int(y[split_mask, :].sum())

    graph_file = OBNB_ROOT / graph_name / "processed" / "data.npz"
    label_file = OBNB_ROOT / label_name / "processed" / "data.gmt"

    return {
        "dataset_id": f"obnb_{graph_name.lower()}_{label_name.lower()}",
        "graph_name": graph_name,
        "label_name": label_name,
        "version": dataset.version,
        "graph_nodes": int(dataset.graph.num_nodes),
        "graph_edges": int(dataset.graph.num_edges),
        "directed": bool(dataset.graph.directed),
        "weighted": bool(dataset.graph.weighted),
        "label_tasks": int(dataset.label.size),
        "dataset_nodes": int(dataset.size),
        "labeled_entities": int(len(dataset.label.entity_ids)),
        "y_shape": list(y.shape),
        "y_positive_total": int(y.sum()),
        "y_mask_observed_total": int(y_mask.sum()),
        "min_task_positives": int(positives_per_task.min()),
        "median_task_positives": float(np.median(positives_per_task)),
        "max_task_positives": int(positives_per_task.max()),
        "min_task_negatives": int(negatives_per_task.min()),
        "median_task_negatives": float(np.median(negatives_per_task)),
        "max_task_negatives": int(negatives_per_task.max()),
        "split_counts": split_counts,
        "split_positive_counts": split_positive_counts,
        "splitter": str(dataset.splitter),
        "first_label_ids": list(dataset.label.label_ids[:10]),
        "graph_file": file_info(graph_file),
        "label_file": file_info(label_file),
    }


def write_reports(results: list[dict[str, object]]) -> None:
    json_path = REPORTS_DIR / "obnb_node_classification_audit.json"
    json_path.write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")

    csv_path = REPORTS_DIR / "obnb_node_classification_audit.csv"
    fields = [
        "dataset_id",
        "graph_name",
        "label_name",
        "version",
        "graph_nodes",
        "graph_edges",
        "directed",
        "weighted",
        "label_tasks",
        "labeled_entities",
        "y_positive_total",
        "y_mask_observed_total",
        "min_task_positives",
        "median_task_positives",
        "max_task_positives",
        "min_task_negatives",
        "median_task_negatives",
        "max_task_negatives",
        "splitter",
    ]
    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for result in results:
            writer.writerow({field: result[field] for field in fields})

    lines = [
        "# OBNB Node Classification Audit",
        "",
        "Fecha: 2026-08-04",
        "",
        "## Objetivo",
        "",
        "Seleccionar un primer candidato reproducible para cubrir node classification en BioGraphBench.",
        "",
        "OBNB se audita con version archivada `obnbdata-0.1.0`, sin entrenar modelos.",
        "",
        "## Candidatos",
        "",
        "| Dataset | Nodos | Aristas | Weighted | Tareas | Entidades etiquetadas | Positivos | Observados | Split train/val/test |",
        "|---|---:|---:|---|---:|---:|---:|---:|---|",
    ]
    for result in results:
        split = result["split_counts"]
        lines.append(
            f"| `{result['dataset_id']}` | {result['graph_nodes']} | {result['graph_edges']} | "
            f"{result['weighted']} | {result['label_tasks']} | {result['labeled_entities']} | "
            f"{result['y_positive_total']} | {result['y_mask_observed_total']} | "
            f"{split.get('train')}/{split.get('val')}/{split.get('test')} |"
        )

    lines.extend(
        [
            "",
            "## Licencia y procedencia",
            "",
            "- OBNB package: MIT, segun repositorio `krishnanlab/obnb`.",
            "- OBNB archived data: `obnbdata-0.1.0` via Zenodo record usado por OBNB.",
            "- GOBP/Gene Ontology: GO data products are CC BY 4.0, segun Gene Ontology citation policy.",
            "- BioGRID: MIT, ya auditado en la fase PPI.",
            "- STRING: CC BY 4.0, ya auditado en la fase PPI.",
            "",
            "Fuentes:",
            "",
            "- https://github.com/krishnanlab/obnb",
            "- https://proceedings.mlr.press/v240/liu24a.html",
            "- https://geneontology.org/docs/go-citation-policy/",
            "",
            "## Decision recomendada",
            "",
            "Usar `obnb_biogrid_gobp` como primer piloto de node classification.",
            "",
            "Motivos:",
            "",
            "1. Es homogeneo, no ponderado y comparable conceptualmente con la red BioGRID PPI ya auditada.",
            "2. Tiene 114 tareas GO Biological Process despues de filtros OBNB.",
            "3. Usa split study-bias 6/2/2, mas interesante que un split aleatorio simple.",
            "4. Evita iniciar con DisGeNET, cuya licencia/version debe auditarse con mas cuidado.",
            "",
            "Mantener `obnb_string_gobp` como comparador secundario, pero recordar que STRING ya tiene alto solapamiento biologico con BioGRID.",
            "",
            "## Riesgos abiertos",
            "",
            "- OBNB no reemplaza nuestra auditoria de leakage; hay que documentar exactamente como se generan negativos y masks.",
            "- `graph_as_feature=False` no incluye features iniciales; para baselines/GNN se debe definir una politica de features, por ejemplo one-hot log degree.",
            "- Las tareas GO son multietiqueta/multitarea; las metricas deben priorizar AUPRC, micro/macro-F1 y calibracion por tarea.",
        ]
    )
    (REPORTS_DIR / "obnb_node_classification_audit.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    results = [audit_candidate(graph, label) for graph, label in CANDIDATES]
    write_reports(results)
    for result in results:
        print(
            f"{result['dataset_id']}: {result['graph_nodes']} nodes, "
            f"{result['graph_edges']} edges, {result['label_tasks']} tasks"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
