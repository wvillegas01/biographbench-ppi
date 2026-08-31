"""Run supervised classical link-prediction baselines on PPI pilot splits.

Pair features are computed from the train-positive graph only:
- common_neighbors
- jaccard
- adamic_adar
- preferential_attachment
- degree_u
- degree_v
- abs_degree_diff
- degree_product

Models:
- LogisticRegression
- RandomForestClassifier
- HistGradientBoostingClassifier
"""

from __future__ import annotations

import csv
import json
import math
import time
from pathlib import Path

import numpy as np
from sklearn.ensemble import HistGradientBoostingClassifier, RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import average_precision_score, brier_score_loss, log_loss, roc_auc_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


ROOT = Path(__file__).resolve().parents[1]
RESULTS_DIR = ROOT / "results" / "raw"
REPORTS_DIR = ROOT / "reports"

DATASETS = {
    "string_human_physical_v12": ROOT / "data" / "processed" / "string_human_physical_v12",
    "biogrid_human_physical": ROOT / "data" / "processed" / "biogrid_human_physical" / "splits",
    "biogrid_human_physical_no_string_overlap": ROOT / "data" / "processed" / "biogrid_human_physical_no_string_overlap" / "splits",
    "string_human_physical_no_biogrid_overlap": ROOT / "data" / "processed" / "string_human_physical_no_biogrid_overlap" / "splits",
}


def edge_columns(dataset_id: str) -> tuple[str, str]:
    return ("protein1", "protein2") if dataset_id.startswith("string") else ("entrez_a", "entrez_b")


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


def edge_features(edge: tuple[str, str], adjacency: dict[str, set[str]]) -> list[float]:
    a, b = edge
    neigh_a = adjacency.get(a, set())
    neigh_b = adjacency.get(b, set())
    deg_a = len(neigh_a)
    deg_b = len(neigh_b)
    common = neigh_a & neigh_b
    union = neigh_a | neigh_b
    common_neighbors = float(len(common))
    jaccard = float(len(common) / len(union)) if union else 0.0
    adamic_adar = 0.0
    for node in common:
        degree = len(adjacency.get(node, set()))
        if degree > 1:
            adamic_adar += 1.0 / math.log(degree)
    preferential_attachment = float(deg_a * deg_b)
    return [
        common_neighbors,
        jaccard,
        adamic_adar,
        preferential_attachment,
        float(deg_a),
        float(deg_b),
        float(abs(deg_a - deg_b)),
        float(deg_a * deg_b),
    ]


def build_matrix(
    pos_edges: list[tuple[str, str]],
    neg_edges: list[tuple[str, str]],
    adjacency: dict[str, set[str]],
) -> tuple[np.ndarray, np.ndarray]:
    edges = pos_edges + neg_edges
    x = np.asarray([edge_features(edge, adjacency) for edge in edges], dtype=np.float64)
    y = np.asarray([1] * len(pos_edges) + [0] * len(neg_edges), dtype=np.int8)
    return x, y


def expected_calibration_error(y_true: np.ndarray, y_prob: np.ndarray, n_bins: int = 10) -> float:
    bins = np.linspace(0.0, 1.0, n_bins + 1)
    ece = 0.0
    for left, right in zip(bins[:-1], bins[1:]):
        if right == 1.0:
            mask = (y_prob >= left) & (y_prob <= right)
        else:
            mask = (y_prob >= left) & (y_prob < right)
        if not np.any(mask):
            continue
        confidence = float(np.mean(y_prob[mask]))
        accuracy = float(np.mean(y_true[mask]))
        ece += float(np.mean(mask)) * abs(confidence - accuracy)
    return ece


def make_models() -> dict[str, object]:
    return {
        "logistic_regression": make_pipeline(
            StandardScaler(),
            LogisticRegression(max_iter=1000, class_weight="balanced", random_state=42),
        ),
        "random_forest": RandomForestClassifier(
            n_estimators=200,
            max_depth=16,
            min_samples_leaf=5,
            n_jobs=-1,
            class_weight="balanced_subsample",
            random_state=42,
        ),
        "hist_gradient_boosting": HistGradientBoostingClassifier(
            max_iter=200,
            learning_rate=0.05,
            max_leaf_nodes=31,
            l2_regularization=0.01,
            random_state=42,
        ),
    }


def run_dataset(dataset_id: str, split_dir: Path) -> list[dict[str, object]]:
    left_col, right_col = edge_columns(dataset_id)
    train_pos = read_edges(split_dir / "train_pos.csv", left_col, right_col)
    train_neg = read_edges(split_dir / "train_neg.csv", left_col, right_col)
    adjacency = build_adjacency(train_pos)

    x_train, y_train = build_matrix(train_pos, train_neg, adjacency)
    eval_data = {}
    for split in ["val", "test"]:
        pos = read_edges(split_dir / f"{split}_pos.csv", left_col, right_col)
        neg = read_edges(split_dir / f"{split}_neg.csv", left_col, right_col)
        eval_data[split] = build_matrix(pos, neg, adjacency)

    rows: list[dict[str, object]] = []
    for model_name, model in make_models().items():
        start = time.perf_counter()
        model.fit(x_train, y_train)
        train_seconds = time.perf_counter() - start

        for split, (x_eval, y_eval) in eval_data.items():
            start = time.perf_counter()
            y_prob = model.predict_proba(x_eval)[:, 1]
            inference_seconds = time.perf_counter() - start
            rows.append(
                {
                    "dataset": dataset_id,
                    "task": "link_prediction",
                    "split": split,
                    "model": model_name,
                    "feature_set": "train_graph_pair_heuristics",
                    "seed": 42,
                    "num_train": int(y_train.shape[0]),
                    "num_eval": int(y_eval.shape[0]),
                    "auroc": float(roc_auc_score(y_eval, y_prob)),
                    "auprc": float(average_precision_score(y_eval, y_prob)),
                    "brier": float(brier_score_loss(y_eval, y_prob)),
                    "nll": float(log_loss(y_eval, y_prob, labels=[0, 1])),
                    "ece_10": expected_calibration_error(y_eval, y_prob, n_bins=10),
                    "train_seconds": train_seconds,
                    "inference_seconds": inference_seconds,
                }
            )
    return rows


def write_outputs(rows: list[dict[str, object]]) -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    csv_path = RESULTS_DIR / "link_prediction_supervised.csv"
    fields = list(rows[0])
    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)

    lines = [
        "# Supervised Link Prediction Baselines",
        "",
        "Fecha: 2026-08-05",
        "",
        "Features de pares calculadas solo desde el grafo positivo de train.",
        "",
        "| Dataset | Split | Modelo | AUROC | AUPRC | Brier | ECE-10 |",
        "|---|---|---|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            f"| `{row['dataset']}` | `{row['split']}` | `{row['model']}` | "
            f"{row['auroc']:.6f} | {row['auprc']:.6f} | {row['brier']:.6f} | {row['ece_10']:.6f} |"
        )
    (REPORTS_DIR / "link_prediction_supervised.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    (REPORTS_DIR / "link_prediction_supervised.json").write_text(json.dumps(rows, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    rows: list[dict[str, object]] = []
    for dataset_id, split_dir in DATASETS.items():
        rows.extend(run_dataset(dataset_id, split_dir))
    write_outputs(rows)
    print(f"Wrote {len(rows)} supervised link prediction rows.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
