"""Run a minimal node-classification baseline on OBNB BioGRID+GOBP.

Model:
- One-vs-Rest logistic regression

Features:
- constant
- one_hot_log_degree

The baseline trains only on train nodes and reports validation/test metrics.
"""

from __future__ import annotations

import csv
import json
import time
from pathlib import Path

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import average_precision_score, f1_score, roc_auc_score
from sklearn.multiclass import OneVsRestClassifier


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data" / "processed" / "obnb_biogrid_gobp"
RESULTS_DIR = ROOT / "results" / "raw"
REPORTS_DIR = ROOT / "reports"

FEATURES = ["constant", "one_hot_log_degree"]


def safe_macro_auroc(y_true: np.ndarray, y_score: np.ndarray) -> float:
    valid = []
    for idx in range(y_true.shape[1]):
        labels = y_true[:, idx]
        if len(np.unique(labels)) < 2:
            continue
        valid.append(roc_auc_score(labels, y_score[:, idx]))
    return float(np.mean(valid)) if valid else float("nan")


def safe_macro_auprc(y_true: np.ndarray, y_score: np.ndarray) -> float:
    scores = []
    for idx in range(y_true.shape[1]):
        labels = y_true[:, idx]
        if labels.sum() == 0:
            continue
        scores.append(average_precision_score(labels, y_score[:, idx]))
    return float(np.mean(scores)) if scores else float("nan")


def run_feature(feature_name: str) -> list[dict[str, object]]:
    arrays = np.load(DATA_DIR / "node_classification_arrays.npz", allow_pickle=False)
    features = np.load(DATA_DIR / "features.npz", allow_pickle=False)
    x = features[feature_name].astype(np.float64)
    y = arrays["y"].astype(np.int8)
    y_mask = arrays["y_mask"].astype(bool)
    train_mask = arrays["train_mask"].astype(bool)
    val_mask = arrays["val_mask"].astype(bool)
    test_mask = arrays["test_mask"].astype(bool)

    # OBNB has a common node split but task-specific observed labels. Training
    # uses unobserved labels as 0 only where y_mask marks them observed.
    train_observed = train_mask & y_mask.any(axis=1)
    x_train = x[train_observed]
    y_train = y[train_observed]

    model = OneVsRestClassifier(
        LogisticRegression(
            solver="liblinear",
            class_weight="balanced",
            max_iter=1000,
            random_state=42,
        )
    )
    start = time.perf_counter()
    model.fit(x_train, y_train)
    train_seconds = time.perf_counter() - start

    rows = []
    for split_name, mask in [("val", val_mask), ("test", test_mask)]:
        x_split = x[mask]
        y_split = y[mask]
        score = model.predict_proba(x_split)
        pred = (score >= 0.5).astype(np.int8)
        rows.append(
            {
                "dataset": "obnb_biogrid_gobp",
                "task": "node_classification",
                "split": split_name,
                "model": "one_vs_rest_logistic_regression",
                "feature": feature_name,
                "seed": 42,
                "num_nodes": int(mask.sum()),
                "num_tasks": int(y.shape[1]),
                "macro_auroc": safe_macro_auroc(y_split, score),
                "macro_auprc": safe_macro_auprc(y_split, score),
                "micro_f1": float(f1_score(y_split.ravel(), pred.ravel(), zero_division=0)),
                "macro_f1": float(f1_score(y_split, pred, average="macro", zero_division=0)),
                "train_seconds": train_seconds,
            }
        )
    return rows


def write_outputs(rows: list[dict[str, object]]) -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    csv_path = RESULTS_DIR / "node_classification_logreg.csv"
    fields = list(rows[0])
    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)

    lines = [
        "# Node Classification Logistic Regression Baseline",
        "",
        "Fecha: 2026-08-05",
        "",
        "| Feature | Split | Macro AUROC | Macro AUPRC | Micro-F1 | Macro-F1 |",
        "|---|---|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            f"| `{row['feature']}` | `{row['split']}` | {row['macro_auroc']:.6f} | "
            f"{row['macro_auprc']:.6f} | {row['micro_f1']:.6f} | {row['macro_f1']:.6f} |"
        )
    (REPORTS_DIR / "node_classification_logreg.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    (REPORTS_DIR / "node_classification_logreg.json").write_text(json.dumps(rows, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    rows: list[dict[str, object]] = []
    for feature in FEATURES:
        rows.extend(run_feature(feature))
    write_outputs(rows)
    print(f"Wrote {len(rows)} node classification baseline rows.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
