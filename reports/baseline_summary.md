# Baseline Summary

Fecha: 2026-08-05

## Link Prediction

| Dataset | Mejor baseline test | AUROC | AUPRC |
|---|---|---:|---:|
| `string_human_physical_v12` | `hist_gradient_boosting` | 0.941380 | 0.950931 |
| `biogrid_human_physical` | `hist_gradient_boosting` | 0.942187 | 0.943193 |
| `biogrid_human_physical_no_string_overlap` | `hist_gradient_boosting` | 0.944687 | 0.942283 |
| `string_human_physical_no_biogrid_overlap` | `hist_gradient_boosting` | 0.955332 | 0.963088 |

## Node Classification

| Dataset | Mejor feature test | Macro AUROC | Macro AUPRC | Micro-F1 |
|---|---|---:|---:|---:|
| `obnb_biogrid_gobp` | `gcn / one_hot_log_degree` | 0.493559 | 0.015926 | 0.000000 |

## Node Classification Threshold-Tuned F1

| Dataset | Mejor modelo test | Micro-F1 | Macro-F1 | Precision | Recall |
|---|---|---:|---:|---:|---:|
| `obnb_biogrid_gobp` | `logistic_regression` | 0.025313 | 0.024530 | 0.013053 | 0.416216 |

## Lectura

- Las heuristicas clasicas son fuertes en PPI, especialmente Adamic-Adar y Preferential Attachment segun dataset.
- Los modelos supervisados sobre heuristicas mejoran la vara inicial y ya reportan calibracion basica.
- Esto confirma que cualquier GNN debe compararse contra baselines estructurales y supervisados serios.
- En node classification, `one_hot_log_degree` mejora el control constante, pero sigue siendo debil; eso deja espacio para modelos que usen propagacion/estructura de forma mas rica.
- El GCN piloto mejora macro-AUPRC frente a logistic regression, pero no resuelve aun el desbalance ni el umbral de decision; debe tratarse como prueba inicial de infraestructura, no como resultado final.
- El tuning de umbrales por tarea recupera F1 distinto de cero y expone el trade-off precision/recall; logistic regression queda mejor en micro-F1 test, mientras GCN conserva mejor macro-AUPRC.
