# Supervised Link Prediction Baselines

Fecha: 2026-08-05

Features de pares calculadas solo desde el grafo positivo de train.

| Dataset | Split | Modelo | AUROC | AUPRC | Brier | ECE-10 |
|---|---|---|---:|---:|---:|---:|
| `string_human_physical_v12` | `val` | `logistic_regression` | 0.935110 | 0.945232 | 0.098379 | 0.026414 |
| `string_human_physical_v12` | `test` | `logistic_regression` | 0.936188 | 0.946318 | 0.097496 | 0.026659 |
| `string_human_physical_v12` | `val` | `random_forest` | 0.940092 | 0.949581 | 0.092241 | 0.004657 |
| `string_human_physical_v12` | `test` | `random_forest` | 0.940953 | 0.950351 | 0.091733 | 0.004765 |
| `string_human_physical_v12` | `val` | `hist_gradient_boosting` | 0.940378 | 0.950093 | 0.092228 | 0.003956 |
| `string_human_physical_v12` | `test` | `hist_gradient_boosting` | 0.941380 | 0.950931 | 0.091562 | 0.003880 |
| `biogrid_human_physical` | `val` | `logistic_regression` | 0.934239 | 0.934459 | 0.105448 | 0.046827 |
| `biogrid_human_physical` | `test` | `logistic_regression` | 0.934550 | 0.934711 | 0.105355 | 0.047610 |
| `biogrid_human_physical` | `val` | `random_forest` | 0.941411 | 0.942150 | 0.096279 | 0.005731 |
| `biogrid_human_physical` | `test` | `random_forest` | 0.941777 | 0.942632 | 0.095921 | 0.004779 |
| `biogrid_human_physical` | `val` | `hist_gradient_boosting` | 0.941841 | 0.942784 | 0.095973 | 0.003239 |
| `biogrid_human_physical` | `test` | `hist_gradient_boosting` | 0.942187 | 0.943193 | 0.095610 | 0.003695 |
| `biogrid_human_physical_no_string_overlap` | `val` | `logistic_regression` | 0.938834 | 0.933243 | 0.103069 | 0.059899 |
| `biogrid_human_physical_no_string_overlap` | `test` | `logistic_regression` | 0.938175 | 0.932816 | 0.103957 | 0.060117 |
| `biogrid_human_physical_no_string_overlap` | `val` | `random_forest` | 0.944276 | 0.941981 | 0.093344 | 0.004087 |
| `biogrid_human_physical_no_string_overlap` | `test` | `random_forest` | 0.943437 | 0.940832 | 0.094284 | 0.003955 |
| `biogrid_human_physical_no_string_overlap` | `val` | `hist_gradient_boosting` | 0.945306 | 0.943198 | 0.092636 | 0.002481 |
| `biogrid_human_physical_no_string_overlap` | `test` | `hist_gradient_boosting` | 0.944687 | 0.942283 | 0.093457 | 0.003861 |
| `string_human_physical_no_biogrid_overlap` | `val` | `logistic_regression` | 0.951902 | 0.959690 | 0.083531 | 0.029993 |
| `string_human_physical_no_biogrid_overlap` | `test` | `logistic_regression` | 0.950636 | 0.958310 | 0.084473 | 0.028553 |
| `string_human_physical_no_biogrid_overlap` | `val` | `random_forest` | 0.956103 | 0.963881 | 0.075780 | 0.006488 |
| `string_human_physical_no_biogrid_overlap` | `test` | `random_forest` | 0.955230 | 0.963034 | 0.076683 | 0.005673 |
| `string_human_physical_no_biogrid_overlap` | `val` | `hist_gradient_boosting` | 0.956622 | 0.964411 | 0.075760 | 0.007172 |
| `string_human_physical_no_biogrid_overlap` | `test` | `hist_gradient_boosting` | 0.955332 | 0.963088 | 0.076881 | 0.005993 |
