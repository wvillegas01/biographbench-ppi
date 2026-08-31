"""Audit overlap between STRING physical and filtered BioGRID physical.

The audit maps STRING protein IDs to Entrez Gene IDs using only explicit Entrez
aliases from STRING aliases:
- Ensembl_HGNC_entrez_id
- UniProt_DR_GeneID

It then compares undirected Entrez pairs against the filtered BioGRID Entrez
edge table.
"""

from __future__ import annotations

import csv
import gzip
import json
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "data" / "raw"
PROCESSED_DIR = ROOT / "data" / "processed"
REPORTS_DIR = ROOT / "reports"

STRING_EDGES = RAW_DIR / "9606.protein.physical.links.v12.0.txt.gz"
STRING_ALIASES = RAW_DIR / "9606.protein.aliases.v12.0.txt.gz"
BIOGRID_EDGES = PROCESSED_DIR / "biogrid_human_physical" / "edges_entrez_undirected.csv"
OUT_DIR = PROCESSED_DIR / "string_biogrid_overlap"

ENTREZ_SOURCES = {"Ensembl_HGNC_entrez_id", "UniProt_DR_GeneID"}


def load_string_to_entrez() -> tuple[dict[str, set[str]], Counter[str]]:
    mapping: dict[str, set[str]] = defaultdict(set)
    source_counts: Counter[str] = Counter()
    with gzip.open(STRING_ALIASES, "rt", encoding="utf-8") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        # STRING comments the first header as #string_protein_id.
        protein_col = reader.fieldnames[0] if reader.fieldnames else "#string_protein_id"
        for row in reader:
            source = row["source"].strip()
            alias = row["alias"].strip()
            if source not in ENTREZ_SOURCES:
                continue
            if not alias.isdigit():
                continue
            protein_id = row[protein_col].strip()
            mapping[protein_id].add(alias)
            source_counts[source] += 1
    return mapping, source_counts


def load_string_edges_mapped(mapping: dict[str, set[str]]) -> tuple[set[tuple[str, str]], dict[str, object]]:
    mapped_pairs: set[tuple[str, str]] = set()
    raw_undirected_string_pairs: set[tuple[str, str]] = set()
    unmapped_edge_count = 0
    ambiguous_edge_count = 0
    expanded_edge_count = 0
    self_loops_after_mapping = 0
    string_nodes: set[str] = set()
    mapped_string_nodes: set[str] = set()

    with gzip.open(STRING_EDGES, "rt", encoding="utf-8") as handle:
        reader = csv.DictReader(handle, delimiter=" ")
        for row in reader:
            protein_a = row["protein1"]
            protein_b = row["protein2"]
            if protein_a == protein_b:
                continue
            raw_undirected_string_pairs.add(tuple(sorted((protein_a, protein_b))))
            string_nodes.update((protein_a, protein_b))

    for protein_a, protein_b in raw_undirected_string_pairs:
        entrez_a = mapping.get(protein_a, set())
        entrez_b = mapping.get(protein_b, set())
        if entrez_a:
            mapped_string_nodes.add(protein_a)
        if entrez_b:
            mapped_string_nodes.add(protein_b)
        if not entrez_a or not entrez_b:
            unmapped_edge_count += 1
            continue
        if len(entrez_a) > 1 or len(entrez_b) > 1:
            ambiguous_edge_count += 1
        for a in entrez_a:
            for b in entrez_b:
                if a == b:
                    self_loops_after_mapping += 1
                    continue
                mapped_pairs.add(tuple(sorted((a, b))))
                expanded_edge_count += 1

    stats = {
        "string_protein_nodes": len(string_nodes),
        "string_protein_nodes_with_entrez": len(mapped_string_nodes),
        "string_raw_undirected_pairs": len(raw_undirected_string_pairs),
        "string_edges_unmapped_to_entrez": unmapped_edge_count,
        "string_edges_ambiguous_entrez": ambiguous_edge_count,
        "string_entrez_pairs_after_mapping": len(mapped_pairs),
        "string_expanded_mapped_edge_rows": expanded_edge_count,
        "string_self_loops_after_mapping_skipped": self_loops_after_mapping,
    }
    return mapped_pairs, stats


def load_biogrid_edges() -> set[tuple[str, str]]:
    edges: set[tuple[str, str]] = set()
    with BIOGRID_EDGES.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            a, b = row["entrez_a"], row["entrez_b"]
            edges.add(tuple(sorted((a, b))))
    return edges


def write_overlap_edges(path: Path, overlap: set[tuple[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["entrez_a", "entrez_b"])
        writer.writeheader()
        for a, b in sorted(overlap):
            writer.writerow({"entrez_a": a, "entrez_b": b})


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    mapping, source_counts = load_string_to_entrez()
    string_pairs, string_stats = load_string_edges_mapped(mapping)
    biogrid_pairs = load_biogrid_edges()
    overlap = string_pairs & biogrid_pairs

    result = {
        "mapping_sources": sorted(ENTREZ_SOURCES),
        "mapping_source_counts": dict(source_counts),
        "string_proteins_with_entrez_mapping": len(mapping),
        **string_stats,
        "biogrid_entrez_pairs": len(biogrid_pairs),
        "overlap_entrez_pairs": len(overlap),
        "string_overlap_ratio": len(overlap) / len(string_pairs) if string_pairs else 0.0,
        "biogrid_overlap_ratio": len(overlap) / len(biogrid_pairs) if biogrid_pairs else 0.0,
        "jaccard_entrez_pair_overlap": len(overlap) / len(string_pairs | biogrid_pairs) if string_pairs or biogrid_pairs else 0.0,
    }

    write_overlap_edges(OUT_DIR / "overlap_entrez_edges.csv", overlap)
    (OUT_DIR / "overlap_manifest.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    (REPORTS_DIR / "string_biogrid_overlap.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")

    md = f"""# STRING-BioGRID Overlap Audit

Fecha: 2026-08-04

## Objetivo

Medir si STRING human physical y BioGRID human physical filtrado son datasets independientes o si comparten una fraccion sustancial de pares biologicos.

## Mapeo usado

STRING usa IDs de proteina tipo `9606.ENSP...`; BioGRID filtrado usa Entrez Gene IDs. Para evitar resolucion silenciosa, solo se usaron aliases Entrez explicitos en STRING:

- `Ensembl_HGNC_entrez_id`
- `UniProt_DR_GeneID`

## Resultados

| Medida | Valor |
|---|---:|
| Proteinas STRING con mapeo Entrez | {result['string_proteins_with_entrez_mapping']} |
| Nodos STRING fisicos | {result['string_protein_nodes']} |
| Nodos STRING fisicos con Entrez | {result['string_protein_nodes_with_entrez']} |
| Pares STRING crudos no dirigidos | {result['string_raw_undirected_pairs']} |
| Pares STRING sin mapeo Entrez completo | {result['string_edges_unmapped_to_entrez']} |
| Pares STRING con mapeo Entrez ambiguo | {result['string_edges_ambiguous_entrez']} |
| Pares STRING Entrez tras mapeo | {result['string_entrez_pairs_after_mapping']} |
| Pares BioGRID Entrez | {result['biogrid_entrez_pairs']} |
| Pares solapados | {result['overlap_entrez_pairs']} |
| Ratio de STRING cubierto por BioGRID | {result['string_overlap_ratio']:.6f} |
| Ratio de BioGRID cubierto por STRING | {result['biogrid_overlap_ratio']:.6f} |
| Jaccard de pares Entrez | {result['jaccard_entrez_pair_overlap']:.6f} |

## Decision metodologica

STRING y BioGRID no deben tratarse automaticamente como datasets independientes. El solapamiento debe reportarse y, para experimentos comparativos, conviene crear al menos una ablacion:

1. BioGRID completo filtrado;
2. BioGRID excluyendo pares presentes en STRING;
3. STRING completo;
4. STRING excluyendo pares presentes en BioGRID, cuando el mapeo Entrez sea confiable.

Esto evita inflar la evidencia de generalizacion cuando dos datasets comparten muchas interacciones.

## Archivos generados

- `{OUT_DIR / 'overlap_entrez_edges.csv'}`
- `{OUT_DIR / 'overlap_manifest.json'}`
"""
    (REPORTS_DIR / "string_biogrid_overlap.md").write_text(md, encoding="utf-8")
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
