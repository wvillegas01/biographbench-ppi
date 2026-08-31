"""Build BioGRID physical ablation excluding pairs observed in STRING.

This creates an overlap-aware BioGRID variant:
- Input BioGRID: filtered human-human physical Entrez pairs.
- Input overlap: Entrez pairs shared with STRING after explicit STRING alias mapping.
- Output: BioGRID edges with overlapping Entrez pairs removed, plus pilot splits.
"""

from __future__ import annotations

import csv
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from biographbench.splits import build_link_prediction_split

BIOGRID_EDGES = ROOT / "data" / "processed" / "biogrid_human_physical" / "edges_entrez_undirected.csv"
OVERLAP_EDGES = ROOT / "data" / "processed" / "string_biogrid_overlap" / "overlap_entrez_edges.csv"
OUT_DIR = ROOT / "data" / "processed" / "biogrid_human_physical_no_string_overlap"
SPLIT_DIR = OUT_DIR / "splits"
REPORTS_DIR = ROOT / "reports"

SEED = 42
VAL_RATIO = 0.10
TEST_RATIO = 0.10


def read_overlap() -> set[tuple[str, str]]:
    edges: set[tuple[str, str]] = set()
    with OVERLAP_EDGES.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            edges.add(tuple(sorted((row["entrez_a"], row["entrez_b"]))))
    return edges


def read_filtered_edges(overlap: set[tuple[str, str]]) -> tuple[dict[tuple[str, str], dict[str, str]], int]:
    kept: dict[tuple[str, str], dict[str, str]] = {}
    removed = 0
    with BIOGRID_EDGES.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            edge = tuple(sorted((row["entrez_a"], row["entrez_b"])))
            if edge in overlap:
                removed += 1
                continue
            kept[edge] = row
    return kept, removed


def write_edges(path: Path, edges: dict[tuple[str, str], dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        fieldnames = [
            "entrez_a",
            "entrez_b",
            "symbol_a",
            "symbol_b",
            "label",
            "evidence_count",
            "publication_count",
            "experimental_systems",
            "throughput",
        ]
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for edge, row in sorted(edges.items()):
            output = {field: row.get(field, "") for field in fieldnames}
            output["entrez_a"], output["entrez_b"] = edge
            writer.writerow(output)


def write_split_edges(path: Path, edges: list[tuple[str, str]], label: int, meta: dict[tuple[str, str], dict[str, str]] | None = None) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        fieldnames = ["entrez_a", "entrez_b", "label", "evidence_count", "publication_count"]
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for a, b in edges:
            row = meta.get((a, b), {}) if meta else {}
            writer.writerow(
                {
                    "entrez_a": a,
                    "entrez_b": b,
                    "label": label,
                    "evidence_count": row.get("evidence_count", ""),
                    "publication_count": row.get("publication_count", ""),
                }
            )


def build_splits(edge_meta: dict[tuple[str, str], dict[str, str]]) -> dict[str, object]:
    SPLIT_DIR.mkdir(parents=True, exist_ok=True)
    split = build_link_prediction_split(edge_meta.keys(), seed=SEED, val_ratio=VAL_RATIO, test_ratio=TEST_RATIO)
    train_pos = split.train_pos
    val_pos = split.val_pos
    test_pos = split.test_pos
    train_neg = split.train_neg
    val_neg = split.val_neg
    test_neg = split.test_neg

    write_split_edges(SPLIT_DIR / "train_pos.csv", train_pos, 1, edge_meta)
    write_split_edges(SPLIT_DIR / "val_pos.csv", val_pos, 1, edge_meta)
    write_split_edges(SPLIT_DIR / "test_pos.csv", test_pos, 1, edge_meta)
    write_split_edges(SPLIT_DIR / "train_neg.csv", train_neg, 0)
    write_split_edges(SPLIT_DIR / "val_neg.csv", val_neg, 0)
    write_split_edges(SPLIT_DIR / "test_neg.csv", test_neg, 0)

    manifest = split.manifest("biogrid_human_physical_no_string_overlap", SPLIT_DIR)
    (SPLIT_DIR / "split_manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return manifest


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    overlap = read_overlap()
    kept_edges, removed = read_filtered_edges(overlap)
    write_edges(OUT_DIR / "edges_entrez_undirected.csv", kept_edges)
    split_manifest = build_splits(kept_edges)
    result = {
        "dataset_id": "biogrid_human_physical_no_string_overlap",
        "source_dataset": "biogrid_human_physical",
        "overlap_source": str(OVERLAP_EDGES),
        "original_biogrid_edges": len(kept_edges) + removed,
        "removed_string_overlap_edges": removed,
        "remaining_edges": len(kept_edges),
        "remaining_nodes": split_manifest["nodes"],
        "split": split_manifest,
    }
    (OUT_DIR / "ablation_manifest.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    (REPORTS_DIR / "biogrid_no_string_overlap.md").write_text(
        f"""# BioGRID No-STRING-Overlap Ablation

Fecha: 2026-08-04

## Objetivo

Crear una variante de BioGRID humano fisico filtrado excluyendo todos los pares Entrez que tambien aparecen en STRING human physical tras mapeo explicito a Entrez.

## Conteos

| Medida | Valor |
|---|---:|
| Aristas BioGRID filtradas originales | {result['original_biogrid_edges']} |
| Aristas removidas por solapamiento STRING | {result['removed_string_overlap_edges']} |
| Aristas restantes | {result['remaining_edges']} |
| Nodos restantes | {result['remaining_nodes']} |

## Split piloto

| Split | Positivos | Negativos |
|---|---:|---:|
| Train | {split_manifest['train_pos']} | {split_manifest['train_neg']} |
| Validation | {split_manifest['val_pos']} | {split_manifest['val_neg']} |
| Test | {split_manifest['test_pos']} | {split_manifest['test_neg']} |

## Checks

- Errores de split: `{split_manifest['split_errors'] if split_manifest['split_errors'] else 'None'}`
- Componentes originales: `{split_manifest['original_components']}`
- Componentes en train: `{split_manifest['train_components']}`
- Componentes preservados: `{split_manifest['train_components_preserved_by_construction']}`

## Decision

Esta ablation permite evaluar BioGRID sin el solapamiento directo observado con STRING. Es una pieza clave para no exagerar claims de generalizacion entre redes PPI.
""",
        encoding="utf-8",
    )
    (REPORTS_DIR / "biogrid_no_string_overlap.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    return 1 if split_manifest["split_errors"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
