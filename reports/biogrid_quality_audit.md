# BioGRID Homo sapiens 5.0.260 - Quality Audit

Fecha de auditoria: 2026-08-04

## Resumen

| Medida | Valor |
|---|---:|
| Archivo interno humano | `BIOGRID-ORGANISM-Homo_sapiens-5.0.260.tab3.txt` |
| Filas crudas | 1404902 |
| Nodos Entrez unicos | 29501 |
| Nodos BioGRID unicos | 29598 |
| Nodos simbolo oficial unicos | 28076 |
| Organism mismatch distinto de 9606/9606 | 112686 |
| Entrez A faltante | 6997 |
| Entrez B faltante | 114 |
| Self-loops Entrez | 9333 |
| Pares Entrez no dirigidos unicos, cualquier tipo | 1054784 |
| Aristas Entrez no dirigidas por tipo | 1056738 |
| Pares fisicos unicos | 1037803 |
| Pares geneticos unicos | 18935 |
| Overlap fisico/genetico | 1954 |
| Duplicados exactos de fila simplificada | 6504 |
| Duplicados por par y tipo | 341053 |
| Duplicados por par sin distinguir tipo | 343007 |

## Tipos de interaccion

- `physical`: 1385452
- `genetic`: 19450

## Sistemas experimentales mas frecuentes

- `Affinity Capture-MS`: 724160
- `Proximity Label-MS`: 213392
- `Two-hybrid`: 121764
- `Affinity Capture-Western`: 91063
- `Co-fractionation`: 76160
- `Reconstituted Complex`: 48845
- `Cross-Linking-MS (XL-MS)`: 31377
- `Affinity Capture-RNA`: 27075
- `Biochemical Activity`: 15945
- `Protein-RNA`: 10954
- `Negative Genetic`: 10611
- `Protein-peptide`: 5831
- `Co-localization`: 5559
- `Positive Genetic`: 4409
- `FRET`: 2814
- `PCA`: 2787
- `Co-crystal Structure`: 2447
- `Affinity Capture-Luminescence`: 2443
- `Synthetic Lethality`: 2266
- `Co-purification`: 1940

## Throughput

- `High Throughput`: 1149515
- `Low Throughput`: 248263
- `High Throughput|Low Throughput`: 7124

## Fuentes principales

- `BIOGRID`: 1404902

## Decision metodologica

BioGRID humano es util como red biologica curada, pero no debe usarse cruda. Para una primera tarea PPI homogenea se recomienda:

1. filtrar `Experimental System Type == physical`;
2. remover self-loops;
3. colapsar multiples evidencias del mismo par Entrez en una sola arista;
4. conservar conteo de evidencias, sistemas experimentales y fuentes como metadatos;
5. decidir si se excluyen high-throughput o si se usan como ablacion;
6. medir solapamiento con STRING antes de declararlo dataset independiente.

La tabla cruda contiene muchas evidencias repetidas por par; eso es biologicamente valioso, pero para link prediction debe separarse claramente la unidad experimental de la unidad de arista.
