"""Build Phase 1 multi-seed PPI link-prediction splits.

This script does not overwrite the original seed-42 MVP splits. It writes new
compressed split files under:

data/processed/phase1_ppi_multiseed_splits/<dataset>/<negative_strategy>/seed_<seed>/

Supported negative strategies:
- random
- degree_matched
- two_hop
"""

from __future__ import annotations

import argparse
import csv
import gzip
import json
import sys
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from biographbench.splits import build_link_prediction_split


OUT_ROOT = ROOT / "data" / "processed" / "phase1_ppi_multiseed_splits"
REPORTS_DIR = ROOT / "reports"

DATASETS = {
    "string_human_physical_v12": {
        "path": ROOT / "data" / "processed" / "string_human_physical_v12" / "edges_undirected.csv",
        "left": "protein1",
        "right": "protein2",
    },
    "biogrid_human_physical": {
        "path": ROOT / "data" / "processed" / "biogrid_human_physical" / "edges_entrez_undirected.csv",
        "left": "entrez_a",
        "right": "entrez_b",
    },
    "biogrid_human_physical_no_string_overlap": {
        "path": ROOT
        / "data"
        / "processed"
        / "biogrid_human_physical_no_string_overlap"
        / "edges_entrez_undirected.csv",
        "left": "entrez_a",
        "right": "entrez_b",
    },
    "string_human_physical_no_biogrid_overlap": {
        "path": ROOT
        / "data"
        / "processed"
        / "string_human_physical_no_biogrid_overlap"
        / "edges_undirected.csv",
        "left": "protein1",
        "right": "protein2",
    },
}


def read_edges(path: Path, left_col: str, right_col: str) -> tuple[list[tuple[str, str]], list[str]]:
    edges: set[tuple[str, str]] = set()
    nodes: set[str] = set()
    with path.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            a = row[left_col]
            b = row[right_col]
            if not a or not b or a == b:
                continue
            edge = tuple(sorted((a, b)))
            edges.add(edge)
            nodes.update(edge)
    return sorted(edges), sorted(nodes)


def write_edges_gz(path: Path, edges: Iterable[tuple[str, str]], left_col: str, right_col: str, label: int) -> None:
    with gzip.open(path, "wt", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=[left_col, right_col, "label"])
        writer.writeheader()
        for a, b in edges:
            writer.writerow({left_col: a, right_col: b, "label": label})


def build_dataset_strategy_seed(dataset_id: str, strategy: str, seed: int, val_ratio: float, test_ratio: float) -> dict[str, object]:
    cfg = DATASETS[dataset_id]
    left_col = str(cfg["left"])
    right_col = str(cfg["right"])
    edges, nodes = read_edges(Path(cfg["path"]), left_col, right_col)
    split = build_link_prediction_split(
        edges,
        nodes=nodes,
        seed=seed,
        val_ratio=val_ratio,
        test_ratio=test_ratio,
        negative_strategy=strategy,
    )

    out_dir = OUT_ROOT / dataset_id / strategy / f"seed_{seed}"
    out_dir.mkdir(parents=True, exist_ok=True)
    write_edges_gz(out_dir / "train_pos.csv.gz", split.train_pos, left_col, right_col, 1)
    write_edges_gz(out_dir / "val_pos.csv.gz", split.val_pos, left_col, right_col, 1)
    write_edges_gz(out_dir / "test_pos.csv.gz", split.test_pos, left_col, right_col, 1)
    write_edges_gz(out_dir / "train_neg.csv.gz", split.train_neg, left_col, right_col, 0)
    write_edges_gz(out_dir / "val_neg.csv.gz", split.val_neg, left_col, right_col, 0)
    write_edges_gz(out_dir / "test_neg.csv.gz", split.test_neg, left_col, right_col, 0)

    manifest = split.manifest(dataset_id, out_dir)
    manifest.update(
        {
            "phase": "phase1_ppi_multiseed",
            "source_edges": str(cfg["path"]),
            "edge_columns": [left_col, right_col],
            "compressed_split_files": True,
        }
    )
    (out_dir / "split_manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return manifest


def read_existing_manifests() -> list[dict[str, object]]:
    manifests: list[dict[str, object]] = []
    for path in sorted(OUT_ROOT.glob("*/*/seed_*/split_manifest.json")):
        manifests.append(json.loads(path.read_text(encoding="utf-8")))
    return manifests


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--datasets", nargs="+", default=list(DATASETS), choices=list(DATASETS))
    parser.add_argument(
        "--strategies",
        nargs="+",
        default=["random", "degree_matched"],
        choices=["random", "degree_matched", "two_hop"],
    )
    parser.add_argument("--seeds", nargs="+", type=int, default=list(range(42, 52)))
    parser.add_argument("--val-ratio", type=float, default=0.10)
    parser.add_argument("--test-ratio", type=float, default=0.10)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    manifests: list[dict[str, object]] = []
    for dataset_id in args.datasets:
        for strategy in args.strategies:
            for seed in args.seeds:
                print(f"Building {dataset_id} / {strategy} / seed={seed}")
                manifest = build_dataset_strategy_seed(dataset_id, strategy, seed, args.val_ratio, args.test_ratio)
                manifests.append(manifest)
                if manifest["split_errors"]:
                    print(f"WARNING split errors: {manifest['split_errors']}")

    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    all_manifests = read_existing_manifests()
    summary = {
        "phase": "phase1_ppi_multiseed",
        "datasets": args.datasets,
        "strategies": args.strategies,
        "seeds": args.seeds,
        "new_split_count": len(manifests),
        "split_count": len(all_manifests),
        "output_root": str(OUT_ROOT),
        "manifests": all_manifests,
    }
    (REPORTS_DIR / "phase1_ppi_multiseed_splits.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    lines = [
        "# Phase 1 PPI Multi-Seed Splits",
        "",
        f"Output root: `{OUT_ROOT}`",
        "",
        "| Dataset | Negative strategy | Seed | Train + | Val + | Test + | Errors |",
        "|---|---|---:|---:|---:|---:|---|",
    ]
    for manifest in all_manifests:
        lines.append(
            f"| `{manifest['dataset_id']}` | `{manifest['negative_strategy']}` | {manifest['seed']} | "
            f"{manifest['train_pos']} | {manifest['val_pos']} | {manifest['test_pos']} | "
            f"{'None' if not manifest['split_errors'] else manifest['split_errors']} |"
        )
    (REPORTS_DIR / "phase1_ppi_multiseed_splits.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {len(manifests)} new split manifests under {OUT_ROOT}")
    print(f"Indexed {len(all_manifests)} total split manifests under {OUT_ROOT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
