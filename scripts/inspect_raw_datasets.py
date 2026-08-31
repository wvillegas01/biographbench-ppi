"""Inspect downloaded raw datasets without modifying them.

Outputs:
- reports/raw_dataset_inspection.md
- reports/raw_dataset_inspection_summary.csv

This is a structural audit only: no benchmark-ready preprocessing happens here.
"""

from __future__ import annotations

import csv
import gzip
import io
import json
import zipfile
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "data" / "raw"
REPORTS_DIR = ROOT / "reports"


def sha_from_manifest(dataset_id: str) -> str:
    path = ROOT / "data" / "manifests" / f"{dataset_id}.json"
    if not path.exists():
        return ""
    return json.loads(path.read_text(encoding="utf-8")).get("sha256", "")


def inspect_string_physical() -> dict[str, object]:
    path = RAW_DIR / "9606.protein.physical.links.v12.0.txt.gz"
    node_ids: set[str] = set()
    edge_counter: Counter[tuple[str, str]] = Counter()
    self_loops = 0
    rows = 0
    min_score: int | None = None
    max_score: int | None = None
    header: list[str] = []
    sample: list[list[str]] = []

    with gzip.open(path, "rt", encoding="utf-8") as handle:
        reader = csv.reader(handle, delimiter=" ")
        header = next(reader)
        for row in reader:
            if not row:
                continue
            rows += 1
            if len(sample) < 5:
                sample.append(row)
            protein1, protein2, combined_score = row[0], row[1], int(row[2])
            node_ids.update((protein1, protein2))
            if protein1 == protein2:
                self_loops += 1
            edge_counter[(protein1, protein2)] += 1
            min_score = combined_score if min_score is None else min(min_score, combined_score)
            max_score = combined_score if max_score is None else max(max_score, combined_score)

    undirected_pairs = {tuple(sorted(edge)) for edge in edge_counter}
    duplicated_directed_edges = sum(count - 1 for count in edge_counter.values() if count > 1)
    reciprocal_pairs = len(edge_counter) - len(undirected_pairs)

    return {
        "dataset_id": "string_human_physical_v12",
        "file": path.name,
        "format": "gzip text, space-delimited",
        "size_bytes": path.stat().st_size,
        "sha256": sha_from_manifest("string_human_physical_v12"),
        "internal_files": "1 compressed table",
        "columns": "; ".join(header),
        "rows_edges": rows,
        "unique_nodes": len(node_ids),
        "directed_duplicate_edges": duplicated_directed_edges,
        "self_loops": self_loops,
        "reciprocal_or_symmetric_entries": reciprocal_pairs,
        "min_score": min_score,
        "max_score": max_score,
        "notes": "Physical protein associations for Homo sapiens; entries appear as directed/symmetric rows and should be deduplicated for undirected PPI tasks.",
        "sample_rows": sample,
    }


def inspect_openbiolink() -> dict[str, object]:
    path = RAW_DIR / "HQ_DIR.zip"
    files: list[zipfile.ZipInfo]
    with zipfile.ZipFile(path) as archive:
        files = archive.infolist()
        names = [info.filename for info in files]
        sample_by_file: dict[str, list[str]] = {}
        counts_by_file: dict[str, int] = {}
        nodes: set[str] = set()
        relations: Counter[str] = Counter()
        edge_rows = 0

        for name in names:
            if name.endswith("/"):
                continue
            with archive.open(name) as raw:
                text = io.TextIOWrapper(raw, encoding="utf-8", errors="replace")
                lines = []
                count = 0
                for line in text:
                    stripped = line.rstrip("\n")
                    if count < 5:
                        lines.append(stripped)
                    count += 1
                    parts = stripped.split("\t")
                    if len(parts) >= 3 and any(split in name.lower() for split in ("train", "test", "valid")):
                        nodes.add(parts[0])
                        nodes.add(parts[2])
                        relations[parts[1]] += 1
                        edge_rows += 1
                sample_by_file[name] = lines
                counts_by_file[name] = count

    return {
        "dataset_id": "openbiolink2020_hq_directed",
        "file": path.name,
        "format": "zip archive",
        "size_bytes": path.stat().st_size,
        "sha256": sha_from_manifest("openbiolink2020_hq_directed"),
        "internal_files": "; ".join(names),
        "columns": "Triples inferred as subject; relation; object for split files",
        "rows_edges": edge_rows,
        "unique_nodes": len(nodes) if nodes else "Unknown",
        "directed_duplicate_edges": "Not checked yet",
        "self_loops": "Not checked yet",
        "reciprocal_or_symmetric_entries": "Not checked yet",
        "min_score": "NA",
        "max_score": "NA",
        "notes": f"Archive contains {len([n for n in names if not n.endswith('/')])} files. Parsed split-like TSV files for preliminary entity/relation counts.",
        "sample_rows": sample_by_file,
        "counts_by_file": counts_by_file,
        "top_relations": relations.most_common(10),
    }


def inspect_biogrid() -> dict[str, object]:
    path = RAW_DIR / "BIOGRID-ORGANISM-LATEST.tab3.zip"
    human_candidates: list[str] = []
    with zipfile.ZipFile(path) as archive:
        files = archive.infolist()
        names = [info.filename for info in files if not info.filename.endswith("/")]
        for name in names:
            lower = name.lower()
            if "homo_sapiens" in lower or "9606" in lower or "homo sapiens" in lower:
                human_candidates.append(name)

        selected = human_candidates[0] if human_candidates else None
        rows = 0
        node_ids: set[str] = set()
        self_loops = 0
        header: list[str] = []
        sample: list[list[str]] = []
        interaction_types: Counter[str] = Counter()

        if selected:
            with archive.open(selected) as raw:
                text = io.TextIOWrapper(raw, encoding="utf-8", errors="replace")
                reader = csv.reader(text, delimiter="\t")
                header = next(reader)
                header_index = {name: i for i, name in enumerate(header)}
                a_idx = header_index.get("Entrez Gene Interactor A")
                b_idx = header_index.get("Entrez Gene Interactor B")
                type_idx = header_index.get("Experimental System Type")
                for row in reader:
                    rows += 1
                    if len(sample) < 5:
                        sample.append(row)
                    if a_idx is not None and b_idx is not None and len(row) > max(a_idx, b_idx):
                        a, b = row[a_idx], row[b_idx]
                        node_ids.update((a, b))
                        if a == b:
                            self_loops += 1
                    if type_idx is not None and len(row) > type_idx:
                        interaction_types[row[type_idx]] += 1

    return {
        "dataset_id": "biogrid_human",
        "file": path.name,
        "format": "zip archive, BioGRID Tab3",
        "size_bytes": path.stat().st_size,
        "sha256": sha_from_manifest("biogrid_organism_latest_tab3"),
        "internal_files": f"{len(names)} organism files",
        "columns": "; ".join(header) if header else "Unknown",
        "rows_edges": rows if human_candidates else "Unknown",
        "unique_nodes": len(node_ids) if human_candidates else "Unknown",
        "directed_duplicate_edges": "Not checked yet",
        "self_loops": self_loops if human_candidates else "Unknown",
        "reciprocal_or_symmetric_entries": "Not checked yet",
        "min_score": "NA",
        "max_score": "NA",
        "notes": f"Human candidate files: {'; '.join(human_candidates[:5]) if human_candidates else 'none found'}",
        "sample_rows": sample,
        "top_interaction_types": interaction_types.most_common(),
    }


def write_summary_csv(results: list[dict[str, object]]) -> None:
    fields = [
        "dataset_id",
        "file",
        "format",
        "size_bytes",
        "sha256",
        "internal_files",
        "columns",
        "rows_edges",
        "unique_nodes",
        "directed_duplicate_edges",
        "self_loops",
        "reciprocal_or_symmetric_entries",
        "min_score",
        "max_score",
        "notes",
    ]
    path = REPORTS_DIR / "raw_dataset_inspection_summary.csv"
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for result in results:
            writer.writerow({field: result.get(field, "") for field in fields})


def table_row(result: dict[str, object]) -> str:
    return (
        f"| `{result['dataset_id']}` | `{result['file']}` | {result['format']} | "
        f"{result['rows_edges']} | {result['unique_nodes']} | {result['self_loops']} | "
        f"{result['directed_duplicate_edges']} | {result['notes']} |"
    )


def write_markdown(results: list[dict[str, object]]) -> None:
    lines = [
        "# Raw Dataset Inspection",
        "",
        "Fecha de inspeccion: 2026-08-04",
        "",
        "Esta inspeccion revisa estructura, columnas y conteos iniciales sin modificar los archivos crudos.",
        "",
        "## Resumen",
        "",
        "| Dataset | Archivo | Formato | Filas/aristas | Nodos unicos | Self-loops | Duplicados dirigidos | Nota |",
        "|---|---|---|---:|---:|---:|---:|---|",
    ]
    lines.extend(table_row(result) for result in results)
    lines.append("")

    for result in results:
        lines.extend(
            [
                f"## {result['dataset_id']}",
                "",
                f"- Archivo: `{result['file']}`",
                f"- Tamano: `{result['size_bytes']}` bytes",
                f"- SHA-256: `{result['sha256']}`",
                f"- Archivos internos: {result['internal_files']}",
                f"- Columnas: {result['columns']}",
                "",
            ]
        )

        if result["dataset_id"] == "openbiolink2020_hq_directed":
            lines.append("### Archivos internos y conteos")
            lines.append("")
            for name, count in result["counts_by_file"].items():
                lines.append(f"- `{name}`: {count} lineas")
            lines.append("")
            lines.append("### Relaciones mas frecuentes")
            lines.append("")
            for relation, count in result["top_relations"]:
                lines.append(f"- `{relation}`: {count}")
            lines.append("")

        if result["dataset_id"] == "biogrid_human":
            lines.append("### Tipos de interaccion")
            lines.append("")
            for interaction_type, count in result["top_interaction_types"]:
                lines.append(f"- `{interaction_type}`: {count}")
            lines.append("")

        lines.append("### Muestra")
        lines.append("")
        sample = result["sample_rows"]
        if isinstance(sample, dict):
            for name, rows in sample.items():
                lines.append(f"`{name}`")
                lines.append("")
                lines.append("```text")
                lines.extend(rows[:5])
                lines.append("```")
                lines.append("")
        else:
            lines.append("```text")
            for row in sample[:5]:
                lines.append("\t".join(row))
            lines.append("```")
            lines.append("")

    (REPORTS_DIR / "raw_dataset_inspection.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    results = [
        inspect_string_physical(),
        inspect_openbiolink(),
        inspect_biogrid(),
    ]
    write_summary_csv(results)
    write_markdown(results)
    for result in results:
        print(f"{result['dataset_id']}: rows={result['rows_edges']} nodes={result['unique_nodes']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
