"""Validate the filtered BioGRID human physical edge table."""

from __future__ import annotations

import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data" / "processed" / "biogrid_human_physical"
EDGES_PATH = DATA_DIR / "edges_entrez_undirected.csv"
MANIFEST_PATH = DATA_DIR / "filter_manifest.json"


def main() -> int:
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    errors: list[str] = []
    edges: set[tuple[str, str]] = set()
    nodes: set[str] = set()
    rows = 0

    with EDGES_PATH.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            rows += 1
            a = row["entrez_a"]
            b = row["entrez_b"]
            if a == b:
                errors.append(f"self-loop found at row {rows}: {a}")
                break
            if a > b:
                errors.append(f"unordered edge found at row {rows}: {a}, {b}")
                break
            edge = (a, b)
            if edge in edges:
                errors.append(f"duplicate edge found at row {rows}: {edge}")
                break
            edges.add(edge)
            nodes.update(edge)

    if rows != manifest["unique_undirected_edges"]:
        errors.append(
            f"edge count mismatch: manifest={manifest['unique_undirected_edges']} observed={rows}"
        )
    if len(nodes) != manifest["unique_nodes_entrez"]:
        errors.append(
            f"node count mismatch: manifest={manifest['unique_nodes_entrez']} observed={len(nodes)}"
        )

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("OK: BioGRID filtered physical table has expected counts, no self-loops, and no duplicate pairs.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
