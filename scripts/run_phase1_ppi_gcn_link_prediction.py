"""Run a simple auditable GCN link-prediction baseline for Phase 1 PPI splits.

The propagation graph is built only from train-positive edges. Node features are
constant, degree, log-degree, and one-hot log-degree bins computed from that same
train-positive graph. Edges are scored with a dot-product decoder.
"""

from __future__ import annotations

import argparse
import csv
import gzip
import json
import random
import time
from pathlib import Path

import numpy as np
import torch
import torch.nn.functional as F
from sklearn.metrics import average_precision_score, brier_score_loss, log_loss, roc_auc_score


ROOT = Path(__file__).resolve().parents[1]
SPLIT_ROOT = ROOT / "data" / "processed" / "phase1_ppi_multiseed_splits"
RESULTS_DIR = ROOT / "results" / "phase1"
REPORTS_DIR = ROOT / "reports"

DATASETS = [
    "string_human_physical_v12",
    "biogrid_human_physical",
    "biogrid_human_physical_no_string_overlap",
    "string_human_physical_no_biogrid_overlap",
]
STRATEGIES = ["random", "degree_matched", "two_hop"]


def edge_columns(dataset_id: str) -> tuple[str, str]:
    return ("protein1", "protein2") if dataset_id.startswith("string") else ("entrez_a", "entrez_b")


def open_text(path: Path):
    if path.suffix == ".gz":
        return gzip.open(path, "rt", newline="", encoding="utf-8")
    return path.open(newline="", encoding="utf-8")


def split_file(split_dir: Path, name: str) -> Path:
    gz = split_dir / f"{name}.csv.gz"
    return gz if gz.exists() else split_dir / f"{name}.csv"


def read_edges(path: Path, left_col: str, right_col: str) -> list[tuple[str, str]]:
    with open_text(path) as handle:
        return [tuple(sorted((row[left_col], row[right_col]))) for row in csv.DictReader(handle)]


def sample_edges(edges: list[tuple[str, str]], limit: int | None, seed: int) -> list[tuple[str, str]]:
    if limit is None or len(edges) <= limit:
        return edges
    rng = random.Random(seed)
    return rng.sample(edges, limit)


def build_node_index(*edge_sets: list[tuple[str, str]]) -> dict[str, int]:
    nodes = sorted({node for edges in edge_sets for edge in edges for node in edge})
    return {node: idx for idx, node in enumerate(nodes)}


def edge_tensor(edges: list[tuple[str, str]], node_to_idx: dict[str, int]) -> torch.Tensor:
    return torch.as_tensor([[node_to_idx[a], node_to_idx[b]] for a, b in edges], dtype=torch.long)


def train_graph_features(train_pos: list[tuple[str, str]], node_to_idx: dict[str, int], max_log_bin: int = 8) -> torch.Tensor:
    degrees = np.zeros(len(node_to_idx), dtype=np.int64)
    for a, b in train_pos:
        degrees[node_to_idx[a]] += 1
        degrees[node_to_idx[b]] += 1
    bins = np.clip(np.floor(np.log2(degrees.astype(np.float64) + 1)).astype(np.int64), 0, max_log_bin)
    one_hot = np.zeros((len(node_to_idx), max_log_bin + 1), dtype=np.float32)
    one_hot[np.arange(len(node_to_idx)), bins] = 1.0
    degree = degrees.astype(np.float32).reshape(-1, 1)
    log_degree = np.log1p(degrees).astype(np.float32).reshape(-1, 1)
    constant = np.ones((len(node_to_idx), 1), dtype=np.float32)
    return torch.as_tensor(np.hstack([constant, degree, log_degree, one_hot]), dtype=torch.float32)


def normalized_adjacency(train_pos: list[tuple[str, str]], node_to_idx: dict[str, int]) -> torch.Tensor:
    n = len(node_to_idx)
    rows: list[int] = []
    cols: list[int] = []
    for a, b in train_pos:
        ia = node_to_idx[a]
        ib = node_to_idx[b]
        rows.extend([ia, ib])
        cols.extend([ib, ia])
    rows.extend(range(n))
    cols.extend(range(n))
    idx = torch.as_tensor([rows, cols], dtype=torch.long)
    values = torch.ones(len(rows), dtype=torch.float32)
    degrees = torch.zeros(n, dtype=torch.float32).index_add_(0, idx[0], values)
    norm_values = values * torch.pow(degrees[idx[0]], -0.5) * torch.pow(degrees[idx[1]], -0.5)
    return torch.sparse_coo_tensor(idx, norm_values, (n, n)).coalesce()


class GCNEncoder(torch.nn.Module):
    def __init__(self, in_dim: int, hidden_dim: int, out_dim: int, dropout: float) -> None:
        super().__init__()
        self.w1 = torch.nn.Linear(in_dim, hidden_dim, bias=False)
        self.w2 = torch.nn.Linear(hidden_dim, out_dim, bias=False)
        self.dropout = dropout

    def forward(self, x: torch.Tensor, adj: torch.Tensor) -> torch.Tensor:
        h = torch.sparse.mm(adj, x)
        h = F.relu(self.w1(h))
        h = F.dropout(h, p=self.dropout, training=self.training)
        h = torch.sparse.mm(adj, h)
        return self.w2(h)


def edge_logits(z: torch.Tensor, edges: torch.Tensor) -> torch.Tensor:
    return (z[edges[:, 0]] * z[edges[:, 1]]).sum(dim=1)


def expected_calibration_error(y_true: np.ndarray, y_prob: np.ndarray, n_bins: int = 10) -> float:
    bins = np.linspace(0.0, 1.0, n_bins + 1)
    ece = 0.0
    for left, right in zip(bins[:-1], bins[1:]):
        mask = ((y_prob >= left) & (y_prob <= right)) if right == 1.0 else ((y_prob >= left) & (y_prob < right))
        if np.any(mask):
            ece += float(np.mean(mask)) * abs(float(np.mean(y_prob[mask])) - float(np.mean(y_true[mask])))
    return ece


def evaluate(
    model: GCNEncoder,
    x: torch.Tensor,
    adj: torch.Tensor,
    pos_edges: torch.Tensor,
    neg_edges: torch.Tensor,
    batch_size: int,
) -> dict[str, float]:
    y_true = np.asarray([1] * pos_edges.shape[0] + [0] * neg_edges.shape[0], dtype=np.int8)
    edges = torch.cat([pos_edges, neg_edges], dim=0)
    probs: list[np.ndarray] = []
    model.eval()
    with torch.no_grad():
        z = model(x, adj)
        for start in range(0, edges.shape[0], batch_size):
            logits = edge_logits(z, edges[start : start + batch_size])
            probs.append(torch.sigmoid(logits).cpu().numpy())
    y_prob = np.concatenate(probs)
    clipped = np.clip(y_prob, 1e-7, 1 - 1e-7)
    return {
        "auroc": float(roc_auc_score(y_true, y_prob)),
        "auprc": float(average_precision_score(y_true, y_prob)),
        "brier": float(brier_score_loss(y_true, y_prob)),
        "nll": float(log_loss(y_true, clipped, labels=[0, 1])),
        "ece_10": expected_calibration_error(y_true, y_prob, n_bins=10),
    }


def output_csv_path() -> Path:
    return RESULTS_DIR / "ppi_gcn_link_prediction.csv"


def read_existing_contexts() -> set[tuple[str, str, int]]:
    path = output_csv_path()
    if not path.exists():
        return set()
    with path.open(newline="", encoding="utf-8") as handle:
        return {(row["dataset"], row["negative_strategy"], int(row["seed"])) for row in csv.DictReader(handle)}


def run_one(dataset_id: str, strategy: str, seed: int, args: argparse.Namespace) -> list[dict[str, object]]:
    torch.manual_seed(seed)
    np.random.seed(seed)
    random.seed(seed)

    split_dir = SPLIT_ROOT / dataset_id / strategy / f"seed_{seed}"
    left_col, right_col = edge_columns(dataset_id)
    train_pos_full = read_edges(split_file(split_dir, "train_pos"), left_col, right_col)
    train_neg_full = read_edges(split_file(split_dir, "train_neg"), left_col, right_col)
    val_pos_full = read_edges(split_file(split_dir, "val_pos"), left_col, right_col)
    val_neg_full = read_edges(split_file(split_dir, "val_neg"), left_col, right_col)
    test_pos_full = read_edges(split_file(split_dir, "test_pos"), left_col, right_col)
    test_neg_full = read_edges(split_file(split_dir, "test_neg"), left_col, right_col)

    train_pos = sample_edges(train_pos_full, args.max_train_pairs_per_class, seed)
    train_neg = sample_edges(train_neg_full, args.max_train_pairs_per_class, seed + 1000)
    val_pos = sample_edges(val_pos_full, args.max_eval_pairs_per_class, seed + 2000)
    val_neg = sample_edges(val_neg_full, args.max_eval_pairs_per_class, seed + 3000)
    test_pos = sample_edges(test_pos_full, args.max_eval_pairs_per_class, seed + 4000)
    test_neg = sample_edges(test_neg_full, args.max_eval_pairs_per_class, seed + 5000)

    node_to_idx = build_node_index(train_pos_full, train_neg_full, val_pos_full, val_neg_full, test_pos_full, test_neg_full)
    x = train_graph_features(train_pos_full, node_to_idx)
    adj = normalized_adjacency(train_pos_full, node_to_idx)
    train_pos_t = edge_tensor(train_pos, node_to_idx)
    train_neg_t = edge_tensor(train_neg, node_to_idx)

    model = GCNEncoder(x.shape[1], args.hidden_dim, args.embedding_dim, args.dropout)
    optimizer = torch.optim.Adam(model.parameters(), lr=args.learning_rate, weight_decay=args.weight_decay)

    train_edges = torch.cat([train_pos_t, train_neg_t], dim=0)
    train_labels = torch.cat([torch.ones(train_pos_t.shape[0]), torch.zeros(train_neg_t.shape[0])])
    generator = torch.Generator().manual_seed(seed)

    start_train = time.perf_counter()
    last_loss = float("nan")
    for _epoch in range(args.epochs):
        model.train()
        if args.training_pairs_per_epoch and train_edges.shape[0] > args.training_pairs_per_epoch:
            idx = torch.randperm(train_edges.shape[0], generator=generator)[: args.training_pairs_per_epoch]
            epoch_edges = train_edges[idx]
            epoch_labels = train_labels[idx]
        else:
            epoch_edges = train_edges
            epoch_labels = train_labels
        z = model(x, adj)
        logits = edge_logits(z, epoch_edges)
        loss = F.binary_cross_entropy_with_logits(logits, epoch_labels)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        last_loss = float(loss.detach().cpu())
    train_seconds = time.perf_counter() - start_train

    rows: list[dict[str, object]] = []
    for split, pos, neg in [
        ("val", val_pos, val_neg),
        ("test", test_pos, test_neg),
    ]:
        pos_t = edge_tensor(pos, node_to_idx)
        neg_t = edge_tensor(neg, node_to_idx)
        start_eval = time.perf_counter()
        metrics = evaluate(model, x, adj, pos_t, neg_t, batch_size=args.eval_batch_size)
        inference_seconds = time.perf_counter() - start_eval
        rows.append(
            {
                "dataset": dataset_id,
                "negative_strategy": strategy,
                "seed": seed,
                "split": split,
                "model": "gcn_dot",
                "feature_set": "train_graph_degree_features",
                "decoder": "dot_product",
                "epochs": args.epochs,
                "hidden_dim": args.hidden_dim,
                "embedding_dim": args.embedding_dim,
                "dropout": args.dropout,
                "learning_rate": args.learning_rate,
                "weight_decay": args.weight_decay,
                "sampled_train_pairs_per_class": args.max_train_pairs_per_class or "",
                "sampled_eval_pairs_per_class": args.max_eval_pairs_per_class or "",
                "num_nodes": len(node_to_idx),
                "num_train": int(train_edges.shape[0]),
                "num_eval": int(pos_t.shape[0] + neg_t.shape[0]),
                "auroc": metrics["auroc"],
                "auprc": metrics["auprc"],
                "brier": metrics["brier"],
                "nll": metrics["nll"],
                "ece_10": metrics["ece_10"],
                "train_seconds": train_seconds,
                "inference_seconds": inference_seconds,
                "last_train_loss": last_loss,
            }
        )
    return rows


def append_rows(rows: list[dict[str, object]]) -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    path = output_csv_path()
    fields = list(rows[0])
    write_header = not path.exists()
    with path.open("a", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        if write_header:
            writer.writeheader()
        writer.writerows(rows)


def write_reports() -> None:
    path = output_csv_path()
    if not path.exists():
        return
    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    (REPORTS_DIR / "phase1_ppi_gcn_link_prediction.json").write_text(json.dumps(rows, indent=2) + "\n", encoding="utf-8")
    lines = [
        "# Phase 1 PPI GCN Link-Prediction Baseline",
        "",
        "Propagation uses train-positive edges only. The decoder is a dot product over GCN node embeddings.",
        "",
        "| Dataset | Negatives | Seed | Split | AUROC | AUPRC | Brier | ECE-10 | Train s | Infer s |",
        "|---|---|---:|---|---:|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            f"| `{row['dataset']}` | `{row['negative_strategy']}` | {row['seed']} | `{row['split']}` | "
            f"{float(row['auroc']):.6f} | {float(row['auprc']):.6f} | {float(row['brier']):.6f} | "
            f"{float(row['ece_10']):.6f} | {float(row['train_seconds']):.2f} | {float(row['inference_seconds']):.2f} |"
        )
    (REPORTS_DIR / "phase1_ppi_gcn_link_prediction.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--datasets", nargs="+", default=DATASETS, choices=DATASETS)
    parser.add_argument("--strategies", nargs="+", default=STRATEGIES, choices=STRATEGIES)
    parser.add_argument("--seeds", nargs="+", type=int, default=list(range(42, 52)))
    parser.add_argument("--epochs", type=int, default=30)
    parser.add_argument("--hidden-dim", type=int, default=64)
    parser.add_argument("--embedding-dim", type=int, default=64)
    parser.add_argument("--dropout", type=float, default=0.2)
    parser.add_argument("--learning-rate", type=float, default=0.01)
    parser.add_argument("--weight-decay", type=float, default=1e-4)
    parser.add_argument("--batch-size", type=int, default=32768)
    parser.add_argument("--eval-batch-size", type=int, default=131072)
    parser.add_argument("--max-train-pairs-per-class", type=int, default=None)
    parser.add_argument("--max-eval-pairs-per-class", type=int, default=None)
    parser.add_argument("--training-pairs-per-epoch", type=int, default=200000)
    parser.add_argument("--resume", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    existing = read_existing_contexts() if args.resume else set()
    written = 0
    for dataset_id in args.datasets:
        for strategy in args.strategies:
            for seed in args.seeds:
                context = (dataset_id, strategy, seed)
                if context in existing:
                    print(f"Skipping existing {dataset_id} / {strategy} / seed={seed}")
                    continue
                print(f"Running gcn_dot {dataset_id} / {strategy} / seed={seed}")
                rows = run_one(dataset_id, strategy, seed, args)
                append_rows(rows)
                existing.add(context)
                written += len(rows)
                print(f"Appended {len(rows)} rows.")
    write_reports()
    print(f"Appended {written} new rows to {output_csv_path()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
