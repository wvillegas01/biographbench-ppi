# Pilot Dataset Readiness

Fecha: 2026-08-04

Este reporte consolida el estado de los datasets piloto que ya tienen auditoria, procesamiento y splits validados para link prediction.

## Resumen ejecutivo

| Dataset | Estado | Nodos | Aristas/clases | Train pos | Val pos | Test pos | Checks |
|---|---|---:|---:|---:|---:|---:|---|
| `string_human_physical_v12` | `yes_for_pilot_link_prediction` | 18767 | 738805 | 591045 | 73880 | 73880 | OK |
| `biogrid_human` | `yes_for_pilot_link_prediction_after_filtering` | 20376 | 961531 | 769225 | 96153 | 96153 | OK |
| `biogrid_human_physical_no_string_overlap` | `yes_for_overlap_ablation_link_prediction` | 19591 | 538003 | 430403 | 53800 | 53800 | OK |
| `string_human_physical_no_biogrid_overlap` | `yes_for_overlap_ablation_link_prediction` | 16781 | 314539 | 251633 | 31453 | 31453 | OK |
| `obnb_biogrid_gobp` | `yes_for_pilot_node_classification` | 19765 | 1554790 |  |  |  | OK |

## Solapamiento STRING-BioGRID

- Pares solapados Entrez: `423528`
- STRING cubierto por BioGRID: `0.552704`
- BioGRID cubierto por STRING: `0.440473`
- Jaccard de pares Entrez: `0.324720`

## Datasets listos para baselines

Listos para baselines de link prediction no neuronales:

- `string_human_physical_v12`
- `biogrid_human` filtrado fisico humano-humano
- `biogrid_human_physical_no_string_overlap`
- `string_human_physical_no_biogrid_overlap`
- `obnb_biogrid_gobp` para node classification

## Datasets pendientes

- `openbiolink2020_hq_directed`: tiene splits y no presenta overlap exacto positivo/negativo, pero requiere revision de relaciones inversas semanticas antes de aceptarlo como KG principal.
- `ogbl_biokg`: descarga verificada, pero aun no descargado/cargado localmente.
- `obnb_string_gobp`: candidato secundario para node classification.

## Comandos reproducibles

Desde esta carpeta:

```bash
make reproduce
make validate
make readiness
```

En Windows sin `make`, cada objetivo corresponde directamente a los scripts listados en el `Makefile`.

## Decision

La fase PPI de link prediction ya tiene suficiente base para comenzar baselines no neuronales. Node classification ya tiene un candidato recomendado (`obnb_biogrid_gobp`). Todavia no conviene entrenar GNNs completas hasta cerrar el KG heterogeneo o definir el alcance exacto de baselines.
