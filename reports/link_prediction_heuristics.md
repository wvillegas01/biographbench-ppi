# Link Prediction Heuristic Baselines

Fecha: 2026-08-05

Baselines calculados usando solo aristas positivas de train para construir el grafo.

| Dataset | Split | Modelo | AUROC | AUPRC |
|---|---|---|---:|---:|
| `string_human_physical_v12` | `val` | `common_neighbors` | 0.917360 | 0.917946 |
| `string_human_physical_v12` | `val` | `jaccard` | 0.908305 | 0.910789 |
| `string_human_physical_v12` | `val` | `adamic_adar` | 0.920481 | 0.926423 |
| `string_human_physical_v12` | `val` | `preferential_attachment` | 0.881074 | 0.884569 |
| `string_human_physical_v12` | `test` | `common_neighbors` | 0.917830 | 0.918560 |
| `string_human_physical_v12` | `test` | `jaccard` | 0.908563 | 0.911427 |
| `string_human_physical_v12` | `test` | `adamic_adar` | 0.921106 | 0.927194 |
| `string_human_physical_v12` | `test` | `preferential_attachment` | 0.882483 | 0.885910 |
| `biogrid_human_physical` | `val` | `common_neighbors` | 0.908493 | 0.906991 |
| `biogrid_human_physical` | `val` | `jaccard` | 0.873998 | 0.861231 |
| `biogrid_human_physical` | `val` | `adamic_adar` | 0.912946 | 0.917186 |
| `biogrid_human_physical` | `val` | `preferential_attachment` | 0.921217 | 0.918442 |
| `biogrid_human_physical` | `test` | `common_neighbors` | 0.909451 | 0.907927 |
| `biogrid_human_physical` | `test` | `jaccard` | 0.875579 | 0.863944 |
| `biogrid_human_physical` | `test` | `adamic_adar` | 0.913971 | 0.918185 |
| `biogrid_human_physical` | `test` | `preferential_attachment` | 0.921092 | 0.918508 |
| `biogrid_human_physical_no_string_overlap` | `val` | `common_neighbors` | 0.869042 | 0.865159 |
| `biogrid_human_physical_no_string_overlap` | `val` | `jaccard` | 0.798197 | 0.728652 |
| `biogrid_human_physical_no_string_overlap` | `val` | `adamic_adar` | 0.874582 | 0.880183 |
| `biogrid_human_physical_no_string_overlap` | `val` | `preferential_attachment` | 0.939699 | 0.935780 |
| `biogrid_human_physical_no_string_overlap` | `test` | `common_neighbors` | 0.866958 | 0.862887 |
| `biogrid_human_physical_no_string_overlap` | `test` | `jaccard` | 0.796340 | 0.726311 |
| `biogrid_human_physical_no_string_overlap` | `test` | `adamic_adar` | 0.872475 | 0.877964 |
| `biogrid_human_physical_no_string_overlap` | `test` | `preferential_attachment` | 0.938496 | 0.934362 |
| `string_human_physical_no_biogrid_overlap` | `val` | `common_neighbors` | 0.918758 | 0.917602 |
| `string_human_physical_no_biogrid_overlap` | `val` | `jaccard` | 0.913151 | 0.910689 |
| `string_human_physical_no_biogrid_overlap` | `val` | `adamic_adar` | 0.921004 | 0.923831 |
| `string_human_physical_no_biogrid_overlap` | `val` | `preferential_attachment` | 0.896693 | 0.896437 |
| `string_human_physical_no_biogrid_overlap` | `test` | `common_neighbors` | 0.915688 | 0.914397 |
| `string_human_physical_no_biogrid_overlap` | `test` | `jaccard` | 0.910123 | 0.906964 |
| `string_human_physical_no_biogrid_overlap` | `test` | `adamic_adar` | 0.918013 | 0.920674 |
| `string_human_physical_no_biogrid_overlap` | `test` | `preferential_attachment` | 0.895249 | 0.895508 |
