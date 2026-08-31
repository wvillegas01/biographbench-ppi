"""Run classical link-prediction heuristics on pilot PPI splits.

Baselines:
- Common Neighbors
- Jaccard
- Adamic-Adar
- Preferential Attachment

These baselines use only train positive edges to build the graph.
"""

from __future__ import annotations

import csv
import json
import math
import time
from pathlib import Path

import numpy as np
from sklearn.metrics import average_precision_score, roc_auc_score


ROOT = Path(__file__).resolve().parents[1]
RESULTS_DIR = ROOT / "results" / "raw"
REPORTS_DIR = ROOT / "reports"


DATASETS = {
    "string_human_physical_v12": ROOT / "data" / "processed" / "string_human_physical_v12",
    "biogrid_human_physical": ROOT / "data" / "processed" / "biogrid_human_physical" / "splits",
    "biogrid_human_physical_no_string_overlap": ROOT / "data" / "processed" / "biogrid_human_physical_no_string_overlap" / "splits",
    "string_human_physical_no_biogrid_overlap": ROOT / "data" / "processed" / "string_human_physical_no_biogrid_overlap" / "splits",
}

HEURISTICS = ["common_neighbors", "jaccard", "adamic_adar", "preferential_attachment"]


def edge_columns(dataset_id: str) -> tuple[str, str]:
    if dataset_id.startswith("string"):
        return "protein1", "protein2"
    return "entrez_a", "entrez_b"


def read_edges(path: Path, left_col: str, right_col: str) -> list[tuple[str, str]]:
    edges: list[tuple[str, str]] = []
    with path.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            edges.append(tuple(sorted((row[left_col], row[right_col]))))
    return edges


def build_adjacency(edges: list[tuple[str, str]]) -> dict[str, set[str]]:
    adjacency: dict[str, set[str]] = {}
    for a, b in edges:
        adjacency.setdefault(a, set()).add(b)
        adjacency.setdefault(b, set()).add(a)
    return adjacency


def score_edge(edge: tuple[str, str], adjacency: dict[str, set[str]]) -> dict[str, float]:
    a, b = edge
    neigh_a = adjacency.get(a, set())
    neigh_b = adjacency.get(b, set())
    common = neigh_a & neigh_b
    union = neigh_a | neigh_b
    common_neighbors = float(len(common))
    jaccard = float(len(common) / len(union)) if union else 0.0
    adamic_adar = 0.0
    for node in common:
        degree = len(adjacency.get(node, set()))
        if degree > 1:
            adamic_adar += 1.0 / math.log(degree)
    preferential_attachment = float(len(neigh_a) * len(neigh_b))
    return {
        "common_neighbors": common_neighbors,
        "jaccard": jaccard,
        "adamic_adar": adamic_adar,
        "preferential_attachment": preferential_attachment,
    }


def evaluate_split(
    dataset_id: str,
    split_dir: Path,
    split_name: str,
    adjacency: dict[str, set[str]],
    left_col: str,
    right_col: str,
) -> list[dict[str, object]]:
    pos = read_edges(split_dir / f"{split_name}_pos.csv", left_col, right_col)
    neg = read_edges(split_dir / f"{split_name}_neg.csv", left_col, right_col)
    labels = np.asarray([1] * len(pos) + [0] * len(neg), dtype=np.int8)
    edges = pos + neg
    scores_by_heuristic = {name: [] for name in HEURISTICS}

    start = time.perf_counter()
    for edge in edges:
        scores = score_edge(edge, adjacency)
        for name in HEURISTICS:
            scores_by_heuristic[name].append(scores[name])
    elapsed = time.perf_counter() - start

    rows: list[dict[str, object]] = []
    for name, scores in scores_by_heuristic.items():
        score_array = np.asarray(scores, dtype=np.float64)
        try:
            auroc = float(roc_auc_score(labels, score_array))
        except ValueError:
            auroc = float("nan")
        auprc = float(average_precision_score(labels, score_array))
        rows.append(
            {
                "dataset": dataset_id,
                "task": "link_prediction",
                "split": split_name,
                "model": name,
                "seed": 42,
                "num_positive": len(pos),
                "num_negative": len(neg),
                "auroc": auroc,
                "auprc": auprc,
                "runtime_seconds_all_heuristics": elapsed,
            }
        )
    return rows


def run_dataset(dataset_id: str, split_dir: Path) -> list[dict[str, object]]:
    left_col, right_col = edge_columns(dataset_id)
    train_pos = read_edges(split_dir / "train_pos.csv", left_col, right_col)
    adjacency = build_adjacency(train_pos)
    rows: list[dict[str, object]] = []
    for split_name in ["val", "test"]:
        rows.extend(evaluate_split(dataset_id, split_dir, split_name, adjacency, left_col, right_col))
    return rows


def write_outputs(rows: list[dict[str, object]]) -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    output_path = RESULTS_DIR / "link_prediction_heuristics.csv"
    fields = list(rows[0])
    with output_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)

    grouped: dict[str, list[dict[str, object]]] = {}
    for row in rows:
        grouped.setdefault(row["dataset"], []).append(row)

    lines = [
        "# Link Prediction Heuristic Baselines",
        "",
        "Fecha: 2026-08-05",
        "",
        "Baselines calculados usando solo aristas positivas de train para construir el grafo.",
        "",
        "| Dataset | Split | Modelo | AUROC | AUPRC |",
        "|---|---|---|---:|---:|",
    ]
    for row in rows:
        lines.append(
            f"| `{row['dataset']}` | `{row['split']}` | `{row['model']}` | "
            f"{row['auroc']:.6f} | {row['auprc']:.6f} |"
        )
    (REPORTS_DIR / "link_prediction_heuristics.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    (REPORTS_DIR / "link_prediction_heuristics.json").write_text(json.dumps(rows, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    rows: list[dict[str, object]] = []
    for dataset_id, split_dir in DATASETS.items():
        rows.extend(run_dataset(dataset_id, split_dir))
    write_outputs(rows)
    print(f"Wrote {len(rows)} link prediction baseline rows.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
