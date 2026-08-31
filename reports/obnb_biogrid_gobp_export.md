# OBNB BioGRID+GOBP Export

Fecha: 2026-08-04

## Objetivo

Exportar el candidato recomendado de node classification a un artefacto local explicito para BioGraphBench.

## Conteos

| Medida | Valor |
|---|---:|
| Nodos | 19765 |
| Aristas | 1554790 |
| Tareas GO BP | 114 |
| Labels positivos totales | 10199 |
| Labels observados totales | 692550 |
| Train nodes | 3645 |
| Val nodes | 1215 |
| Test nodes | 1215 |
| Positivos min/med/max por tarea | 50 / 76.0 / 186 |
| Negativos min/med/max por tarea | 5889 / 5999.0 / 6025 |

## Split

`RatioPartition(property_converter=GenePropertyConverter(name='PubMedCount'), ascending=False, ratios=(0.6, 0.2, 0.2))`

OBNB usa un split study-bias 6/2/2 basado en PubMedCount: train contiene genes mas estudiados, test genes menos estudiados y validation el resto.

## Archivos generados

- `node_classification_arrays.npz`
- `nodes.csv`
- `labels.csv`
- `manifest.json`

## Decision

Este artefacto ya permite implementar baselines de node classification. Falta definir politica de features antes de entrenar: no usar informacion derivada de validation/test para features estructurales.
