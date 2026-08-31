"""Build a leakage-checked pilot link-prediction split for STRING physical.

Outputs are stored under:
data/processed/string_human_physical_v12/

This script intentionally builds a simple, auditable split before any model
training exists. It preserves a spanning forest in train positives so the train
graph keeps the original connected components.
"""

from __future__ import annotations

import csv
import gzip
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from biographbench.splits import build_link_prediction_split

RAW_PATH = ROOT / "data" / "raw" / "9606.protein.physical.links.v12.0.txt.gz"
OUT_DIR = ROOT / "data" / "processed" / "string_human_physical_v12"
REPORTS_DIR = ROOT / "reports"

SEED = 42
VAL_RATIO = 0.10
TEST_RATIO = 0.10


def read_collapsed_edges() -> tuple[dict[tuple[str, str], int], list[str]]:
    edge_scores: dict[tuple[str, str], int] = {}
    nodes: set[str] = set()
    with gzip.open(RAW_PATH, "rt", encoding="utf-8") as handle:
        reader = csv.DictReader(handle, delimiter=" ")
        for row in reader:
            a = row["protein1"]
            b = row["protein2"]
            if a == b:
                continue
            score = int(row["combined_score"])
            edge = tuple(sorted((a, b)))
            edge_scores[edge] = max(score, edge_scores.get(edge, score))
            nodes.update(edge)
    return edge_scores, sorted(nodes)


def write_edges(path: Path, edges: list[tuple[str, str]], label: int, scores: dict[tuple[str, str], int] | None = None) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        fieldnames = ["protein1", "protein2", "label", "combined_score"]
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
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


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    edge_scores, nodes = read_collapsed_edges()
    split = build_link_prediction_split(edge_scores.keys(), nodes=nodes, seed=SEED, val_ratio=VAL_RATIO, test_ratio=TEST_RATIO)
    all_pos = split.all_pos
    train_pos = split.train_pos
    val_pos = split.val_pos
    test_pos = split.test_pos
    train_neg = split.train_neg
    val_neg = split.val_neg
    test_neg = split.test_neg

    write_edges(OUT_DIR / "edges_undirected.csv", sorted(all_pos), 1, edge_scores)
    write_edges(OUT_DIR / "train_pos.csv", train_pos, 1, edge_scores)
    write_edges(OUT_DIR / "val_pos.csv", val_pos, 1, edge_scores)
    write_edges(OUT_DIR / "test_pos.csv", test_pos, 1, edge_scores)
    write_edges(OUT_DIR / "train_neg.csv", train_neg, 0)
    write_edges(OUT_DIR / "val_neg.csv", val_neg, 0)
    write_edges(OUT_DIR / "test_neg.csv", test_neg, 0)

    errors = split.split_errors
    original_components = split.original_components
    train_components = split.train_components
    manifest = split.manifest("string_human_physical_v12", OUT_DIR)
    (OUT_DIR / "split_manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    md = f"""# STRING Pilot Link Prediction Split

Fecha: 2026-08-04

## Objetivo

Construir el primer split reproducible para BioGraphBench sin entrenar modelos todavia.

Dataset: STRING Homo sapiens physical links v12.0.

## Politica aplicada

1. Se colapsaron aristas simetricas `A-B` y `B-A` en una sola arista no dirigida.
2. Se conservaron los scores `combined_score` como metadato de arista positiva.
3. Se protegieron las aristas de un bosque generador para no romper la conectividad original al separar validacion/test.
4. Se generaron negativos solo desde pares de proteinas que no existen como positivos en el grafo completo.
5. Los pares se guardaron siempre ordenados, por lo que no puede aparecer fuga inversa `B-A`.
6. Se uso seed fija `{SEED}`.

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
| Self-loops en splits | {'OK' if not errors else 'Revisar'} |
| Fuga inversa | {'OK' if not errors else 'Revisar'} |
| Componentes preservados por construccion | {original_components == train_components} |

Errores detectados:

```text
{chr(10).join(errors) if errors else 'None'}
```

## Archivos generados

- `edges_undirected.csv`
- `train_pos.csv`
- `val_pos.csv`
- `test_pos.csv`
- `train_neg.csv`
- `val_neg.csv`
- `test_neg.csv`
- `split_manifest.json`

## Nota metodologica

Este split es suficiente para comenzar baselines de link prediction, pero todavia debe complementarse con pruebas automatizadas formales: no overlap, no reverse leakage, negative sampling y split reproducibility.
"""
    (REPORTS_DIR / "string_pilot_split.md").write_text(md, encoding="utf-8")
    (REPORTS_DIR / "string_pilot_split.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    print(json.dumps(manifest, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
