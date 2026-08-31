# BioGraphBench MVP Status Report

Fecha: 2026-08-05

## Principio rector

> BioGraphBench no empieza con modelos; empieza con confianza.

Este MVP ya tiene una base auditable para dos tareas: link prediction y node classification. Incluye descargas con hashes, inspeccion de datos, filtrado, splits validados, features iniciales, baselines clasicos, modelos supervisados y un GNN piloto.

## Datasets y estado

| Dataset | Tarea | Tipo | Nodos | Aristas/clases | Estado | Riesgo principal |
|---|---|---|---:|---:|---|---|
| `openbiolink2020_hq_directed` | `link_prediction_with_negatives` | `knowledge_graph` | 184732 | 4563405 | `candidate_needs_inverse_relation_review` | Quality audited: no exact split overlap and no bad labels; negatives include 54 same-relation reverse hits against positives and require review/filtering |
| `biogrid_human` | `link_prediction_or_external_node_labels` | `filtered_physical_ppi_network` | 20376 | 961531 | `yes_for_pilot_link_prediction_after_filtering` | Filtered physical human-human network and pilot split built; overlap with STRING mapped pairs covers 0.440 of BioGRID pairs, so independence claims need overlap-aware ablation |
| `string_human_physical_v12` | `link_prediction` | `weighted_interaction_network` | 18767 | 738805 | `yes_for_pilot_link_prediction` | Pilot split built and validated; Entrez-mapped overlap with BioGRID filtered is 0.553 of STRING mapped pairs, so independence claims need overlap-aware ablation |
| `biogrid_human_physical_no_string_overlap` | `link_prediction` | `filtered_physical_ppi_network_ablation` | 19591 | 538003 | `yes_for_overlap_ablation_link_prediction` | BioGRID physical filtered with STRING-overlapping Entrez pairs removed; split validated no overlap no self-loops connectivity preserved |
| `string_human_physical_no_biogrid_overlap` | `link_prediction` | `filtered_physical_ppi_network_ablation` | 16781 | 314539 | `yes_for_overlap_ablation_link_prediction` | STRING physical with BioGRID-overlapping Entrez-mapped pairs removed; split validated no overlap no self-loops connectivity preserved |
| `obnb_biogrid_gobp` | `multilabel_node_classification_gobp` | `obnb_node_classification_network` | 19765 | 1554790 | `yes_for_pilot_node_classification` | Exported arrays masks labels and initial features validated; ready for node-classification baselines |

## Mejores resultados iniciales

| Tarea | Dataset | Modelo | Input/features | AUROC | AUPRC | Nota |
|---|---|---|---|---:|---:|---|
| `link_prediction` | `string_human_physical_v12` | `hist_gradient_boosting` | `train_graph_pair_heuristics` | 0.941380 | 0.950931 | Brier=0.0916; ECE10=0.0039 |
| `link_prediction` | `biogrid_human_physical` | `hist_gradient_boosting` | `train_graph_pair_heuristics` | 0.942187 | 0.943193 | Brier=0.0956; ECE10=0.0037 |
| `link_prediction` | `biogrid_human_physical_no_string_overlap` | `hist_gradient_boosting` | `train_graph_pair_heuristics` | 0.944687 | 0.942283 | Brier=0.0935; ECE10=0.0039 |
| `link_prediction` | `string_human_physical_no_biogrid_overlap` | `hist_gradient_boosting` | `train_graph_pair_heuristics` | 0.955332 | 0.963088 | Brier=0.0769; ECE10=0.0060 |
| `node_classification` | `obnb_biogrid_gobp` | `gcn` | `one_hot_log_degree` | 0.493559 | 0.015926 | micro_f1@0.5=0.0000 |
| `node_classification_threshold_tuned` | `obnb_biogrid_gobp` | `logistic_regression` | `one_hot_log_degree + per_task_val_f1` | 0.530988 | 0.014365 | micro_f1=0.0253; recall=0.4162 |

## Lo que ya esta cubierto

- Descarga reproducible de STRING, BioGRID, OpenBioLink y OBNB.
- Auditoria de datasets existentes y gap analysis.
- Link prediction en STRING y BioGRID.
- Node classification en OBNB BioGRID+GOBP.
- Splits positivos/negativos sin overlap para PPI.
- Ablaciones de solapamiento STRING/BioGRID.
- Features iniciales para node classification.
- Baselines heuristicas, supervisados y GNN piloto.
- Calibracion basica en link prediction supervisado: Brier, NLL y ECE-10.
- Threshold tuning por tarea para node classification.

## Hallazgos importantes

- STRING y BioGRID tienen alto solapamiento biologico: 423,528 pares Entrez compartidos.
- Las heuristicas clasicas en PPI son muy fuertes; cualquier GNN debe compararse contra ellas.
- Los modelos supervisados sobre heuristicas elevan aun mas la vara en link prediction.
- Node classification es mucho mas dificil y desbalanceado; AUPRC y threshold tuning son mas informativos que F1 con umbral 0.5.
- El GCN piloto prueba infraestructura, pero aun no es un resultado final competitivo.

## Riesgos abiertos

- OpenBioLink requiere revision semantica de relaciones inversas antes de aceptarlo como KG principal.
- OGB `ogbl-biokg` esta verificado para descarga, pero aun no cargado/procesado localmente.
- Falta robustez, escalabilidad, interpretabilidad y estadistica con multiples semillas.
- Las features biologicas externas no deben incorporarse sin auditoria de licencia y leakage temporal.
- El MVP actual usa una semilla principal; el protocolo final necesita 5-10 semillas segun fase.

## Decision

El MVP auditado esta listo para convertirse en un repositorio benchmark inicial. La siguiente fase ya puede moverse desde `Auditoria` hacia una estructura de paquete reproducible, conservando estos reportes como evidencia.
