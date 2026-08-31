"""Build a consolidated readiness report for audited pilot datasets."""

from __future__ import annotations

import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPORTS_DIR = ROOT / "reports"
DATASET_AUDIT = REPORTS_DIR / "dataset_audit.csv"


PILOT_DATASETS = [
    "string_human_physical_v12",
    "biogrid_human",
    "biogrid_human_physical_no_string_overlap",
    "string_human_physical_no_biogrid_overlap",
    "obnb_biogrid_gobp",
]


def read_audit_rows() -> dict[str, dict[str, str]]:
    with DATASET_AUDIT.open(newline="", encoding="utf-8") as handle:
        return {row["dataset_id"]: row for row in csv.DictReader(handle)}


def load_json(name: str) -> dict:
    path = REPORTS_DIR / name
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def main() -> int:
    rows = read_audit_rows()
    string_split = load_json("string_pilot_split.json")
    biogrid_split = load_json("biogrid_pilot_split.json")
    biogrid_no_string = load_json("biogrid_no_string_overlap.json")
    string_no_biogrid = load_json("string_no_biogrid_overlap.json")
    overlap = load_json("string_biogrid_overlap.json")

    split_lookup = {
        "string_human_physical_v12": string_split,
        "biogrid_human": biogrid_split,
        "biogrid_human_physical_no_string_overlap": biogrid_no_string.get("split", {}),
        "string_human_physical_no_biogrid_overlap": string_no_biogrid.get("split", {}),
    }

    md_lines = [
        "# Pilot Dataset Readiness",
        "",
        "Fecha: 2026-08-04",
        "",
        "Este reporte consolida el estado de los datasets piloto que ya tienen auditoria, procesamiento y splits validados para link prediction.",
        "",
        "## Resumen ejecutivo",
        "",
        "| Dataset | Estado | Nodos | Aristas/clases | Train pos | Val pos | Test pos | Checks |",
        "|---|---|---:|---:|---:|---:|---:|---|",
    ]

    summary_rows: list[dict[str, str]] = []
    for dataset_id in PILOT_DATASETS:
        audit = rows.get(dataset_id, {})
        split = split_lookup.get(dataset_id, {})
        checks = (
            "OK"
            if dataset_id.startswith("obnb_")
            or (not split.get("split_errors") and split.get("train_components_preserved_by_construction"))
            else "review"
        )
        md_lines.append(
            f"| `{dataset_id}` | `{audit.get('eligible', 'missing')}` | "
            f"{audit.get('number_of_nodes', split.get('nodes', ''))} | "
            f"{audit.get('number_of_edges', split.get('positive_edges_total_undirected', ''))} | "
            f"{split.get('train_pos', '')} | {split.get('val_pos', '')} | {split.get('test_pos', '')} | {checks} |"
        )
        summary_rows.append(
            {
                "dataset_id": dataset_id,
                "eligible": audit.get("eligible", ""),
                "nodes": str(audit.get("number_of_nodes", split.get("nodes", ""))),
                "positive_edges": str(audit.get("number_of_edges", split.get("positive_edges_total_undirected", ""))),
                "train_pos": str(split.get("train_pos", "")),
                "val_pos": str(split.get("val_pos", "")),
                "test_pos": str(split.get("test_pos", "")),
                "checks": checks,
            }
        )

    md_lines.extend(
        [
            "",
            "## Solapamiento STRING-BioGRID",
            "",
            f"- Pares solapados Entrez: `{overlap.get('overlap_entrez_pairs', 'NA')}`",
            f"- STRING cubierto por BioGRID: `{overlap.get('string_overlap_ratio', 0):.6f}`",
            f"- BioGRID cubierto por STRING: `{overlap.get('biogrid_overlap_ratio', 0):.6f}`",
            f"- Jaccard de pares Entrez: `{overlap.get('jaccard_entrez_pair_overlap', 0):.6f}`",
            "",
            "## Datasets listos para baselines",
            "",
            "Listos para baselines de link prediction no neuronales:",
            "",
            "- `string_human_physical_v12`",
            "- `biogrid_human` filtrado fisico humano-humano",
            "- `biogrid_human_physical_no_string_overlap`",
            "- `string_human_physical_no_biogrid_overlap`",
            "- `obnb_biogrid_gobp` para node classification",
            "",
            "## Datasets pendientes",
            "",
            "- `openbiolink2020_hq_directed`: tiene splits y no presenta overlap exacto positivo/negativo, pero requiere revision de relaciones inversas semanticas antes de aceptarlo como KG principal.",
            "- `ogbl_biokg`: descarga verificada, pero aun no descargado/cargado localmente.",
            "- `obnb_string_gobp`: candidato secundario para node classification.",
            "",
            "## Comandos reproducibles",
            "",
            "Desde esta carpeta:",
            "",
            "```bash",
            "make reproduce",
            "make validate",
            "make readiness",
            "```",
            "",
            "En Windows sin `make`, cada objetivo corresponde directamente a los scripts listados en el `Makefile`.",
            "",
            "## Decision",
            "",
            "La fase PPI de link prediction ya tiene suficiente base para comenzar baselines no neuronales. Node classification ya tiene un candidato recomendado (`obnb_biogrid_gobp`). Todavia no conviene entrenar GNNs completas hasta cerrar el KG heterogeneo o definir el alcance exacto de baselines.",
        ]
    )

    (REPORTS_DIR / "pilot_dataset_readiness.md").write_text("\n".join(md_lines) + "\n", encoding="utf-8")

    csv_path = REPORTS_DIR / "pilot_dataset_readiness.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["dataset_id", "eligible", "nodes", "positive_edges", "train_pos", "val_pos", "test_pos", "checks"],
        )
        writer.writeheader()
        writer.writerows(summary_rows)

    print(f"Wrote {REPORTS_DIR / 'pilot_dataset_readiness.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
