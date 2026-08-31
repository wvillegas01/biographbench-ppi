# OBNB Node Classification Audit

Fecha: 2026-08-04

## Objetivo

Seleccionar un primer candidato reproducible para cubrir node classification en BioGraphBench.

OBNB se audita con version archivada `obnbdata-0.1.0`, sin entrenar modelos.

## Candidatos

| Dataset | Nodos | Aristas | Weighted | Tareas | Entidades etiquetadas | Positivos | Observados | Split train/val/test |
|---|---:|---:|---|---:|---:|---:|---:|---|
| `obnb_biogrid_gobp` | 19765 | 1554790 | False | 114 | 6075 | 10199 | 692550 | 3645/1215/1215 |
| `obnb_string_gobp` | 18480 | 11019492 | True | 116 | 6104 | 10318 | 708064 | 3662/1221/1221 |

## Licencia y procedencia

- OBNB package: MIT, segun repositorio `krishnanlab/obnb`.
- OBNB archived data: `obnbdata-0.1.0` via Zenodo record usado por OBNB.
- GOBP/Gene Ontology: GO data products are CC BY 4.0, segun Gene Ontology citation policy.
- BioGRID: MIT, ya auditado en la fase PPI.
- STRING: CC BY 4.0, ya auditado en la fase PPI.

Fuentes:

- https://github.com/krishnanlab/obnb
- https://proceedings.mlr.press/v240/liu24a.html
- https://geneontology.org/docs/go-citation-policy/

## Decision recomendada

Usar `obnb_biogrid_gobp` como primer piloto de node classification.

Motivos:

1. Es homogeneo, no ponderado y comparable conceptualmente con la red BioGRID PPI ya auditada.
2. Tiene 114 tareas GO Biological Process despues de filtros OBNB.
3. Usa split study-bias 6/2/2, mas interesante que un split aleatorio simple.
4. Evita iniciar con DisGeNET, cuya licencia/version debe auditarse con mas cuidado.

Mantener `obnb_string_gobp` como comparador secundario, pero recordar que STRING ya tiene alto solapamiento biologico con BioGRID.

## Riesgos abiertos

- OBNB no reemplaza nuestra auditoria de leakage; hay que documentar exactamente como se generan negativos y masks.
- `graph_as_feature=False` no incluye features iniciales; para baselines/GNN se debe definir una politica de features, por ejemplo one-hot log degree.
- Las tareas GO son multietiqueta/multitarea; las metricas deben priorizar AUPRC, micro/macro-F1 y calibracion por tarea.
