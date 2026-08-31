"""Build leakage-checked pilot link-prediction splits for filtered BioGRID.

Input:
- data/processed/biogrid_human_physical/edges_entrez_undirected.csv

Output:
- data/processed/biogrid_human_physical/splits/

This mirrors the STRING pilot split policy for a second homogeneous PPI
candidate dataset.
"""

from __future__ import annotations

import csv
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from biographbench.splits import build_link_prediction_split

DATA_DIR = ROOT / "data" / "processed" / "biogrid_human_physical"
EDGES_PATH = DATA_DIR / "edges_entrez_undirected.csv"
OUT_DIR = DATA_DIR / "splits"
REPORTS_DIR = ROOT / "reports"

SEED = 42
VAL_RATIO = 0.10
TEST_RATIO = 0.10


def read_edges() -> tuple[dict[tuple[str, str], dict[str, str]], list[str]]:
    edge_meta: dict[tuple[str, str], dict[str, str]] = {}
    nodes: set[str] = set()
    with EDGES_PATH.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            a, b = row["entrez_a"], row["entrez_b"]
            if a == b:
                continue
            if a > b:
                a, b = b, a
            edge = (a, b)
            edge_meta[edge] = row
            nodes.update(edge)
    return edge_meta, sorted(nodes)


def write_edges(
    path: Path,
    edges: list[tuple[str, str]],
    label: int,
    metadata: dict[tuple[str, str], dict[str, str]] | None = None,
) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        fieldnames = ["entrez_a", "entrez_b", "label", "evidence_count", "publication_count"]
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for a, b in edges:
            meta = metadata.get((a, b), {}) if metadata else {}
            writer.writerow(
                {
                    "entrez_a": a,
                    "entrez_b": b,
                    "label": label,
                    "evidence_count": meta.get("evidence_count", ""),
                    "publication_count": meta.get("publication_count", ""),
                }
            )


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    edge_meta, nodes = read_edges()
    split = build_link_prediction_split(edge_meta.keys(), nodes=nodes, seed=SEED, val_ratio=VAL_RATIO, test_ratio=TEST_RATIO)
    all_pos = split.all_pos
    train_pos = split.train_pos
    val_pos = split.val_pos
    test_pos = split.test_pos
    train_neg = split.train_neg
    val_neg = split.val_neg
    test_neg = split.test_neg

    write_edges(OUT_DIR / "train_pos.csv", train_pos, 1, edge_meta)
    write_edges(OUT_DIR / "val_pos.csv", val_pos, 1, edge_meta)
    write_edges(OUT_DIR / "test_pos.csv", test_pos, 1, edge_meta)
    write_edges(OUT_DIR / "train_neg.csv", train_neg, 0)
    write_edges(OUT_DIR / "val_neg.csv", val_neg, 0)
    write_edges(OUT_DIR / "test_neg.csv", test_neg, 0)

    errors = split.split_errors
    original_components = split.original_components
    train_components = split.train_components
    manifest = split.manifest("biogrid_human_physical", OUT_DIR)
    (OUT_DIR / "split_manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    (REPORTS_DIR / "biogrid_pilot_split.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    md = f"""# BioGRID Human Physical Pilot Link Prediction Split

Fecha: 2026-08-04

## Objetivo

Construir un split piloto reproducible para BioGRID humano fisico filtrado, sin entrenar modelos todavia.

## Politica aplicada

1. Usar pares Entrez no dirigidos ya filtrados a interacciones fisicas humano-humano.
2. Preservar un bosque generador para que train conserve los componentes originales.
3. Generar negativos desde pares Entrez no conectados en el grafo completo.
4. Guardar pares siempre ordenados para evitar fuga inversa.
5. Usar seed fija `{SEED}`.

## Conteos

| Split | Positivos | Negativos |
|---|---:|---:|
| Train | {len(train_pos)} | {len(train_neg)} |
| Validation | {len(val_pos)} | {len(val_neg)} |
| Test | {len(test_pos)} | {len(test_neg)} |

## Checks

| Check | Resultado |
|---|---|
| Overlap entre splits | {'OK' if not errors else 'FALLA'} |
| Self-loops | {'OK' if not errors else 'Revisar'} |
| Fuga inversa por pares ordenados | {'OK' if not errors else 'Revisar'} |
| Componentes originales | {original_components} |
| Componentes en train | {train_components} |
| Componentes preservados | {original_components == train_components} |

Errores detectados:

```text
{chr(10).join(errors) if errors else 'None'}
```

## Archivos generados

- `train_pos.csv`
- `val_pos.csv`
- `test_pos.csv`
- `train_neg.csv`
- `val_neg.csv`
- `test_neg.csv`
- `split_manifest.json`

## Nota metodologica

Este split permite comparar baselines iniciales contra STRING en una segunda red PPI homogenea. Antes de declarar independencia biologica entre ambos datasets, falta medir solapamiento entre BioGRID Entrez y STRING protein IDs mediante una tabla de mapeo.
"""
    (REPORTS_DIR / "biogrid_pilot_split.md").write_text(md, encoding="utf-8")
    print(json.dumps(manifest, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
