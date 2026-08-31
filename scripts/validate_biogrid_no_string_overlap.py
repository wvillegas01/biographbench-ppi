"""Validate BioGRID no-STRING-overlap ablation."""

from __future__ import annotations

import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data" / "processed" / "biogrid_human_physical_no_string_overlap"
SPLIT_DIR = DATA_DIR / "splits"
OVERLAP_PATH = ROOT / "data" / "processed" / "string_biogrid_overlap" / "overlap_entrez_edges.csv"

SPLIT_FILES = [
    "train_pos.csv",
    "val_pos.csv",
    "test_pos.csv",
    "train_neg.csv",
    "val_neg.csv",
    "test_neg.csv",
]


def read_edges(path: Path, a_col: str = "entrez_a", b_col: str = "entrez_b") -> set[tuple[str, str]]:
    edges: set[tuple[str, str]] = set()
    with path.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            edges.add(tuple(sorted((row[a_col], row[b_col]))))
    return edges


def main() -> int:
    errors: list[str] = []
    manifest = json.loads((DATA_DIR / "ablation_manifest.json").read_text(encoding="utf-8"))
    overlap = read_edges(OVERLAP_PATH)
    ablation_edges = read_edges(DATA_DIR / "edges_entrez_undirected.csv")

    if ablation_edges & overlap:
        errors.append(f"ablation contains {len(ablation_edges & overlap)} overlap edges")
    if len(ablation_edges) != manifest["remaining_edges"]:
        errors.append("ablation edge count does not match manifest")
    if any(a == b for a, b in ablation_edges):
        errors.append("ablation contains self-loops")

    split_edges = {name: read_edges(SPLIT_DIR / name) for name in SPLIT_FILES}
    for name, edges in split_edges.items():
        if not edges:
            errors.append(f"{name} is empty")
        if any(a == b for a, b in edges):
            errors.append(f"{name} contains self-loops")
        expected = manifest["split"][name.replace(".csv", "")]
        if len(edges) != expected:
            errors.append(f"{name} count mismatch: expected {expected}, observed {len(edges)}")

    names = sorted(split_edges)
    for i, left in enumerate(names):
        for right in names[i + 1 :]:
            overlap_edges = split_edges[left] & split_edges[right]
            if overlap_edges:
                errors.append(f"{left} overlaps {right}: {len(overlap_edges)}")

    if not manifest["split"]["train_components_preserved_by_construction"]:
        errors.append("train components were not preserved")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("OK: BioGRID no-STRING-overlap ablation and splits are valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
