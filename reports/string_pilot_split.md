# STRING Pilot Link Prediction Split

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
6. Se uso seed fija `42`.

## Conteos

| Split | Positivos | Negativos |
|---|---:|---:|
| Train | 591045 | 591045 |
| Validation | 73880 | 73880 |
| Test | 73880 | 73880 |

## Checks

| Check | Resultado |
|---|---|
| Overlap entre splits | OK |
| Self-loops en splits | OK |
| Fuga inversa | OK |
| Componentes preservados por construccion | True |

Errores detectados:

```text
None
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
