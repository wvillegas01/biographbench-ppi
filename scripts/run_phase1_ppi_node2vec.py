"""Run an auditable node2vec-compatible random-walk baseline for Phase 1 PPI.

The embedding stage uses unbiased node2vec walks (p=q=1, equivalent to
DeepWalk-style walks) trained with a skip-gram negative-sampling objective in
PyTorch. Link prediction is evaluated with a logistic decoder over four
embedding-pair features: dot product, cosine similarity, L2 distance, and L1
distance.

This avoids PyG/DGL/node2vec package dependencies while keeping the baseline
reproducible and inspectable.
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
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import average_precision_score, brier_score_loss, log_loss, roc_auc_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


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


def build_node_index(edges: list[tuple[str, str]]) -> tuple[list[str], dict[str, int]]:
    nodes = sorted({node for edge in edges for node in edge})
    return nodes, {node: idx for idx, node in enumerate(nodes)}


def build_adjacency_indices(edges: list[tuple[str, str]], node_to_idx: dict[str, int]) -> list[list[int]]:
    adjacency = [[] for _ in range(len(node_to_idx))]
    for a, b in edges:
        ia = node_to_idx[a]
        ib = node_to_idx[b]
        adjacency[ia].append(ib)
        adjacency[ib].append(ia)
    return [sorted(set(neighbors)) for neighbors in adjacency]


def generate_walk_pairs(
    adjacency: list[list[int]],
    rng: random.Random,
    walks_per_node: int,
    walk_length: int,
    window_size: int,
    max_pairs: int,
) -> np.ndarray:
    nodes = list(range(len(adjacency)))
    pairs: list[tuple[int, int]] = []
    for _ in range(walks_per_node):
        rng.shuffle(nodes)
        for start in nodes:
            if not adjacency[start]:
                continue
            walk = [start]
            current = start
            for _step in range(walk_length - 1):
                neighbors = adjacency[current]
                if not neighbors:
                    break
                current = rng.choice(neighbors)
                walk.append(current)
            for i, center in enumerate(walk):
                left = max(0, i - window_size)
                right = min(len(walk), i + window_size + 1)
                for j in range(left, right):
                    if i == j:
                        continue
                    pairs.append((center, walk[j]))
                    if len(pairs) >= max_pairs:
                        return np.asarray(pairs, dtype=np.int64)
    return np.asarray(pairs, dtype=np.int64)


def train_embeddings(
    num_nodes: int,
    positive_pairs: np.ndarray,
    seed: int,
    dim: int,
    epochs: int,
    batch_size: int,
    negative_samples: int,
    learning_rate: float,
) -> np.ndarray:
    torch.manual_seed(seed)
    rng = np.random.default_rng(seed)
    target = torch.nn.Embedding(num_nodes, dim)
    context = torch.nn.Embedding(num_nodes, dim)
    torch.nn.init.xavier_uniform_(target.weight)
    torch.nn.init.xavier_uniform_(context.weight)
    optimizer = torch.optim.Adam(list(target.parameters()) + list(context.parameters()), lr=learning_rate)
    pairs = positive_pairs.copy()

    for _epoch in range(epochs):
        rng.shuffle(pairs)
        for start in range(0, pairs.shape[0], batch_size):
            batch = pairs[start : start + batch_size]
            centers = torch.as_tensor(batch[:, 0], dtype=torch.long)
            positives = torch.as_tensor(batch[:, 1], dtype=torch.long)
            negatives = torch.randint(0, num_nodes, (centers.shape[0], negative_samples), dtype=torch.long)
            center_vec = target(centers)
            positive_vec = context(positives)
            negative_vec = context(negatives)
            positive_score = torch.sum(center_vec * positive_vec, dim=1)
            negative_score = torch.sum(center_vec.unsqueeze(1) * negative_vec, dim=2)
            loss = -F.logsigmoid(positive_score).mean() - F.logsigmoid(-negative_score).mean()
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

    embeddings = (target.weight.detach().cpu().numpy() + context.weight.detach().cpu().numpy()) / 2.0
    return embeddings.astype(np.float32)


def edge_embedding_features(edges: list[tuple[str, str]], embeddings: np.ndarray, node_to_idx: dict[str, int]) -> np.ndarray:
    features = np.zeros((len(edges), 4), dtype=np.float32)
    for i, (a, b) in enumerate(edges):
        va = embeddings[node_to_idx[a]]
        vb = embeddings[node_to_idx[b]]
        dot = float(np.dot(va, vb))
        denom = float(np.linalg.norm(va) * np.linalg.norm(vb))
        cosine = dot / denom if denom > 0 else 0.0
        features[i] = [dot, cosine, float(np.linalg.norm(va - vb)), float(np.mean(np.abs(va - vb)))]
    return features


def build_xy(
    pos_edges: list[tuple[str, str]],
    neg_edges: list[tuple[str, str]],
    embeddings: np.ndarray,
    node_to_idx: dict[str, int],
) -> tuple[np.ndarray, np.ndarray]:
    edges = pos_edges + neg_edges
    x = edge_embedding_features(edges, embeddings, node_to_idx)
    y = np.asarray([1] * len(pos_edges) + [0] * len(neg_edges), dtype=np.int8)
    return x, y


def expected_calibration_error(y_true: np.ndarray, y_prob: np.ndarray, n_bins: int = 10) -> float:
    bins = np.linspace(0.0, 1.0, n_bins + 1)
    ece = 0.0
    for left, right in zip(bins[:-1], bins[1:]):
        mask = ((y_prob >= left) & (y_prob <= right)) if right == 1.0 else ((y_prob >= left) & (y_prob < right))
        if not np.any(mask):
            continue
        ece += float(np.mean(mask)) * abs(float(np.mean(y_prob[mask])) - float(np.mean(y_true[mask])))
    return ece


def output_csv_path() -> Path:
    return RESULTS_DIR / "ppi_node2vec_link_prediction.csv"


def read_existing_contexts() -> set[tuple[str, str, int]]:
    path = output_csv_path()
    if not path.exists():
        return set()
    contexts: set[tuple[str, str, int]] = set()
    with path.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            contexts.add((row["dataset"], row["negative_strategy"], int(row["seed"])))
    return contexts


def run_one(dataset_id: str, strategy: str, seed: int, args: argparse.Namespace) -> list[dict[str, object]]:
    split_dir = SPLIT_ROOT / dataset_id / strategy / f"seed_{seed}"
    left_col, right_col = edge_columns(dataset_id)
    train_pos = read_edges(split_file(split_dir, "train_pos"), left_col, right_col)
    train_neg = read_edges(split_file(split_dir, "train_neg"), left_col, right_col)
    nodes, node_to_idx = build_node_index(train_pos)
    adjacency = build_adjacency_indices(train_pos, node_to_idx)

    start = time.perf_counter()
    pairs = generate_walk_pairs(
        adjacency,
        random.Random(seed),
        walks_per_node=args.walks_per_node,
        walk_length=args.walk_length,
        window_size=args.window_size,
        max_pairs=args.max_pairs,
    )
    walk_seconds = time.perf_counter() - start
    if pairs.shape[0] == 0:
        raise RuntimeError(f"no random-walk pairs generated for {dataset_id}/{strategy}/seed={seed}")

    start = time.perf_counter()
    embeddings = train_embeddings(
        len(nodes),
        pairs,
        seed=seed,
        dim=args.embedding_dim,
        epochs=args.epochs,
        batch_size=args.batch_size,
        negative_samples=args.negative_samples,
        learning_rate=args.learning_rate,
    )
    embedding_seconds = time.perf_counter() - start

    x_train, y_train = build_xy(train_pos, train_neg, embeddings, node_to_idx)
    decoder = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000, class_weight="balanced", random_state=seed))
    start = time.perf_counter()
    decoder.fit(x_train, y_train)
    decoder_seconds = time.perf_counter() - start

    rows: list[dict[str, object]] = []
    for split in ["val", "test"]:
        pos = read_edges(split_file(split_dir, f"{split}_pos"), left_col, right_col)
        neg = read_edges(split_file(split_dir, f"{split}_neg"), left_col, right_col)
        x_eval, y_eval = build_xy(pos, neg, embeddings, node_to_idx)
        start = time.perf_counter()
        y_prob = decoder.predict_proba(x_eval)[:, 1]
        inference_seconds = time.perf_counter() - start
        rows.append(
            {
                "dataset": dataset_id,
                "negative_strategy": strategy,
                "seed": seed,
                "split": split,
                "model": "node2vec_walk_logreg",
                "embedding_dim": args.embedding_dim,
                "walks_per_node": args.walks_per_node,
                "walk_length": args.walk_length,
                "window_size": args.window_size,
                "max_pairs": args.max_pairs,
                "positive_walk_pairs": int(pairs.shape[0]),
                "num_train": int(y_train.shape[0]),
                "num_eval": int(y_eval.shape[0]),
                "auroc": float(roc_auc_score(y_eval, y_prob)),
                "auprc": float(average_precision_score(y_eval, y_prob)),
                "brier": float(brier_score_loss(y_eval, y_prob)),
                "nll": float(log_loss(y_eval, y_prob, labels=[0, 1])),
                "ece_10": expected_calibration_error(y_eval, y_prob, n_bins=10),
                "walk_seconds": walk_seconds,
                "embedding_seconds": embedding_seconds,
                "decoder_seconds": decoder_seconds,
                "inference_seconds": inference_seconds,
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
    (REPORTS_DIR / "phase1_ppi_node2vec_link_prediction.json").write_text(json.dumps(rows, indent=2) + "\n", encoding="utf-8")
    lines = [
        "# Phase 1 PPI node2vec-compatible Random-Walk Baseline",
        "",
        "| Dataset | Negatives | Seed | Split | AUROC | AUPRC | ECE-10 | Embed s | Decoder s |",
        "|---|---|---:|---|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            f"| `{row['dataset']}` | `{row['negative_strategy']}` | {row['seed']} | `{row['split']}` | "
            f"{float(row['auroc']):.6f} | {float(row['auprc']):.6f} | {float(row['ece_10']):.6f} | "
            f"{float(row['embedding_seconds']):.2f} | {float(row['decoder_seconds']):.2f} |"
        )
    (REPORTS_DIR / "phase1_ppi_node2vec_link_prediction.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--datasets", nargs="+", default=DATASETS, choices=DATASETS)
    parser.add_argument("--strategies", nargs="+", default=STRATEGIES, choices=STRATEGIES)
    parser.add_argument("--seeds", nargs="+", type=int, default=list(range(42, 52)))
    parser.add_argument("--embedding-dim", type=int, default=64)
    parser.add_argument("--walks-per-node", type=int, default=2)
    parser.add_argument("--walk-length", type=int, default=16)
    parser.add_argument("--window-size", type=int, default=3)
    parser.add_argument("--max-pairs", type=int, default=2_000_000)
    parser.add_argument("--epochs", type=int, default=1)
    parser.add_argument("--batch-size", type=int, default=8192)
    parser.add_argument("--negative-samples", type=int, default=5)
    parser.add_argument("--learning-rate", type=float, default=0.01)
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
                print(f"Running node2vec_walk_logreg {dataset_id} / {strategy} / seed={seed}")
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
