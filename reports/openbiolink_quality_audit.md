# OpenBioLink2020 HQ Directed - Quality Audit

Fecha de auditoria: 2026-08-04

## Resumen

- Archivo: `HQ_DIR.zip`
- Tamano: `109387184` bytes
- Grafo dirigido segun `graph_props.json`: `True`
- Nodos en `nodes.csv`: `184667`
- Nodos tocados por triples de splits: `184732`
- Relaciones observadas en splits: `28`
- Triples positivos unicos: `4563405`
- Triples negativos unicos: `4739142`

## Conteos por split

| Split | Filas | Duplicados exactos | Etiquetas inesperadas | Reverse same-relation hits |
|---|---:|---:|---:|---:|
| `train_pos` | 4192002 | 0 | 0 | 1442114 |
| `val_pos` | 188394 | 0 | 0 | 2854 |
| `test_pos` | 183009 | 0 | 0 | 3144 |
| `train_neg` | 4311578 | 0 | 0 | 52 |
| `val_neg` | 208672 | 0 | 0 | 0 |
| `test_neg` | 218892 | 0 | 0 | 2 |

## Checks de leakage

- Overlap positivo/negativo exacto: `0`
- Overlaps entre splits con valor distinto de cero: `None`
- Duplicados internos con valor distinto de cero: `None`
- Etiquetas inesperadas: `None`

El chequeo `reverse same-relation hits` busca triples inversos con la misma relacion. En positivos puede reflejar relaciones simetricas reales; en negativos es una alerta de posible leakage para relaciones que deban tratarse como no dirigidas o simetricas.

## Tipos de nodo

- `ANATOMY`: 16031
- `DIS`: 9509
- `DRUG`: 77635
- `GENE`: 19598
- `GO`: 44945
- `PATHWAY`: 2363
- `PHENOTYPE`: 14586

## Relaciones mas frecuentes

- `GENE_EXPRESSED_ANATOMY`: 2917406
- `GENE_GENE`: 1508169
- `GENE_REACTION_GENE`: 739393
- `GENE_CATALYSIS_GENE`: 575750
- `GENE_BINDING_GENE`: 544832
- `GENE_GO`: 408225
- `DRUG_BINDING_GENE`: 357779
- `GENE_DRUG`: 347235
- `GENE_PHENOTYPE`: 322006
- `GENE_PATHWAY`: 271618
- `GENE_OVEREXPRESSED_ANATOMY`: 267418
- `IS_A`: 262068
- `GENE_UNDEREXPRESSED_ANATOMY`: 258474
- `DRUG_PHENOTYPE`: 178192
- `GENE_ACTIVATION_GENE`: 56215

## Fuentes mas frecuentes

- `GENERATED`: 4145702
- `Bgee`: 2301699
- `STRING`: 1652789
- `STITCH`: 423554
- `GO`: 287951
- `HPO`: 203397
- `CDT`: 135809
- `SIDER`: 89096
- `UBERON`: 33344
- `DrugCentral`: 14290
- `DO`: 11953
- `DisGeNet`: 2963

## Decision metodologica

OpenBioLink HQ directed es util como candidato de KG link prediction porque ya trae positivos, negativos y splits. Antes de aceptarlo como dataset principal, el siguiente control debe revisar relaciones inversas semanticas, no solo inversas con el mismo nombre. La auditoria actual sugiere filtrar o marcar negativos con inverso positivo de la misma relacion antes de comparar modelos.