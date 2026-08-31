"""Export the selected OBNB BioGRID+GOBP node-classification pilot.

This creates a lightweight, framework-agnostic artifact under:
data/processed/obnb_biogrid_gobp/

The export keeps OBNB as the source of truth while making masks, labels and
metadata explicit for BioGraphBench auditing.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path

import numpy as np
from obnb.dataset import OpenBiomedNetBench


ROOT = Path(__file__).resolve().parents[1]
OBNB_ROOT = ROOT / "data" / "obnb"
OUT_DIR = ROOT / "data" / "processed" / "obnb_biogrid_gobp"
REPORTS_DIR = ROOT / "reports"

VERSION = "obnbdata-0.1.0"
GRAPH_NAME = "BioGRID"
LABEL_NAME = "GOBP"


def export() -> dict[str, object]:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    dataset = OpenBiomedNetBench(
        root=str(OBNB_ROOT),
        graph_name=GRAPH_NAME,
        label_name=LABEL_NAME,
        version=VERSION,
        graph_as_feature=False,
    )

    y = dataset.y.astype(np.int8)
    y_mask = dataset.y_mask.astype(bool)
    masks = {name: mask.astype(bool).reshape(-1) for name, mask in dataset.masks.items()}
    node_ids = np.asarray(dataset.graph.node_ids, dtype=str)
    label_ids = np.asarray(dataset.label.label_ids, dtype=str)

    np.savez_compressed(
        OUT_DIR / "node_classification_arrays.npz",
        y=y,
        y_mask=y_mask,
        train_mask=masks["train"],
        val_mask=masks["val"],
        test_mask=masks["test"],
        node_ids=node_ids,
        label_ids=label_ids,
    )

    with (OUT_DIR / "nodes.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["node_index", "gene_id"])
        writer.writeheader()
        for idx, gene_id in enumerate(node_ids):
            writer.writerow({"node_index": idx, "gene_id": gene_id})

    with (OUT_DIR / "labels.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["label_index", "go_id", "positive_count"])
        writer.writeheader()
        positives_per_task = y.sum(axis=0)
        for idx, go_id in enumerate(label_ids):
            writer.writerow(
                {
                    "label_index": idx,
                    "go_id": go_id,
                    "positive_count": int(positives_per_task[idx]),
                }
            )

    split_counts = {name: int(mask.sum()) for name, mask in masks.items()}
    split_positive_counts = {name: int(y[mask, :].sum()) for name, mask in masks.items()}
    positives_per_task = y.sum(axis=0)
    observed_per_task = y_mask.sum(axis=0)
    negatives_per_task = observed_per_task - positives_per_task

    manifest = {
        "dataset_id": "obnb_biogrid_gobp",
        "source": "Open Biomedical Network Benchmark",
        "obnb_root": str(OBNB_ROOT),
        "version": dataset.version,
        "graph_name": GRAPH_NAME,
        "label_name": LABEL_NAME,
        "graph_nodes": int(dataset.graph.num_nodes),
        "graph_edges": int(dataset.graph.num_edges),
        "directed": bool(dataset.graph.directed),
        "weighted": bool(dataset.graph.weighted),
        "label_tasks": int(dataset.label.size),
        "y_shape": list(y.shape),
        "y_mask_shape": list(y_mask.shape),
        "total_positive_labels": int(y.sum()),
        "total_observed_labels": int(y_mask.sum()),
        "split_counts": split_counts,
        "split_positive_counts": split_positive_counts,
        "min_task_positives": int(positives_per_task.min()),
        "median_task_positives": float(np.median(positives_per_task)),
        "max_task_positives": int(positives_per_task.max()),
        "min_task_negatives": int(negatives_per_task.min()),
        "median_task_negatives": float(np.median(negatives_per_task)),
        "max_task_negatives": int(negatives_per_task.max()),
        "splitter": str(dataset.splitter),
        "feature_policy": "not_exported_yet; recommended initial feature OneHotLogDeg or graph-as-feature baseline",
        "output_dir": str(OUT_DIR),
    }
    (OUT_DIR / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return manifest


def write_report(manifest: dict[str, object]) -> None:
    md = f"""# OBNB BioGRID+GOBP Export

Fecha: 2026-08-04

## Objetivo

Exportar el candidato recomendado de node classification a un artefacto local explicito para BioGraphBench.

## Conteos

| Medida | Valor |
|---|---:|
| Nodos | {manifest['graph_nodes']} |
| Aristas | {manifest['graph_edges']} |
| Tareas GO BP | {manifest['label_tasks']} |
| Labels positivos totales | {manifest['total_positive_labels']} |
| Labels observados totales | {manifest['total_observed_labels']} |
| Train nodes | {manifest['split_counts']['train']} |
| Val nodes | {manifest['split_counts']['val']} |
| Test nodes | {manifest['split_counts']['test']} |
| Positivos min/med/max por tarea | {manifest['min_task_positives']} / {manifest['median_task_positives']} / {manifest['max_task_positives']} |
| Negativos min/med/max por tarea | {manifest['min_task_negatives']} / {manifest['median_task_negatives']} / {manifest['max_task_negatives']} |

## Split

`{manifest['splitter']}`

OBNB usa un split study-bias 6/2/2 basado en PubMedCount: train contiene genes mas estudiados, test genes menos estudiados y validation el resto.

## Archivos generados

- `node_classification_arrays.npz`
- `nodes.csv`
- `labels.csv`
- `manifest.json`

## Decision

Este artefacto ya permite implementar baselines de node classification. Falta definir politica de features antes de entrenar: no usar informacion derivada de validation/test para features estructurales.
"""
    (REPORTS_DIR / "obnb_biogrid_gobp_export.md").write_text(md, encoding="utf-8")
    (REPORTS_DIR / "obnb_biogrid_gobp_export.json").write_text(
        json.dumps(manifest, indent=2) + "\n",
        encoding="utf-8",
    )


def main() -> int:
    manifest = export()
    write_report(manifest)
    print(
        "OBNB BioGRID+GOBP exported: "
        f"{manifest['graph_nodes']} nodes, "
        f"{manifest['label_tasks']} tasks"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
