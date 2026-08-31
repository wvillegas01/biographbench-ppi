# Phase 1 node2vec-compatible Baseline Statistics

| Dataset | Negatives | n | AUROC mean | AUPRC mean | SD | CI95 low | CI95 high |
|---|---|---:|---:|---:|---:|---:|---:|
| `biogrid_human_physical` | `degree_matched` | 10 | 0.705709 | 0.697622 | 0.003135 | 0.695379 | 0.699864 |
| `biogrid_human_physical` | `random` | 10 | 0.867051 | 0.873371 | 0.001682 | 0.872168 | 0.874574 |
| `biogrid_human_physical` | `two_hop` | 10 | 0.645125 | 0.638958 | 0.001514 | 0.637875 | 0.640041 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 10 | 0.733227 | 0.724663 | 0.002759 | 0.722690 | 0.726637 |
| `biogrid_human_physical_no_string_overlap` | `random` | 10 | 0.892889 | 0.898468 | 0.001439 | 0.897439 | 0.899497 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 10 | 0.623073 | 0.604805 | 0.002463 | 0.603043 | 0.606567 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 10 | 0.906777 | 0.903597 | 0.001865 | 0.902263 | 0.904931 |
| `string_human_physical_no_biogrid_overlap` | `random` | 10 | 0.927293 | 0.940531 | 0.001561 | 0.939414 | 0.941648 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 10 | 0.743186 | 0.735606 | 0.002246 | 0.734000 | 0.737213 |
| `string_human_physical_v12` | `degree_matched` | 10 | 0.796536 | 0.804031 | 0.001760 | 0.802772 | 0.805290 |
| `string_human_physical_v12` | `random` | 10 | 0.859226 | 0.876736 | 0.001070 | 0.875970 | 0.877502 |
| `string_human_physical_v12` | `two_hop` | 10 | 0.714953 | 0.730962 | 0.001276 | 0.730049 | 0.731875 |

## Paired AUPRC Differences: Reference minus node2vec

| Dataset | Negatives | Reference | n | Mean diff | Wilcoxon p | Cohen dz |
|---|---|---|---:|---:|---:|---:|
| `biogrid_human_physical` | `degree_matched` | `hist_gradient_boosting` | 10 | 0.072848 | 0.00195312 | 22.258643 |
| `biogrid_human_physical` | `degree_matched` | `random_forest` | 10 | 0.073567 | 0.00195312 | 20.633277 |
| `biogrid_human_physical` | `degree_matched` | `logistic_regression` | 10 | 0.018625 | 0.00195312 | 5.591123 |
| `biogrid_human_physical` | `random` | `hist_gradient_boosting` | 10 | 0.069515 | 0.00195312 | 46.571873 |
| `biogrid_human_physical` | `random` | `random_forest` | 10 | 0.068899 | 0.00195312 | 46.070903 |
| `biogrid_human_physical` | `random` | `logistic_regression` | 10 | 0.061302 | 0.00195312 | 42.720426 |
| `biogrid_human_physical` | `two_hop` | `hist_gradient_boosting` | 10 | 0.135424 | 0.00195312 | 79.671085 |
| `biogrid_human_physical` | `two_hop` | `random_forest` | 10 | 0.133981 | 0.00195312 | 94.557294 |
| `biogrid_human_physical` | `two_hop` | `logistic_regression` | 10 | 0.015357 | 0.00195312 | 9.264612 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | `hist_gradient_boosting` | 10 | -0.041073 | 0.00195312 | -14.021813 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | `random_forest` | 10 | -0.038124 | 0.00195312 | -13.642072 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | `logistic_regression` | 10 | -0.130789 | 0.00195312 | -37.604233 |
| `biogrid_human_physical_no_string_overlap` | `random` | `hist_gradient_boosting` | 10 | 0.043787 | 0.00195312 | 31.895070 |
| `biogrid_human_physical_no_string_overlap` | `random` | `random_forest` | 10 | 0.042409 | 0.00195312 | 33.350176 |
| `biogrid_human_physical_no_string_overlap` | `random` | `logistic_regression` | 10 | 0.034365 | 0.00195312 | 20.760478 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | `hist_gradient_boosting` | 10 | 0.244467 | 0.00195312 | 105.117863 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | `random_forest` | 10 | 0.225421 | 0.00195312 | 111.423232 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | `logistic_regression` | 10 | 0.117485 | 0.00195312 | 44.169215 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | `hist_gradient_boosting` | 10 | 0.012046 | 0.00195312 | 5.853073 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | `random_forest` | 10 | 0.011508 | 0.00195312 | 5.302227 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | `logistic_regression` | 10 | -0.014710 | 0.00195312 | -8.218120 |
| `string_human_physical_no_biogrid_overlap` | `random` | `hist_gradient_boosting` | 10 | 0.023624 | 0.00195312 | 22.375156 |
| `string_human_physical_no_biogrid_overlap` | `random` | `random_forest` | 10 | 0.023130 | 0.00195312 | 21.914000 |
| `string_human_physical_no_biogrid_overlap` | `random` | `logistic_regression` | 10 | 0.019259 | 0.00195312 | 18.371095 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | `hist_gradient_boosting` | 10 | 0.111135 | 0.00195312 | 44.303528 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | `random_forest` | 10 | 0.115410 | 0.00195312 | 44.607964 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | `logistic_regression` | 10 | -0.053676 | 0.00195312 | -19.394222 |
| `string_human_physical_v12` | `degree_matched` | `hist_gradient_boosting` | 10 | 0.077293 | 0.00195312 | 49.263688 |
| `string_human_physical_v12` | `degree_matched` | `random_forest` | 10 | 0.076485 | 0.00195312 | 47.442337 |
| `string_human_physical_v12` | `degree_matched` | `logistic_regression` | 10 | 0.060415 | 0.00195312 | 34.542541 |
| `string_human_physical_v12` | `random` | `hist_gradient_boosting` | 10 | 0.073525 | 0.00195312 | 82.033286 |
| `string_human_physical_v12` | `random` | `random_forest` | 10 | 0.073108 | 0.00195312 | 75.765163 |
| `string_human_physical_v12` | `random` | `logistic_regression` | 10 | 0.068908 | 0.00195312 | 82.524879 |
| `string_human_physical_v12` | `two_hop` | `hist_gradient_boosting` | 10 | 0.125420 | 0.00195312 | 98.557033 |
| `string_human_physical_v12` | `two_hop` | `random_forest` | 10 | 0.126101 | 0.00195312 | 104.537815 |
| `string_human_physical_v12` | `two_hop` | `logistic_regression` | 10 | 0.021756 | 0.00195312 | 26.720500 |
