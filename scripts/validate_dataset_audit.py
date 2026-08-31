"""Validate the BioGraphBench dataset audit CSV schema.

This script intentionally checks only the audit table contract. It does not
download data or decide eligibility.
"""

from __future__ import annotations

import csv
import sys
from pathlib import Path


REQUIRED_COLUMNS = [
    "dataset_id",
    "dataset_name",
    "source",
    "official_url",
    "version",
    "download_date",
    "license",
    "redistribution_allowed",
    "citation",
    "organism",
    "biological_domain",
    "graph_type",
    "directed",
    "weighted",
    "heterogeneous",
    "temporal",
    "number_of_nodes",
    "number_of_edges",
    "node_types",
    "edge_types",
    "feature_dimension",
    "label_type",
    "number_of_classes",
    "positive_instances",
    "negative_instances",
    "class_imbalance_ratio",
    "missing_features",
    "duplicate_edges",
    "self_loops",
    "isolated_nodes",
    "connected_components",
    "largest_component_ratio",
    "average_degree",
    "density",
    "transitivity",
    "download_status",
    "preprocessing_status",
    "eligible",
    "exclusion_reason",
]


def validate(path: Path) -> list[str]:
    errors: list[str] = []
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != REQUIRED_COLUMNS:
            errors.append("CSV columns do not match the required schema exactly.")
            missing = [c for c in REQUIRED_COLUMNS if c not in (reader.fieldnames or [])]
            extra = [c for c in (reader.fieldnames or []) if c not in REQUIRED_COLUMNS]
            if missing:
                errors.append(f"Missing columns: {', '.join(missing)}")
            if extra:
                errors.append(f"Extra columns: {', '.join(extra)}")

        seen_ids: set[str] = set()
        for line_number, row in enumerate(reader, start=2):
            if None in row:
                errors.append(
                    f"Line {line_number}: row has extra unassigned fields: {row[None]!r}."
                )

            dataset_id = (row.get("dataset_id") or "").strip()
            if not dataset_id:
                errors.append(f"Line {line_number}: dataset_id is empty.")
            elif dataset_id in seen_ids:
                errors.append(f"Line {line_number}: duplicate dataset_id {dataset_id!r}.")
            seen_ids.add(dataset_id)

            for column in ("dataset_name", "source", "official_url", "license", "download_status", "preprocessing_status", "eligible"):
                if not (row.get(column) or "").strip():
                    errors.append(f"Line {line_number}: required audit field {column!r} is empty.")

    return errors


def main() -> int:
    default_path = Path(__file__).resolve().parents[1] / "reports" / "dataset_audit.csv"
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else default_path
    errors = validate(path)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(f"OK: {path} matches the required audit schema.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
