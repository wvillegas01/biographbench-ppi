"""Build STRING physical ablation excluding pairs observed in BioGRID.

STRING is stored as STRING protein IDs. The overlap was computed in Entrez
space, so this script removes any STRING protein pair whose explicit Entrez
mapping intersects an overlapping STRING-BioGRID Entrez pair.
"""

from __future__ import annotations

import csv
import gzip
import json
import sys
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from biographbench.splits import build_link_prediction_split

RAW_DIR = ROOT / "data" / "raw"
PROCESSED_DIR = ROOT / "data" / "processed"
REPORTS_DIR = ROOT / "reports"

STRING_EDGES = RAW_DIR / "9606.protein.physical.links.v12.0.txt.gz"
STRING_ALIASES = RAW_DIR / "9606.protein.aliases.v12.0.txt.gz"
OVERLAP_EDGES = PROCESSED_DIR / "string_biogrid_overlap" / "overlap_entrez_edges.csv"
OUT_DIR = PROCESSED_DIR / "string_human_physical_no_biogrid_overlap"
SPLIT_DIR = OUT_DIR / "splits"

ENTREZ_SOURCES = {"Ensembl_HGNC_entrez_id", "UniProt_DR_GeneID"}
SEED = 42
VAL_RATIO = 0.10
TEST_RATIO = 0.10


def load_string_to_entrez() -> dict[str, set[str]]:
    mapping: dict[str, set[str]] = defaultdict(set)
    with gzip.open(STRING_ALIASES, "rt", encoding="utf-8") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        protein_col = reader.fieldnames[0] if reader.fieldnames else "#string_protein_id"
        for row in reader:
            source = row["source"].strip()
            alias = row["alias"].strip()
            if source in ENTREZ_SOURCES and alias.isdigit():
                mapping[row[protein_col].strip()].add(alias)
    return mapping


def load_overlap_entrez() -> set[tuple[str, str]]:
    overlap: set[tuple[str, str]] = set()
    with OVERLAP_EDGES.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            overlap.add(tuple(sorted((row["entrez_a"], row["entrez_b"]))))
    return overlap


def read_string_edges() -> dict[tuple[str, str], int]:
    edges: dict[tuple[str, str], int] = {}
    with gzip.open(STRING_EDGES, "rt", encoding="utf-8") as handle:
        reader = csv.DictReader(handle, delimiter=" ")
        for row in reader:
            a, b = row["protein1"], row["protein2"]
            if a == b:
                continue
            edge = tuple(sorted((a, b)))
            score = int(row["combined_score"])
            edges[edge] = max(score, edges.get(edge, score))
    return edges


def edge_maps_to_overlap(edge: tuple[str, str], mapping: dict[str, set[str]], overlap_entrez: set[tuple[str, str]]) -> bool:
    left = mapping.get(edge[0], set())
    right = mapping.get(edge[1], set())
    for a in left:
        for b in right:
            if a != b and tuple(sorted((a, b))) in overlap_entrez:
                return True
    return False


def write_edges(path: Path, edges: dict[tuple[str, str], int]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["protein1", "protein2", "label", "combined_score"])
        writer.writeheader()
        for (a, b), score in sorted(edges.items()):
            writer.writerow({"protein1": a, "protein2": b, "label": 1, "combined_score": score})


def write_split_edges(path: Path, edges: list[tuple[str, str]], label: int, scores: dict[tuple[str, str], int] | None = None) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["protein1", "protein2", "label", "combined_score"])
        writer.writeheader()
        for a, b in edges:
            writer.writerow(
                {
                    "protein1": a,
                    "protein2": b,
                    "label": label,
                    "combined_score": scores.get((a, b), "") if scores else "",
                }
            )


def build_splits(edges: dict[tuple[str, str], int]) -> dict[str, object]:
    SPLIT_DIR.mkdir(parents=True, exist_ok=True)
    split = build_link_prediction_split(edges.keys(), seed=SEED, val_ratio=VAL_RATIO, test_ratio=TEST_RATIO)
    train_pos = split.train_pos
    val_pos = split.val_pos
    test_pos = split.test_pos
    train_neg = split.train_neg
    val_neg = split.val_neg
    test_neg = split.test_neg

    write_split_edges(SPLIT_DIR / "train_pos.csv", train_pos, 1, edges)
    write_split_edges(SPLIT_DIR / "val_pos.csv", val_pos, 1, edges)
    write_split_edges(SPLIT_DIR / "test_pos.csv", test_pos, 1, edges)
    write_split_edges(SPLIT_DIR / "train_neg.csv", train_neg, 0)
    write_split_edges(SPLIT_DIR / "val_neg.csv", val_neg, 0)
    write_split_edges(SPLIT_DIR / "test_neg.csv", test_neg, 0)

    manifest = split.manifest("string_human_physical_no_biogrid_overlap", SPLIT_DIR)
    (SPLIT_DIR / "split_manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return manifest


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    mapping = load_string_to_entrez()
    overlap_entrez = load_overlap_entrez()
    original_edges = read_string_edges()

    kept: dict[tuple[str, str], int] = {}
    removed = 0
    unmapped_kept = 0
    for edge, score in original_edges.items():
        if edge_maps_to_overlap(edge, mapping, overlap_entrez):
            removed += 1
            continue
        kept[edge] = score
        if not mapping.get(edge[0]) or not mapping.get(edge[1]):
            unmapped_kept += 1

    write_edges(OUT_DIR / "edges_undirected.csv", kept)
    split_manifest = build_splits(kept)

    result = {
        "dataset_id": "string_human_physical_no_biogrid_overlap",
        "source_dataset": "string_human_physical_v12",
        "overlap_source": str(OVERLAP_EDGES),
        "original_string_edges": len(original_edges),
        "removed_biogrid_overlap_edges": removed,
        "remaining_edges": len(kept),
        "remaining_nodes": split_manifest["nodes"],
        "remaining_edges_with_incomplete_entrez_mapping": unmapped_kept,
        "split": split_manifest,
    }
    (OUT_DIR / "ablation_manifest.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    (REPORTS_DIR / "string_no_biogrid_overlap.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    (REPORTS_DIR / "string_no_biogrid_overlap.md").write_text(
        f"""# STRING No-BioGRID-Overlap Ablation

Fecha: 2026-08-04

## Objetivo

Crear una variante de STRING human physical excluyendo pares que se solapan con BioGRID filtrado, usando mapeo explicito STRING protein ID -> Entrez.

## Conteos

| Medida | Valor |
|---|---:|
| Aristas STRING originales no dirigidas | {result['original_string_edges']} |
| Aristas removidas por solapamiento BioGRID | {result['removed_biogrid_overlap_edges']} |
| Aristas restantes | {result['remaining_edges']} |
| Nodos restantes | {result['remaining_nodes']} |
| Aristas restantes con mapeo Entrez incompleto | {result['remaining_edges_with_incomplete_entrez_mapping']} |

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

Esta ablation complementa la version BioGRID sin STRING. Debe interpretarse con cuidado: remover solapamiento en STRING depende del mapeo Entrez disponible y puede dejar pares no removidos si el mapeo es incompleto.
""",
        encoding="utf-8",
    )
    print(json.dumps(result, indent=2))
    return 1 if split_manifest["split_errors"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
