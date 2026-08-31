"""Quality audit for BioGRID Homo sapiens Tab3.

The audit reads the human organism file from BIOGRID-ORGANISM-LATEST.tab3.zip
without extracting raw data permanently.
"""

from __future__ import annotations

import csv
import json
import zipfile
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RAW_PATH = ROOT / "data" / "raw" / "BIOGRID-ORGANISM-LATEST.tab3.zip"
REPORTS_DIR = ROOT / "reports"


HUMAN_MARKER = "BIOGRID-ORGANISM-Homo_sapiens"


def get_human_file(archive: zipfile.ZipFile) -> str:
    candidates = [
        name
        for name in archive.namelist()
        if HUMAN_MARKER in name and name.endswith(".tab3.txt")
    ]
    if len(candidates) != 1:
        raise RuntimeError(f"Expected one human BioGRID file, found {candidates}")
    return candidates[0]


def audit() -> dict[str, object]:
    rows = 0
    entrez_nodes: set[str] = set()
    biogrid_nodes: set[str] = set()
    symbol_nodes: set[str] = set()
    undirected_entrez_edges: Counter[tuple[str, str, str]] = Counter()
    undirected_entrez_pairs_any_type: Counter[tuple[str, str]] = Counter()
    exact_rows: Counter[tuple[str, str, str, str, str]] = Counter()
    self_loops = 0
    missing_entrez_a = 0
    missing_entrez_b = 0
    organism_mismatch = 0
    interaction_type_counts: Counter[str] = Counter()
    experimental_system_counts: Counter[str] = Counter()
    throughput_counts: Counter[str] = Counter()
    source_counts: Counter[str] = Counter()
    publication_counts: Counter[str] = Counter()
    score_missing = 0
    score_nonempty = 0

    with zipfile.ZipFile(RAW_PATH) as archive:
        human_file = get_human_file(archive)
        with archive.open(human_file) as raw:
            text = (line.decode("utf-8", errors="replace").rstrip("\n") for line in raw)
            reader = csv.DictReader(text, delimiter="\t")
            fieldnames = reader.fieldnames or []

            for row in reader:
                rows += 1
                entrez_a = row.get("Entrez Gene Interactor A", "").strip()
                entrez_b = row.get("Entrez Gene Interactor B", "").strip()
                biogrid_a = row.get("BioGRID ID Interactor A", "").strip()
                biogrid_b = row.get("BioGRID ID Interactor B", "").strip()
                symbol_a = row.get("Official Symbol Interactor A", "").strip()
                symbol_b = row.get("Official Symbol Interactor B", "").strip()
                system = row.get("Experimental System", "").strip()
                system_type = row.get("Experimental System Type", "").strip()
                throughput = row.get("Throughput", "").strip()
                source = row.get("Source Database", "").strip()
                publication = row.get("Publication Source", "").strip()
                score = row.get("Score", "").strip()
                org_a = row.get("Organism ID Interactor A", "").strip()
                org_b = row.get("Organism ID Interactor B", "").strip()

                if org_a != "9606" or org_b != "9606":
                    organism_mismatch += 1

                if not entrez_a or entrez_a == "-":
                    missing_entrez_a += 1
                if not entrez_b or entrez_b == "-":
                    missing_entrez_b += 1

                if entrez_a and entrez_a != "-":
                    entrez_nodes.add(entrez_a)
                if entrez_b and entrez_b != "-":
                    entrez_nodes.add(entrez_b)
                if biogrid_a and biogrid_a != "-":
                    biogrid_nodes.add(biogrid_a)
                if biogrid_b and biogrid_b != "-":
                    biogrid_nodes.add(biogrid_b)
                if symbol_a and symbol_a != "-":
                    symbol_nodes.add(symbol_a)
                if symbol_b and symbol_b != "-":
                    symbol_nodes.add(symbol_b)

                if entrez_a and entrez_b and entrez_a != "-" and entrez_b != "-":
                    if entrez_a == entrez_b:
                        self_loops += 1
                    pair = tuple(sorted((entrez_a, entrez_b)))
                    undirected_entrez_edges[(pair[0], pair[1], system_type)] += 1
                    undirected_entrez_pairs_any_type[pair] += 1
                    exact_rows[(entrez_a, entrez_b, system, system_type, publication)] += 1

                interaction_type_counts[system_type] += 1
                experimental_system_counts[system] += 1
                throughput_counts[throughput] += 1
                source_counts[source] += 1
                publication_counts[publication] += 1
                if score:
                    score_nonempty += 1
                else:
                    score_missing += 1

    exact_duplicate_rows = sum(count - 1 for count in exact_rows.values() if count > 1)
    duplicate_same_type_edges = sum(count - 1 for count in undirected_entrez_edges.values() if count > 1)
    duplicate_any_type_pairs = sum(count - 1 for count in undirected_entrez_pairs_any_type.values() if count > 1)
    physical_edges = {
        (a, b)
        for (a, b, system_type), count in undirected_entrez_edges.items()
        if system_type == "physical"
    }
    genetic_edges = {
        (a, b)
        for (a, b, system_type), count in undirected_entrez_edges.items()
        if system_type == "genetic"
    }

    return {
        "dataset_id": "biogrid_human",
        "file": RAW_PATH.name,
        "human_internal_file": human_file,
        "size_bytes": RAW_PATH.stat().st_size,
        "rows": rows,
        "columns": fieldnames,
        "unique_entrez_nodes": len(entrez_nodes),
        "unique_biogrid_nodes": len(biogrid_nodes),
        "unique_symbol_nodes": len(symbol_nodes),
        "self_loops": self_loops,
        "organism_mismatch": organism_mismatch,
        "missing_entrez_a": missing_entrez_a,
        "missing_entrez_b": missing_entrez_b,
        "unique_undirected_entrez_pairs_any_type": len(undirected_entrez_pairs_any_type),
        "unique_undirected_entrez_edges_by_type": len(undirected_entrez_edges),
        "unique_physical_pairs": len(physical_edges),
        "unique_genetic_pairs": len(genetic_edges),
        "physical_genetic_overlap_pairs": len(physical_edges & genetic_edges),
        "exact_duplicate_rows": exact_duplicate_rows,
        "duplicate_same_type_edges": duplicate_same_type_edges,
        "duplicate_any_type_pairs": duplicate_any_type_pairs,
        "score_missing": score_missing,
        "score_nonempty": score_nonempty,
        "interaction_type_counts": interaction_type_counts.most_common(),
        "top_experimental_systems": experimental_system_counts.most_common(20),
        "throughput_counts": throughput_counts.most_common(),
        "top_sources": source_counts.most_common(20),
        "top_publications": publication_counts.most_common(10),
    }


def write_reports(result: dict[str, object]) -> None:
    (REPORTS_DIR / "biogrid_quality_audit.json").write_text(
        json.dumps(result, indent=2) + "\n",
        encoding="utf-8",
    )

    md = f"""# BioGRID Homo sapiens 5.0.260 - Quality Audit

Fecha de auditoria: 2026-08-04

## Resumen

| Medida | Valor |
|---|---:|
| Archivo interno humano | `{result['human_internal_file']}` |
| Filas crudas | {result['rows']} |
| Nodos Entrez unicos | {result['unique_entrez_nodes']} |
| Nodos BioGRID unicos | {result['unique_biogrid_nodes']} |
| Nodos simbolo oficial unicos | {result['unique_symbol_nodes']} |
| Organism mismatch distinto de 9606/9606 | {result['organism_mismatch']} |
| Entrez A faltante | {result['missing_entrez_a']} |
| Entrez B faltante | {result['missing_entrez_b']} |
| Self-loops Entrez | {result['self_loops']} |
| Pares Entrez no dirigidos unicos, cualquier tipo | {result['unique_undirected_entrez_pairs_any_type']} |
| Aristas Entrez no dirigidas por tipo | {result['unique_undirected_entrez_edges_by_type']} |
| Pares fisicos unicos | {result['unique_physical_pairs']} |
| Pares geneticos unicos | {result['unique_genetic_pairs']} |
| Overlap fisico/genetico | {result['physical_genetic_overlap_pairs']} |
| Duplicados exactos de fila simplificada | {result['exact_duplicate_rows']} |
| Duplicados por par y tipo | {result['duplicate_same_type_edges']} |
| Duplicados por par sin distinguir tipo | {result['duplicate_any_type_pairs']} |

## Tipos de interaccion

"""
    for name, count in result["interaction_type_counts"]:
        md += f"- `{name}`: {count}\n"

    md += "\n## Sistemas experimentales mas frecuentes\n\n"
    for name, count in result["top_experimental_systems"]:
        md += f"- `{name}`: {count}\n"

    md += "\n## Throughput\n\n"
    for name, count in result["throughput_counts"]:
        md += f"- `{name}`: {count}\n"

    md += "\n## Fuentes principales\n\n"
    for name, count in result["top_sources"]:
        md += f"- `{name}`: {count}\n"

    md += f"""
## Decision metodologica

BioGRID humano es util como red biologica curada, pero no debe usarse cruda. Para una primera tarea PPI homogenea se recomienda:

1. filtrar `Experimental System Type == physical`;
2. remover self-loops;
3. colapsar multiples evidencias del mismo par Entrez en una sola arista;
4. conservar conteo de evidencias, sistemas experimentales y fuentes como metadatos;
5. decidir si se excluyen high-throughput o si se usan como ablacion;
6. medir solapamiento con STRING antes de declararlo dataset independiente.

La tabla cruda contiene muchas evidencias repetidas por par; eso es biologicamente valioso, pero para link prediction debe separarse claramente la unidad experimental de la unidad de arista.
"""
    (REPORTS_DIR / "biogrid_quality_audit.md").write_text(md, encoding="utf-8")

    csv_path = REPORTS_DIR / "biogrid_quality_audit_summary.csv"
    fields = [
        "dataset_id",
        "rows",
        "unique_entrez_nodes",
        "self_loops",
        "unique_undirected_entrez_pairs_any_type",
        "unique_physical_pairs",
        "unique_genetic_pairs",
        "duplicate_same_type_edges",
        "duplicate_any_type_pairs",
        "organism_mismatch",
    ]
    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerow({field: result[field] for field in fields})


def main() -> int:
    result = audit()
    write_reports(result)
    print(
        "BioGRID audit complete: "
        f"{result['rows']} rows, "
        f"{result['unique_physical_pairs']} physical pairs, "
        f"{result['unique_genetic_pairs']} genetic pairs"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
