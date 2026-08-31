"""Build a filtered BioGRID Homo sapiens physical interaction edge table.

Input:
- data/raw/BIOGRID-ORGANISM-LATEST.tab3.zip

Output:
- data/processed/biogrid_human_physical/edges_entrez_undirected.csv
- data/processed/biogrid_human_physical/filter_manifest.json
- reports/biogrid_filtered_physical.md

This is preprocessing for audit readiness, not model training.
"""

from __future__ import annotations

import csv
import json
import zipfile
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RAW_PATH = ROOT / "data" / "raw" / "BIOGRID-ORGANISM-LATEST.tab3.zip"
OUT_DIR = ROOT / "data" / "processed" / "biogrid_human_physical"
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


def compact_counter(counter: Counter[str]) -> str:
    return ";".join(f"{key}:{value}" for key, value in sorted(counter.items()))


def build() -> dict[str, object]:
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    raw_rows = 0
    kept_rows = 0
    excluded = Counter()
    edge_evidence_count: Counter[tuple[str, str]] = Counter()
    edge_systems: dict[tuple[str, str], Counter[str]] = defaultdict(Counter)
    edge_throughput: dict[tuple[str, str], Counter[str]] = defaultdict(Counter)
    edge_publications: dict[tuple[str, str], set[str]] = defaultdict(set)
    edge_symbols: dict[tuple[str, str], tuple[str, str]] = {}
    node_ids: set[str] = set()
    system_counts: Counter[str] = Counter()
    throughput_counts: Counter[str] = Counter()

    with zipfile.ZipFile(RAW_PATH) as archive:
        human_file = get_human_file(archive)
        with archive.open(human_file) as raw:
            text = (line.decode("utf-8", errors="replace").rstrip("\n") for line in raw)
            reader = csv.DictReader(text, delimiter="\t")
            for row in reader:
                raw_rows += 1
                system_type = row.get("Experimental System Type", "").strip()
                org_a = row.get("Organism ID Interactor A", "").strip()
                org_b = row.get("Organism ID Interactor B", "").strip()
                entrez_a = row.get("Entrez Gene Interactor A", "").strip()
                entrez_b = row.get("Entrez Gene Interactor B", "").strip()

                if system_type != "physical":
                    excluded["not_physical"] += 1
                    continue
                if org_a != "9606" or org_b != "9606":
                    excluded["not_human_human"] += 1
                    continue
                if not entrez_a or not entrez_b or entrez_a == "-" or entrez_b == "-":
                    excluded["missing_entrez"] += 1
                    continue
                if entrez_a == entrez_b:
                    excluded["self_loop"] += 1
                    continue

                a, b = sorted((entrez_a, entrez_b))
                edge = (a, b)
                kept_rows += 1
                node_ids.update(edge)
                edge_evidence_count[edge] += 1
                edge_systems[edge][row.get("Experimental System", "").strip()] += 1
                edge_throughput[edge][row.get("Throughput", "").strip()] += 1
                publication = row.get("Publication Source", "").strip()
                if publication:
                    edge_publications[edge].add(publication)
                symbol_a = row.get("Official Symbol Interactor A", "").strip()
                symbol_b = row.get("Official Symbol Interactor B", "").strip()
                edge_symbols.setdefault(edge, (symbol_a, symbol_b))
                system_counts[row.get("Experimental System", "").strip()] += 1
                throughput_counts[row.get("Throughput", "").strip()] += 1

    edges_path = OUT_DIR / "edges_entrez_undirected.csv"
    with edges_path.open("w", newline="", encoding="utf-8") as handle:
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
        for edge, evidence_count in sorted(edge_evidence_count.items()):
            symbol_a, symbol_b = edge_symbols.get(edge, ("", ""))
            writer.writerow(
                {
                    "entrez_a": edge[0],
                    "entrez_b": edge[1],
                    "symbol_a": symbol_a,
                    "symbol_b": symbol_b,
                    "label": 1,
                    "evidence_count": evidence_count,
                    "publication_count": len(edge_publications[edge]),
                    "experimental_systems": compact_counter(edge_systems[edge]),
                    "throughput": compact_counter(edge_throughput[edge]),
                }
            )

    possible_edges = len(node_ids) * (len(node_ids) - 1) / 2
    density = len(edge_evidence_count) / possible_edges if possible_edges else 0.0
    evidence_values = list(edge_evidence_count.values())
    manifest = {
        "dataset_id": "biogrid_human_physical_filtered",
        "source_dataset": "biogrid_human",
        "raw_file": str(RAW_PATH),
        "output_file": str(edges_path),
        "raw_rows": raw_rows,
        "kept_evidence_rows": kept_rows,
        "excluded": dict(excluded),
        "unique_nodes_entrez": len(node_ids),
        "unique_undirected_edges": len(edge_evidence_count),
        "density": density,
        "min_evidence_count": min(evidence_values) if evidence_values else 0,
        "max_evidence_count": max(evidence_values) if evidence_values else 0,
        "mean_evidence_count": sum(evidence_values) / len(evidence_values) if evidence_values else 0.0,
        "top_experimental_systems": system_counts.most_common(20),
        "throughput_counts": throughput_counts.most_common(),
        "filter_policy": {
            "experimental_system_type": "physical",
            "organism_a": "9606",
            "organism_b": "9606",
            "remove_missing_entrez": True,
            "remove_self_loops": True,
            "collapse_undirected_entrez_pairs": True,
        },
    }
    (OUT_DIR / "filter_manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return manifest


def write_report(manifest: dict[str, object]) -> None:
    excluded = manifest["excluded"]
    md = f"""# BioGRID Human Physical Filtered Dataset

Fecha: 2026-08-04

## Objetivo

Crear una version filtrada y auditable de BioGRID Homo sapiens para una futura tarea de link prediction PPI homogenea.

## Politica de filtrado

1. Mantener solo `Experimental System Type == physical`.
2. Mantener solo interacciones humano-humano: `Organism ID Interactor A == 9606` y `Organism ID Interactor B == 9606`.
3. Excluir filas sin Entrez Gene ID.
4. Excluir self-loops.
5. Colapsar pares Entrez no dirigidos.
6. Conservar `evidence_count`, `publication_count`, sistemas experimentales y throughput como metadatos.

## Conteos

| Medida | Valor |
|---|---:|
| Filas crudas | {manifest['raw_rows']} |
| Filas de evidencia conservadas | {manifest['kept_evidence_rows']} |
| Nodos Entrez unicos | {manifest['unique_nodes_entrez']} |
| Aristas no dirigidas unicas | {manifest['unique_undirected_edges']} |
| Densidad | {manifest['density']:.8f} |
| Evidencia minima por arista | {manifest['min_evidence_count']} |
| Evidencia media por arista | {manifest['mean_evidence_count']:.4f} |
| Evidencia maxima por arista | {manifest['max_evidence_count']} |

## Exclusiones

"""
    for reason, count in sorted(excluded.items()):
        md += f"- `{reason}`: {count}\n"

    md += "\n## Sistemas experimentales principales\n\n"
    for name, count in manifest["top_experimental_systems"]:
        md += f"- `{name}`: {count}\n"

    md += "\n## Throughput\n\n"
    for name, count in manifest["throughput_counts"]:
        md += f"- `{name}`: {count}\n"

    md += f"""
## Archivos generados

- `{manifest['output_file']}`
- `{Path(manifest['output_file']).with_name('filter_manifest.json')}`

## Decision

Esta version filtrada es mucho mas adecuada que BioGRID crudo para una tarea PPI homogenea. Todavia falta construir splits de link prediction y medir solapamiento biologico con STRING mediante una capa de mapeo de identificadores.
"""
    (REPORTS_DIR / "biogrid_filtered_physical.md").write_text(md, encoding="utf-8")
    (REPORTS_DIR / "biogrid_filtered_physical.json").write_text(
        json.dumps(manifest, indent=2) + "\n",
        encoding="utf-8",
    )


def main() -> int:
    manifest = build()
    write_report(manifest)
    print(
        "BioGRID filtered physical built: "
        f"{manifest['unique_nodes_entrez']} nodes, "
        f"{manifest['unique_undirected_edges']} edges"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
