"""Validate the BioGRID pilot link-prediction split."""

from __future__ import annotations

import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPLIT_DIR = ROOT / "data" / "processed" / "biogrid_human_physical" / "splits"

FILES = [
    "train_pos.csv",
    "val_pos.csv",
    "test_pos.csv",
    "train_neg.csv",
    "val_neg.csv",
    "test_neg.csv",
]


def read_edges(path: Path) -> set[tuple[str, str]]:
    edges: set[tuple[str, str]] = set()
    with path.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            a, b = row["entrez_a"], row["entrez_b"]
            if a > b:
                a, b = b, a
            edges.add((a, b))
    return edges


def main() -> int:
    errors: list[str] = []
    manifest = json.loads((SPLIT_DIR / "split_manifest.json").read_text(encoding="utf-8"))
    edges_by_name = {name: read_edges(SPLIT_DIR / name) for name in FILES}

    for name, edges in edges_by_name.items():
        if not edges:
            errors.append(f"{name} is empty")
        if any(a == b for a, b in edges):
            errors.append(f"{name} contains self-loops")

    names = list(edges_by_name)
    for i, left in enumerate(names):
        for right in names[i + 1 :]:
            overlap = edges_by_name[left] & edges_by_name[right]
            if overlap:
                errors.append(f"{left} overlaps {right}: {len(overlap)}")

    for name in FILES:
        key = name.replace(".csv", "")
        expected = manifest[key]
        observed = len(edges_by_name[name])
        if observed != expected:
            errors.append(f"{name} count mismatch: expected {expected}, observed {observed}")

    if not manifest.get("train_components_preserved_by_construction"):
        errors.append("train components were not preserved")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print("OK: BioGRID pilot split has no overlap, no self-loops, and expected counts.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
