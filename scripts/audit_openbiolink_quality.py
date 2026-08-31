"""Quality audit for OpenBioLink2020 HQ directed.

The audit checks the official split files inside HQ_DIR.zip without extracting
or modifying raw data.
"""

from __future__ import annotations

import csv
import hashlib
import json
import zipfile
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RAW_PATH = ROOT / "data" / "raw" / "HQ_DIR.zip"
REPORTS_DIR = ROOT / "reports"


SPLIT_FILES = {
    "train_pos": "HQ_DIR/train_test_data/train_sample.csv",
    "val_pos": "HQ_DIR/train_test_data/val_sample.csv",
    "test_pos": "HQ_DIR/train_test_data/test_sample.csv",
    "train_neg": "HQ_DIR/train_test_data/negative_train_sample.csv",
    "val_neg": "HQ_DIR/train_test_data/negative_val_sample.csv",
    "test_neg": "HQ_DIR/train_test_data/negative_test_sample.csv",
}


def triple_digest(subject: str, relation: str, obj: str) -> bytes:
    return hashlib.blake2b(
        f"{subject}\t{relation}\t{obj}".encode("utf-8"),
        digest_size=16,
    ).digest()


def read_nodes(archive: zipfile.ZipFile) -> tuple[dict[str, str], Counter[str]]:
    node_types: dict[str, str] = {}
    type_counts: Counter[str] = Counter()
    with archive.open("HQ_DIR/graph_files/nodes.csv") as raw:
        text = (line.decode("utf-8", errors="replace").strip() for line in raw)
        for line in text:
            parts = line.split("\t")
            if len(parts) >= 2:
                node_types[parts[0]] = parts[1]
                type_counts[parts[1]] += 1
    return node_types, type_counts


def read_graph_props(archive: zipfile.ZipFile) -> dict[str, str]:
    with archive.open("HQ_DIR/graph_files/graph_props.json") as raw:
        return json.loads(raw.read().decode("utf-8", errors="replace"))


def audit() -> dict[str, object]:
    split_sets: dict[str, set[bytes]] = {}
    split_counts: dict[str, int] = {}
    duplicate_counts: dict[str, int] = {}
    bad_label_counts: dict[str, int] = {}
    relation_counts: Counter[str] = Counter()
    source_counts: Counter[str] = Counter()
    touched_nodes: set[str] = set()
    same_relation_reverse_hits: dict[str, int] = {}

    with zipfile.ZipFile(RAW_PATH) as archive:
        node_types, node_type_counts = read_nodes(archive)
        graph_props = read_graph_props(archive)

        for split_name, internal_path in SPLIT_FILES.items():
            expected_label = "1" if split_name.endswith("_pos") else "0"
            seen: set[bytes] = set()
            duplicates = 0
            bad_labels = 0
            rows = 0
            with archive.open(internal_path) as raw:
                for raw_line in raw:
                    line = raw_line.decode("utf-8", errors="replace").strip()
                    if not line:
                        continue
                    parts = line.split("\t")
                    if len(parts) < 5:
                        bad_labels += 1
                        continue
                    subject, relation, obj = parts[0], parts[1], parts[2]
                    label = parts[4]
                    source = parts[5] if len(parts) > 5 else "Unknown"
                    digest = triple_digest(subject, relation, obj)
                    if digest in seen:
                        duplicates += 1
                    seen.add(digest)
                    if label != expected_label:
                        bad_labels += 1
                    relation_counts[relation] += 1
                    source_counts[source] += 1
                    touched_nodes.add(subject)
                    touched_nodes.add(obj)
                    rows += 1
            split_sets[split_name] = seen
            split_counts[split_name] = rows
            duplicate_counts[split_name] = duplicates
            bad_label_counts[split_name] = bad_labels

        positives = split_sets["train_pos"] | split_sets["val_pos"] | split_sets["test_pos"]
        negatives = split_sets["train_neg"] | split_sets["val_neg"] | split_sets["test_neg"]

        overlaps: dict[str, int] = {}
        names = sorted(split_sets)
        for i, left in enumerate(names):
            for right in names[i + 1 :]:
                overlaps[f"{left}__{right}"] = len(split_sets[left] & split_sets[right])

        pos_neg_overlap = len(positives & negatives)

        # Same-relation reverse check is a conservative signal for directed KG
        # leakage. It does not detect curated inverse-relation pairs.
        for split_name, internal_path in SPLIT_FILES.items():
            reverse_hits = 0
            target = positives if split_name.endswith("_neg") else split_sets[split_name]
            with archive.open(internal_path) as raw:
                for raw_line in raw:
                    parts = raw_line.decode("utf-8", errors="replace").strip().split("\t")
                    if len(parts) < 3:
                        continue
                    subject, relation, obj = parts[0], parts[1], parts[2]
                    if triple_digest(obj, relation, subject) in target:
                        reverse_hits += 1
            same_relation_reverse_hits[split_name] = reverse_hits

    return {
        "dataset_id": "openbiolink2020_hq_directed",
        "file": RAW_PATH.name,
        "size_bytes": RAW_PATH.stat().st_size,
        "graph_directed": graph_props.get("DIRECTED", "Unknown"),
        "node_type_counts": dict(node_type_counts),
        "nodes_in_nodes_csv": len(node_types),
        "nodes_touched_by_split_triples": len(touched_nodes),
        "split_counts": split_counts,
        "duplicate_counts": duplicate_counts,
        "bad_label_counts": bad_label_counts,
        "overlaps": overlaps,
        "positive_negative_overlap": pos_neg_overlap,
        "same_relation_reverse_hits": same_relation_reverse_hits,
        "unique_positive_triples": len(positives),
        "unique_negative_triples": len(negatives),
        "relation_count": len(relation_counts),
        "top_relations": relation_counts.most_common(15),
        "top_sources": source_counts.most_common(15),
    }


def write_reports(result: dict[str, object]) -> None:
    (REPORTS_DIR / "openbiolink_quality_audit.json").write_text(
        json.dumps(result, indent=2) + "\n",
        encoding="utf-8",
    )

    split_counts = result["split_counts"]
    duplicate_counts = result["duplicate_counts"]
    bad_label_counts = result["bad_label_counts"]
    overlaps = result["overlaps"]
    reverse_hits = result["same_relation_reverse_hits"]

    overlap_errors = {key: value for key, value in overlaps.items() if value}
    duplicate_errors = {key: value for key, value in duplicate_counts.items() if value}
    bad_label_errors = {key: value for key, value in bad_label_counts.items() if value}

    lines = [
        "# OpenBioLink2020 HQ Directed - Quality Audit",
        "",
        "Fecha de auditoria: 2026-08-04",
        "",
        "## Resumen",
        "",
        f"- Archivo: `{result['file']}`",
        f"- Tamano: `{result['size_bytes']}` bytes",
        f"- Grafo dirigido segun `graph_props.json`: `{result['graph_directed']}`",
        f"- Nodos en `nodes.csv`: `{result['nodes_in_nodes_csv']}`",
        f"- Nodos tocados por triples de splits: `{result['nodes_touched_by_split_triples']}`",
        f"- Relaciones observadas en splits: `{result['relation_count']}`",
        f"- Triples positivos unicos: `{result['unique_positive_triples']}`",
        f"- Triples negativos unicos: `{result['unique_negative_triples']}`",
        "",
        "## Conteos por split",
        "",
        "| Split | Filas | Duplicados exactos | Etiquetas inesperadas | Reverse same-relation hits |",
        "|---|---:|---:|---:|---:|",
    ]
    for split in SPLIT_FILES:
        lines.append(
            f"| `{split}` | {split_counts[split]} | {duplicate_counts[split]} | "
            f"{bad_label_counts[split]} | {reverse_hits[split]} |"
        )

    lines.extend(
        [
            "",
            "## Checks de leakage",
            "",
            f"- Overlap positivo/negativo exacto: `{result['positive_negative_overlap']}`",
            f"- Overlaps entre splits con valor distinto de cero: `{overlap_errors if overlap_errors else 'None'}`",
            f"- Duplicados internos con valor distinto de cero: `{duplicate_errors if duplicate_errors else 'None'}`",
            f"- Etiquetas inesperadas: `{bad_label_errors if bad_label_errors else 'None'}`",
            "",
            "El chequeo `reverse same-relation hits` busca triples inversos con la misma relacion. En positivos puede reflejar relaciones simetricas reales; en negativos es una alerta de posible leakage para relaciones que deban tratarse como no dirigidas o simetricas.",
            "",
            "## Tipos de nodo",
            "",
        ]
    )
    for node_type, count in sorted(result["node_type_counts"].items()):
        lines.append(f"- `{node_type}`: {count}")

    lines.extend(["", "## Relaciones mas frecuentes", ""])
    for relation, count in result["top_relations"]:
        lines.append(f"- `{relation}`: {count}")

    lines.extend(["", "## Fuentes mas frecuentes", ""])
    for source, count in result["top_sources"]:
        lines.append(f"- `{source}`: {count}")

    lines.extend(
        [
            "",
            "## Decision metodologica",
            "",
            "OpenBioLink HQ directed es util como candidato de KG link prediction porque ya trae positivos, negativos y splits. Antes de aceptarlo como dataset principal, el siguiente control debe revisar relaciones inversas semanticas, no solo inversas con el mismo nombre. La auditoria actual sugiere filtrar o marcar negativos con inverso positivo de la misma relacion antes de comparar modelos.",
        ]
    )

    (REPORTS_DIR / "openbiolink_quality_audit.md").write_text("\n".join(lines), encoding="utf-8")

    csv_path = REPORTS_DIR / "openbiolink_quality_audit_summary.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["split", "rows", "duplicates", "bad_labels", "same_relation_reverse_hits"],
        )
        writer.writeheader()
        for split in SPLIT_FILES:
            writer.writerow(
                {
                    "split": split,
                    "rows": split_counts[split],
                    "duplicates": duplicate_counts[split],
                    "bad_labels": bad_label_counts[split],
                    "same_relation_reverse_hits": reverse_hits[split],
                }
            )


def main() -> int:
    result = audit()
    write_reports(result)
    print(
        "OpenBioLink audit complete: "
        f"{result['unique_positive_triples']} positives, "
        f"{result['unique_negative_triples']} negatives, "
        f"pos/neg overlap={result['positive_negative_overlap']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
