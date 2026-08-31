"""Run pilot neural baselines for OBNB BioGRID+GOBP node classification.

Models:
- MLP over one_hot_log_degree features
- 2-layer GCN implemented with torch sparse matrix multiplication

This is intentionally a pilot, not the final GNN benchmark. It verifies that
the audited node-classification artifact can support train/val/test neural
experiments without PyG.
"""

from __future__ import annotations

import csv
import json
import time
from pathlib import Path

import numpy as np
import torch
from obnb.dataset import OpenBiomedNetBench
from sklearn.metrics import average_precision_score, f1_score, roc_auc_score


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


def set_seed(seed: int) -> None:
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


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


def compute_metrics(y_true: np.ndarray, y_prob: np.ndarray) -> dict[str, float]:
    pred = (y_prob >= 0.5).astype(np.int8)
    return {
        "macro_auroc": safe_macro_auroc(y_true, y_prob),
        "macro_auprc": safe_macro_auprc(y_true, y_prob),
        "micro_f1": float(f1_score(y_true.ravel(), pred.ravel(), zero_division=0)),
        "macro_f1": float(f1_score(y_true, pred, average="macro", zero_division=0)),
    }


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
    adjacency = torch.sparse_coo_tensor(indices, vals, (num_nodes, num_nodes), device=device)
    return adjacency.coalesce()


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


def masked_bce_loss(logits: torch.Tensor, y: torch.Tensor, mask: torch.Tensor) -> torch.Tensor:
    loss = torch.nn.functional.binary_cross_entropy_with_logits(logits, y, reduction="none")
    masked = loss * mask.float()
    return masked.sum() / mask.float().sum().clamp_min(1.0)


def load_data(device: torch.device) -> dict[str, torch.Tensor | np.ndarray]:
    arrays = np.load(DATA_DIR / "node_classification_arrays.npz", allow_pickle=False)
    features = np.load(DATA_DIR / "features.npz", allow_pickle=False)
    x = torch.tensor(features["one_hot_log_degree"], dtype=torch.float32, device=device)
    y = torch.tensor(arrays["y"], dtype=torch.float32, device=device)
    y_mask = torch.tensor(arrays["y_mask"].astype(bool), dtype=torch.bool, device=device)
    train_mask = torch.tensor(arrays["train_mask"].astype(bool), dtype=torch.bool, device=device)
    val_mask = torch.tensor(arrays["val_mask"].astype(bool), dtype=torch.bool, device=device)
    test_mask = torch.tensor(arrays["test_mask"].astype(bool), dtype=torch.bool, device=device)
    return {
        "x": x,
        "y": y,
        "y_mask": y_mask,
        "train_mask": train_mask,
        "val_mask": val_mask,
        "test_mask": test_mask,
        "y_np": arrays["y"].astype(np.int8),
    }


@torch.no_grad()
def evaluate(
    model: torch.nn.Module,
    x: torch.Tensor,
    adjacency: torch.Tensor | None,
    y_np: np.ndarray,
    split_mask: torch.Tensor,
) -> dict[str, float]:
    model.eval()
    logits = model(x, adjacency)
    prob = torch.sigmoid(logits).detach().cpu().numpy()
    split = split_mask.detach().cpu().numpy().astype(bool)
    return compute_metrics(y_np[split], prob[split])


def train_model(model_name: str, device: torch.device) -> dict[str, object]:
    set_seed(SEED)
    data = load_data(device)
    x = data["x"]
    y = data["y"]
    y_mask = data["y_mask"]
    train_mask = data["train_mask"]
    val_mask = data["val_mask"]
    test_mask = data["test_mask"]
    y_np = data["y_np"]

    adjacency = build_normalized_adjacency(device) if model_name == "gcn" else None
    out_dim = y.shape[1]
    in_dim = x.shape[1]
    if model_name == "mlp":
        model: torch.nn.Module = MLP(in_dim, HIDDEN_DIM, out_dim).to(device)
    elif model_name == "gcn":
        model = GCN(in_dim, HIDDEN_DIM, out_dim).to(device)
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

        val_metrics = evaluate(model, x, adjacency, y_np, val_mask)
        val_score = val_metrics["macro_auprc"]
        if val_score > best_val:
            best_val = val_score
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

    val_metrics = evaluate(model, x, adjacency, y_np, val_mask)
    test_metrics = evaluate(model, x, adjacency, y_np, test_mask)
    return {
        "dataset": "obnb_biogrid_gobp",
        "task": "node_classification",
        "model": model_name,
        "feature": "one_hot_log_degree",
        "seed": SEED,
        "best_epoch": best_epoch,
        "train_seconds": train_seconds,
        "val": val_metrics,
        "test": test_metrics,
    }


def flatten_results(results: list[dict[str, object]]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for result in results:
        for split in ["val", "test"]:
            metrics = result[split]
            rows.append(
                {
                    "dataset": result["dataset"],
                    "task": result["task"],
                    "split": split,
                    "model": result["model"],
                    "feature": result["feature"],
                    "seed": result["seed"],
                    "best_epoch": result["best_epoch"],
                    "macro_auroc": metrics["macro_auroc"],
                    "macro_auprc": metrics["macro_auprc"],
                    "micro_f1": metrics["micro_f1"],
                    "macro_f1": metrics["macro_f1"],
                    "train_seconds": result["train_seconds"],
                }
            )
    return rows


def write_outputs(results: list[dict[str, object]]) -> None:
    rows = flatten_results(results)
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    csv_path = RESULTS_DIR / "node_classification_gnn.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

    lines = [
        "# Node Classification Neural Baselines",
        "",
        "Fecha: 2026-08-05",
        "",
        "Modelos piloto entrenados sobre `one_hot_log_degree`.",
        "",
        "| Modelo | Split | Best epoch | Macro AUROC | Macro AUPRC | Micro-F1 | Macro-F1 |",
        "|---|---|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            f"| `{row['model']}` | `{row['split']}` | {row['best_epoch']} | "
            f"{row['macro_auroc']:.6f} | {row['macro_auprc']:.6f} | "
            f"{row['micro_f1']:.6f} | {row['macro_f1']:.6f} |"
        )
    (REPORTS_DIR / "node_classification_gnn.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    (REPORTS_DIR / "node_classification_gnn.json").write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    results = [train_model("mlp", device), train_model("gcn", device)]
    write_outputs(results)
    print(f"Wrote neural node-classification baselines on {device}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
