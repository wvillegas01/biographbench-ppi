"""Tune per-task decision thresholds for node-classification outputs.

This script retrains/loads the current lightweight node-classification models,
computes validation probabilities, selects per-task thresholds that maximize F1
on validation, and reports calibrated-threshold metrics on validation/test.

Models:
- logistic_regression with one_hot_log_degree
- mlp with one_hot_log_degree
- gcn with one_hot_log_degree
"""

from __future__ import annotations

import csv
import json
import time
from pathlib import Path

import numpy as np
import torch
from obnb.dataset import OpenBiomedNetBench
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import average_precision_score, f1_score, precision_score, recall_score, roc_auc_score
from sklearn.multiclass import OneVsRestClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


ROOT = Path(__file__).resolve().parents[1]
OBNB_ROOT = ROOT / "data" / "obnb"
DATA_DIR = ROOT / "data" / "processed" / "obnb_biogrid_gobp"
RESULTS_DIR = ROOT / "results" / "raw"
REPORTS_DIR = ROOT / "reports"

VERSION = "obnbdata-0.1.0"
GRAPH_NAME = "BioGRID"
LABEL_NAME = "GOBP"
SEED = 42
EPOCHS = 200
PATIENCE = 25
HIDDEN_DIM = 64
LEARNING_RATE = 0.01
WEIGHT_DECAY = 5e-4
THRESHOLDS = np.linspace(0.01, 0.99, 99)


def set_seed(seed: int) -> None:
    np.random.seed(seed)
    torch.manual_seed(seed)


def safe_macro_auroc(y_true: np.ndarray, y_score: np.ndarray) -> float:
    values = []
    for idx in range(y_true.shape[1]):
        labels = y_true[:, idx]
        if len(np.unique(labels)) < 2:
            continue
        values.append(roc_auc_score(labels, y_score[:, idx]))
    return float(np.mean(values)) if values else float("nan")


def safe_macro_auprc(y_true: np.ndarray, y_score: np.ndarray) -> float:
    values = []
    for idx in range(y_true.shape[1]):
        labels = y_true[:, idx]
        if labels.sum() == 0:
            continue
        values.append(average_precision_score(labels, y_score[:, idx]))
    return float(np.mean(values)) if values else float("nan")


def tune_thresholds(y_val: np.ndarray, p_val: np.ndarray) -> np.ndarray:
    thresholds = np.full(y_val.shape[1], 0.5, dtype=np.float64)
    for task_idx in range(y_val.shape[1]):
        labels = y_val[:, task_idx]
        if labels.sum() == 0:
            continue
        best_threshold = 0.5
        best_f1 = -1.0
        scores = p_val[:, task_idx]
        for threshold in THRESHOLDS:
            pred = (scores >= threshold).astype(np.int8)
            f1 = f1_score(labels, pred, zero_division=0)
            if f1 > best_f1:
                best_f1 = f1
                best_threshold = float(threshold)
        thresholds[task_idx] = best_threshold
    return thresholds


def threshold_metrics(y_true: np.ndarray, p: np.ndarray, thresholds: np.ndarray) -> dict[str, float]:
    pred = (p >= thresholds.reshape(1, -1)).astype(np.int8)
    return {
        "macro_auroc": safe_macro_auroc(y_true, p),
        "macro_auprc": safe_macro_auprc(y_true, p),
        "micro_f1": float(f1_score(y_true.ravel(), pred.ravel(), zero_division=0)),
        "macro_f1": float(f1_score(y_true, pred, average="macro", zero_division=0)),
        "micro_precision": float(precision_score(y_true.ravel(), pred.ravel(), zero_division=0)),
        "micro_recall": float(recall_score(y_true.ravel(), pred.ravel(), zero_division=0)),
    }


class MLP(torch.nn.Module):
    def __init__(self, in_dim: int, hidden_dim: int, out_dim: int) -> None:
        super().__init__()
        self.net = torch.nn.Sequential(
            torch.nn.Linear(in_dim, hidden_dim),
            torch.nn.ReLU(),
            torch.nn.Dropout(0.3),
            torch.nn.Linear(hidden_dim, out_dim),
        )

    def forward(self, x: torch.Tensor, adjacency: torch.Tensor | None = None) -> torch.Tensor:
        return self.net(x)


class GCN(torch.nn.Module):
    def __init__(self, in_dim: int, hidden_dim: int, out_dim: int) -> None:
        super().__init__()
        self.lin1 = torch.nn.Linear(in_dim, hidden_dim)
        self.lin2 = torch.nn.Linear(hidden_dim, out_dim)
        self.dropout = torch.nn.Dropout(0.3)

    def forward(self, x: torch.Tensor, adjacency: torch.Tensor | None = None) -> torch.Tensor:
        if adjacency is None:
            raise ValueError("GCN requires adjacency.")
        h = torch.sparse.mm(adjacency, x)
        h = self.lin1(h)
        h = torch.relu(h)
        h = self.dropout(h)
        h = torch.sparse.mm(adjacency, h)
        return self.lin2(h)


def build_normalized_adjacency(device: torch.device) -> torch.Tensor:
    dataset = OpenBiomedNetBench(
        root=str(OBNB_ROOT),
        graph_name=GRAPH_NAME,
        label_name=LABEL_NAME,
        version=VERSION,
        graph_as_feature=False,
    )
    edge_index, _ = dataset.graph.to_coo()
    edge_index = np.asarray(edge_index, dtype=np.int64)
    num_nodes = dataset.graph.num_nodes
    rows = np.concatenate([edge_index[0], np.arange(num_nodes, dtype=np.int64)])
    cols = np.concatenate([edge_index[1], np.arange(num_nodes, dtype=np.int64)])
    values = np.ones(rows.shape[0], dtype=np.float32)
    degree = np.bincount(rows, weights=values, minlength=num_nodes).astype(np.float32)
    degree_inv_sqrt = np.power(degree, -0.5, where=degree > 0)
    degree_inv_sqrt[degree == 0] = 0.0
    norm_values = degree_inv_sqrt[rows] * values * degree_inv_sqrt[cols]
    indices = torch.tensor(np.vstack([rows, cols]), dtype=torch.long, device=device)
    vals = torch.tensor(norm_values, dtype=torch.float32, device=device)
    return torch.sparse_coo_tensor(indices, vals, (num_nodes, num_nodes), device=device).coalesce()


def masked_bce_loss(logits: torch.Tensor, y: torch.Tensor, mask: torch.Tensor) -> torch.Tensor:
    loss = torch.nn.functional.binary_cross_entropy_with_logits(logits, y, reduction="none")
    masked = loss * mask.float()
    return masked.sum() / mask.float().sum().clamp_min(1.0)


def load_arrays() -> dict[str, np.ndarray]:
    arrays = np.load(DATA_DIR / "node_classification_arrays.npz", allow_pickle=False)
    features = np.load(DATA_DIR / "features.npz", allow_pickle=False)
    return {
        "x": features["one_hot_log_degree"].astype(np.float32),
        "y": arrays["y"].astype(np.int8),
        "y_mask": arrays["y_mask"].astype(bool),
        "train_mask": arrays["train_mask"].astype(bool),
        "val_mask": arrays["val_mask"].astype(bool),
        "test_mask": arrays["test_mask"].astype(bool),
    }


def train_logistic(data: dict[str, np.ndarray]) -> dict[str, object]:
    train = data["train_mask"]
    model = OneVsRestClassifier(
        make_pipeline(
            StandardScaler(),
            LogisticRegression(
                solver="liblinear",
                class_weight="balanced",
                max_iter=1000,
                random_state=SEED,
            ),
        )
    )
    start = time.perf_counter()
    model.fit(data["x"][train], data["y"][train])
    train_seconds = time.perf_counter() - start
    return {
        "model": "logistic_regression",
        "train_seconds": train_seconds,
        "val_prob": model.predict_proba(data["x"][data["val_mask"]]),
        "test_prob": model.predict_proba(data["x"][data["test_mask"]]),
    }


@torch.no_grad()
def model_prob(model: torch.nn.Module, x: torch.Tensor, adjacency: torch.Tensor | None) -> np.ndarray:
    model.eval()
    return torch.sigmoid(model(x, adjacency)).detach().cpu().numpy()


def train_neural(data: dict[str, np.ndarray], model_name: str, device: torch.device) -> dict[str, object]:
    set_seed(SEED)
    x = torch.tensor(data["x"], dtype=torch.float32, device=device)
    y = torch.tensor(data["y"], dtype=torch.float32, device=device)
    y_mask = torch.tensor(data["y_mask"], dtype=torch.bool, device=device)
    train_mask = torch.tensor(data["train_mask"], dtype=torch.bool, device=device)
    val_mask = torch.tensor(data["val_mask"], dtype=torch.bool, device=device)

    adjacency = build_normalized_adjacency(device) if model_name == "gcn" else None
    if model_name == "mlp":
        model: torch.nn.Module = MLP(x.shape[1], HIDDEN_DIM, y.shape[1]).to(device)
    elif model_name == "gcn":
        model = GCN(x.shape[1], HIDDEN_DIM, y.shape[1]).to(device)
    else:
        raise ValueError(model_name)

    optimizer = torch.optim.Adam(model.parameters(), lr=LEARNING_RATE, weight_decay=WEIGHT_DECAY)
    train_label_mask = y_mask & train_mask[:, None]
    best_state = None
    best_val = -float("inf")
    best_epoch = 0
    stale = 0
    start = time.perf_counter()
    for epoch in range(1, EPOCHS + 1):
        model.train()
        optimizer.zero_grad()
        logits = model(x, adjacency)
        loss = masked_bce_loss(logits, y, train_label_mask)
        loss.backward()
        optimizer.step()
        p_val = model_prob(model, x, adjacency)[data["val_mask"]]
        val_auprc = safe_macro_auprc(data["y"][data["val_mask"]], p_val)
        if val_auprc > best_val:
            best_val = val_auprc
            best_epoch = epoch
            best_state = {key: value.detach().cpu().clone() for key, value in model.state_dict().items()}
            stale = 0
        else:
            stale += 1
        if stale >= PATIENCE:
            break
    train_seconds = time.perf_counter() - start
    if best_state is not None:
        model.load_state_dict(best_state)
    all_prob = model_prob(model, x, adjacency)
    return {
        "model": model_name,
        "best_epoch": best_epoch,
        "train_seconds": train_seconds,
        "val_prob": all_prob[data["val_mask"]],
        "test_prob": all_prob[data["test_mask"]],
    }


def run() -> list[dict[str, object]]:
    data = load_arrays()
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    fitted = [
        train_logistic(data),
        train_neural(data, "mlp", device),
        train_neural(data, "gcn", device),
    ]
    rows: list[dict[str, object]] = []
    y_val = data["y"][data["val_mask"]]
    y_test = data["y"][data["test_mask"]]
    for result in fitted:
        thresholds = tune_thresholds(y_val, result["val_prob"])
        for split, y_true, prob in [("val", y_val, result["val_prob"]), ("test", y_test, result["test_prob"])]:
            metrics = threshold_metrics(y_true, prob, thresholds)
            rows.append(
                {
                    "dataset": "obnb_biogrid_gobp",
                    "task": "node_classification",
                    "split": split,
                    "model": result["model"],
                    "feature": "one_hot_log_degree",
                    "seed": SEED,
                    "best_epoch": result.get("best_epoch", ""),
                    "threshold_strategy": "per_task_val_f1",
                    "threshold_min": float(thresholds.min()),
                    "threshold_median": float(np.median(thresholds)),
                    "threshold_max": float(thresholds.max()),
                    "macro_auroc": metrics["macro_auroc"],
                    "macro_auprc": metrics["macro_auprc"],
                    "micro_f1": metrics["micro_f1"],
                    "macro_f1": metrics["macro_f1"],
                    "micro_precision": metrics["micro_precision"],
                    "micro_recall": metrics["micro_recall"],
                    "train_seconds": result["train_seconds"],
                }
            )
    return rows


def write_outputs(rows: list[dict[str, object]]) -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    csv_path = RESULTS_DIR / "node_classification_threshold_tuning.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

    lines = [
        "# Node Classification Threshold Tuning",
        "",
        "Fecha: 2026-08-05",
        "",
        "Umbrales por tarea seleccionados en validation para maximizar F1 y aplicados a test.",
        "",
        "| Modelo | Split | Macro AUROC | Macro AUPRC | Micro-F1 | Macro-F1 | Precision | Recall | Threshold median |",
        "|---|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            f"| `{row['model']}` | `{row['split']}` | {row['macro_auroc']:.6f} | "
            f"{row['macro_auprc']:.6f} | {row['micro_f1']:.6f} | {row['macro_f1']:.6f} | "
            f"{row['micro_precision']:.6f} | {row['micro_recall']:.6f} | {row['threshold_median']:.4f} |"
        )
    (REPORTS_DIR / "node_classification_threshold_tuning.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    (REPORTS_DIR / "node_classification_threshold_tuning.json").write_text(json.dumps(rows, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    rows = run()
    write_outputs(rows)
    print(f"Wrote {len(rows)} threshold-tuned node classification rows.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
