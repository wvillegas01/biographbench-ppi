# Phase 1 PPI Link Prediction Baselines

| Dataset | Negatives | Seed | Split | Model | AUROC | AUPRC | ECE-10 | Train s |
|---|---|---:|---|---|---:|---:|---:|---:|
| `string_human_physical_no_biogrid_overlap` | `random` | 42 | `val` | `common_neighbors` | 0.918758 | 0.917602 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `random` | 42 | `val` | `jaccard` | 0.913151 | 0.910689 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `random` | 42 | `val` | `adamic_adar` | 0.921004 | 0.923831 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `random` | 42 | `val` | `preferential_attachment` | 0.896693 | 0.896437 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `random` | 42 | `test` | `common_neighbors` | 0.915688 | 0.914397 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `random` | 42 | `test` | `jaccard` | 0.910123 | 0.906964 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `random` | 42 | `test` | `adamic_adar` | 0.918013 | 0.920674 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `random` | 42 | `test` | `preferential_attachment` | 0.895249 | 0.895508 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `random` | 42 | `val` | `logistic_regression` | 0.951933 | 0.959735 | 0.030188 | 1.42 |
| `string_human_physical_no_biogrid_overlap` | `random` | 42 | `test` | `logistic_regression` | 0.950669 | 0.958360 | 0.028833 | 1.42 |
| `string_human_physical_no_biogrid_overlap` | `random` | 42 | `val` | `hist_gradient_boosting` | 0.956622 | 0.964411 | 0.007172 | 5.50 |
| `string_human_physical_no_biogrid_overlap` | `random` | 42 | `test` | `hist_gradient_boosting` | 0.955332 | 0.963088 | 0.005993 | 5.50 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 42 | `val` | `common_neighbors` | 0.828384 | 0.806187 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 42 | `val` | `jaccard` | 0.854726 | 0.856280 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 42 | `val` | `adamic_adar` | 0.839489 | 0.826285 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 42 | `val` | `preferential_attachment` | 0.534492 | 0.548252 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 42 | `test` | `common_neighbors` | 0.825167 | 0.802096 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 42 | `test` | `jaccard` | 0.850818 | 0.851574 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 42 | `test` | `adamic_adar` | 0.836543 | 0.822013 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 42 | `test` | `preferential_attachment` | 0.535067 | 0.549998 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 42 | `val` | `logistic_regression` | 0.882348 | 0.891046 | 0.083356 | 1.09 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 42 | `test` | `logistic_regression` | 0.879937 | 0.887165 | 0.082460 | 1.09 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 42 | `val` | `hist_gradient_boosting` | 0.903420 | 0.915742 | 0.011920 | 5.06 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 42 | `test` | `hist_gradient_boosting` | 0.902542 | 0.915264 | 0.012355 | 5.06 |
| `string_human_physical_no_biogrid_overlap` | `random` | 43 | `val` | `common_neighbors` | 0.918007 | 0.917159 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `random` | 43 | `val` | `jaccard` | 0.912284 | 0.910297 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `random` | 43 | `val` | `adamic_adar` | 0.920175 | 0.923212 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `random` | 43 | `val` | `preferential_attachment` | 0.896963 | 0.897673 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `random` | 43 | `test` | `common_neighbors` | 0.918178 | 0.917337 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `random` | 43 | `test` | `jaccard` | 0.912597 | 0.910263 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `random` | 43 | `test` | `adamic_adar` | 0.920351 | 0.923325 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `random` | 43 | `test` | `preferential_attachment` | 0.898725 | 0.899371 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `random` | 43 | `val` | `logistic_regression` | 0.952080 | 0.959809 | 0.031296 | 1.76 |
| `string_human_physical_no_biogrid_overlap` | `random` | 43 | `test` | `logistic_regression` | 0.952945 | 0.960778 | 0.030311 | 1.76 |
| `string_human_physical_no_biogrid_overlap` | `random` | 43 | `val` | `hist_gradient_boosting` | 0.956287 | 0.963862 | 0.006341 | 4.84 |
| `string_human_physical_no_biogrid_overlap` | `random` | 43 | `test` | `hist_gradient_boosting` | 0.957293 | 0.964834 | 0.006333 | 4.84 |
| `string_human_physical_no_biogrid_overlap` | `random` | 44 | `val` | `common_neighbors` | 0.917697 | 0.916720 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `random` | 44 | `val` | `jaccard` | 0.911840 | 0.909776 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `random` | 44 | `val` | `adamic_adar` | 0.920035 | 0.922996 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `random` | 44 | `val` | `preferential_attachment` | 0.898585 | 0.899118 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `random` | 44 | `test` | `common_neighbors` | 0.917797 | 0.916938 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `random` | 44 | `test` | `jaccard` | 0.912020 | 0.909598 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `random` | 44 | `test` | `adamic_adar` | 0.919984 | 0.923006 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `random` | 44 | `test` | `preferential_attachment` | 0.896681 | 0.897675 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `random` | 44 | `val` | `logistic_regression` | 0.952858 | 0.960617 | 0.030061 | 1.25 |
| `string_human_physical_no_biogrid_overlap` | `random` | 44 | `test` | `logistic_regression` | 0.951552 | 0.959691 | 0.028460 | 1.25 |
| `string_human_physical_no_biogrid_overlap` | `random` | 44 | `val` | `hist_gradient_boosting` | 0.957123 | 0.964652 | 0.006720 | 4.62 |
| `string_human_physical_no_biogrid_overlap` | `random` | 44 | `test` | `hist_gradient_boosting` | 0.956026 | 0.963976 | 0.005528 | 4.62 |
| `string_human_physical_no_biogrid_overlap` | `random` | 45 | `val` | `common_neighbors` | 0.916872 | 0.915718 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `random` | 45 | `val` | `jaccard` | 0.910698 | 0.907191 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `random` | 45 | `val` | `adamic_adar` | 0.919174 | 0.922030 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `random` | 45 | `val` | `preferential_attachment` | 0.895053 | 0.896011 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `random` | 45 | `test` | `common_neighbors` | 0.919293 | 0.918191 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `random` | 45 | `test` | `jaccard` | 0.914002 | 0.912374 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `random` | 45 | `test` | `adamic_adar` | 0.921576 | 0.924394 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `random` | 45 | `test` | `preferential_attachment` | 0.895835 | 0.896386 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `random` | 45 | `val` | `logistic_regression` | 0.950522 | 0.958399 | 0.030213 | 1.85 |
| `string_human_physical_no_biogrid_overlap` | `random` | 45 | `test` | `logistic_regression` | 0.952614 | 0.960494 | 0.030407 | 1.85 |
| `string_human_physical_no_biogrid_overlap` | `random` | 45 | `val` | `hist_gradient_boosting` | 0.955171 | 0.963071 | 0.005874 | 4.83 |
| `string_human_physical_no_biogrid_overlap` | `random` | 45 | `test` | `hist_gradient_boosting` | 0.957258 | 0.964783 | 0.006952 | 4.83 |
| `string_human_physical_no_biogrid_overlap` | `random` | 46 | `val` | `common_neighbors` | 0.918619 | 0.917697 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `random` | 46 | `val` | `jaccard` | 0.912466 | 0.910148 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `random` | 46 | `val` | `adamic_adar` | 0.920839 | 0.923791 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `random` | 46 | `val` | `preferential_attachment` | 0.898766 | 0.899216 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `random` | 46 | `test` | `common_neighbors` | 0.917460 | 0.916373 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `random` | 46 | `test` | `jaccard` | 0.912228 | 0.910065 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `random` | 46 | `test` | `adamic_adar` | 0.919654 | 0.922471 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `random` | 46 | `test` | `preferential_attachment` | 0.895204 | 0.895171 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `random` | 46 | `val` | `logistic_regression` | 0.952948 | 0.960497 | 0.031746 | 1.53 |
| `string_human_physical_no_biogrid_overlap` | `random` | 46 | `test` | `logistic_regression` | 0.951634 | 0.959382 | 0.029645 | 1.53 |
| `string_human_physical_no_biogrid_overlap` | `random` | 46 | `val` | `hist_gradient_boosting` | 0.957391 | 0.964910 | 0.006846 | 4.97 |
| `string_human_physical_no_biogrid_overlap` | `random` | 46 | `test` | `hist_gradient_boosting` | 0.956260 | 0.963946 | 0.005817 | 4.97 |
| `string_human_physical_no_biogrid_overlap` | `random` | 47 | `val` | `common_neighbors` | 0.918889 | 0.917309 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `random` | 47 | `val` | `jaccard` | 0.913836 | 0.911751 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `random` | 47 | `val` | `adamic_adar` | 0.920970 | 0.923126 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `random` | 47 | `val` | `preferential_attachment` | 0.897727 | 0.896766 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `random` | 47 | `test` | `common_neighbors` | 0.918789 | 0.917600 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `random` | 47 | `test` | `jaccard` | 0.912982 | 0.910905 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `random` | 47 | `test` | `adamic_adar` | 0.921109 | 0.923944 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `random` | 47 | `test` | `preferential_attachment` | 0.895619 | 0.896411 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `random` | 47 | `val` | `logistic_regression` | 0.952413 | 0.959472 | 0.031051 | 1.85 |
| `string_human_physical_no_biogrid_overlap` | `random` | 47 | `test` | `logistic_regression` | 0.951543 | 0.959538 | 0.029275 | 1.85 |
| `string_human_physical_no_biogrid_overlap` | `random` | 47 | `val` | `hist_gradient_boosting` | 0.956480 | 0.963550 | 0.005610 | 4.74 |
| `string_human_physical_no_biogrid_overlap` | `random` | 47 | `test` | `hist_gradient_boosting` | 0.956107 | 0.964090 | 0.006432 | 4.74 |
| `string_human_physical_no_biogrid_overlap` | `random` | 48 | `val` | `common_neighbors` | 0.919997 | 0.918396 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `random` | 48 | `val` | `jaccard` | 0.913995 | 0.909771 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `random` | 48 | `val` | `adamic_adar` | 0.922227 | 0.924407 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `random` | 48 | `val` | `preferential_attachment` | 0.898011 | 0.899265 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `random` | 48 | `test` | `common_neighbors` | 0.918189 | 0.917013 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `random` | 48 | `test` | `jaccard` | 0.912587 | 0.910407 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `random` | 48 | `test` | `adamic_adar` | 0.920469 | 0.923330 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `random` | 48 | `test` | `preferential_attachment` | 0.896096 | 0.896681 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `random` | 48 | `val` | `logistic_regression` | 0.952635 | 0.960217 | 0.029521 | 1.90 |
| `string_human_physical_no_biogrid_overlap` | `random` | 48 | `test` | `logistic_regression` | 0.952138 | 0.960033 | 0.030791 | 1.90 |
| `string_human_physical_no_biogrid_overlap` | `random` | 48 | `val` | `hist_gradient_boosting` | 0.957485 | 0.964760 | 0.009250 | 5.45 |
| `string_human_physical_no_biogrid_overlap` | `random` | 48 | `test` | `hist_gradient_boosting` | 0.956656 | 0.964395 | 0.007679 | 5.45 |
| `string_human_physical_no_biogrid_overlap` | `random` | 49 | `val` | `common_neighbors` | 0.916618 | 0.915313 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `random` | 49 | `val` | `jaccard` | 0.911115 | 0.908370 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `random` | 49 | `val` | `adamic_adar` | 0.918922 | 0.921572 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `random` | 49 | `val` | `preferential_attachment` | 0.894719 | 0.894687 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `random` | 49 | `test` | `common_neighbors` | 0.915565 | 0.914117 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `random` | 49 | `test` | `jaccard` | 0.909782 | 0.907542 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `random` | 49 | `test` | `adamic_adar` | 0.917820 | 0.920439 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `random` | 49 | `test` | `preferential_attachment` | 0.894048 | 0.894360 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `random` | 49 | `val` | `logistic_regression` | 0.950643 | 0.958451 | 0.028371 | 1.32 |
| `string_human_physical_no_biogrid_overlap` | `random` | 49 | `test` | `logistic_regression` | 0.950020 | 0.957745 | 0.029215 | 1.32 |
| `string_human_physical_no_biogrid_overlap` | `random` | 49 | `val` | `hist_gradient_boosting` | 0.955388 | 0.963091 | 0.006258 | 4.95 |
| `string_human_physical_no_biogrid_overlap` | `random` | 49 | `test` | `hist_gradient_boosting` | 0.954479 | 0.962184 | 0.006350 | 4.95 |
| `string_human_physical_no_biogrid_overlap` | `random` | 50 | `val` | `common_neighbors` | 0.916580 | 0.915502 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `random` | 50 | `val` | `jaccard` | 0.910775 | 0.907895 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `random` | 50 | `val` | `adamic_adar` | 0.918778 | 0.921529 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `random` | 50 | `val` | `preferential_attachment` | 0.896529 | 0.896862 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `random` | 50 | `test` | `common_neighbors` | 0.917541 | 0.917011 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `random` | 50 | `test` | `jaccard` | 0.911910 | 0.910868 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `random` | 50 | `test` | `adamic_adar` | 0.919770 | 0.923143 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `random` | 50 | `test` | `preferential_attachment` | 0.897361 | 0.898551 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `random` | 50 | `val` | `logistic_regression` | 0.951047 | 0.958832 | 0.031354 | 1.58 |
| `string_human_physical_no_biogrid_overlap` | `random` | 50 | `test` | `logistic_regression` | 0.952106 | 0.960056 | 0.029820 | 1.58 |
| `string_human_physical_no_biogrid_overlap` | `random` | 50 | `val` | `hist_gradient_boosting` | 0.955872 | 0.963611 | 0.006063 | 5.26 |
| `string_human_physical_no_biogrid_overlap` | `random` | 50 | `test` | `hist_gradient_boosting` | 0.956819 | 0.964592 | 0.006548 | 5.26 |
| `string_human_physical_no_biogrid_overlap` | `random` | 51 | `val` | `common_neighbors` | 0.918353 | 0.917399 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `random` | 51 | `val` | `jaccard` | 0.912278 | 0.910355 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `random` | 51 | `val` | `adamic_adar` | 0.920729 | 0.923872 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `random` | 51 | `val` | `preferential_attachment` | 0.897410 | 0.898230 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `random` | 51 | `test` | `common_neighbors` | 0.920814 | 0.919584 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `random` | 51 | `test` | `jaccard` | 0.915500 | 0.914301 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `random` | 51 | `test` | `adamic_adar` | 0.923018 | 0.925561 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `random` | 51 | `test` | `preferential_attachment` | 0.898863 | 0.897942 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `random` | 51 | `val` | `logistic_regression` | 0.952974 | 0.960713 | 0.031824 | 1.37 |
| `string_human_physical_no_biogrid_overlap` | `random` | 51 | `test` | `logistic_regression` | 0.954297 | 0.961821 | 0.031168 | 1.37 |
| `string_human_physical_no_biogrid_overlap` | `random` | 51 | `val` | `hist_gradient_boosting` | 0.957055 | 0.964617 | 0.008353 | 4.76 |
| `string_human_physical_no_biogrid_overlap` | `random` | 51 | `test` | `hist_gradient_boosting` | 0.958412 | 0.965657 | 0.008360 | 4.76 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 43 | `val` | `common_neighbors` | 0.828924 | 0.804916 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 43 | `val` | `jaccard` | 0.853949 | 0.854508 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 43 | `val` | `adamic_adar` | 0.839682 | 0.824640 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 43 | `val` | `preferential_attachment` | 0.533948 | 0.548082 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 43 | `test` | `common_neighbors` | 0.828899 | 0.806019 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 43 | `test` | `jaccard` | 0.854446 | 0.855713 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 43 | `test` | `adamic_adar` | 0.839834 | 0.825744 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 43 | `test` | `preferential_attachment` | 0.537169 | 0.550967 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 43 | `val` | `logistic_regression` | 0.882971 | 0.890438 | 0.081617 | 1.44 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 43 | `test` | `logistic_regression` | 0.881660 | 0.890423 | 0.082379 | 1.44 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 43 | `val` | `hist_gradient_boosting` | 0.903468 | 0.915778 | 0.010247 | 4.86 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 43 | `test` | `hist_gradient_boosting` | 0.902636 | 0.915685 | 0.010844 | 4.86 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 44 | `val` | `common_neighbors` | 0.829468 | 0.807782 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 44 | `val` | `jaccard` | 0.854135 | 0.855239 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 44 | `val` | `adamic_adar` | 0.840714 | 0.828044 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 44 | `val` | `preferential_attachment` | 0.535048 | 0.549946 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 44 | `test` | `common_neighbors` | 0.828674 | 0.806748 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 44 | `test` | `jaccard` | 0.853526 | 0.855295 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 44 | `test` | `adamic_adar` | 0.839538 | 0.826653 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 44 | `test` | `preferential_attachment` | 0.535454 | 0.549984 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 44 | `val` | `logistic_regression` | 0.882671 | 0.890592 | 0.082494 | 0.94 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 44 | `test` | `logistic_regression` | 0.882208 | 0.891015 | 0.079348 | 0.94 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 44 | `val` | `hist_gradient_boosting` | 0.904052 | 0.916408 | 0.008380 | 5.01 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 44 | `test` | `hist_gradient_boosting` | 0.903679 | 0.915753 | 0.009721 | 5.01 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 45 | `val` | `common_neighbors` | 0.826496 | 0.801662 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 45 | `val` | `jaccard` | 0.851917 | 0.851050 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 45 | `val` | `adamic_adar` | 0.837612 | 0.821604 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 45 | `val` | `preferential_attachment` | 0.534477 | 0.547407 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 45 | `test` | `common_neighbors` | 0.828752 | 0.800950 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 45 | `test` | `jaccard` | 0.854559 | 0.851981 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 45 | `test` | `adamic_adar` | 0.839604 | 0.820322 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 45 | `test` | `preferential_attachment` | 0.534529 | 0.548483 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 45 | `val` | `logistic_regression` | 0.879120 | 0.885991 | 0.083422 | 1.12 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 45 | `test` | `logistic_regression` | 0.882883 | 0.887516 | 0.085396 | 1.12 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 45 | `val` | `hist_gradient_boosting` | 0.901949 | 0.914519 | 0.008446 | 4.95 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 45 | `test` | `hist_gradient_boosting` | 0.905091 | 0.916841 | 0.011382 | 4.95 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 46 | `val` | `common_neighbors` | 0.828073 | 0.804923 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 46 | `val` | `jaccard` | 0.853832 | 0.854247 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 46 | `val` | `adamic_adar` | 0.838959 | 0.824624 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 46 | `val` | `preferential_attachment` | 0.535523 | 0.549526 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 46 | `test` | `common_neighbors` | 0.828185 | 0.802759 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 46 | `test` | `jaccard` | 0.852566 | 0.851122 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 46 | `test` | `adamic_adar` | 0.839294 | 0.822604 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 46 | `test` | `preferential_attachment` | 0.536081 | 0.550040 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 46 | `val` | `logistic_regression` | 0.881294 | 0.889284 | 0.081923 | 0.84 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 46 | `test` | `logistic_regression` | 0.878754 | 0.885518 | 0.081818 | 0.84 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 46 | `val` | `hist_gradient_boosting` | 0.903520 | 0.916142 | 0.011340 | 5.44 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 46 | `test` | `hist_gradient_boosting` | 0.902992 | 0.915538 | 0.009101 | 5.44 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 47 | `val` | `common_neighbors` | 0.827363 | 0.801682 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 47 | `val` | `jaccard` | 0.853765 | 0.853191 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 47 | `val` | `adamic_adar` | 0.838445 | 0.821492 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 47 | `val` | `preferential_attachment` | 0.532944 | 0.546084 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 47 | `test` | `common_neighbors` | 0.829326 | 0.806320 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 47 | `test` | `jaccard` | 0.854724 | 0.854375 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 47 | `test` | `adamic_adar` | 0.840555 | 0.826409 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 47 | `test` | `preferential_attachment` | 0.536309 | 0.552002 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 47 | `val` | `logistic_regression` | 0.880625 | 0.887514 | 0.085078 | 1.25 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 47 | `test` | `logistic_regression` | 0.882321 | 0.889571 | 0.086212 | 1.25 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 47 | `val` | `hist_gradient_boosting` | 0.902903 | 0.915390 | 0.009651 | 4.91 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 47 | `test` | `hist_gradient_boosting` | 0.904544 | 0.916474 | 0.012708 | 4.91 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 48 | `val` | `common_neighbors` | 0.829731 | 0.805328 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 48 | `val` | `jaccard` | 0.856219 | 0.856037 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 48 | `val` | `adamic_adar` | 0.841012 | 0.825452 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 48 | `val` | `preferential_attachment` | 0.533675 | 0.547604 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 48 | `test` | `common_neighbors` | 0.829111 | 0.805889 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 48 | `test` | `jaccard` | 0.854559 | 0.855891 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 48 | `test` | `adamic_adar` | 0.840127 | 0.825836 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 48 | `test` | `preferential_attachment` | 0.536567 | 0.550691 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 48 | `val` | `logistic_regression` | 0.884705 | 0.890942 | 0.083235 | 1.05 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 48 | `test` | `logistic_regression` | 0.882509 | 0.890747 | 0.083581 | 1.05 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 48 | `val` | `hist_gradient_boosting` | 0.906286 | 0.917955 | 0.012662 | 5.58 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 48 | `test` | `hist_gradient_boosting` | 0.903575 | 0.915868 | 0.011106 | 5.58 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 49 | `val` | `common_neighbors` | 0.826548 | 0.801280 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 49 | `val` | `jaccard` | 0.851480 | 0.850224 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 49 | `val` | `adamic_adar` | 0.837726 | 0.821204 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 49 | `val` | `preferential_attachment` | 0.535716 | 0.549484 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 49 | `test` | `common_neighbors` | 0.826788 | 0.804611 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 49 | `test` | `jaccard` | 0.852578 | 0.854135 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 49 | `test` | `adamic_adar` | 0.837699 | 0.824658 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 49 | `test` | `preferential_attachment` | 0.535896 | 0.550262 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 49 | `val` | `logistic_regression` | 0.878139 | 0.884827 | 0.083330 | 0.89 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 49 | `test` | `logistic_regression` | 0.881301 | 0.889737 | 0.082519 | 0.89 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 49 | `val` | `hist_gradient_boosting` | 0.901975 | 0.914650 | 0.009840 | 4.95 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 49 | `test` | `hist_gradient_boosting` | 0.902285 | 0.914535 | 0.009930 | 4.95 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 50 | `val` | `common_neighbors` | 0.825747 | 0.802380 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 50 | `val` | `jaccard` | 0.851221 | 0.852004 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 50 | `val` | `adamic_adar` | 0.836672 | 0.822279 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 50 | `val` | `preferential_attachment` | 0.535188 | 0.549353 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 50 | `test` | `common_neighbors` | 0.827728 | 0.805112 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 50 | `test` | `jaccard` | 0.853103 | 0.853573 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 50 | `test` | `adamic_adar` | 0.838743 | 0.824983 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 50 | `test` | `preferential_attachment` | 0.535391 | 0.550145 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 50 | `val` | `logistic_regression` | 0.880210 | 0.888165 | 0.078777 | 1.12 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 50 | `test` | `logistic_regression` | 0.880044 | 0.888568 | 0.079843 | 1.12 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 50 | `val` | `hist_gradient_boosting` | 0.901918 | 0.913805 | 0.009095 | 5.12 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 50 | `test` | `hist_gradient_boosting` | 0.902150 | 0.914853 | 0.009969 | 5.12 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 51 | `val` | `common_neighbors` | 0.826896 | 0.801714 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 51 | `val` | `jaccard` | 0.852443 | 0.851396 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 51 | `val` | `adamic_adar` | 0.838062 | 0.821539 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 51 | `val` | `preferential_attachment` | 0.534427 | 0.549461 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 51 | `test` | `common_neighbors` | 0.828761 | 0.803871 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 51 | `test` | `jaccard` | 0.854313 | 0.853918 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 51 | `test` | `adamic_adar` | 0.839907 | 0.823915 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 51 | `test` | `preferential_attachment` | 0.536036 | 0.548866 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 51 | `val` | `logistic_regression` | 0.881162 | 0.887223 | 0.082724 | 1.08 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 51 | `test` | `logistic_regression` | 0.881136 | 0.888608 | 0.080604 | 1.08 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 51 | `val` | `hist_gradient_boosting` | 0.903061 | 0.915124 | 0.009367 | 4.74 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 51 | `test` | `hist_gradient_boosting` | 0.903330 | 0.915612 | 0.010004 | 4.74 |
| `string_human_physical_no_biogrid_overlap` | `random` | 42 | `val` | `random_forest` | 0.956103 | 0.963881 | 0.006488 | 15.75 |
| `string_human_physical_no_biogrid_overlap` | `random` | 42 | `test` | `random_forest` | 0.955230 | 0.963034 | 0.005673 | 15.75 |
| `string_human_physical_no_biogrid_overlap` | `random` | 43 | `val` | `random_forest` | 0.956246 | 0.963854 | 0.006276 | 15.97 |
| `string_human_physical_no_biogrid_overlap` | `random` | 43 | `test` | `random_forest` | 0.956927 | 0.964472 | 0.005784 | 15.97 |
| `string_human_physical_no_biogrid_overlap` | `random` | 44 | `val` | `random_forest` | 0.956965 | 0.964514 | 0.005753 | 15.71 |
| `string_human_physical_no_biogrid_overlap` | `random` | 44 | `test` | `random_forest` | 0.955210 | 0.963077 | 0.004991 | 15.71 |
| `string_human_physical_no_biogrid_overlap` | `random` | 45 | `val` | `random_forest` | 0.954828 | 0.962654 | 0.004855 | 16.90 |
| `string_human_physical_no_biogrid_overlap` | `random` | 45 | `test` | `random_forest` | 0.956493 | 0.963913 | 0.006153 | 16.90 |
| `string_human_physical_no_biogrid_overlap` | `random` | 46 | `val` | `random_forest` | 0.956913 | 0.964462 | 0.005974 | 16.31 |
| `string_human_physical_no_biogrid_overlap` | `random` | 46 | `test` | `random_forest` | 0.955813 | 0.963574 | 0.005019 | 16.31 |
| `string_human_physical_no_biogrid_overlap` | `random` | 47 | `val` | `random_forest` | 0.956263 | 0.963299 | 0.004876 | 15.54 |
| `string_human_physical_no_biogrid_overlap` | `random` | 47 | `test` | `random_forest` | 0.955729 | 0.963447 | 0.005329 | 15.54 |
| `string_human_physical_no_biogrid_overlap` | `random` | 48 | `val` | `random_forest` | 0.957086 | 0.964404 | 0.009007 | 15.45 |
| `string_human_physical_no_biogrid_overlap` | `random` | 48 | `test` | `random_forest` | 0.956115 | 0.963919 | 0.006424 | 15.45 |
| `string_human_physical_no_biogrid_overlap` | `random` | 49 | `val` | `random_forest` | 0.955159 | 0.962790 | 0.005571 | 15.25 |
| `string_human_physical_no_biogrid_overlap` | `random` | 49 | `test` | `random_forest` | 0.954341 | 0.961817 | 0.005120 | 15.25 |
| `string_human_physical_no_biogrid_overlap` | `random` | 50 | `val` | `random_forest` | 0.955596 | 0.963395 | 0.005123 | 15.94 |
| `string_human_physical_no_biogrid_overlap` | `random` | 50 | `test` | `random_forest` | 0.956424 | 0.964057 | 0.005323 | 15.94 |
| `string_human_physical_no_biogrid_overlap` | `random` | 51 | `val` | `random_forest` | 0.957034 | 0.964691 | 0.007039 | 15.59 |
| `string_human_physical_no_biogrid_overlap` | `random` | 51 | `test` | `random_forest` | 0.958102 | 0.965296 | 0.008109 | 15.59 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 42 | `val` | `random_forest` | 0.903196 | 0.915311 | 0.009188 | 16.75 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 42 | `test` | `random_forest` | 0.902205 | 0.914746 | 0.008534 | 16.75 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 43 | `val` | `random_forest` | 0.903147 | 0.915606 | 0.008507 | 17.50 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 43 | `test` | `random_forest` | 0.902418 | 0.915125 | 0.009008 | 17.50 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 44 | `val` | `random_forest` | 0.903535 | 0.915202 | 0.007232 | 15.42 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 44 | `test` | `random_forest` | 0.902964 | 0.914773 | 0.008542 | 15.42 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 45 | `val` | `random_forest` | 0.901867 | 0.914081 | 0.006219 | 13.37 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 45 | `test` | `random_forest` | 0.905126 | 0.916586 | 0.011142 | 13.37 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 46 | `val` | `random_forest` | 0.903321 | 0.915630 | 0.009089 | 13.17 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 46 | `test` | `random_forest` | 0.902845 | 0.915327 | 0.007748 | 13.17 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 47 | `val` | `random_forest` | 0.902950 | 0.914836 | 0.008942 | 12.88 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 47 | `test` | `random_forest` | 0.904246 | 0.915994 | 0.010745 | 12.88 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 48 | `val` | `random_forest` | 0.905930 | 0.917372 | 0.011558 | 12.66 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 48 | `test` | `random_forest` | 0.903039 | 0.915136 | 0.009256 | 12.66 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 49 | `val` | `random_forest` | 0.902067 | 0.914400 | 0.008050 | 13.39 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 49 | `test` | `random_forest` | 0.902069 | 0.913981 | 0.008224 | 13.39 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 50 | `val` | `random_forest` | 0.901583 | 0.913245 | 0.006956 | 12.70 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 50 | `test` | `random_forest` | 0.902176 | 0.914455 | 0.009734 | 12.70 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 51 | `val` | `random_forest` | 0.903138 | 0.914664 | 0.008005 | 12.61 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 51 | `test` | `random_forest` | 0.903028 | 0.914927 | 0.008296 | 12.61 |
| `biogrid_human_physical_no_string_overlap` | `random` | 42 | `val` | `common_neighbors` | 0.869042 | 0.865159 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `random` | 42 | `val` | `jaccard` | 0.798197 | 0.728652 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `random` | 42 | `val` | `adamic_adar` | 0.874582 | 0.880183 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `random` | 42 | `val` | `preferential_attachment` | 0.939699 | 0.935780 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `random` | 42 | `test` | `common_neighbors` | 0.866958 | 0.862887 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `random` | 42 | `test` | `jaccard` | 0.796340 | 0.726311 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `random` | 42 | `test` | `adamic_adar` | 0.872475 | 0.877964 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `random` | 42 | `test` | `preferential_attachment` | 0.938496 | 0.934362 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `random` | 42 | `val` | `logistic_regression` | 0.938831 | 0.933239 | 0.059888 | 1.21 |
| `biogrid_human_physical_no_string_overlap` | `random` | 42 | `test` | `logistic_regression` | 0.938172 | 0.932812 | 0.060052 | 1.21 |
| `biogrid_human_physical_no_string_overlap` | `random` | 42 | `val` | `hist_gradient_boosting` | 0.945306 | 0.943198 | 0.002481 | 3.67 |
| `biogrid_human_physical_no_string_overlap` | `random` | 42 | `test` | `hist_gradient_boosting` | 0.944687 | 0.942283 | 0.003861 | 3.67 |
| `biogrid_human_physical_no_string_overlap` | `random` | 43 | `val` | `common_neighbors` | 0.868540 | 0.864587 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `random` | 43 | `val` | `jaccard` | 0.797862 | 0.727790 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `random` | 43 | `val` | `adamic_adar` | 0.873916 | 0.879379 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `random` | 43 | `val` | `preferential_attachment` | 0.939845 | 0.935681 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `random` | 43 | `test` | `common_neighbors` | 0.868839 | 0.864355 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `random` | 43 | `test` | `jaccard` | 0.799687 | 0.730337 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `random` | 43 | `test` | `adamic_adar` | 0.874341 | 0.879299 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `random` | 43 | `test` | `preferential_attachment` | 0.938858 | 0.934444 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `random` | 43 | `val` | `logistic_regression` | 0.938987 | 0.933193 | 0.060775 | 1.04 |
| `biogrid_human_physical_no_string_overlap` | `random` | 43 | `test` | `logistic_regression` | 0.938397 | 0.932739 | 0.060402 | 1.04 |
| `biogrid_human_physical_no_string_overlap` | `random` | 43 | `val` | `hist_gradient_boosting` | 0.945196 | 0.942519 | 0.003492 | 3.61 |
| `biogrid_human_physical_no_string_overlap` | `random` | 43 | `test` | `hist_gradient_boosting` | 0.944580 | 0.941701 | 0.002465 | 3.61 |
| `biogrid_human_physical_no_string_overlap` | `random` | 44 | `val` | `common_neighbors` | 0.868051 | 0.863537 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `random` | 44 | `val` | `jaccard` | 0.797121 | 0.725579 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `random` | 44 | `val` | `adamic_adar` | 0.873616 | 0.878576 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `random` | 44 | `val` | `preferential_attachment` | 0.940222 | 0.935636 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `random` | 44 | `test` | `common_neighbors` | 0.867409 | 0.862636 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `random` | 44 | `test` | `jaccard` | 0.798379 | 0.730430 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `random` | 44 | `test` | `adamic_adar` | 0.872928 | 0.877528 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `random` | 44 | `test` | `preferential_attachment` | 0.939271 | 0.934275 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `random` | 44 | `val` | `logistic_regression` | 0.939740 | 0.934390 | 0.060817 | 1.06 |
| `biogrid_human_physical_no_string_overlap` | `random` | 44 | `test` | `logistic_regression` | 0.938813 | 0.932540 | 0.061682 | 1.06 |
| `biogrid_human_physical_no_string_overlap` | `random` | 44 | `val` | `hist_gradient_boosting` | 0.945903 | 0.943156 | 0.003798 | 3.54 |
| `biogrid_human_physical_no_string_overlap` | `random` | 44 | `test` | `hist_gradient_boosting` | 0.944756 | 0.941219 | 0.002812 | 3.54 |
| `biogrid_human_physical_no_string_overlap` | `random` | 45 | `val` | `common_neighbors` | 0.868254 | 0.863644 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `random` | 45 | `val` | `jaccard` | 0.799078 | 0.729321 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `random` | 45 | `val` | `adamic_adar` | 0.873722 | 0.878559 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `random` | 45 | `val` | `preferential_attachment` | 0.939139 | 0.934454 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `random` | 45 | `test` | `common_neighbors` | 0.868674 | 0.864872 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `random` | 45 | `test` | `jaccard` | 0.797890 | 0.727701 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `random` | 45 | `test` | `adamic_adar` | 0.874366 | 0.880034 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `random` | 45 | `test` | `preferential_attachment` | 0.939478 | 0.935529 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `random` | 45 | `val` | `logistic_regression` | 0.938510 | 0.932303 | 0.061258 | 1.04 |
| `biogrid_human_physical_no_string_overlap` | `random` | 45 | `test` | `logistic_regression` | 0.938907 | 0.933123 | 0.061078 | 1.04 |
| `biogrid_human_physical_no_string_overlap` | `random` | 45 | `val` | `hist_gradient_boosting` | 0.944893 | 0.941885 | 0.002189 | 3.53 |
| `biogrid_human_physical_no_string_overlap` | `random` | 45 | `test` | `hist_gradient_boosting` | 0.945600 | 0.943395 | 0.002810 | 3.53 |
| `biogrid_human_physical_no_string_overlap` | `random` | 46 | `val` | `common_neighbors` | 0.868580 | 0.864617 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `random` | 46 | `val` | `jaccard` | 0.798877 | 0.729460 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `random` | 46 | `val` | `adamic_adar` | 0.874174 | 0.879538 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `random` | 46 | `val` | `preferential_attachment` | 0.939508 | 0.934863 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `random` | 46 | `test` | `common_neighbors` | 0.867187 | 0.862877 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `random` | 46 | `test` | `jaccard` | 0.797725 | 0.727522 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `random` | 46 | `test` | `adamic_adar` | 0.872731 | 0.878025 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `random` | 46 | `test` | `preferential_attachment` | 0.938849 | 0.934522 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `random` | 46 | `val` | `logistic_regression` | 0.939304 | 0.933684 | 0.059743 | 1.08 |
| `biogrid_human_physical_no_string_overlap` | `random` | 46 | `test` | `logistic_regression` | 0.938373 | 0.933123 | 0.059924 | 1.08 |
| `biogrid_human_physical_no_string_overlap` | `random` | 46 | `val` | `hist_gradient_boosting` | 0.945718 | 0.942637 | 0.003288 | 3.46 |
| `biogrid_human_physical_no_string_overlap` | `random` | 46 | `test` | `hist_gradient_boosting` | 0.944596 | 0.941939 | 0.003704 | 3.46 |
| `biogrid_human_physical_no_string_overlap` | `random` | 47 | `val` | `common_neighbors` | 0.864583 | 0.860009 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `random` | 47 | `val` | `jaccard` | 0.794185 | 0.722920 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `random` | 47 | `val` | `adamic_adar` | 0.870236 | 0.875166 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `random` | 47 | `val` | `preferential_attachment` | 0.937761 | 0.932617 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `random` | 47 | `test` | `common_neighbors` | 0.867905 | 0.862769 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `random` | 47 | `test` | `jaccard` | 0.797348 | 0.727896 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `random` | 47 | `test` | `adamic_adar` | 0.873719 | 0.878150 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `random` | 47 | `test` | `preferential_attachment` | 0.939205 | 0.934018 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `random` | 47 | `val` | `logistic_regression` | 0.936820 | 0.929954 | 0.060498 | 1.01 |
| `biogrid_human_physical_no_string_overlap` | `random` | 47 | `test` | `logistic_regression` | 0.938370 | 0.931534 | 0.061446 | 1.01 |
| `biogrid_human_physical_no_string_overlap` | `random` | 47 | `val` | `hist_gradient_boosting` | 0.943636 | 0.940161 | 0.004105 | 3.55 |
| `biogrid_human_physical_no_string_overlap` | `random` | 47 | `test` | `hist_gradient_boosting` | 0.945174 | 0.941809 | 0.003589 | 3.55 |
| `biogrid_human_physical_no_string_overlap` | `random` | 48 | `val` | `common_neighbors` | 0.866261 | 0.861437 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `random` | 48 | `val` | `jaccard` | 0.796930 | 0.728067 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `random` | 48 | `val` | `adamic_adar` | 0.871886 | 0.876412 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `random` | 48 | `val` | `preferential_attachment` | 0.938287 | 0.933553 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `random` | 48 | `test` | `common_neighbors` | 0.866764 | 0.862837 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `random` | 48 | `test` | `jaccard` | 0.795887 | 0.726167 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `random` | 48 | `test` | `adamic_adar` | 0.872550 | 0.878204 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `random` | 48 | `test` | `preferential_attachment` | 0.939021 | 0.935093 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `random` | 48 | `val` | `logistic_regression` | 0.937831 | 0.931646 | 0.062035 | 1.15 |
| `biogrid_human_physical_no_string_overlap` | `random` | 48 | `test` | `logistic_regression` | 0.938745 | 0.933395 | 0.062772 | 1.15 |
| `biogrid_human_physical_no_string_overlap` | `random` | 48 | `val` | `hist_gradient_boosting` | 0.944231 | 0.941262 | 0.002086 | 3.54 |
| `biogrid_human_physical_no_string_overlap` | `random` | 48 | `test` | `hist_gradient_boosting` | 0.944792 | 0.942429 | 0.002262 | 3.54 |
| `biogrid_human_physical_no_string_overlap` | `random` | 49 | `val` | `common_neighbors` | 0.868741 | 0.863319 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `random` | 49 | `val` | `jaccard` | 0.798745 | 0.728350 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `random` | 49 | `val` | `adamic_adar` | 0.874349 | 0.878357 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `random` | 49 | `val` | `preferential_attachment` | 0.938808 | 0.934089 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `random` | 49 | `test` | `common_neighbors` | 0.868414 | 0.864408 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `random` | 49 | `test` | `jaccard` | 0.798764 | 0.728556 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `random` | 49 | `test` | `adamic_adar` | 0.874031 | 0.879448 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `random` | 49 | `test` | `preferential_attachment` | 0.939211 | 0.934899 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `random` | 49 | `val` | `logistic_regression` | 0.938469 | 0.932517 | 0.059887 | 1.16 |
| `biogrid_human_physical_no_string_overlap` | `random` | 49 | `test` | `logistic_regression` | 0.938732 | 0.933303 | 0.060560 | 1.16 |
| `biogrid_human_physical_no_string_overlap` | `random` | 49 | `val` | `hist_gradient_boosting` | 0.944888 | 0.941657 | 0.002914 | 3.44 |
| `biogrid_human_physical_no_string_overlap` | `random` | 49 | `test` | `hist_gradient_boosting` | 0.945039 | 0.942429 | 0.003754 | 3.44 |
| `biogrid_human_physical_no_string_overlap` | `random` | 50 | `val` | `common_neighbors` | 0.867675 | 0.864343 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `random` | 50 | `val` | `jaccard` | 0.797049 | 0.727441 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `random` | 50 | `val` | `adamic_adar` | 0.873194 | 0.879280 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `random` | 50 | `val` | `preferential_attachment` | 0.939474 | 0.935366 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `random` | 50 | `test` | `common_neighbors` | 0.868775 | 0.864360 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `random` | 50 | `test` | `jaccard` | 0.797914 | 0.727114 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `random` | 50 | `test` | `adamic_adar` | 0.874563 | 0.879663 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `random` | 50 | `test` | `preferential_attachment` | 0.939862 | 0.935636 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `random` | 50 | `val` | `logistic_regression` | 0.938814 | 0.933457 | 0.060295 | 1.15 |
| `biogrid_human_physical_no_string_overlap` | `random` | 50 | `test` | `logistic_regression` | 0.939340 | 0.933982 | 0.061559 | 1.15 |
| `biogrid_human_physical_no_string_overlap` | `random` | 50 | `val` | `hist_gradient_boosting` | 0.944901 | 0.942546 | 0.003214 | 3.45 |
| `biogrid_human_physical_no_string_overlap` | `random` | 50 | `test` | `hist_gradient_boosting` | 0.945603 | 0.943255 | 0.002222 | 3.45 |
| `biogrid_human_physical_no_string_overlap` | `random` | 51 | `val` | `common_neighbors` | 0.866596 | 0.863383 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `random` | 51 | `val` | `jaccard` | 0.795268 | 0.725453 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `random` | 51 | `val` | `adamic_adar` | 0.872325 | 0.878843 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `random` | 51 | `val` | `preferential_attachment` | 0.939013 | 0.935283 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `random` | 51 | `test` | `common_neighbors` | 0.869712 | 0.865235 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `random` | 51 | `test` | `jaccard` | 0.801411 | 0.732862 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `random` | 51 | `test` | `adamic_adar` | 0.874986 | 0.879923 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `random` | 51 | `test` | `preferential_attachment` | 0.939011 | 0.934649 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `random` | 51 | `val` | `logistic_regression` | 0.938496 | 0.933685 | 0.061366 | 1.04 |
| `biogrid_human_physical_no_string_overlap` | `random` | 51 | `test` | `logistic_regression` | 0.938117 | 0.931783 | 0.062833 | 1.04 |
| `biogrid_human_physical_no_string_overlap` | `random` | 51 | `val` | `hist_gradient_boosting` | 0.944792 | 0.942697 | 0.002745 | 3.39 |
| `biogrid_human_physical_no_string_overlap` | `random` | 51 | `test` | `hist_gradient_boosting` | 0.944778 | 0.942098 | 0.003175 | 3.39 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 42 | `val` | `common_neighbors` | 0.594955 | 0.587024 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 42 | `val` | `jaccard` | 0.579375 | 0.567821 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 42 | `val` | `adamic_adar` | 0.600616 | 0.593870 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 42 | `val` | `preferential_attachment` | 0.547059 | 0.553000 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 42 | `test` | `common_neighbors` | 0.596538 | 0.589976 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 42 | `test` | `jaccard` | 0.579839 | 0.569778 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 42 | `test` | `adamic_adar` | 0.602039 | 0.596837 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 42 | `test` | `preferential_attachment` | 0.547768 | 0.555206 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 42 | `val` | `logistic_regression` | 0.601474 | 0.592090 | 0.020844 | 0.67 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 42 | `test` | `logistic_regression` | 0.602701 | 0.595038 | 0.020634 | 0.67 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 42 | `val` | `hist_gradient_boosting` | 0.683633 | 0.682677 | 0.023620 | 3.42 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 42 | `test` | `hist_gradient_boosting` | 0.684032 | 0.683397 | 0.022861 | 3.42 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 43 | `val` | `common_neighbors` | 0.594142 | 0.587533 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 43 | `val` | `jaccard` | 0.579195 | 0.569006 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 43 | `val` | `adamic_adar` | 0.599746 | 0.594262 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 43 | `val` | `preferential_attachment` | 0.546867 | 0.553301 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 43 | `test` | `common_neighbors` | 0.596314 | 0.588612 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 43 | `test` | `jaccard` | 0.579168 | 0.566335 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 43 | `test` | `adamic_adar` | 0.602038 | 0.595735 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 43 | `test` | `preferential_attachment` | 0.549725 | 0.556270 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 43 | `val` | `logistic_regression` | 0.600106 | 0.592695 | 0.017812 | 0.72 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 43 | `test` | `logistic_regression` | 0.600750 | 0.591422 | 0.018414 | 0.72 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 43 | `val` | `hist_gradient_boosting` | 0.682158 | 0.681632 | 0.022786 | 3.32 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 43 | `test` | `hist_gradient_boosting` | 0.683157 | 0.682106 | 0.022672 | 3.32 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 44 | `val` | `common_neighbors` | 0.594478 | 0.585542 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 44 | `val` | `jaccard` | 0.578947 | 0.567034 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 44 | `val` | `adamic_adar` | 0.600135 | 0.592463 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 44 | `val` | `preferential_attachment` | 0.546103 | 0.551960 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 44 | `test` | `common_neighbors` | 0.596445 | 0.589854 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 44 | `test` | `jaccard` | 0.580325 | 0.570603 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 44 | `test` | `adamic_adar` | 0.602156 | 0.596802 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 44 | `test` | `preferential_attachment` | 0.548811 | 0.555576 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 44 | `val` | `logistic_regression` | 0.600659 | 0.590600 | 0.019428 | 0.69 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 44 | `test` | `logistic_regression` | 0.603040 | 0.595812 | 0.019886 | 0.69 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 44 | `val` | `hist_gradient_boosting` | 0.683643 | 0.681908 | 0.022924 | 3.29 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 44 | `test` | `hist_gradient_boosting` | 0.683816 | 0.683861 | 0.023753 | 3.29 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 45 | `val` | `common_neighbors` | 0.595257 | 0.587625 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 45 | `val` | `jaccard` | 0.580178 | 0.569463 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 45 | `val` | `adamic_adar` | 0.600952 | 0.594328 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 45 | `val` | `preferential_attachment` | 0.546841 | 0.552532 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 45 | `test` | `common_neighbors` | 0.595079 | 0.588897 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 45 | `test` | `jaccard` | 0.577622 | 0.567404 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 45 | `test` | `adamic_adar` | 0.601215 | 0.595694 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 45 | `test` | `preferential_attachment` | 0.549215 | 0.555810 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 45 | `val` | `logistic_regression` | 0.600536 | 0.593133 | 0.018405 | 0.67 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 45 | `test` | `logistic_regression` | 0.598443 | 0.593003 | 0.017273 | 0.67 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 45 | `val` | `hist_gradient_boosting` | 0.683656 | 0.684230 | 0.022826 | 3.42 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 45 | `test` | `hist_gradient_boosting` | 0.683941 | 0.683749 | 0.023418 | 3.42 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 46 | `val` | `common_neighbors` | 0.594821 | 0.587940 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 46 | `val` | `jaccard` | 0.578816 | 0.568131 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 46 | `val` | `adamic_adar` | 0.600937 | 0.595067 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 46 | `val` | `preferential_attachment` | 0.547862 | 0.554207 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 46 | `test` | `common_neighbors` | 0.595213 | 0.588396 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 46 | `test` | `jaccard` | 0.579178 | 0.566659 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 46 | `test` | `adamic_adar` | 0.601068 | 0.595385 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 46 | `test` | `preferential_attachment` | 0.548252 | 0.555461 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 46 | `val` | `logistic_regression` | 0.599572 | 0.591405 | 0.019535 | 0.69 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 46 | `test` | `logistic_regression` | 0.599644 | 0.591309 | 0.018893 | 0.69 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 46 | `val` | `hist_gradient_boosting` | 0.685712 | 0.686432 | 0.025148 | 3.37 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 46 | `test` | `hist_gradient_boosting` | 0.683441 | 0.681983 | 0.023919 | 3.37 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 47 | `val` | `common_neighbors` | 0.593909 | 0.588138 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 47 | `val` | `jaccard` | 0.577963 | 0.567569 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 47 | `val` | `adamic_adar` | 0.599690 | 0.594790 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 47 | `val` | `preferential_attachment` | 0.546648 | 0.553671 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 47 | `test` | `common_neighbors` | 0.596343 | 0.589255 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 47 | `test` | `jaccard` | 0.579656 | 0.567457 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 47 | `test` | `adamic_adar` | 0.602307 | 0.596151 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 47 | `test` | `preferential_attachment` | 0.549573 | 0.555930 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 47 | `val` | `logistic_regression` | 0.599998 | 0.592686 | 0.017150 | 0.69 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 47 | `test` | `logistic_regression` | 0.601111 | 0.593256 | 0.019375 | 0.69 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 47 | `val` | `hist_gradient_boosting` | 0.684351 | 0.684495 | 0.022903 | 3.36 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 47 | `test` | `hist_gradient_boosting` | 0.686285 | 0.685502 | 0.024799 | 3.36 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 48 | `val` | `common_neighbors` | 0.594872 | 0.588362 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 48 | `val` | `jaccard` | 0.579724 | 0.569705 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 48 | `val` | `adamic_adar` | 0.600448 | 0.594918 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 48 | `val` | `preferential_attachment` | 0.547004 | 0.553057 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 48 | `test` | `common_neighbors` | 0.596119 | 0.589649 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 48 | `test` | `jaccard` | 0.579591 | 0.570107 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 48 | `test` | `adamic_adar` | 0.602096 | 0.596900 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 48 | `test` | `preferential_attachment` | 0.548757 | 0.555428 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 48 | `val` | `logistic_regression` | 0.600519 | 0.593801 | 0.019038 | 0.69 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 48 | `test` | `logistic_regression` | 0.601508 | 0.595066 | 0.020811 | 0.69 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 48 | `val` | `hist_gradient_boosting` | 0.685247 | 0.683661 | 0.025161 | 3.41 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 48 | `test` | `hist_gradient_boosting` | 0.684004 | 0.683808 | 0.022936 | 3.41 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 49 | `val` | `common_neighbors` | 0.594920 | 0.587143 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 49 | `val` | `jaccard` | 0.580186 | 0.568544 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 49 | `val` | `adamic_adar` | 0.600604 | 0.594008 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 49 | `val` | `preferential_attachment` | 0.546912 | 0.553382 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 49 | `test` | `common_neighbors` | 0.596213 | 0.589719 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 49 | `test` | `jaccard` | 0.580120 | 0.569742 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 49 | `test` | `adamic_adar` | 0.602094 | 0.596647 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 49 | `test` | `preferential_attachment` | 0.548051 | 0.555095 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 49 | `val` | `logistic_regression` | 0.600709 | 0.591715 | 0.019374 | 0.67 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 49 | `test` | `logistic_regression` | 0.601240 | 0.594248 | 0.019846 | 0.67 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 49 | `val` | `hist_gradient_boosting` | 0.683782 | 0.683693 | 0.023531 | 3.33 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 49 | `test` | `hist_gradient_boosting` | 0.684860 | 0.684472 | 0.025671 | 3.33 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 50 | `val` | `common_neighbors` | 0.595429 | 0.590284 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 50 | `val` | `jaccard` | 0.579478 | 0.570496 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 50 | `val` | `adamic_adar` | 0.600767 | 0.596712 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 50 | `val` | `preferential_attachment` | 0.547911 | 0.554014 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 50 | `test` | `common_neighbors` | 0.597311 | 0.591425 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 50 | `test` | `jaccard` | 0.579364 | 0.568432 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 50 | `test` | `adamic_adar` | 0.603099 | 0.598278 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 50 | `test` | `preferential_attachment` | 0.548949 | 0.556315 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 50 | `val` | `logistic_regression` | 0.601830 | 0.596284 | 0.018716 | 0.67 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 50 | `test` | `logistic_regression` | 0.602543 | 0.595807 | 0.019870 | 0.67 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 50 | `val` | `hist_gradient_boosting` | 0.683551 | 0.683645 | 0.023299 | 3.35 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 50 | `test` | `hist_gradient_boosting` | 0.685795 | 0.686256 | 0.025309 | 3.35 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 51 | `val` | `common_neighbors` | 0.595226 | 0.588774 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 51 | `val` | `jaccard` | 0.579577 | 0.569494 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 51 | `val` | `adamic_adar` | 0.601212 | 0.595714 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 51 | `val` | `preferential_attachment` | 0.547697 | 0.554281 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 51 | `test` | `common_neighbors` | 0.598190 | 0.589935 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 51 | `test` | `jaccard` | 0.581473 | 0.568807 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 51 | `test` | `adamic_adar` | 0.603862 | 0.596654 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 51 | `test` | `preferential_attachment` | 0.550111 | 0.556979 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 51 | `val` | `logistic_regression` | 0.600749 | 0.593932 | 0.019292 | 0.69 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 51 | `test` | `logistic_regression` | 0.602581 | 0.593786 | 0.020143 | 0.69 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 51 | `val` | `hist_gradient_boosting` | 0.684012 | 0.682280 | 0.023232 | 3.30 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 51 | `test` | `hist_gradient_boosting` | 0.683725 | 0.680775 | 0.024203 | 3.30 |
| `biogrid_human_physical_no_string_overlap` | `random` | 42 | `val` | `random_forest` | 0.944276 | 0.941981 | 0.004087 | 19.26 |
| `biogrid_human_physical_no_string_overlap` | `random` | 42 | `test` | `random_forest` | 0.943437 | 0.940832 | 0.003955 | 19.26 |
| `biogrid_human_physical_no_string_overlap` | `random` | 43 | `val` | `random_forest` | 0.944469 | 0.941892 | 0.004028 | 19.96 |
| `biogrid_human_physical_no_string_overlap` | `random` | 43 | `test` | `random_forest` | 0.943342 | 0.939979 | 0.002978 | 19.96 |
| `biogrid_human_physical_no_string_overlap` | `random` | 44 | `val` | `random_forest` | 0.944721 | 0.941886 | 0.004059 | 20.53 |
| `biogrid_human_physical_no_string_overlap` | `random` | 44 | `test` | `random_forest` | 0.943930 | 0.940188 | 0.003524 | 20.53 |
| `biogrid_human_physical_no_string_overlap` | `random` | 45 | `val` | `random_forest` | 0.943958 | 0.940838 | 0.003116 | 19.99 |
| `biogrid_human_physical_no_string_overlap` | `random` | 45 | `test` | `random_forest` | 0.944488 | 0.941727 | 0.004645 | 19.99 |
| `biogrid_human_physical_no_string_overlap` | `random` | 46 | `val` | `random_forest` | 0.944654 | 0.941356 | 0.004481 | 20.81 |
| `biogrid_human_physical_no_string_overlap` | `random` | 46 | `test` | `random_forest` | 0.943668 | 0.940602 | 0.004273 | 20.81 |
| `biogrid_human_physical_no_string_overlap` | `random` | 47 | `val` | `random_forest` | 0.942554 | 0.938880 | 0.004206 | 20.25 |
| `biogrid_human_physical_no_string_overlap` | `random` | 47 | `test` | `random_forest` | 0.944161 | 0.940717 | 0.003910 | 20.25 |
| `biogrid_human_physical_no_string_overlap` | `random` | 48 | `val` | `random_forest` | 0.943056 | 0.939946 | 0.003113 | 20.86 |
| `biogrid_human_physical_no_string_overlap` | `random` | 48 | `test` | `random_forest` | 0.943625 | 0.940798 | 0.002859 | 20.86 |
| `biogrid_human_physical_no_string_overlap` | `random` | 49 | `val` | `random_forest` | 0.943832 | 0.940549 | 0.004366 | 20.72 |
| `biogrid_human_physical_no_string_overlap` | `random` | 49 | `test` | `random_forest` | 0.943958 | 0.941294 | 0.004851 | 20.72 |
| `biogrid_human_physical_no_string_overlap` | `random` | 50 | `val` | `random_forest` | 0.944091 | 0.941629 | 0.003366 | 20.20 |
| `biogrid_human_physical_no_string_overlap` | `random` | 50 | `test` | `random_forest` | 0.944591 | 0.941962 | 0.002926 | 20.20 |
| `biogrid_human_physical_no_string_overlap` | `random` | 51 | `val` | `random_forest` | 0.943620 | 0.941275 | 0.004745 | 21.01 |
| `biogrid_human_physical_no_string_overlap` | `random` | 51 | `test` | `random_forest` | 0.943655 | 0.940673 | 0.003701 | 21.01 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 42 | `val` | `random_forest` | 0.687218 | 0.688562 | 0.024002 | 24.15 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 42 | `test` | `random_forest` | 0.686731 | 0.687099 | 0.023358 | 24.15 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 43 | `val` | `random_forest` | 0.684750 | 0.684529 | 0.023288 | 24.02 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 43 | `test` | `random_forest` | 0.685610 | 0.686451 | 0.023431 | 24.02 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 44 | `val` | `random_forest` | 0.685269 | 0.686087 | 0.022341 | 24.05 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 44 | `test` | `random_forest` | 0.684605 | 0.685711 | 0.023984 | 24.05 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 45 | `val` | `random_forest` | 0.685661 | 0.686731 | 0.024419 | 23.39 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 45 | `test` | `random_forest` | 0.685917 | 0.686773 | 0.024044 | 23.39 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 46 | `val` | `random_forest` | 0.687919 | 0.688221 | 0.025775 | 23.22 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 46 | `test` | `random_forest` | 0.685131 | 0.685878 | 0.023777 | 23.22 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 47 | `val` | `random_forest` | 0.685171 | 0.686922 | 0.022896 | 26.28 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 47 | `test` | `random_forest` | 0.687691 | 0.689367 | 0.024683 | 26.28 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 48 | `val` | `random_forest` | 0.686275 | 0.685381 | 0.026080 | 25.31 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 48 | `test` | `random_forest` | 0.684764 | 0.685912 | 0.024561 | 25.31 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 49 | `val` | `random_forest` | 0.685259 | 0.686335 | 0.025310 | 26.05 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 49 | `test` | `random_forest` | 0.686920 | 0.686813 | 0.025263 | 26.05 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 50 | `val` | `random_forest` | 0.684016 | 0.684959 | 0.021432 | 25.94 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 50 | `test` | `random_forest` | 0.687628 | 0.687162 | 0.024642 | 25.94 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 51 | `val` | `random_forest` | 0.686229 | 0.685198 | 0.024482 | 25.24 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 51 | `test` | `random_forest` | 0.685764 | 0.684228 | 0.024236 | 25.24 |
| `string_human_physical_v12` | `random` | 42 | `val` | `common_neighbors` | 0.917360 | 0.917946 |  | 0.00 |
| `string_human_physical_v12` | `random` | 42 | `val` | `jaccard` | 0.908305 | 0.910789 |  | 0.00 |
| `string_human_physical_v12` | `random` | 42 | `val` | `adamic_adar` | 0.920481 | 0.926423 |  | 0.00 |
| `string_human_physical_v12` | `random` | 42 | `val` | `preferential_attachment` | 0.881074 | 0.884569 |  | 0.00 |
| `string_human_physical_v12` | `random` | 42 | `test` | `common_neighbors` | 0.917830 | 0.918560 |  | 0.00 |
| `string_human_physical_v12` | `random` | 42 | `test` | `jaccard` | 0.908563 | 0.911427 |  | 0.00 |
| `string_human_physical_v12` | `random` | 42 | `test` | `adamic_adar` | 0.921106 | 0.927194 |  | 0.00 |
| `string_human_physical_v12` | `random` | 42 | `test` | `preferential_attachment` | 0.882483 | 0.885910 |  | 0.00 |
| `string_human_physical_v12` | `random` | 42 | `val` | `logistic_regression` | 0.935107 | 0.945228 | 0.026388 | 1.55 |
| `string_human_physical_v12` | `random` | 42 | `test` | `logistic_regression` | 0.936185 | 0.946312 | 0.026518 | 1.55 |
| `string_human_physical_v12` | `random` | 42 | `val` | `hist_gradient_boosting` | 0.940378 | 0.950093 | 0.003956 | 4.71 |
| `string_human_physical_v12` | `random` | 42 | `test` | `hist_gradient_boosting` | 0.941380 | 0.950931 | 0.003880 | 4.71 |
| `string_human_physical_v12` | `random` | 43 | `val` | `common_neighbors` | 0.917904 | 0.918243 |  | 0.00 |
| `string_human_physical_v12` | `random` | 43 | `val` | `jaccard` | 0.908739 | 0.910866 |  | 0.00 |
| `string_human_physical_v12` | `random` | 43 | `val` | `adamic_adar` | 0.921156 | 0.926896 |  | 0.00 |
| `string_human_physical_v12` | `random` | 43 | `val` | `preferential_attachment` | 0.880738 | 0.884487 |  | 0.00 |
| `string_human_physical_v12` | `random` | 43 | `test` | `common_neighbors` | 0.916765 | 0.917204 |  | 0.00 |
| `string_human_physical_v12` | `random` | 43 | `test` | `jaccard` | 0.907414 | 0.909947 |  | 0.00 |
| `string_human_physical_v12` | `random` | 43 | `test` | `adamic_adar` | 0.920029 | 0.925932 |  | 0.00 |
| `string_human_physical_v12` | `random` | 43 | `test` | `preferential_attachment` | 0.880949 | 0.884323 |  | 0.00 |
| `string_human_physical_v12` | `random` | 43 | `val` | `logistic_regression` | 0.935487 | 0.945703 | 0.026462 | 1.54 |
| `string_human_physical_v12` | `random` | 43 | `test` | `logistic_regression` | 0.935165 | 0.945235 | 0.027507 | 1.54 |
| `string_human_physical_v12` | `random` | 43 | `val` | `hist_gradient_boosting` | 0.940863 | 0.950435 | 0.004885 | 4.61 |
| `string_human_physical_v12` | `random` | 43 | `test` | `hist_gradient_boosting` | 0.940412 | 0.949817 | 0.002918 | 4.61 |
| `string_human_physical_v12` | `random` | 44 | `val` | `common_neighbors` | 0.916730 | 0.917537 |  | 0.00 |
| `string_human_physical_v12` | `random` | 44 | `val` | `jaccard` | 0.907308 | 0.909899 |  | 0.00 |
| `string_human_physical_v12` | `random` | 44 | `val` | `adamic_adar` | 0.919980 | 0.926155 |  | 0.00 |
| `string_human_physical_v12` | `random` | 44 | `val` | `preferential_attachment` | 0.881330 | 0.885104 |  | 0.00 |
| `string_human_physical_v12` | `random` | 44 | `test` | `common_neighbors` | 0.916948 | 0.917616 |  | 0.00 |
| `string_human_physical_v12` | `random` | 44 | `test` | `jaccard` | 0.907993 | 0.910979 |  | 0.00 |
| `string_human_physical_v12` | `random` | 44 | `test` | `adamic_adar` | 0.920178 | 0.926203 |  | 0.00 |
| `string_human_physical_v12` | `random` | 44 | `test` | `preferential_attachment` | 0.880115 | 0.883486 |  | 0.00 |
| `string_human_physical_v12` | `random` | 44 | `val` | `logistic_regression` | 0.935321 | 0.945439 | 0.026010 | 1.54 |
| `string_human_physical_v12` | `random` | 44 | `test` | `logistic_regression` | 0.934952 | 0.945352 | 0.025417 | 1.54 |
| `string_human_physical_v12` | `random` | 44 | `val` | `hist_gradient_boosting` | 0.940240 | 0.949919 | 0.004440 | 4.55 |
| `string_human_physical_v12` | `random` | 44 | `test` | `hist_gradient_boosting` | 0.940099 | 0.949913 | 0.004301 | 4.55 |
| `string_human_physical_v12` | `random` | 45 | `val` | `common_neighbors` | 0.917602 | 0.918358 |  | 0.00 |
| `string_human_physical_v12` | `random` | 45 | `val` | `jaccard` | 0.908248 | 0.911251 |  | 0.00 |
| `string_human_physical_v12` | `random` | 45 | `val` | `adamic_adar` | 0.920858 | 0.927038 |  | 0.00 |
| `string_human_physical_v12` | `random` | 45 | `val` | `preferential_attachment` | 0.882219 | 0.885720 |  | 0.00 |
| `string_human_physical_v12` | `random` | 45 | `test` | `common_neighbors` | 0.917725 | 0.918044 |  | 0.00 |
| `string_human_physical_v12` | `random` | 45 | `test` | `jaccard` | 0.908345 | 0.910855 |  | 0.00 |
| `string_human_physical_v12` | `random` | 45 | `test` | `adamic_adar` | 0.920991 | 0.926723 |  | 0.00 |
| `string_human_physical_v12` | `random` | 45 | `test` | `preferential_attachment` | 0.881210 | 0.884530 |  | 0.00 |
| `string_human_physical_v12` | `random` | 45 | `val` | `logistic_regression` | 0.936064 | 0.946268 | 0.027105 | 1.47 |
| `string_human_physical_v12` | `random` | 45 | `test` | `logistic_regression` | 0.935485 | 0.945293 | 0.026953 | 1.47 |
| `string_human_physical_v12` | `random` | 45 | `val` | `hist_gradient_boosting` | 0.941230 | 0.950802 | 0.003198 | 4.39 |
| `string_human_physical_v12` | `random` | 45 | `test` | `hist_gradient_boosting` | 0.940805 | 0.950094 | 0.003626 | 4.39 |
| `string_human_physical_v12` | `random` | 46 | `val` | `common_neighbors` | 0.917371 | 0.917878 |  | 0.00 |
| `string_human_physical_v12` | `random` | 46 | `val` | `jaccard` | 0.908501 | 0.911200 |  | 0.00 |
| `string_human_physical_v12` | `random` | 46 | `val` | `adamic_adar` | 0.920614 | 0.926462 |  | 0.00 |
| `string_human_physical_v12` | `random` | 46 | `val` | `preferential_attachment` | 0.880161 | 0.883292 |  | 0.00 |
| `string_human_physical_v12` | `random` | 46 | `test` | `common_neighbors` | 0.918436 | 0.918970 |  | 0.00 |
| `string_human_physical_v12` | `random` | 46 | `test` | `jaccard` | 0.908916 | 0.911427 |  | 0.00 |
| `string_human_physical_v12` | `random` | 46 | `test` | `adamic_adar` | 0.921650 | 0.927509 |  | 0.00 |
| `string_human_physical_v12` | `random` | 46 | `test` | `preferential_attachment` | 0.882712 | 0.886079 |  | 0.00 |
| `string_human_physical_v12` | `random` | 46 | `val` | `logistic_regression` | 0.935394 | 0.945374 | 0.024196 | 1.39 |
| `string_human_physical_v12` | `random` | 46 | `test` | `logistic_regression` | 0.936624 | 0.946637 | 0.026264 | 1.39 |
| `string_human_physical_v12` | `random` | 46 | `val` | `hist_gradient_boosting` | 0.940498 | 0.950020 | 0.004728 | 4.52 |
| `string_human_physical_v12` | `random` | 46 | `test` | `hist_gradient_boosting` | 0.941717 | 0.951121 | 0.004048 | 4.52 |
| `string_human_physical_v12` | `random` | 47 | `val` | `common_neighbors` | 0.917572 | 0.918196 |  | 0.00 |
| `string_human_physical_v12` | `random` | 47 | `val` | `jaccard` | 0.908639 | 0.911497 |  | 0.00 |
| `string_human_physical_v12` | `random` | 47 | `val` | `adamic_adar` | 0.920803 | 0.926839 |  | 0.00 |
| `string_human_physical_v12` | `random` | 47 | `val` | `preferential_attachment` | 0.882404 | 0.885902 |  | 0.00 |
| `string_human_physical_v12` | `random` | 47 | `test` | `common_neighbors` | 0.916841 | 0.917352 |  | 0.00 |
| `string_human_physical_v12` | `random` | 47 | `test` | `jaccard` | 0.907999 | 0.910454 |  | 0.00 |
| `string_human_physical_v12` | `random` | 47 | `test` | `adamic_adar` | 0.920090 | 0.925990 |  | 0.00 |
| `string_human_physical_v12` | `random` | 47 | `test` | `preferential_attachment` | 0.880144 | 0.883662 |  | 0.00 |
| `string_human_physical_v12` | `random` | 47 | `val` | `logistic_regression` | 0.936588 | 0.946543 | 0.028226 | 1.51 |
| `string_human_physical_v12` | `random` | 47 | `test` | `logistic_regression` | 0.935095 | 0.945167 | 0.025530 | 1.51 |
| `string_human_physical_v12` | `random` | 47 | `val` | `hist_gradient_boosting` | 0.941593 | 0.950879 | 0.003070 | 4.43 |
| `string_human_physical_v12` | `random` | 47 | `test` | `hist_gradient_boosting` | 0.940288 | 0.949696 | 0.003540 | 4.43 |
| `string_human_physical_v12` | `random` | 48 | `val` | `common_neighbors` | 0.917130 | 0.917731 |  | 0.00 |
| `string_human_physical_v12` | `random` | 48 | `val` | `jaccard` | 0.907647 | 0.909638 |  | 0.00 |
| `string_human_physical_v12` | `random` | 48 | `val` | `adamic_adar` | 0.920333 | 0.926288 |  | 0.00 |
| `string_human_physical_v12` | `random` | 48 | `val` | `preferential_attachment` | 0.880485 | 0.884513 |  | 0.00 |
| `string_human_physical_v12` | `random` | 48 | `test` | `common_neighbors` | 0.918615 | 0.919190 |  | 0.00 |
| `string_human_physical_v12` | `random` | 48 | `test` | `jaccard` | 0.909479 | 0.911998 |  | 0.00 |
| `string_human_physical_v12` | `random` | 48 | `test` | `adamic_adar` | 0.921940 | 0.927863 |  | 0.00 |
| `string_human_physical_v12` | `random` | 48 | `test` | `preferential_attachment` | 0.881377 | 0.884715 |  | 0.00 |
| `string_human_physical_v12` | `random` | 48 | `val` | `logistic_regression` | 0.935047 | 0.945264 | 0.025697 | 1.43 |
| `string_human_physical_v12` | `random` | 48 | `test` | `logistic_regression` | 0.936904 | 0.946847 | 0.025963 | 1.43 |
| `string_human_physical_v12` | `random` | 48 | `val` | `hist_gradient_boosting` | 0.940567 | 0.950240 | 0.004490 | 4.67 |
| `string_human_physical_v12` | `random` | 48 | `test` | `hist_gradient_boosting` | 0.942118 | 0.951416 | 0.005190 | 4.67 |
| `string_human_physical_v12` | `random` | 49 | `val` | `common_neighbors` | 0.917188 | 0.917737 |  | 0.00 |
| `string_human_physical_v12` | `random` | 49 | `val` | `jaccard` | 0.908113 | 0.910417 |  | 0.00 |
| `string_human_physical_v12` | `random` | 49 | `val` | `adamic_adar` | 0.920394 | 0.926322 |  | 0.00 |
| `string_human_physical_v12` | `random` | 49 | `val` | `preferential_attachment` | 0.881380 | 0.884993 |  | 0.00 |
| `string_human_physical_v12` | `random` | 49 | `test` | `common_neighbors` | 0.916802 | 0.917216 |  | 0.00 |
| `string_human_physical_v12` | `random` | 49 | `test` | `jaccard` | 0.907825 | 0.910977 |  | 0.00 |
| `string_human_physical_v12` | `random` | 49 | `test` | `adamic_adar` | 0.920059 | 0.925898 |  | 0.00 |
| `string_human_physical_v12` | `random` | 49 | `test` | `preferential_attachment` | 0.879723 | 0.882867 |  | 0.00 |
| `string_human_physical_v12` | `random` | 49 | `val` | `logistic_regression` | 0.934951 | 0.945260 | 0.026001 | 1.53 |
| `string_human_physical_v12` | `random` | 49 | `test` | `logistic_regression` | 0.934998 | 0.945433 | 0.025018 | 1.53 |
| `string_human_physical_v12` | `random` | 49 | `val` | `hist_gradient_boosting` | 0.940231 | 0.949995 | 0.002907 | 4.55 |
| `string_human_physical_v12` | `random` | 49 | `test` | `hist_gradient_boosting` | 0.940191 | 0.949877 | 0.004752 | 4.55 |
| `string_human_physical_v12` | `random` | 50 | `val` | `common_neighbors` | 0.917425 | 0.918199 |  | 0.00 |
| `string_human_physical_v12` | `random` | 50 | `val` | `jaccard` | 0.908215 | 0.911131 |  | 0.00 |
| `string_human_physical_v12` | `random` | 50 | `val` | `adamic_adar` | 0.920761 | 0.927005 |  | 0.00 |
| `string_human_physical_v12` | `random` | 50 | `val` | `preferential_attachment` | 0.880908 | 0.884305 |  | 0.00 |
| `string_human_physical_v12` | `random` | 50 | `test` | `common_neighbors` | 0.916855 | 0.917435 |  | 0.00 |
| `string_human_physical_v12` | `random` | 50 | `test` | `jaccard` | 0.907823 | 0.910833 |  | 0.00 |
| `string_human_physical_v12` | `random` | 50 | `test` | `adamic_adar` | 0.920083 | 0.926098 |  | 0.00 |
| `string_human_physical_v12` | `random` | 50 | `test` | `preferential_attachment` | 0.879865 | 0.883500 |  | 0.00 |
| `string_human_physical_v12` | `random` | 50 | `val` | `logistic_regression` | 0.935913 | 0.946076 | 0.025745 | 1.44 |
| `string_human_physical_v12` | `random` | 50 | `test` | `logistic_regression` | 0.934330 | 0.944727 | 0.025273 | 1.44 |
| `string_human_physical_v12` | `random` | 50 | `val` | `hist_gradient_boosting` | 0.941085 | 0.950770 | 0.004099 | 4.36 |
| `string_human_physical_v12` | `random` | 50 | `test` | `hist_gradient_boosting` | 0.939878 | 0.949629 | 0.003271 | 4.36 |
| `string_human_physical_v12` | `random` | 51 | `val` | `common_neighbors` | 0.917896 | 0.918066 |  | 0.00 |
| `string_human_physical_v12` | `random` | 51 | `val` | `jaccard` | 0.908709 | 0.911067 |  | 0.00 |
| `string_human_physical_v12` | `random` | 51 | `val` | `adamic_adar` | 0.921203 | 0.926856 |  | 0.00 |
| `string_human_physical_v12` | `random` | 51 | `val` | `preferential_attachment` | 0.880599 | 0.883767 |  | 0.00 |
| `string_human_physical_v12` | `random` | 51 | `test` | `common_neighbors` | 0.916664 | 0.917565 |  | 0.00 |
| `string_human_physical_v12` | `random` | 51 | `test` | `jaccard` | 0.907265 | 0.910305 |  | 0.00 |
| `string_human_physical_v12` | `random` | 51 | `test` | `adamic_adar` | 0.919912 | 0.926230 |  | 0.00 |
| `string_human_physical_v12` | `random` | 51 | `test` | `preferential_attachment` | 0.881352 | 0.884782 |  | 0.00 |
| `string_human_physical_v12` | `random` | 51 | `val` | `logistic_regression` | 0.935622 | 0.945577 | 0.026744 | 1.60 |
| `string_human_physical_v12` | `random` | 51 | `test` | `logistic_regression` | 0.934802 | 0.945438 | 0.025862 | 1.60 |
| `string_human_physical_v12` | `random` | 51 | `val` | `hist_gradient_boosting` | 0.940663 | 0.950120 | 0.004084 | 4.43 |
| `string_human_physical_v12` | `random` | 51 | `test` | `hist_gradient_boosting` | 0.940271 | 0.950116 | 0.003851 | 4.43 |
| `string_human_physical_v12` | `degree_matched` | 42 | `val` | `common_neighbors` | 0.752076 | 0.753729 |  | 0.00 |
| `string_human_physical_v12` | `degree_matched` | 42 | `val` | `jaccard` | 0.795615 | 0.820507 |  | 0.00 |
| `string_human_physical_v12` | `degree_matched` | 42 | `val` | `adamic_adar` | 0.764413 | 0.771673 |  | 0.00 |
| `string_human_physical_v12` | `degree_matched` | 42 | `val` | `preferential_attachment` | 0.543568 | 0.554663 |  | 0.00 |
| `string_human_physical_v12` | `degree_matched` | 42 | `test` | `common_neighbors` | 0.753248 | 0.753435 |  | 0.00 |
| `string_human_physical_v12` | `degree_matched` | 42 | `test` | `jaccard` | 0.796545 | 0.820086 |  | 0.00 |
| `string_human_physical_v12` | `degree_matched` | 42 | `test` | `adamic_adar` | 0.765802 | 0.771478 |  | 0.00 |
| `string_human_physical_v12` | `degree_matched` | 42 | `test` | `preferential_attachment` | 0.545475 | 0.557940 |  | 0.00 |
| `string_human_physical_v12` | `degree_matched` | 42 | `val` | `logistic_regression` | 0.842969 | 0.864047 | 0.050602 | 1.25 |
| `string_human_physical_v12` | `degree_matched` | 42 | `test` | `logistic_regression` | 0.844412 | 0.864333 | 0.050056 | 1.25 |
| `string_human_physical_v12` | `degree_matched` | 42 | `val` | `hist_gradient_boosting` | 0.860465 | 0.880896 | 0.010522 | 4.53 |
| `string_human_physical_v12` | `degree_matched` | 42 | `test` | `hist_gradient_boosting` | 0.861651 | 0.881462 | 0.011083 | 4.53 |
| `string_human_physical_v12` | `degree_matched` | 43 | `val` | `common_neighbors` | 0.753072 | 0.752769 |  | 0.00 |
| `string_human_physical_v12` | `degree_matched` | 43 | `val` | `jaccard` | 0.796689 | 0.820090 |  | 0.00 |
| `string_human_physical_v12` | `degree_matched` | 43 | `val` | `adamic_adar` | 0.765658 | 0.771064 |  | 0.00 |
| `string_human_physical_v12` | `degree_matched` | 43 | `val` | `preferential_attachment` | 0.544122 | 0.555580 |  | 0.00 |
| `string_human_physical_v12` | `degree_matched` | 43 | `test` | `common_neighbors` | 0.752634 | 0.753395 |  | 0.00 |
| `string_human_physical_v12` | `degree_matched` | 43 | `test` | `jaccard` | 0.796106 | 0.820331 |  | 0.00 |
| `string_human_physical_v12` | `degree_matched` | 43 | `test` | `adamic_adar` | 0.765065 | 0.771505 |  | 0.00 |
| `string_human_physical_v12` | `degree_matched` | 43 | `test` | `preferential_attachment` | 0.544247 | 0.555923 |  | 0.00 |
| `string_human_physical_v12` | `degree_matched` | 43 | `val` | `logistic_regression` | 0.844568 | 0.864294 | 0.051650 | 1.09 |
| `string_human_physical_v12` | `degree_matched` | 43 | `test` | `logistic_regression` | 0.844374 | 0.865127 | 0.051123 | 1.09 |
| `string_human_physical_v12` | `degree_matched` | 43 | `val` | `hist_gradient_boosting` | 0.861898 | 0.881279 | 0.011943 | 4.55 |
| `string_human_physical_v12` | `degree_matched` | 43 | `test` | `hist_gradient_boosting` | 0.861023 | 0.881234 | 0.011545 | 4.55 |
| `string_human_physical_v12` | `degree_matched` | 44 | `val` | `common_neighbors` | 0.751776 | 0.752204 |  | 0.00 |
| `string_human_physical_v12` | `degree_matched` | 44 | `val` | `jaccard` | 0.795131 | 0.819225 |  | 0.00 |
| `string_human_physical_v12` | `degree_matched` | 44 | `val` | `adamic_adar` | 0.764203 | 0.770093 |  | 0.00 |
| `string_human_physical_v12` | `degree_matched` | 44 | `val` | `preferential_attachment` | 0.544318 | 0.555832 |  | 0.00 |
| `string_human_physical_v12` | `degree_matched` | 44 | `test` | `common_neighbors` | 0.753332 | 0.752784 |  | 0.00 |
| `string_human_physical_v12` | `degree_matched` | 44 | `test` | `jaccard` | 0.796323 | 0.820017 |  | 0.00 |
| `string_human_physical_v12` | `degree_matched` | 44 | `test` | `adamic_adar` | 0.765670 | 0.770672 |  | 0.00 |
| `string_human_physical_v12` | `degree_matched` | 44 | `test` | `preferential_attachment` | 0.545484 | 0.556714 |  | 0.00 |
| `string_human_physical_v12` | `degree_matched` | 44 | `val` | `logistic_regression` | 0.843077 | 0.862953 | 0.050262 | 1.15 |
| `string_human_physical_v12` | `degree_matched` | 44 | `test` | `logistic_regression` | 0.843579 | 0.863524 | 0.050655 | 1.15 |
| `string_human_physical_v12` | `degree_matched` | 44 | `val` | `hist_gradient_boosting` | 0.860084 | 0.880172 | 0.010353 | 4.80 |
| `string_human_physical_v12` | `degree_matched` | 44 | `test` | `hist_gradient_boosting` | 0.860597 | 0.880732 | 0.011175 | 4.80 |
| `string_human_physical_v12` | `degree_matched` | 45 | `val` | `common_neighbors` | 0.751400 | 0.752357 |  | 0.00 |
| `string_human_physical_v12` | `degree_matched` | 45 | `val` | `jaccard` | 0.795414 | 0.819642 |  | 0.00 |
| `string_human_physical_v12` | `degree_matched` | 45 | `val` | `adamic_adar` | 0.763915 | 0.770449 |  | 0.00 |
| `string_human_physical_v12` | `degree_matched` | 45 | `val` | `preferential_attachment` | 0.542816 | 0.554835 |  | 0.00 |
| `string_human_physical_v12` | `degree_matched` | 45 | `test` | `common_neighbors` | 0.752552 | 0.752987 |  | 0.00 |
| `string_human_physical_v12` | `degree_matched` | 45 | `test` | `jaccard` | 0.796595 | 0.820223 |  | 0.00 |
| `string_human_physical_v12` | `degree_matched` | 45 | `test` | `adamic_adar` | 0.765043 | 0.770926 |  | 0.00 |
| `string_human_physical_v12` | `degree_matched` | 45 | `test` | `preferential_attachment` | 0.544593 | 0.556816 |  | 0.00 |
| `string_human_physical_v12` | `degree_matched` | 45 | `val` | `logistic_regression` | 0.842737 | 0.863411 | 0.049124 | 1.26 |
| `string_human_physical_v12` | `degree_matched` | 45 | `test` | `logistic_regression` | 0.843637 | 0.863814 | 0.050628 | 1.26 |
| `string_human_physical_v12` | `degree_matched` | 45 | `val` | `hist_gradient_boosting` | 0.860476 | 0.880901 | 0.010148 | 4.70 |
| `string_human_physical_v12` | `degree_matched` | 45 | `test` | `hist_gradient_boosting` | 0.860923 | 0.881158 | 0.010826 | 4.70 |
| `string_human_physical_v12` | `degree_matched` | 46 | `val` | `common_neighbors` | 0.752925 | 0.753203 |  | 0.00 |
| `string_human_physical_v12` | `degree_matched` | 46 | `val` | `jaccard` | 0.797082 | 0.820928 |  | 0.00 |
| `string_human_physical_v12` | `degree_matched` | 46 | `val` | `adamic_adar` | 0.765479 | 0.771320 |  | 0.00 |
| `string_human_physical_v12` | `degree_matched` | 46 | `val` | `preferential_attachment` | 0.543580 | 0.555018 |  | 0.00 |
| `string_human_physical_v12` | `degree_matched` | 46 | `test` | `common_neighbors` | 0.753603 | 0.754752 |  | 0.00 |
| `string_human_physical_v12` | `degree_matched` | 46 | `test` | `jaccard` | 0.796811 | 0.820839 |  | 0.00 |
| `string_human_physical_v12` | `degree_matched` | 46 | `test` | `adamic_adar` | 0.766055 | 0.772805 |  | 0.00 |
| `string_human_physical_v12` | `degree_matched` | 46 | `test` | `preferential_attachment` | 0.545565 | 0.558254 |  | 0.00 |
| `string_human_physical_v12` | `degree_matched` | 46 | `val` | `logistic_regression` | 0.845718 | 0.865256 | 0.051229 | 1.18 |
| `string_human_physical_v12` | `degree_matched` | 46 | `test` | `logistic_regression` | 0.843601 | 0.864359 | 0.049352 | 1.18 |
| `string_human_physical_v12` | `degree_matched` | 46 | `val` | `hist_gradient_boosting` | 0.862785 | 0.882272 | 0.011696 | 4.94 |
| `string_human_physical_v12` | `degree_matched` | 46 | `test` | `hist_gradient_boosting` | 0.860694 | 0.880845 | 0.009939 | 4.94 |
| `string_human_physical_v12` | `degree_matched` | 47 | `val` | `common_neighbors` | 0.751163 | 0.751265 |  | 0.00 |
| `string_human_physical_v12` | `degree_matched` | 47 | `val` | `jaccard` | 0.794904 | 0.818526 |  | 0.00 |
| `string_human_physical_v12` | `degree_matched` | 47 | `val` | `adamic_adar` | 0.763716 | 0.769329 |  | 0.00 |
| `string_human_physical_v12` | `degree_matched` | 47 | `val` | `preferential_attachment` | 0.543809 | 0.554730 |  | 0.00 |
| `string_human_physical_v12` | `degree_matched` | 47 | `test` | `common_neighbors` | 0.752132 | 0.752925 |  | 0.00 |
| `string_human_physical_v12` | `degree_matched` | 47 | `test` | `jaccard` | 0.795542 | 0.819377 |  | 0.00 |
| `string_human_physical_v12` | `degree_matched` | 47 | `test` | `adamic_adar` | 0.764566 | 0.770966 |  | 0.00 |
| `string_human_physical_v12` | `degree_matched` | 47 | `test` | `preferential_attachment` | 0.545347 | 0.557662 |  | 0.00 |
| `string_human_physical_v12` | `degree_matched` | 47 | `val` | `logistic_regression` | 0.843288 | 0.863103 | 0.049889 | 1.11 |
| `string_human_physical_v12` | `degree_matched` | 47 | `test` | `logistic_regression` | 0.843804 | 0.864126 | 0.050545 | 1.11 |
| `string_human_physical_v12` | `degree_matched` | 47 | `val` | `hist_gradient_boosting` | 0.860190 | 0.880214 | 0.010327 | 4.53 |
| `string_human_physical_v12` | `degree_matched` | 47 | `test` | `hist_gradient_boosting` | 0.860636 | 0.880818 | 0.011680 | 4.53 |
| `string_human_physical_v12` | `degree_matched` | 48 | `val` | `common_neighbors` | 0.750983 | 0.751224 |  | 0.00 |
| `string_human_physical_v12` | `degree_matched` | 48 | `val` | `jaccard` | 0.794315 | 0.818968 |  | 0.00 |
| `string_human_physical_v12` | `degree_matched` | 48 | `val` | `adamic_adar` | 0.763435 | 0.769218 |  | 0.00 |
| `string_human_physical_v12` | `degree_matched` | 48 | `val` | `preferential_attachment` | 0.543547 | 0.555620 |  | 0.00 |
| `string_human_physical_v12` | `degree_matched` | 48 | `test` | `common_neighbors` | 0.754513 | 0.755197 |  | 0.00 |
| `string_human_physical_v12` | `degree_matched` | 48 | `test` | `jaccard` | 0.797934 | 0.821865 |  | 0.00 |
| `string_human_physical_v12` | `degree_matched` | 48 | `test` | `adamic_adar` | 0.767136 | 0.773419 |  | 0.00 |
| `string_human_physical_v12` | `degree_matched` | 48 | `test` | `preferential_attachment` | 0.544968 | 0.557460 |  | 0.00 |
| `string_human_physical_v12` | `degree_matched` | 48 | `val` | `logistic_regression` | 0.842551 | 0.863158 | 0.051195 | 1.02 |
| `string_human_physical_v12` | `degree_matched` | 48 | `test` | `logistic_regression` | 0.844919 | 0.865506 | 0.051467 | 1.02 |
| `string_human_physical_v12` | `degree_matched` | 48 | `val` | `hist_gradient_boosting` | 0.860346 | 0.880653 | 0.011118 | 4.64 |
| `string_human_physical_v12` | `degree_matched` | 48 | `test` | `hist_gradient_boosting` | 0.861992 | 0.881939 | 0.011181 | 4.64 |
| `string_human_physical_v12` | `degree_matched` | 49 | `val` | `common_neighbors` | 0.751975 | 0.753524 |  | 0.00 |
| `string_human_physical_v12` | `degree_matched` | 49 | `val` | `jaccard` | 0.795448 | 0.820073 |  | 0.00 |
| `string_human_physical_v12` | `degree_matched` | 49 | `val` | `adamic_adar` | 0.764308 | 0.771529 |  | 0.00 |
| `string_human_physical_v12` | `degree_matched` | 49 | `val` | `preferential_attachment` | 0.543431 | 0.555803 |  | 0.00 |
| `string_human_physical_v12` | `degree_matched` | 49 | `test` | `common_neighbors` | 0.754274 | 0.754353 |  | 0.00 |
| `string_human_physical_v12` | `degree_matched` | 49 | `test` | `jaccard` | 0.797385 | 0.821245 |  | 0.00 |
| `string_human_physical_v12` | `degree_matched` | 49 | `test` | `adamic_adar` | 0.766803 | 0.772493 |  | 0.00 |
| `string_human_physical_v12` | `degree_matched` | 49 | `test` | `preferential_attachment` | 0.545473 | 0.556910 |  | 0.00 |
| `string_human_physical_v12` | `degree_matched` | 49 | `val` | `logistic_regression` | 0.843287 | 0.863934 | 0.051070 | 1.19 |
| `string_human_physical_v12` | `degree_matched` | 49 | `test` | `logistic_regression` | 0.845210 | 0.865478 | 0.052179 | 1.19 |
| `string_human_physical_v12` | `degree_matched` | 49 | `val` | `hist_gradient_boosting` | 0.860637 | 0.880608 | 0.010333 | 4.85 |
| `string_human_physical_v12` | `degree_matched` | 49 | `test` | `hist_gradient_boosting` | 0.862151 | 0.882283 | 0.012567 | 4.85 |
| `string_human_physical_v12` | `degree_matched` | 50 | `val` | `common_neighbors` | 0.753092 | 0.753245 |  | 0.00 |
| `string_human_physical_v12` | `degree_matched` | 50 | `val` | `jaccard` | 0.796841 | 0.820516 |  | 0.00 |
| `string_human_physical_v12` | `degree_matched` | 50 | `val` | `adamic_adar` | 0.765677 | 0.771401 |  | 0.00 |
| `string_human_physical_v12` | `degree_matched` | 50 | `val` | `preferential_attachment` | 0.543384 | 0.554731 |  | 0.00 |
| `string_human_physical_v12` | `degree_matched` | 50 | `test` | `common_neighbors` | 0.752404 | 0.753556 |  | 0.00 |
| `string_human_physical_v12` | `degree_matched` | 50 | `test` | `jaccard` | 0.795436 | 0.819796 |  | 0.00 |
| `string_human_physical_v12` | `degree_matched` | 50 | `test` | `adamic_adar` | 0.764763 | 0.771535 |  | 0.00 |
| `string_human_physical_v12` | `degree_matched` | 50 | `test` | `preferential_attachment` | 0.545238 | 0.557695 |  | 0.00 |
| `string_human_physical_v12` | `degree_matched` | 50 | `val` | `logistic_regression` | 0.845284 | 0.865353 | 0.052451 | 1.14 |
| `string_human_physical_v12` | `degree_matched` | 50 | `test` | `logistic_regression` | 0.842420 | 0.863661 | 0.049577 | 1.14 |
| `string_human_physical_v12` | `degree_matched` | 50 | `val` | `hist_gradient_boosting` | 0.861696 | 0.881641 | 0.010811 | 4.55 |
| `string_human_physical_v12` | `degree_matched` | 50 | `test` | `hist_gradient_boosting` | 0.860206 | 0.880561 | 0.010085 | 4.55 |
| `string_human_physical_v12` | `degree_matched` | 51 | `val` | `common_neighbors` | 0.752170 | 0.752272 |  | 0.00 |
| `string_human_physical_v12` | `degree_matched` | 51 | `val` | `jaccard` | 0.796148 | 0.820015 |  | 0.00 |
| `string_human_physical_v12` | `degree_matched` | 51 | `val` | `adamic_adar` | 0.764872 | 0.770447 |  | 0.00 |
| `string_human_physical_v12` | `degree_matched` | 51 | `val` | `preferential_attachment` | 0.543334 | 0.554805 |  | 0.00 |
| `string_human_physical_v12` | `degree_matched` | 51 | `test` | `common_neighbors` | 0.754067 | 0.755336 |  | 0.00 |
| `string_human_physical_v12` | `degree_matched` | 51 | `test` | `jaccard` | 0.796654 | 0.820856 |  | 0.00 |
| `string_human_physical_v12` | `degree_matched` | 51 | `test` | `adamic_adar` | 0.766379 | 0.773242 |  | 0.00 |
| `string_human_physical_v12` | `degree_matched` | 51 | `test` | `preferential_attachment` | 0.546029 | 0.558806 |  | 0.00 |
| `string_human_physical_v12` | `degree_matched` | 51 | `val` | `logistic_regression` | 0.844535 | 0.864783 | 0.051246 | 1.18 |
| `string_human_physical_v12` | `degree_matched` | 51 | `test` | `logistic_regression` | 0.844291 | 0.864538 | 0.050571 | 1.18 |
| `string_human_physical_v12` | `degree_matched` | 51 | `val` | `hist_gradient_boosting` | 0.861816 | 0.882050 | 0.011886 | 4.65 |
| `string_human_physical_v12` | `degree_matched` | 51 | `test` | `hist_gradient_boosting` | 0.862535 | 0.882211 | 0.012771 | 4.65 |
| `biogrid_human_physical` | `random` | 42 | `val` | `common_neighbors` | 0.908493 | 0.906991 |  | 0.00 |
| `biogrid_human_physical` | `random` | 42 | `val` | `jaccard` | 0.873998 | 0.861231 |  | 0.00 |
| `biogrid_human_physical` | `random` | 42 | `val` | `adamic_adar` | 0.912946 | 0.917186 |  | 0.00 |
| `biogrid_human_physical` | `random` | 42 | `val` | `preferential_attachment` | 0.921217 | 0.918442 |  | 0.00 |
| `biogrid_human_physical` | `random` | 42 | `test` | `common_neighbors` | 0.909451 | 0.907927 |  | 0.00 |
| `biogrid_human_physical` | `random` | 42 | `test` | `jaccard` | 0.875579 | 0.863944 |  | 0.00 |
| `biogrid_human_physical` | `random` | 42 | `test` | `adamic_adar` | 0.913971 | 0.918185 |  | 0.00 |
| `biogrid_human_physical` | `random` | 42 | `test` | `preferential_attachment` | 0.921092 | 0.918508 |  | 0.00 |
| `biogrid_human_physical` | `random` | 42 | `val` | `logistic_regression` | 0.934236 | 0.934453 | 0.046825 | 1.71 |
| `biogrid_human_physical` | `random` | 42 | `test` | `logistic_regression` | 0.934547 | 0.934704 | 0.047595 | 1.71 |
| `biogrid_human_physical` | `random` | 42 | `val` | `hist_gradient_boosting` | 0.941841 | 0.942784 | 0.003239 | 6.19 |
| `biogrid_human_physical` | `random` | 42 | `test` | `hist_gradient_boosting` | 0.942187 | 0.943193 | 0.003695 | 6.19 |
| `biogrid_human_physical` | `random` | 43 | `val` | `common_neighbors` | 0.908348 | 0.906746 |  | 0.00 |
| `biogrid_human_physical` | `random` | 43 | `val` | `jaccard` | 0.874265 | 0.862210 |  | 0.00 |
| `biogrid_human_physical` | `random` | 43 | `val` | `adamic_adar` | 0.912888 | 0.917052 |  | 0.00 |
| `biogrid_human_physical` | `random` | 43 | `val` | `preferential_attachment` | 0.920161 | 0.917435 |  | 0.00 |
| `biogrid_human_physical` | `random` | 43 | `test` | `common_neighbors` | 0.909539 | 0.907476 |  | 0.00 |
| `biogrid_human_physical` | `random` | 43 | `test` | `jaccard` | 0.875400 | 0.862340 |  | 0.00 |
| `biogrid_human_physical` | `random` | 43 | `test` | `adamic_adar` | 0.914008 | 0.917631 |  | 0.00 |
| `biogrid_human_physical` | `random` | 43 | `test` | `preferential_attachment` | 0.920340 | 0.917285 |  | 0.00 |
| `biogrid_human_physical` | `random` | 43 | `val` | `logistic_regression` | 0.934227 | 0.934383 | 0.047709 | 1.76 |
| `biogrid_human_physical` | `random` | 43 | `test` | `logistic_regression` | 0.934643 | 0.934702 | 0.046736 | 1.76 |
| `biogrid_human_physical` | `random` | 43 | `val` | `hist_gradient_boosting` | 0.941452 | 0.942384 | 0.003891 | 5.69 |
| `biogrid_human_physical` | `random` | 43 | `test` | `hist_gradient_boosting` | 0.941898 | 0.942543 | 0.004230 | 5.69 |
| `biogrid_human_physical` | `random` | 44 | `val` | `common_neighbors` | 0.908366 | 0.906806 |  | 0.00 |
| `biogrid_human_physical` | `random` | 44 | `val` | `jaccard` | 0.873702 | 0.861379 |  | 0.00 |
| `biogrid_human_physical` | `random` | 44 | `val` | `adamic_adar` | 0.912845 | 0.917015 |  | 0.00 |
| `biogrid_human_physical` | `random` | 44 | `val` | `preferential_attachment` | 0.920038 | 0.917270 |  | 0.00 |
| `biogrid_human_physical` | `random` | 44 | `test` | `common_neighbors` | 0.909404 | 0.907411 |  | 0.00 |
| `biogrid_human_physical` | `random` | 44 | `test` | `jaccard` | 0.875701 | 0.863215 |  | 0.00 |
| `biogrid_human_physical` | `random` | 44 | `test` | `adamic_adar` | 0.913949 | 0.917748 |  | 0.00 |
| `biogrid_human_physical` | `random` | 44 | `test` | `preferential_attachment` | 0.920137 | 0.917395 |  | 0.00 |
| `biogrid_human_physical` | `random` | 44 | `val` | `logistic_regression` | 0.933771 | 0.933828 | 0.047500 | 1.99 |
| `biogrid_human_physical` | `random` | 44 | `test` | `logistic_regression` | 0.934212 | 0.934351 | 0.047592 | 1.99 |
| `biogrid_human_physical` | `random` | 44 | `val` | `hist_gradient_boosting` | 0.941256 | 0.942176 | 0.003606 | 5.79 |
| `biogrid_human_physical` | `random` | 44 | `test` | `hist_gradient_boosting` | 0.941609 | 0.942409 | 0.003653 | 5.79 |
| `biogrid_human_physical` | `random` | 45 | `val` | `common_neighbors` | 0.909350 | 0.907961 |  | 0.00 |
| `biogrid_human_physical` | `random` | 45 | `val` | `jaccard` | 0.875137 | 0.863909 |  | 0.00 |
| `biogrid_human_physical` | `random` | 45 | `val` | `adamic_adar` | 0.913809 | 0.918190 |  | 0.00 |
| `biogrid_human_physical` | `random` | 45 | `val` | `preferential_attachment` | 0.921413 | 0.918843 |  | 0.00 |
| `biogrid_human_physical` | `random` | 45 | `test` | `common_neighbors` | 0.909256 | 0.907830 |  | 0.00 |
| `biogrid_human_physical` | `random` | 45 | `test` | `jaccard` | 0.874969 | 0.862835 |  | 0.00 |
| `biogrid_human_physical` | `random` | 45 | `test` | `adamic_adar` | 0.913762 | 0.918145 |  | 0.00 |
| `biogrid_human_physical` | `random` | 45 | `test` | `preferential_attachment` | 0.920529 | 0.917878 |  | 0.00 |
| `biogrid_human_physical` | `random` | 45 | `val` | `logistic_regression` | 0.934654 | 0.934960 | 0.045853 | 1.75 |
| `biogrid_human_physical` | `random` | 45 | `test` | `logistic_regression` | 0.934036 | 0.934609 | 0.046461 | 1.75 |
| `biogrid_human_physical` | `random` | 45 | `val` | `hist_gradient_boosting` | 0.942084 | 0.943211 | 0.004333 | 5.83 |
| `biogrid_human_physical` | `random` | 45 | `test` | `hist_gradient_boosting` | 0.941544 | 0.942731 | 0.003414 | 5.83 |
| `biogrid_human_physical` | `random` | 46 | `val` | `common_neighbors` | 0.908045 | 0.906620 |  | 0.00 |
| `biogrid_human_physical` | `random` | 46 | `val` | `jaccard` | 0.874244 | 0.862355 |  | 0.00 |
| `biogrid_human_physical` | `random` | 46 | `val` | `adamic_adar` | 0.912555 | 0.916933 |  | 0.00 |
| `biogrid_human_physical` | `random` | 46 | `val` | `preferential_attachment` | 0.920224 | 0.917741 |  | 0.00 |
| `biogrid_human_physical` | `random` | 46 | `test` | `common_neighbors` | 0.907766 | 0.906651 |  | 0.00 |
| `biogrid_human_physical` | `random` | 46 | `test` | `jaccard` | 0.873707 | 0.861299 |  | 0.00 |
| `biogrid_human_physical` | `random` | 46 | `test` | `adamic_adar` | 0.912312 | 0.916954 |  | 0.00 |
| `biogrid_human_physical` | `random` | 46 | `test` | `preferential_attachment` | 0.919986 | 0.917353 |  | 0.00 |
| `biogrid_human_physical` | `random` | 46 | `val` | `logistic_regression` | 0.933541 | 0.933983 | 0.046872 | 1.60 |
| `biogrid_human_physical` | `random` | 46 | `test` | `logistic_regression` | 0.933570 | 0.934020 | 0.046118 | 1.60 |
| `biogrid_human_physical` | `random` | 46 | `val` | `hist_gradient_boosting` | 0.941092 | 0.942276 | 0.003408 | 5.67 |
| `biogrid_human_physical` | `random` | 46 | `test` | `hist_gradient_boosting` | 0.941390 | 0.942608 | 0.003598 | 5.67 |
| `biogrid_human_physical` | `random` | 47 | `val` | `common_neighbors` | 0.909050 | 0.907537 |  | 0.00 |
| `biogrid_human_physical` | `random` | 47 | `val` | `jaccard` | 0.875204 | 0.863037 |  | 0.00 |
| `biogrid_human_physical` | `random` | 47 | `val` | `adamic_adar` | 0.913422 | 0.917692 |  | 0.00 |
| `biogrid_human_physical` | `random` | 47 | `val` | `preferential_attachment` | 0.920885 | 0.918343 |  | 0.00 |
| `biogrid_human_physical` | `random` | 47 | `test` | `common_neighbors` | 0.910151 | 0.908714 |  | 0.00 |
| `biogrid_human_physical` | `random` | 47 | `test` | `jaccard` | 0.875577 | 0.863303 |  | 0.00 |
| `biogrid_human_physical` | `random` | 47 | `test` | `adamic_adar` | 0.914609 | 0.918912 |  | 0.00 |
| `biogrid_human_physical` | `random` | 47 | `test` | `preferential_attachment` | 0.922056 | 0.919605 |  | 0.00 |
| `biogrid_human_physical` | `random` | 47 | `val` | `logistic_regression` | 0.934334 | 0.934621 | 0.048234 | 1.94 |
| `biogrid_human_physical` | `random` | 47 | `test` | `logistic_regression` | 0.935710 | 0.936296 | 0.047595 | 1.94 |
| `biogrid_human_physical` | `random` | 47 | `val` | `hist_gradient_boosting` | 0.941729 | 0.942964 | 0.003223 | 6.01 |
| `biogrid_human_physical` | `random` | 47 | `test` | `hist_gradient_boosting` | 0.942931 | 0.944049 | 0.004720 | 6.01 |
| `biogrid_human_physical` | `random` | 48 | `val` | `common_neighbors` | 0.909660 | 0.908125 |  | 0.00 |
| `biogrid_human_physical` | `random` | 48 | `val` | `jaccard` | 0.875481 | 0.863433 |  | 0.00 |
| `biogrid_human_physical` | `random` | 48 | `val` | `adamic_adar` | 0.914042 | 0.918269 |  | 0.00 |
| `biogrid_human_physical` | `random` | 48 | `val` | `preferential_attachment` | 0.922054 | 0.919614 |  | 0.00 |
| `biogrid_human_physical` | `random` | 48 | `test` | `common_neighbors` | 0.909437 | 0.907650 |  | 0.00 |
| `biogrid_human_physical` | `random` | 48 | `test` | `jaccard` | 0.874817 | 0.862424 |  | 0.00 |
| `biogrid_human_physical` | `random` | 48 | `test` | `adamic_adar` | 0.913953 | 0.917952 |  | 0.00 |
| `biogrid_human_physical` | `random` | 48 | `test` | `preferential_attachment` | 0.920832 | 0.918062 |  | 0.00 |
| `biogrid_human_physical` | `random` | 48 | `val` | `logistic_regression` | 0.935197 | 0.935608 | 0.046639 | 1.67 |
| `biogrid_human_physical` | `random` | 48 | `test` | `logistic_regression` | 0.934522 | 0.934687 | 0.047535 | 1.67 |
| `biogrid_human_physical` | `random` | 48 | `val` | `hist_gradient_boosting` | 0.942495 | 0.943478 | 0.004306 | 5.91 |
| `biogrid_human_physical` | `random` | 48 | `test` | `hist_gradient_boosting` | 0.942144 | 0.943134 | 0.004658 | 5.91 |
| `biogrid_human_physical` | `random` | 49 | `val` | `common_neighbors` | 0.909174 | 0.907440 |  | 0.00 |
| `biogrid_human_physical` | `random` | 49 | `val` | `jaccard` | 0.875377 | 0.863453 |  | 0.00 |
| `biogrid_human_physical` | `random` | 49 | `val` | `adamic_adar` | 0.913654 | 0.917644 |  | 0.00 |
| `biogrid_human_physical` | `random` | 49 | `val` | `preferential_attachment` | 0.921078 | 0.918254 |  | 0.00 |
| `biogrid_human_physical` | `random` | 49 | `test` | `common_neighbors` | 0.908909 | 0.907400 |  | 0.00 |
| `biogrid_human_physical` | `random` | 49 | `test` | `jaccard` | 0.874728 | 0.862600 |  | 0.00 |
| `biogrid_human_physical` | `random` | 49 | `test` | `adamic_adar` | 0.913470 | 0.917706 |  | 0.00 |
| `biogrid_human_physical` | `random` | 49 | `test` | `preferential_attachment` | 0.920626 | 0.917881 |  | 0.00 |
| `biogrid_human_physical` | `random` | 49 | `val` | `logistic_regression` | 0.934990 | 0.935252 | 0.047015 | 1.82 |
| `biogrid_human_physical` | `random` | 49 | `test` | `logistic_regression` | 0.934427 | 0.934733 | 0.046262 | 1.82 |
| `biogrid_human_physical` | `random` | 49 | `val` | `hist_gradient_boosting` | 0.942263 | 0.943178 | 0.004157 | 5.89 |
| `biogrid_human_physical` | `random` | 49 | `test` | `hist_gradient_boosting` | 0.942059 | 0.943002 | 0.004119 | 5.89 |
| `biogrid_human_physical` | `random` | 50 | `val` | `common_neighbors` | 0.908834 | 0.907131 |  | 0.00 |
| `biogrid_human_physical` | `random` | 50 | `val` | `jaccard` | 0.875193 | 0.863158 |  | 0.00 |
| `biogrid_human_physical` | `random` | 50 | `val` | `adamic_adar` | 0.913346 | 0.917421 |  | 0.00 |
| `biogrid_human_physical` | `random` | 50 | `val` | `preferential_attachment` | 0.920283 | 0.917693 |  | 0.00 |
| `biogrid_human_physical` | `random` | 50 | `test` | `common_neighbors` | 0.907547 | 0.906111 |  | 0.00 |
| `biogrid_human_physical` | `random` | 50 | `test` | `jaccard` | 0.873505 | 0.861209 |  | 0.00 |
| `biogrid_human_physical` | `random` | 50 | `test` | `adamic_adar` | 0.912141 | 0.916482 |  | 0.00 |
| `biogrid_human_physical` | `random` | 50 | `test` | `preferential_attachment` | 0.920618 | 0.917940 |  | 0.00 |
| `biogrid_human_physical` | `random` | 50 | `val` | `logistic_regression` | 0.934020 | 0.934425 | 0.047273 | 1.62 |
| `biogrid_human_physical` | `random` | 50 | `test` | `logistic_regression` | 0.934235 | 0.934336 | 0.046890 | 1.62 |
| `biogrid_human_physical` | `random` | 50 | `val` | `hist_gradient_boosting` | 0.941421 | 0.942442 | 0.003368 | 5.86 |
| `biogrid_human_physical` | `random` | 50 | `test` | `hist_gradient_boosting` | 0.941668 | 0.942575 | 0.004283 | 5.86 |
| `biogrid_human_physical` | `random` | 51 | `val` | `common_neighbors` | 0.909317 | 0.907496 |  | 0.00 |
| `biogrid_human_physical` | `random` | 51 | `val` | `jaccard` | 0.875094 | 0.862528 |  | 0.00 |
| `biogrid_human_physical` | `random` | 51 | `val` | `adamic_adar` | 0.913812 | 0.917696 |  | 0.00 |
| `biogrid_human_physical` | `random` | 51 | `val` | `preferential_attachment` | 0.921464 | 0.918345 |  | 0.00 |
| `biogrid_human_physical` | `random` | 51 | `test` | `common_neighbors` | 0.909613 | 0.907650 |  | 0.00 |
| `biogrid_human_physical` | `random` | 51 | `test` | `jaccard` | 0.874889 | 0.861840 |  | 0.00 |
| `biogrid_human_physical` | `random` | 51 | `test` | `adamic_adar` | 0.914081 | 0.917879 |  | 0.00 |
| `biogrid_human_physical` | `random` | 51 | `test` | `preferential_attachment` | 0.920884 | 0.917765 |  | 0.00 |
| `biogrid_human_physical` | `random` | 51 | `val` | `logistic_regression` | 0.935326 | 0.935313 | 0.048071 | 1.98 |
| `biogrid_human_physical` | `random` | 51 | `test` | `logistic_regression` | 0.934421 | 0.934285 | 0.047699 | 1.98 |
| `biogrid_human_physical` | `random` | 51 | `val` | `hist_gradient_boosting` | 0.942533 | 0.943202 | 0.004423 | 5.80 |
| `biogrid_human_physical` | `random` | 51 | `test` | `hist_gradient_boosting` | 0.941786 | 0.942609 | 0.003896 | 5.80 |
| `biogrid_human_physical` | `degree_matched` | 42 | `val` | `common_neighbors` | 0.646870 | 0.645862 |  | 0.00 |
| `biogrid_human_physical` | `degree_matched` | 42 | `val` | `jaccard` | 0.664518 | 0.676260 |  | 0.00 |
| `biogrid_human_physical` | `degree_matched` | 42 | `val` | `adamic_adar` | 0.655679 | 0.654931 |  | 0.00 |
| `biogrid_human_physical` | `degree_matched` | 42 | `val` | `preferential_attachment` | 0.557849 | 0.570247 |  | 0.00 |
| `biogrid_human_physical` | `degree_matched` | 42 | `test` | `common_neighbors` | 0.650011 | 0.648749 |  | 0.00 |
| `biogrid_human_physical` | `degree_matched` | 42 | `test` | `jaccard` | 0.667113 | 0.678113 |  | 0.00 |
| `biogrid_human_physical` | `degree_matched` | 42 | `test` | `adamic_adar` | 0.658908 | 0.658007 |  | 0.00 |
| `biogrid_human_physical` | `degree_matched` | 42 | `test` | `preferential_attachment` | 0.561047 | 0.574183 |  | 0.00 |
| `biogrid_human_physical` | `degree_matched` | 42 | `val` | `logistic_regression` | 0.707595 | 0.714703 | 0.035926 | 1.45 |
| `biogrid_human_physical` | `degree_matched` | 42 | `test` | `logistic_regression` | 0.710481 | 0.716890 | 0.038721 | 1.45 |
| `biogrid_human_physical` | `degree_matched` | 42 | `val` | `hist_gradient_boosting` | 0.759186 | 0.768319 | 0.018344 | 5.92 |
| `biogrid_human_physical` | `degree_matched` | 42 | `test` | `hist_gradient_boosting` | 0.760583 | 0.769135 | 0.019404 | 5.92 |
| `biogrid_human_physical` | `degree_matched` | 43 | `val` | `common_neighbors` | 0.648718 | 0.647662 |  | 0.00 |
| `biogrid_human_physical` | `degree_matched` | 43 | `val` | `jaccard` | 0.666354 | 0.677809 |  | 0.00 |
| `biogrid_human_physical` | `degree_matched` | 43 | `val` | `adamic_adar` | 0.657579 | 0.656698 |  | 0.00 |
| `biogrid_human_physical` | `degree_matched` | 43 | `val` | `preferential_attachment` | 0.559516 | 0.572056 |  | 0.00 |
| `biogrid_human_physical` | `degree_matched` | 43 | `test` | `common_neighbors` | 0.650714 | 0.649007 |  | 0.00 |
| `biogrid_human_physical` | `degree_matched` | 43 | `test` | `jaccard` | 0.668305 | 0.678599 |  | 0.00 |
| `biogrid_human_physical` | `degree_matched` | 43 | `test` | `adamic_adar` | 0.659686 | 0.658160 |  | 0.00 |
| `biogrid_human_physical` | `degree_matched` | 43 | `test` | `preferential_attachment` | 0.560778 | 0.573584 |  | 0.00 |
| `biogrid_human_physical` | `degree_matched` | 43 | `val` | `logistic_regression` | 0.709656 | 0.716033 | 0.038091 | 1.37 |
| `biogrid_human_physical` | `degree_matched` | 43 | `test` | `logistic_regression` | 0.711166 | 0.716461 | 0.038877 | 1.37 |
| `biogrid_human_physical` | `degree_matched` | 43 | `val` | `hist_gradient_boosting` | 0.761331 | 0.770861 | 0.020371 | 6.07 |
| `biogrid_human_physical` | `degree_matched` | 43 | `test` | `hist_gradient_boosting` | 0.762718 | 0.771416 | 0.020889 | 6.07 |
| `biogrid_human_physical` | `degree_matched` | 44 | `val` | `common_neighbors` | 0.648912 | 0.646800 |  | 0.00 |
| `biogrid_human_physical` | `degree_matched` | 44 | `val` | `jaccard` | 0.667048 | 0.677878 |  | 0.00 |
| `biogrid_human_physical` | `degree_matched` | 44 | `val` | `adamic_adar` | 0.657804 | 0.655899 |  | 0.00 |
| `biogrid_human_physical` | `degree_matched` | 44 | `val` | `preferential_attachment` | 0.558838 | 0.570594 |  | 0.00 |
| `biogrid_human_physical` | `degree_matched` | 44 | `test` | `common_neighbors` | 0.650312 | 0.648679 |  | 0.00 |
| `biogrid_human_physical` | `degree_matched` | 44 | `test` | `jaccard` | 0.667911 | 0.677806 |  | 0.00 |
| `biogrid_human_physical` | `degree_matched` | 44 | `test` | `adamic_adar` | 0.659278 | 0.657862 |  | 0.00 |
| `biogrid_human_physical` | `degree_matched` | 44 | `test` | `preferential_attachment` | 0.560845 | 0.573563 |  | 0.00 |
| `biogrid_human_physical` | `degree_matched` | 44 | `val` | `logistic_regression` | 0.710983 | 0.716739 | 0.039618 | 1.19 |
| `biogrid_human_physical` | `degree_matched` | 44 | `test` | `logistic_regression` | 0.711284 | 0.715863 | 0.040478 | 1.19 |
| `biogrid_human_physical` | `degree_matched` | 44 | `val` | `hist_gradient_boosting` | 0.761534 | 0.770447 | 0.021154 | 6.12 |
| `biogrid_human_physical` | `degree_matched` | 44 | `test` | `hist_gradient_boosting` | 0.762423 | 0.769866 | 0.021399 | 6.12 |
| `biogrid_human_physical` | `degree_matched` | 45 | `val` | `common_neighbors` | 0.648857 | 0.646947 |  | 0.00 |
| `biogrid_human_physical` | `degree_matched` | 45 | `val` | `jaccard` | 0.665899 | 0.677072 |  | 0.00 |
| `biogrid_human_physical` | `degree_matched` | 45 | `val` | `adamic_adar` | 0.657764 | 0.655969 |  | 0.00 |
| `biogrid_human_physical` | `degree_matched` | 45 | `val` | `preferential_attachment` | 0.559819 | 0.572023 |  | 0.00 |
| `biogrid_human_physical` | `degree_matched` | 45 | `test` | `common_neighbors` | 0.650553 | 0.648598 |  | 0.00 |
| `biogrid_human_physical` | `degree_matched` | 45 | `test` | `jaccard` | 0.667963 | 0.678992 |  | 0.00 |
| `biogrid_human_physical` | `degree_matched` | 45 | `test` | `adamic_adar` | 0.659510 | 0.657912 |  | 0.00 |
| `biogrid_human_physical` | `degree_matched` | 45 | `test` | `preferential_attachment` | 0.560219 | 0.572729 |  | 0.00 |
| `biogrid_human_physical` | `degree_matched` | 45 | `val` | `logistic_regression` | 0.708832 | 0.715376 | 0.036492 | 1.35 |
| `biogrid_human_physical` | `degree_matched` | 45 | `test` | `logistic_regression` | 0.710453 | 0.717187 | 0.037479 | 1.35 |
| `biogrid_human_physical` | `degree_matched` | 45 | `val` | `hist_gradient_boosting` | 0.761135 | 0.770464 | 0.020643 | 5.80 |
| `biogrid_human_physical` | `degree_matched` | 45 | `test` | `hist_gradient_boosting` | 0.762139 | 0.772324 | 0.022351 | 5.80 |
| `biogrid_human_physical` | `degree_matched` | 46 | `val` | `common_neighbors` | 0.647815 | 0.646764 |  | 0.00 |
| `biogrid_human_physical` | `degree_matched` | 46 | `val` | `jaccard` | 0.665715 | 0.677830 |  | 0.00 |
| `biogrid_human_physical` | `degree_matched` | 46 | `val` | `adamic_adar` | 0.656745 | 0.655873 |  | 0.00 |
| `biogrid_human_physical` | `degree_matched` | 46 | `val` | `preferential_attachment` | 0.558618 | 0.570564 |  | 0.00 |
| `biogrid_human_physical` | `degree_matched` | 46 | `test` | `common_neighbors` | 0.649905 | 0.648603 |  | 0.00 |
| `biogrid_human_physical` | `degree_matched` | 46 | `test` | `jaccard` | 0.666794 | 0.678171 |  | 0.00 |
| `biogrid_human_physical` | `degree_matched` | 46 | `test` | `adamic_adar` | 0.658845 | 0.657922 |  | 0.00 |
| `biogrid_human_physical` | `degree_matched` | 46 | `test` | `preferential_attachment` | 0.560714 | 0.573442 |  | 0.00 |
| `biogrid_human_physical` | `degree_matched` | 46 | `val` | `logistic_regression` | 0.710180 | 0.716680 | 0.037298 | 1.31 |
| `biogrid_human_physical` | `degree_matched` | 46 | `test` | `logistic_regression` | 0.709596 | 0.716619 | 0.037464 | 1.31 |
| `biogrid_human_physical` | `degree_matched` | 46 | `val` | `hist_gradient_boosting` | 0.760540 | 0.770188 | 0.019749 | 5.92 |
| `biogrid_human_physical` | `degree_matched` | 46 | `test` | `hist_gradient_boosting` | 0.762009 | 0.771104 | 0.020622 | 5.92 |
| `biogrid_human_physical` | `degree_matched` | 47 | `val` | `common_neighbors` | 0.648119 | 0.645913 |  | 0.00 |
| `biogrid_human_physical` | `degree_matched` | 47 | `val` | `jaccard` | 0.666173 | 0.677113 |  | 0.00 |
| `biogrid_human_physical` | `degree_matched` | 47 | `val` | `adamic_adar` | 0.656875 | 0.654873 |  | 0.00 |
| `biogrid_human_physical` | `degree_matched` | 47 | `val` | `preferential_attachment` | 0.558242 | 0.570277 |  | 0.00 |
| `biogrid_human_physical` | `degree_matched` | 47 | `test` | `common_neighbors` | 0.652272 | 0.650692 |  | 0.00 |
| `biogrid_human_physical` | `degree_matched` | 47 | `test` | `jaccard` | 0.669356 | 0.680334 |  | 0.00 |
| `biogrid_human_physical` | `degree_matched` | 47 | `test` | `adamic_adar` | 0.661190 | 0.659942 |  | 0.00 |
| `biogrid_human_physical` | `degree_matched` | 47 | `test` | `preferential_attachment` | 0.562126 | 0.574626 |  | 0.00 |
| `biogrid_human_physical` | `degree_matched` | 47 | `val` | `logistic_regression` | 0.708483 | 0.714932 | 0.037164 | 1.34 |
| `biogrid_human_physical` | `degree_matched` | 47 | `test` | `logistic_regression` | 0.710930 | 0.717980 | 0.037381 | 1.34 |
| `biogrid_human_physical` | `degree_matched` | 47 | `val` | `hist_gradient_boosting` | 0.759650 | 0.768630 | 0.018986 | 5.84 |
| `biogrid_human_physical` | `degree_matched` | 47 | `test` | `hist_gradient_boosting` | 0.763194 | 0.771990 | 0.021500 | 5.84 |
| `biogrid_human_physical` | `degree_matched` | 48 | `val` | `common_neighbors` | 0.648789 | 0.645751 |  | 0.00 |
| `biogrid_human_physical` | `degree_matched` | 48 | `val` | `jaccard` | 0.666072 | 0.676592 |  | 0.00 |
| `biogrid_human_physical` | `degree_matched` | 48 | `val` | `adamic_adar` | 0.657655 | 0.654815 |  | 0.00 |
| `biogrid_human_physical` | `degree_matched` | 48 | `val` | `preferential_attachment` | 0.559249 | 0.570857 |  | 0.00 |
| `biogrid_human_physical` | `degree_matched` | 48 | `test` | `common_neighbors` | 0.649876 | 0.648194 |  | 0.00 |
| `biogrid_human_physical` | `degree_matched` | 48 | `test` | `jaccard` | 0.667254 | 0.677597 |  | 0.00 |
| `biogrid_human_physical` | `degree_matched` | 48 | `test` | `adamic_adar` | 0.658864 | 0.657438 |  | 0.00 |
| `biogrid_human_physical` | `degree_matched` | 48 | `test` | `preferential_attachment` | 0.560420 | 0.573375 |  | 0.00 |
| `biogrid_human_physical` | `degree_matched` | 48 | `val` | `logistic_regression` | 0.708665 | 0.714597 | 0.037497 | 1.54 |
| `biogrid_human_physical` | `degree_matched` | 48 | `test` | `logistic_regression` | 0.709761 | 0.716103 | 0.037508 | 1.54 |
| `biogrid_human_physical` | `degree_matched` | 48 | `val` | `hist_gradient_boosting` | 0.761081 | 0.769749 | 0.019548 | 5.98 |
| `biogrid_human_physical` | `degree_matched` | 48 | `test` | `hist_gradient_boosting` | 0.761745 | 0.770324 | 0.020019 | 5.98 |
| `biogrid_human_physical` | `degree_matched` | 49 | `val` | `common_neighbors` | 0.648688 | 0.647389 |  | 0.00 |
| `biogrid_human_physical` | `degree_matched` | 49 | `val` | `jaccard` | 0.666190 | 0.677099 |  | 0.00 |
| `biogrid_human_physical` | `degree_matched` | 49 | `val` | `adamic_adar` | 0.657695 | 0.656642 |  | 0.00 |
| `biogrid_human_physical` | `degree_matched` | 49 | `val` | `preferential_attachment` | 0.559172 | 0.571926 |  | 0.00 |
| `biogrid_human_physical` | `degree_matched` | 49 | `test` | `common_neighbors` | 0.650421 | 0.648935 |  | 0.00 |
| `biogrid_human_physical` | `degree_matched` | 49 | `test` | `jaccard` | 0.666835 | 0.677424 |  | 0.00 |
| `biogrid_human_physical` | `degree_matched` | 49 | `test` | `adamic_adar` | 0.659373 | 0.658073 |  | 0.00 |
| `biogrid_human_physical` | `degree_matched` | 49 | `test` | `preferential_attachment` | 0.561623 | 0.574621 |  | 0.00 |
| `biogrid_human_physical` | `degree_matched` | 49 | `val` | `logistic_regression` | 0.709809 | 0.715809 | 0.038207 | 1.46 |
| `biogrid_human_physical` | `degree_matched` | 49 | `test` | `logistic_regression` | 0.708343 | 0.714620 | 0.037140 | 1.46 |
| `biogrid_human_physical` | `degree_matched` | 49 | `val` | `hist_gradient_boosting` | 0.761046 | 0.770082 | 0.020693 | 5.85 |
| `biogrid_human_physical` | `degree_matched` | 49 | `test` | `hist_gradient_boosting` | 0.761685 | 0.769962 | 0.021655 | 5.85 |
| `biogrid_human_physical` | `degree_matched` | 50 | `val` | `common_neighbors` | 0.648517 | 0.646110 |  | 0.00 |
| `biogrid_human_physical` | `degree_matched` | 50 | `val` | `jaccard` | 0.666899 | 0.678009 |  | 0.00 |
| `biogrid_human_physical` | `degree_matched` | 50 | `val` | `adamic_adar` | 0.657461 | 0.655249 |  | 0.00 |
| `biogrid_human_physical` | `degree_matched` | 50 | `val` | `preferential_attachment` | 0.557959 | 0.569595 |  | 0.00 |
| `biogrid_human_physical` | `degree_matched` | 50 | `test` | `common_neighbors` | 0.648598 | 0.647250 |  | 0.00 |
| `biogrid_human_physical` | `degree_matched` | 50 | `test` | `jaccard` | 0.665674 | 0.676031 |  | 0.00 |
| `biogrid_human_physical` | `degree_matched` | 50 | `test` | `adamic_adar` | 0.657689 | 0.656588 |  | 0.00 |
| `biogrid_human_physical` | `degree_matched` | 50 | `test` | `preferential_attachment` | 0.560312 | 0.572794 |  | 0.00 |
| `biogrid_human_physical` | `degree_matched` | 50 | `val` | `logistic_regression` | 0.710746 | 0.717221 | 0.038339 | 1.43 |
| `biogrid_human_physical` | `degree_matched` | 50 | `test` | `logistic_regression` | 0.708526 | 0.714697 | 0.036467 | 1.43 |
| `biogrid_human_physical` | `degree_matched` | 50 | `val` | `hist_gradient_boosting` | 0.762086 | 0.771816 | 0.020289 | 6.12 |
| `biogrid_human_physical` | `degree_matched` | 50 | `test` | `hist_gradient_boosting` | 0.761143 | 0.769704 | 0.019900 | 6.12 |
| `biogrid_human_physical` | `degree_matched` | 51 | `val` | `common_neighbors` | 0.648111 | 0.646902 |  | 0.00 |
| `biogrid_human_physical` | `degree_matched` | 51 | `val` | `jaccard` | 0.665511 | 0.677227 |  | 0.00 |
| `biogrid_human_physical` | `degree_matched` | 51 | `val` | `adamic_adar` | 0.657138 | 0.656125 |  | 0.00 |
| `biogrid_human_physical` | `degree_matched` | 51 | `val` | `preferential_attachment` | 0.559321 | 0.571553 |  | 0.00 |
| `biogrid_human_physical` | `degree_matched` | 51 | `test` | `common_neighbors` | 0.649271 | 0.647840 |  | 0.00 |
| `biogrid_human_physical` | `degree_matched` | 51 | `test` | `jaccard` | 0.666418 | 0.677217 |  | 0.00 |
| `biogrid_human_physical` | `degree_matched` | 51 | `test` | `adamic_adar` | 0.658258 | 0.657210 |  | 0.00 |
| `biogrid_human_physical` | `degree_matched` | 51 | `test` | `preferential_attachment` | 0.559906 | 0.572808 |  | 0.00 |
| `biogrid_human_physical` | `degree_matched` | 51 | `val` | `logistic_regression` | 0.709465 | 0.716800 | 0.037634 | 1.49 |
| `biogrid_human_physical` | `degree_matched` | 51 | `test` | `logistic_regression` | 0.709707 | 0.716046 | 0.037697 | 1.49 |
| `biogrid_human_physical` | `degree_matched` | 51 | `val` | `hist_gradient_boosting` | 0.761298 | 0.771297 | 0.020101 | 6.16 |
| `biogrid_human_physical` | `degree_matched` | 51 | `test` | `hist_gradient_boosting` | 0.759820 | 0.768873 | 0.018104 | 6.16 |
| `string_human_physical_v12` | `random` | 42 | `val` | `random_forest` | 0.940092 | 0.949581 | 0.004657 | 31.17 |
| `string_human_physical_v12` | `random` | 42 | `test` | `random_forest` | 0.940953 | 0.950351 | 0.004765 | 31.17 |
| `string_human_physical_v12` | `random` | 43 | `val` | `random_forest` | 0.940653 | 0.949990 | 0.005069 | 31.90 |
| `string_human_physical_v12` | `random` | 43 | `test` | `random_forest` | 0.940151 | 0.949434 | 0.003407 | 31.90 |
| `string_human_physical_v12` | `random` | 44 | `val` | `random_forest` | 0.940024 | 0.949547 | 0.003716 | 32.47 |
| `string_human_physical_v12` | `random` | 44 | `test` | `random_forest` | 0.939778 | 0.949329 | 0.005188 | 32.47 |
| `string_human_physical_v12` | `random` | 45 | `val` | `random_forest` | 0.941071 | 0.950575 | 0.004112 | 31.98 |
| `string_human_physical_v12` | `random` | 45 | `test` | `random_forest` | 0.940650 | 0.949759 | 0.003864 | 31.98 |
| `string_human_physical_v12` | `random` | 46 | `val` | `random_forest` | 0.940299 | 0.949685 | 0.006068 | 30.28 |
| `string_human_physical_v12` | `random` | 46 | `test` | `random_forest` | 0.941474 | 0.950757 | 0.004850 | 30.28 |
| `string_human_physical_v12` | `random` | 47 | `val` | `random_forest` | 0.941300 | 0.950409 | 0.003152 | 29.75 |
| `string_human_physical_v12` | `random` | 47 | `test` | `random_forest` | 0.939963 | 0.949183 | 0.003453 | 29.75 |
| `string_human_physical_v12` | `random` | 48 | `val` | `random_forest` | 0.940234 | 0.949689 | 0.004853 | 31.01 |
| `string_human_physical_v12` | `random` | 48 | `test` | `random_forest` | 0.941969 | 0.951059 | 0.004827 | 31.01 |
| `string_human_physical_v12` | `random` | 49 | `val` | `random_forest` | 0.940153 | 0.949637 | 0.003810 | 30.17 |
| `string_human_physical_v12` | `random` | 49 | `test` | `random_forest` | 0.939781 | 0.949362 | 0.006082 | 30.17 |
| `string_human_physical_v12` | `random` | 50 | `val` | `random_forest` | 0.940829 | 0.950369 | 0.004691 | 29.72 |
| `string_human_physical_v12` | `random` | 50 | `test` | `random_forest` | 0.939955 | 0.949414 | 0.004451 | 29.72 |
| `string_human_physical_v12` | `random` | 51 | `val` | `random_forest` | 0.940503 | 0.949770 | 0.005200 | 30.20 |
| `string_human_physical_v12` | `random` | 51 | `test` | `random_forest` | 0.940129 | 0.949790 | 0.004945 | 30.20 |
| `string_human_physical_v12` | `degree_matched` | 42 | `val` | `random_forest` | 0.859222 | 0.879617 | 0.009302 | 32.08 |
| `string_human_physical_v12` | `degree_matched` | 42 | `test` | `random_forest` | 0.860267 | 0.880370 | 0.010106 | 32.08 |
| `string_human_physical_v12` | `degree_matched` | 43 | `val` | `random_forest` | 0.860605 | 0.880292 | 0.010893 | 32.82 |
| `string_human_physical_v12` | `degree_matched` | 43 | `test` | `random_forest` | 0.859892 | 0.880245 | 0.011240 | 32.82 |
| `string_human_physical_v12` | `degree_matched` | 44 | `val` | `random_forest` | 0.858750 | 0.878905 | 0.009496 | 33.70 |
| `string_human_physical_v12` | `degree_matched` | 44 | `test` | `random_forest` | 0.859707 | 0.879891 | 0.010737 | 33.70 |
| `string_human_physical_v12` | `degree_matched` | 45 | `val` | `random_forest` | 0.859434 | 0.880006 | 0.009134 | 33.00 |
| `string_human_physical_v12` | `degree_matched` | 45 | `test` | `random_forest` | 0.859686 | 0.880236 | 0.009997 | 33.00 |
| `string_human_physical_v12` | `degree_matched` | 46 | `val` | `random_forest` | 0.861584 | 0.881370 | 0.010958 | 31.58 |
| `string_human_physical_v12` | `degree_matched` | 46 | `test` | `random_forest` | 0.859805 | 0.880062 | 0.010220 | 31.58 |
| `string_human_physical_v12` | `degree_matched` | 47 | `val` | `random_forest` | 0.859108 | 0.879409 | 0.009303 | 32.12 |
| `string_human_physical_v12` | `degree_matched` | 47 | `test` | `random_forest` | 0.859543 | 0.879912 | 0.011514 | 32.12 |
| `string_human_physical_v12` | `degree_matched` | 48 | `val` | `random_forest` | 0.859305 | 0.879905 | 0.011679 | 32.97 |
| `string_human_physical_v12` | `degree_matched` | 48 | `test` | `random_forest` | 0.861140 | 0.881299 | 0.011124 | 32.97 |
| `string_human_physical_v12` | `degree_matched` | 49 | `val` | `random_forest` | 0.859511 | 0.879926 | 0.009452 | 33.32 |
| `string_human_physical_v12` | `degree_matched` | 49 | `test` | `random_forest` | 0.861173 | 0.881927 | 0.011849 | 33.32 |
| `string_human_physical_v12` | `degree_matched` | 50 | `val` | `random_forest` | 0.860540 | 0.880937 | 0.010851 | 32.75 |
| `string_human_physical_v12` | `degree_matched` | 50 | `test` | `random_forest` | 0.859409 | 0.879849 | 0.010205 | 32.75 |
| `string_human_physical_v12` | `degree_matched` | 51 | `val` | `random_forest` | 0.860521 | 0.880711 | 0.010873 | 32.07 |
| `string_human_physical_v12` | `degree_matched` | 51 | `test` | `random_forest` | 0.861190 | 0.881375 | 0.011586 | 32.07 |
| `biogrid_human_physical` | `random` | 42 | `val` | `random_forest` | 0.941411 | 0.942150 | 0.005731 | 40.24 |
| `biogrid_human_physical` | `random` | 42 | `test` | `random_forest` | 0.941777 | 0.942632 | 0.004779 | 40.24 |
| `biogrid_human_physical` | `random` | 43 | `val` | `random_forest` | 0.941021 | 0.941772 | 0.005704 | 41.78 |
| `biogrid_human_physical` | `random` | 43 | `test` | `random_forest` | 0.941397 | 0.941806 | 0.004774 | 41.78 |
| `biogrid_human_physical` | `random` | 44 | `val` | `random_forest` | 0.940757 | 0.941436 | 0.004896 | 40.66 |
| `biogrid_human_physical` | `random` | 44 | `test` | `random_forest` | 0.941066 | 0.941754 | 0.005205 | 40.66 |
| `biogrid_human_physical` | `random` | 45 | `val` | `random_forest` | 0.941534 | 0.942560 | 0.005929 | 40.21 |
| `biogrid_human_physical` | `random` | 45 | `test` | `random_forest` | 0.941006 | 0.942088 | 0.005287 | 40.21 |
| `biogrid_human_physical` | `random` | 46 | `val` | `random_forest` | 0.940602 | 0.941605 | 0.005192 | 41.58 |
| `biogrid_human_physical` | `random` | 46 | `test` | `random_forest` | 0.941015 | 0.942188 | 0.005877 | 41.58 |
| `biogrid_human_physical` | `random` | 47 | `val` | `random_forest` | 0.941279 | 0.942311 | 0.004640 | 41.64 |
| `biogrid_human_physical` | `random` | 47 | `test` | `random_forest` | 0.942396 | 0.943468 | 0.006126 | 41.64 |
| `biogrid_human_physical` | `random` | 48 | `val` | `random_forest` | 0.942023 | 0.942825 | 0.004855 | 41.22 |
| `biogrid_human_physical` | `random` | 48 | `test` | `random_forest` | 0.941718 | 0.942635 | 0.005559 | 41.22 |
| `biogrid_human_physical` | `random` | 49 | `val` | `random_forest` | 0.941765 | 0.942593 | 0.004238 | 40.35 |
| `biogrid_human_physical` | `random` | 49 | `test` | `random_forest` | 0.941553 | 0.942224 | 0.005691 | 40.35 |
| `biogrid_human_physical` | `random` | 50 | `val` | `random_forest` | 0.940956 | 0.941859 | 0.005003 | 40.22 |
| `biogrid_human_physical` | `random` | 50 | `test` | `random_forest` | 0.941243 | 0.941989 | 0.005116 | 40.22 |
| `biogrid_human_physical` | `random` | 51 | `val` | `random_forest` | 0.941916 | 0.942295 | 0.005159 | 41.21 |
| `biogrid_human_physical` | `random` | 51 | `test` | `random_forest` | 0.941245 | 0.941912 | 0.005879 | 41.21 |
| `biogrid_human_physical` | `degree_matched` | 42 | `val` | `random_forest` | 0.758413 | 0.769958 | 0.023760 | 44.25 |
| `biogrid_human_physical` | `degree_matched` | 42 | `test` | `random_forest` | 0.759624 | 0.770667 | 0.023510 | 44.25 |
| `biogrid_human_physical` | `degree_matched` | 43 | `val` | `random_forest` | 0.760273 | 0.771959 | 0.025682 | 46.33 |
| `biogrid_human_physical` | `degree_matched` | 43 | `test` | `random_forest` | 0.760803 | 0.772352 | 0.025761 | 46.33 |
| `biogrid_human_physical` | `degree_matched` | 44 | `val` | `random_forest` | 0.760562 | 0.772038 | 0.025836 | 45.37 |
| `biogrid_human_physical` | `degree_matched` | 44 | `test` | `random_forest` | 0.760825 | 0.770704 | 0.025935 | 45.37 |
| `biogrid_human_physical` | `degree_matched` | 45 | `val` | `random_forest` | 0.759522 | 0.771017 | 0.024201 | 47.06 |
| `biogrid_human_physical` | `degree_matched` | 45 | `test` | `random_forest` | 0.760728 | 0.773004 | 0.025102 | 47.06 |
| `biogrid_human_physical` | `degree_matched` | 46 | `val` | `random_forest` | 0.759307 | 0.771379 | 0.024919 | 45.24 |
| `biogrid_human_physical` | `degree_matched` | 46 | `test` | `random_forest` | 0.760064 | 0.771656 | 0.025175 | 45.24 |
| `biogrid_human_physical` | `degree_matched` | 47 | `val` | `random_forest` | 0.758438 | 0.769353 | 0.024040 | 45.99 |
| `biogrid_human_physical` | `degree_matched` | 47 | `test` | `random_forest` | 0.761623 | 0.772994 | 0.026993 | 45.99 |
| `biogrid_human_physical` | `degree_matched` | 48 | `val` | `random_forest` | 0.759171 | 0.770731 | 0.023158 | 46.67 |
| `biogrid_human_physical` | `degree_matched` | 48 | `test` | `random_forest` | 0.759717 | 0.770190 | 0.024689 | 46.67 |
| `biogrid_human_physical` | `degree_matched` | 49 | `val` | `random_forest` | 0.759738 | 0.771467 | 0.023709 | 45.68 |
| `biogrid_human_physical` | `degree_matched` | 49 | `test` | `random_forest` | 0.760453 | 0.770952 | 0.025818 | 45.68 |
| `biogrid_human_physical` | `degree_matched` | 50 | `val` | `random_forest` | 0.761166 | 0.772643 | 0.026014 | 45.73 |
| `biogrid_human_physical` | `degree_matched` | 50 | `test` | `random_forest` | 0.758981 | 0.769900 | 0.025807 | 45.73 |
| `biogrid_human_physical` | `degree_matched` | 51 | `val` | `random_forest` | 0.758978 | 0.771251 | 0.024830 | 46.65 |
| `biogrid_human_physical` | `degree_matched` | 51 | `test` | `random_forest` | 0.758176 | 0.769469 | 0.022783 | 46.65 |
| `string_human_physical_v12` | `two_hop` | 42 | `val` | `common_neighbors` | 0.692504 | 0.725251 |  | 0.00 |
| `string_human_physical_v12` | `two_hop` | 42 | `val` | `jaccard` | 0.676947 | 0.730841 |  | 0.00 |
| `string_human_physical_v12` | `two_hop` | 42 | `val` | `adamic_adar` | 0.680506 | 0.730704 |  | 0.00 |
| `string_human_physical_v12` | `two_hop` | 42 | `val` | `preferential_attachment` | 0.606046 | 0.603063 |  | 0.00 |
| `string_human_physical_v12` | `two_hop` | 42 | `test` | `common_neighbors` | 0.694345 | 0.728674 |  | 0.00 |
| `string_human_physical_v12` | `two_hop` | 42 | `test` | `jaccard` | 0.679306 | 0.732064 |  | 0.00 |
| `string_human_physical_v12` | `two_hop` | 42 | `test` | `adamic_adar` | 0.683356 | 0.734949 |  | 0.00 |
| `string_human_physical_v12` | `two_hop` | 42 | `test` | `preferential_attachment` | 0.606836 | 0.607308 |  | 0.00 |
| `string_human_physical_v12` | `two_hop` | 42 | `val` | `logistic_regression` | 0.715753 | 0.750815 | 0.042410 | 0.90 |
| `string_human_physical_v12` | `two_hop` | 42 | `test` | `logistic_regression` | 0.716347 | 0.752277 | 0.043269 | 0.90 |
| `string_human_physical_v12` | `two_hop` | 42 | `val` | `random_forest` | 0.844852 | 0.855652 | 0.013195 | 31.15 |
| `string_human_physical_v12` | `two_hop` | 42 | `test` | `random_forest` | 0.844669 | 0.856607 | 0.013198 | 31.15 |
| `string_human_physical_v12` | `two_hop` | 42 | `val` | `hist_gradient_boosting` | 0.845303 | 0.855005 | 0.009800 | 4.60 |
| `string_human_physical_v12` | `two_hop` | 42 | `test` | `hist_gradient_boosting` | 0.844978 | 0.855603 | 0.012515 | 4.60 |
| `string_human_physical_v12` | `two_hop` | 43 | `val` | `common_neighbors` | 0.693539 | 0.725558 |  | 0.00 |
| `string_human_physical_v12` | `two_hop` | 43 | `val` | `jaccard` | 0.679673 | 0.733404 |  | 0.00 |
| `string_human_physical_v12` | `two_hop` | 43 | `val` | `adamic_adar` | 0.681699 | 0.731292 |  | 0.00 |
| `string_human_physical_v12` | `two_hop` | 43 | `val` | `preferential_attachment` | 0.603704 | 0.601475 |  | 0.00 |
| `string_human_physical_v12` | `two_hop` | 43 | `test` | `common_neighbors` | 0.692551 | 0.726685 |  | 0.00 |
| `string_human_physical_v12` | `two_hop` | 43 | `test` | `jaccard` | 0.678453 | 0.732830 |  | 0.00 |
| `string_human_physical_v12` | `two_hop` | 43 | `test` | `adamic_adar` | 0.681199 | 0.732881 |  | 0.00 |
| `string_human_physical_v12` | `two_hop` | 43 | `test` | `preferential_attachment` | 0.604732 | 0.603583 |  | 0.00 |
| `string_human_physical_v12` | `two_hop` | 43 | `val` | `logistic_regression` | 0.718106 | 0.752472 | 0.045407 | 0.88 |
| `string_human_physical_v12` | `two_hop` | 43 | `test` | `logistic_regression` | 0.715468 | 0.751740 | 0.042136 | 0.88 |
| `string_human_physical_v12` | `two_hop` | 43 | `val` | `random_forest` | 0.844843 | 0.855580 | 0.014314 | 34.80 |
| `string_human_physical_v12` | `two_hop` | 43 | `test` | `random_forest` | 0.845309 | 0.857392 | 0.013772 | 34.80 |
| `string_human_physical_v12` | `two_hop` | 43 | `val` | `hist_gradient_boosting` | 0.845566 | 0.855304 | 0.009906 | 5.36 |
| `string_human_physical_v12` | `two_hop` | 43 | `test` | `hist_gradient_boosting` | 0.845889 | 0.856945 | 0.012674 | 5.36 |
| `string_human_physical_v12` | `two_hop` | 44 | `val` | `common_neighbors` | 0.693668 | 0.727282 |  | 0.00 |
| `string_human_physical_v12` | `two_hop` | 44 | `val` | `jaccard` | 0.678884 | 0.733220 |  | 0.00 |
| `string_human_physical_v12` | `two_hop` | 44 | `val` | `adamic_adar` | 0.682364 | 0.732998 |  | 0.00 |
| `string_human_physical_v12` | `two_hop` | 44 | `val` | `preferential_attachment` | 0.606776 | 0.604329 |  | 0.00 |
| `string_human_physical_v12` | `two_hop` | 44 | `test` | `common_neighbors` | 0.693455 | 0.726931 |  | 0.00 |
| `string_human_physical_v12` | `two_hop` | 44 | `test` | `jaccard` | 0.679072 | 0.733367 |  | 0.00 |
| `string_human_physical_v12` | `two_hop` | 44 | `test` | `adamic_adar` | 0.682542 | 0.733193 |  | 0.00 |
| `string_human_physical_v12` | `two_hop` | 44 | `test` | `preferential_attachment` | 0.605203 | 0.604654 |  | 0.00 |
| `string_human_physical_v12` | `two_hop` | 44 | `val` | `logistic_regression` | 0.717103 | 0.753449 | 0.043617 | 0.85 |
| `string_human_physical_v12` | `two_hop` | 44 | `test` | `logistic_regression` | 0.716084 | 0.751793 | 0.043167 | 0.85 |
| `string_human_physical_v12` | `two_hop` | 44 | `val` | `random_forest` | 0.846138 | 0.857337 | 0.014317 | 33.35 |
| `string_human_physical_v12` | `two_hop` | 44 | `test` | `random_forest` | 0.844937 | 0.856617 | 0.014348 | 33.35 |
| `string_human_physical_v12` | `two_hop` | 44 | `val` | `hist_gradient_boosting` | 0.846242 | 0.856584 | 0.012181 | 5.16 |
| `string_human_physical_v12` | `two_hop` | 44 | `test` | `hist_gradient_boosting` | 0.845204 | 0.855965 | 0.013001 | 5.16 |
| `string_human_physical_v12` | `two_hop` | 45 | `val` | `common_neighbors` | 0.692932 | 0.725650 |  | 0.00 |
| `string_human_physical_v12` | `two_hop` | 45 | `val` | `jaccard` | 0.679427 | 0.734297 |  | 0.00 |
| `string_human_physical_v12` | `two_hop` | 45 | `val` | `adamic_adar` | 0.681013 | 0.731243 |  | 0.00 |
| `string_human_physical_v12` | `two_hop` | 45 | `val` | `preferential_attachment` | 0.604800 | 0.602203 |  | 0.00 |
| `string_human_physical_v12` | `two_hop` | 45 | `test` | `common_neighbors` | 0.693411 | 0.727429 |  | 0.00 |
| `string_human_physical_v12` | `two_hop` | 45 | `test` | `jaccard` | 0.680382 | 0.733897 |  | 0.00 |
| `string_human_physical_v12` | `two_hop` | 45 | `test` | `adamic_adar` | 0.682341 | 0.733447 |  | 0.00 |
| `string_human_physical_v12` | `two_hop` | 45 | `test` | `preferential_attachment` | 0.604616 | 0.603823 |  | 0.00 |
| `string_human_physical_v12` | `two_hop` | 45 | `val` | `logistic_regression` | 0.716917 | 0.752733 | 0.042949 | 0.87 |
| `string_human_physical_v12` | `two_hop` | 45 | `test` | `logistic_regression` | 0.715896 | 0.752591 | 0.041887 | 0.87 |
| `string_human_physical_v12` | `two_hop` | 45 | `val` | `random_forest` | 0.846173 | 0.857557 | 0.014186 | 33.43 |
| `string_human_physical_v12` | `two_hop` | 45 | `test` | `random_forest` | 0.843401 | 0.855962 | 0.012704 | 33.43 |
| `string_human_physical_v12` | `two_hop` | 45 | `val` | `hist_gradient_boosting` | 0.846550 | 0.857077 | 0.011794 | 5.35 |
| `string_human_physical_v12` | `two_hop` | 45 | `test` | `hist_gradient_boosting` | 0.843844 | 0.855488 | 0.011300 | 5.35 |
| `string_human_physical_v12` | `two_hop` | 46 | `val` | `common_neighbors` | 0.695888 | 0.729131 |  | 0.00 |
| `string_human_physical_v12` | `two_hop` | 46 | `val` | `jaccard` | 0.681211 | 0.734545 |  | 0.00 |
| `string_human_physical_v12` | `two_hop` | 46 | `val` | `adamic_adar` | 0.684546 | 0.735066 |  | 0.00 |
| `string_human_physical_v12` | `two_hop` | 46 | `val` | `preferential_attachment` | 0.607400 | 0.605013 |  | 0.00 |
| `string_human_physical_v12` | `two_hop` | 46 | `test` | `common_neighbors` | 0.696130 | 0.729727 |  | 0.00 |
| `string_human_physical_v12` | `two_hop` | 46 | `test` | `jaccard` | 0.680852 | 0.734551 |  | 0.00 |
| `string_human_physical_v12` | `two_hop` | 46 | `test` | `adamic_adar` | 0.684953 | 0.735705 |  | 0.00 |
| `string_human_physical_v12` | `two_hop` | 46 | `test` | `preferential_attachment` | 0.608580 | 0.607359 |  | 0.00 |
| `string_human_physical_v12` | `two_hop` | 46 | `val` | `logistic_regression` | 0.719141 | 0.754618 | 0.045249 | 0.88 |
| `string_human_physical_v12` | `two_hop` | 46 | `test` | `logistic_regression` | 0.718374 | 0.754241 | 0.045067 | 0.88 |
| `string_human_physical_v12` | `two_hop` | 46 | `val` | `random_forest` | 0.846185 | 0.857607 | 0.014363 | 34.22 |
| `string_human_physical_v12` | `two_hop` | 46 | `test` | `random_forest` | 0.845006 | 0.856469 | 0.014643 | 34.22 |
| `string_human_physical_v12` | `two_hop` | 46 | `val` | `hist_gradient_boosting` | 0.846204 | 0.856658 | 0.011902 | 5.26 |
| `string_human_physical_v12` | `two_hop` | 46 | `test` | `hist_gradient_boosting` | 0.844675 | 0.855409 | 0.011515 | 5.26 |
| `string_human_physical_v12` | `two_hop` | 47 | `val` | `common_neighbors` | 0.691791 | 0.724730 |  | 0.00 |
| `string_human_physical_v12` | `two_hop` | 47 | `val` | `jaccard` | 0.677949 | 0.731942 |  | 0.00 |
| `string_human_physical_v12` | `two_hop` | 47 | `val` | `adamic_adar` | 0.680112 | 0.730368 |  | 0.00 |
| `string_human_physical_v12` | `two_hop` | 47 | `val` | `preferential_attachment` | 0.604518 | 0.602394 |  | 0.00 |
| `string_human_physical_v12` | `two_hop` | 47 | `test` | `common_neighbors` | 0.694379 | 0.728294 |  | 0.00 |
| `string_human_physical_v12` | `two_hop` | 47 | `test` | `jaccard` | 0.680440 | 0.734781 |  | 0.00 |
| `string_human_physical_v12` | `two_hop` | 47 | `test` | `adamic_adar` | 0.683271 | 0.734497 |  | 0.00 |
| `string_human_physical_v12` | `two_hop` | 47 | `test` | `preferential_attachment` | 0.605906 | 0.606392 |  | 0.00 |
| `string_human_physical_v12` | `two_hop` | 47 | `val` | `logistic_regression` | 0.715728 | 0.751145 | 0.041546 | 0.88 |
| `string_human_physical_v12` | `two_hop` | 47 | `test` | `logistic_regression` | 0.717222 | 0.752955 | 0.043823 | 0.88 |
| `string_human_physical_v12` | `two_hop` | 47 | `val` | `random_forest` | 0.843643 | 0.855512 | 0.012209 | 33.95 |
| `string_human_physical_v12` | `two_hop` | 47 | `test` | `random_forest` | 0.845985 | 0.857584 | 0.014341 | 33.95 |
| `string_human_physical_v12` | `two_hop` | 47 | `val` | `hist_gradient_boosting` | 0.844266 | 0.855257 | 0.010568 | 5.13 |
| `string_human_physical_v12` | `two_hop` | 47 | `test` | `hist_gradient_boosting` | 0.846277 | 0.857059 | 0.012473 | 5.13 |
| `string_human_physical_v12` | `two_hop` | 48 | `val` | `common_neighbors` | 0.693316 | 0.726106 |  | 0.00 |
| `string_human_physical_v12` | `two_hop` | 48 | `val` | `jaccard` | 0.678798 | 0.732747 |  | 0.00 |
| `string_human_physical_v12` | `two_hop` | 48 | `val` | `adamic_adar` | 0.681596 | 0.731865 |  | 0.00 |
| `string_human_physical_v12` | `two_hop` | 48 | `val` | `preferential_attachment` | 0.605292 | 0.603630 |  | 0.00 |
| `string_human_physical_v12` | `two_hop` | 48 | `test` | `common_neighbors` | 0.696681 | 0.729248 |  | 0.00 |
| `string_human_physical_v12` | `two_hop` | 48 | `test` | `jaccard` | 0.681984 | 0.734668 |  | 0.00 |
| `string_human_physical_v12` | `two_hop` | 48 | `test` | `adamic_adar` | 0.685793 | 0.735496 |  | 0.00 |
| `string_human_physical_v12` | `two_hop` | 48 | `test` | `preferential_attachment` | 0.607430 | 0.605662 |  | 0.00 |
| `string_human_physical_v12` | `two_hop` | 48 | `val` | `logistic_regression` | 0.717310 | 0.752458 | 0.045111 | 0.89 |
| `string_human_physical_v12` | `two_hop` | 48 | `test` | `logistic_regression` | 0.719273 | 0.754402 | 0.046250 | 0.89 |
| `string_human_physical_v12` | `two_hop` | 48 | `val` | `random_forest` | 0.846432 | 0.857694 | 0.014452 | 34.58 |
| `string_human_physical_v12` | `two_hop` | 48 | `test` | `random_forest` | 0.845625 | 0.856771 | 0.014601 | 34.58 |
| `string_human_physical_v12` | `two_hop` | 48 | `val` | `hist_gradient_boosting` | 0.846732 | 0.857183 | 0.011733 | 5.13 |
| `string_human_physical_v12` | `two_hop` | 48 | `test` | `hist_gradient_boosting` | 0.845579 | 0.856035 | 0.011775 | 5.13 |
| `string_human_physical_v12` | `two_hop` | 49 | `val` | `common_neighbors` | 0.693617 | 0.727505 |  | 0.00 |
| `string_human_physical_v12` | `two_hop` | 49 | `val` | `jaccard` | 0.678639 | 0.732608 |  | 0.00 |
| `string_human_physical_v12` | `two_hop` | 49 | `val` | `adamic_adar` | 0.681783 | 0.733227 |  | 0.00 |
| `string_human_physical_v12` | `two_hop` | 49 | `val` | `preferential_attachment` | 0.606511 | 0.604749 |  | 0.00 |
| `string_human_physical_v12` | `two_hop` | 49 | `test` | `common_neighbors` | 0.695136 | 0.727989 |  | 0.00 |
| `string_human_physical_v12` | `two_hop` | 49 | `test` | `jaccard` | 0.680687 | 0.733894 |  | 0.00 |
| `string_human_physical_v12` | `two_hop` | 49 | `test` | `adamic_adar` | 0.684105 | 0.734333 |  | 0.00 |
| `string_human_physical_v12` | `two_hop` | 49 | `test` | `preferential_attachment` | 0.606219 | 0.605765 |  | 0.00 |
| `string_human_physical_v12` | `two_hop` | 49 | `val` | `logistic_regression` | 0.717223 | 0.753034 | 0.042813 | 0.87 |
| `string_human_physical_v12` | `two_hop` | 49 | `test` | `logistic_regression` | 0.716871 | 0.752072 | 0.043805 | 0.87 |
| `string_human_physical_v12` | `two_hop` | 49 | `val` | `random_forest` | 0.845989 | 0.857806 | 0.014092 | 33.84 |
| `string_human_physical_v12` | `two_hop` | 49 | `test` | `random_forest` | 0.846326 | 0.857616 | 0.015016 | 33.84 |
| `string_human_physical_v12` | `two_hop` | 49 | `val` | `hist_gradient_boosting` | 0.846661 | 0.857326 | 0.012225 | 5.11 |
| `string_human_physical_v12` | `two_hop` | 49 | `test` | `hist_gradient_boosting` | 0.846478 | 0.856712 | 0.013754 | 5.11 |
| `string_human_physical_v12` | `two_hop` | 50 | `val` | `common_neighbors` | 0.691012 | 0.723979 |  | 0.00 |
| `string_human_physical_v12` | `two_hop` | 50 | `val` | `jaccard` | 0.678995 | 0.733121 |  | 0.00 |
| `string_human_physical_v12` | `two_hop` | 50 | `val` | `adamic_adar` | 0.679512 | 0.729777 |  | 0.00 |
| `string_human_physical_v12` | `two_hop` | 50 | `val` | `preferential_attachment` | 0.601524 | 0.598705 |  | 0.00 |
| `string_human_physical_v12` | `two_hop` | 50 | `test` | `common_neighbors` | 0.692675 | 0.726978 |  | 0.00 |
| `string_human_physical_v12` | `two_hop` | 50 | `test` | `jaccard` | 0.678982 | 0.733976 |  | 0.00 |
| `string_human_physical_v12` | `two_hop` | 50 | `test` | `adamic_adar` | 0.681139 | 0.732923 |  | 0.00 |
| `string_human_physical_v12` | `two_hop` | 50 | `test` | `preferential_attachment` | 0.604473 | 0.604795 |  | 0.00 |
| `string_human_physical_v12` | `two_hop` | 50 | `val` | `logistic_regression` | 0.716483 | 0.752197 | 0.041499 | 0.89 |
| `string_human_physical_v12` | `two_hop` | 50 | `test` | `logistic_regression` | 0.715397 | 0.752365 | 0.042630 | 0.89 |
| `string_human_physical_v12` | `two_hop` | 50 | `val` | `random_forest` | 0.844827 | 0.856735 | 0.012203 | 33.59 |
| `string_human_physical_v12` | `two_hop` | 50 | `test` | `random_forest` | 0.845250 | 0.856915 | 0.014930 | 33.59 |
| `string_human_physical_v12` | `two_hop` | 50 | `val` | `hist_gradient_boosting` | 0.845213 | 0.856245 | 0.011743 | 5.07 |
| `string_human_physical_v12` | `two_hop` | 50 | `test` | `hist_gradient_boosting` | 0.845667 | 0.856483 | 0.012326 | 5.07 |
| `string_human_physical_v12` | `two_hop` | 51 | `val` | `common_neighbors` | 0.692398 | 0.724772 |  | 0.00 |
| `string_human_physical_v12` | `two_hop` | 51 | `val` | `jaccard` | 0.678771 | 0.730723 |  | 0.00 |
| `string_human_physical_v12` | `two_hop` | 51 | `val` | `adamic_adar` | 0.680727 | 0.730564 |  | 0.00 |
| `string_human_physical_v12` | `two_hop` | 51 | `val` | `preferential_attachment` | 0.605120 | 0.602579 |  | 0.00 |
| `string_human_physical_v12` | `two_hop` | 51 | `test` | `common_neighbors` | 0.692967 | 0.726968 |  | 0.00 |
| `string_human_physical_v12` | `two_hop` | 51 | `test` | `jaccard` | 0.679886 | 0.734804 |  | 0.00 |
| `string_human_physical_v12` | `two_hop` | 51 | `test` | `adamic_adar` | 0.681649 | 0.733108 |  | 0.00 |
| `string_human_physical_v12` | `two_hop` | 51 | `test` | `preferential_attachment` | 0.603537 | 0.603367 |  | 0.00 |
| `string_human_physical_v12` | `two_hop` | 51 | `val` | `logistic_regression` | 0.715814 | 0.750170 | 0.042809 | 0.87 |
| `string_human_physical_v12` | `two_hop` | 51 | `test` | `logistic_regression` | 0.716754 | 0.752747 | 0.042789 | 0.87 |
| `string_human_physical_v12` | `two_hop` | 51 | `val` | `random_forest` | 0.843028 | 0.854453 | 0.011859 | 33.15 |
| `string_human_physical_v12` | `two_hop` | 51 | `test` | `random_forest` | 0.847121 | 0.858697 | 0.015493 | 33.15 |
| `string_human_physical_v12` | `two_hop` | 51 | `val` | `hist_gradient_boosting` | 0.843033 | 0.853483 | 0.008192 | 5.10 |
| `string_human_physical_v12` | `two_hop` | 51 | `test` | `hist_gradient_boosting` | 0.847238 | 0.858119 | 0.013231 | 5.10 |
| `biogrid_human_physical` | `two_hop` | 42 | `val` | `common_neighbors` | 0.608039 | 0.624706 |  | 0.00 |
| `biogrid_human_physical` | `two_hop` | 42 | `val` | `jaccard` | 0.574422 | 0.600662 |  | 0.00 |
| `biogrid_human_physical` | `two_hop` | 42 | `val` | `adamic_adar` | 0.593474 | 0.620599 |  | 0.00 |
| `biogrid_human_physical` | `two_hop` | 42 | `val` | `preferential_attachment` | 0.590600 | 0.586788 |  | 0.00 |
| `biogrid_human_physical` | `two_hop` | 42 | `test` | `common_neighbors` | 0.611727 | 0.632112 |  | 0.00 |
| `biogrid_human_physical` | `two_hop` | 42 | `test` | `jaccard` | 0.577647 | 0.604762 |  | 0.00 |
| `biogrid_human_physical` | `two_hop` | 42 | `test` | `adamic_adar` | 0.597734 | 0.628841 |  | 0.00 |
| `biogrid_human_physical` | `two_hop` | 42 | `test` | `preferential_attachment` | 0.593498 | 0.594464 |  | 0.00 |
| `biogrid_human_physical` | `two_hop` | 42 | `val` | `logistic_regression` | 0.661686 | 0.654093 | 0.031570 | 1.22 |
| `biogrid_human_physical` | `two_hop` | 42 | `test` | `logistic_regression` | 0.658648 | 0.654435 | 0.030996 | 1.22 |
| `biogrid_human_physical` | `two_hop` | 42 | `val` | `random_forest` | 0.767372 | 0.773487 | 0.027211 | 48.49 |
| `biogrid_human_physical` | `two_hop` | 42 | `test` | `random_forest` | 0.766073 | 0.772874 | 0.026422 | 48.49 |
| `biogrid_human_physical` | `two_hop` | 42 | `val` | `hist_gradient_boosting` | 0.771405 | 0.775991 | 0.018581 | 6.49 |
| `biogrid_human_physical` | `two_hop` | 42 | `test` | `hist_gradient_boosting` | 0.769545 | 0.774569 | 0.017535 | 6.49 |
| `biogrid_human_physical` | `two_hop` | 43 | `val` | `common_neighbors` | 0.609924 | 0.627902 |  | 0.00 |
| `biogrid_human_physical` | `two_hop` | 43 | `val` | `jaccard` | 0.577207 | 0.602674 |  | 0.00 |
| `biogrid_human_physical` | `two_hop` | 43 | `val` | `adamic_adar` | 0.595457 | 0.623982 |  | 0.00 |
| `biogrid_human_physical` | `two_hop` | 43 | `val` | `preferential_attachment` | 0.590225 | 0.589342 |  | 0.00 |
| `biogrid_human_physical` | `two_hop` | 43 | `test` | `common_neighbors` | 0.613656 | 0.632967 |  | 0.00 |
| `biogrid_human_physical` | `two_hop` | 43 | `test` | `jaccard` | 0.580275 | 0.605798 |  | 0.00 |
| `biogrid_human_physical` | `two_hop` | 43 | `test` | `adamic_adar` | 0.599997 | 0.630005 |  | 0.00 |
| `biogrid_human_physical` | `two_hop` | 43 | `test` | `preferential_attachment` | 0.593386 | 0.594419 |  | 0.00 |
| `biogrid_human_physical` | `two_hop` | 43 | `val` | `logistic_regression` | 0.661783 | 0.655643 | 0.031149 | 1.18 |
| `biogrid_human_physical` | `two_hop` | 43 | `test` | `logistic_regression` | 0.659342 | 0.653935 | 0.031419 | 1.18 |
| `biogrid_human_physical` | `two_hop` | 43 | `val` | `random_forest` | 0.767141 | 0.773591 | 0.027226 | 46.20 |
| `biogrid_human_physical` | `two_hop` | 43 | `test` | `random_forest` | 0.766208 | 0.772662 | 0.026056 | 46.20 |
| `biogrid_human_physical` | `two_hop` | 43 | `val` | `hist_gradient_boosting` | 0.770475 | 0.775406 | 0.017302 | 6.83 |
| `biogrid_human_physical` | `two_hop` | 43 | `test` | `hist_gradient_boosting` | 0.768283 | 0.773250 | 0.016743 | 6.83 |
| `biogrid_human_physical` | `two_hop` | 44 | `val` | `common_neighbors` | 0.609845 | 0.626950 |  | 0.00 |
| `biogrid_human_physical` | `two_hop` | 44 | `val` | `jaccard` | 0.576064 | 0.600783 |  | 0.00 |
| `biogrid_human_physical` | `two_hop` | 44 | `val` | `adamic_adar` | 0.595421 | 0.623194 |  | 0.00 |
| `biogrid_human_physical` | `two_hop` | 44 | `val` | `preferential_attachment` | 0.591265 | 0.589736 |  | 0.00 |
| `biogrid_human_physical` | `two_hop` | 44 | `test` | `common_neighbors` | 0.611131 | 0.630735 |  | 0.00 |
| `biogrid_human_physical` | `two_hop` | 44 | `test` | `jaccard` | 0.576386 | 0.601923 |  | 0.00 |
| `biogrid_human_physical` | `two_hop` | 44 | `test` | `adamic_adar` | 0.597393 | 0.627679 |  | 0.00 |
| `biogrid_human_physical` | `two_hop` | 44 | `test` | `preferential_attachment` | 0.593399 | 0.593662 |  | 0.00 |
| `biogrid_human_physical` | `two_hop` | 44 | `val` | `logistic_regression` | 0.659910 | 0.652540 | 0.031887 | 1.15 |
| `biogrid_human_physical` | `two_hop` | 44 | `test` | `logistic_regression` | 0.656299 | 0.651441 | 0.031059 | 1.15 |
| `biogrid_human_physical` | `two_hop` | 44 | `val` | `random_forest` | 0.765427 | 0.771492 | 0.026656 | 47.07 |
| `biogrid_human_physical` | `two_hop` | 44 | `test` | `random_forest` | 0.763657 | 0.770678 | 0.024624 | 47.07 |
| `biogrid_human_physical` | `two_hop` | 44 | `val` | `hist_gradient_boosting` | 0.769118 | 0.773384 | 0.016988 | 6.41 |
| `biogrid_human_physical` | `two_hop` | 44 | `test` | `hist_gradient_boosting` | 0.766958 | 0.772400 | 0.018576 | 6.41 |
| `biogrid_human_physical` | `two_hop` | 45 | `val` | `common_neighbors` | 0.610937 | 0.628902 |  | 0.00 |
| `biogrid_human_physical` | `two_hop` | 45 | `val` | `jaccard` | 0.577246 | 0.602942 |  | 0.00 |
| `biogrid_human_physical` | `two_hop` | 45 | `val` | `adamic_adar` | 0.596554 | 0.624971 |  | 0.00 |
| `biogrid_human_physical` | `two_hop` | 45 | `val` | `preferential_attachment` | 0.592382 | 0.590531 |  | 0.00 |
| `biogrid_human_physical` | `two_hop` | 45 | `test` | `common_neighbors` | 0.610484 | 0.630148 |  | 0.00 |
| `biogrid_human_physical` | `two_hop` | 45 | `test` | `jaccard` | 0.576675 | 0.603728 |  | 0.00 |
| `biogrid_human_physical` | `two_hop` | 45 | `test` | `adamic_adar` | 0.596560 | 0.626796 |  | 0.00 |
| `biogrid_human_physical` | `two_hop` | 45 | `test` | `preferential_attachment` | 0.592065 | 0.591612 |  | 0.00 |
| `biogrid_human_physical` | `two_hop` | 45 | `val` | `logistic_regression` | 0.662118 | 0.656852 | 0.031269 | 1.18 |
| `biogrid_human_physical` | `two_hop` | 45 | `test` | `logistic_regression` | 0.657502 | 0.653603 | 0.028352 | 1.18 |
| `biogrid_human_physical` | `two_hop` | 45 | `val` | `random_forest` | 0.767761 | 0.774474 | 0.026438 | 50.19 |
| `biogrid_human_physical` | `two_hop` | 45 | `test` | `random_forest` | 0.765427 | 0.772650 | 0.025098 | 50.19 |
| `biogrid_human_physical` | `two_hop` | 45 | `val` | `hist_gradient_boosting` | 0.771011 | 0.776144 | 0.017981 | 6.47 |
| `biogrid_human_physical` | `two_hop` | 45 | `test` | `hist_gradient_boosting` | 0.768712 | 0.774505 | 0.018634 | 6.47 |
| `biogrid_human_physical` | `two_hop` | 46 | `val` | `common_neighbors` | 0.608515 | 0.628255 |  | 0.00 |
| `biogrid_human_physical` | `two_hop` | 46 | `val` | `jaccard` | 0.575698 | 0.604272 |  | 0.00 |
| `biogrid_human_physical` | `two_hop` | 46 | `val` | `adamic_adar` | 0.594058 | 0.624419 |  | 0.00 |
| `biogrid_human_physical` | `two_hop` | 46 | `val` | `preferential_attachment` | 0.590414 | 0.588975 |  | 0.00 |
| `biogrid_human_physical` | `two_hop` | 46 | `test` | `common_neighbors` | 0.611480 | 0.630945 |  | 0.00 |
| `biogrid_human_physical` | `two_hop` | 46 | `test` | `jaccard` | 0.577189 | 0.604670 |  | 0.00 |
| `biogrid_human_physical` | `two_hop` | 46 | `test` | `adamic_adar` | 0.597794 | 0.627786 |  | 0.00 |
| `biogrid_human_physical` | `two_hop` | 46 | `test` | `preferential_attachment` | 0.592371 | 0.592535 |  | 0.00 |
| `biogrid_human_physical` | `two_hop` | 46 | `val` | `logistic_regression` | 0.660160 | 0.655410 | 0.030353 | 1.18 |
| `biogrid_human_physical` | `two_hop` | 46 | `test` | `logistic_regression` | 0.658719 | 0.653681 | 0.032207 | 1.18 |
| `biogrid_human_physical` | `two_hop` | 46 | `val` | `random_forest` | 0.765849 | 0.773135 | 0.026004 | 47.42 |
| `biogrid_human_physical` | `two_hop` | 46 | `test` | `random_forest` | 0.766167 | 0.772723 | 0.026097 | 47.42 |
| `biogrid_human_physical` | `two_hop` | 46 | `val` | `hist_gradient_boosting` | 0.770037 | 0.775724 | 0.018128 | 6.43 |
| `biogrid_human_physical` | `two_hop` | 46 | `test` | `hist_gradient_boosting` | 0.769795 | 0.774614 | 0.020668 | 6.43 |
| `biogrid_human_physical` | `two_hop` | 47 | `val` | `common_neighbors` | 0.608618 | 0.625809 |  | 0.00 |
| `biogrid_human_physical` | `two_hop` | 47 | `val` | `jaccard` | 0.575606 | 0.601708 |  | 0.00 |
| `biogrid_human_physical` | `two_hop` | 47 | `val` | `adamic_adar` | 0.594124 | 0.621848 |  | 0.00 |
| `biogrid_human_physical` | `two_hop` | 47 | `val` | `preferential_attachment` | 0.589863 | 0.587493 |  | 0.00 |
| `biogrid_human_physical` | `two_hop` | 47 | `test` | `common_neighbors` | 0.614051 | 0.635002 |  | 0.00 |
| `biogrid_human_physical` | `two_hop` | 47 | `test` | `jaccard` | 0.578950 | 0.606651 |  | 0.00 |
| `biogrid_human_physical` | `two_hop` | 47 | `test` | `adamic_adar` | 0.600355 | 0.631904 |  | 0.00 |
| `biogrid_human_physical` | `two_hop` | 47 | `test` | `preferential_attachment` | 0.594878 | 0.596028 |  | 0.00 |
| `biogrid_human_physical` | `two_hop` | 47 | `val` | `logistic_regression` | 0.660081 | 0.653889 | 0.030428 | 1.20 |
| `biogrid_human_physical` | `two_hop` | 47 | `test` | `logistic_regression` | 0.659485 | 0.656140 | 0.030936 | 1.20 |
| `biogrid_human_physical` | `two_hop` | 47 | `val` | `random_forest` | 0.767166 | 0.773146 | 0.028313 | 46.71 |
| `biogrid_human_physical` | `two_hop` | 47 | `test` | `random_forest` | 0.766186 | 0.773088 | 0.026554 | 46.71 |
| `biogrid_human_physical` | `two_hop` | 47 | `val` | `hist_gradient_boosting` | 0.770992 | 0.775689 | 0.016487 | 7.17 |
| `biogrid_human_physical` | `two_hop` | 47 | `test` | `hist_gradient_boosting` | 0.768992 | 0.773985 | 0.018166 | 7.17 |
| `biogrid_human_physical` | `two_hop` | 48 | `val` | `common_neighbors` | 0.610498 | 0.627925 |  | 0.00 |
| `biogrid_human_physical` | `two_hop` | 48 | `val` | `jaccard` | 0.575923 | 0.601835 |  | 0.00 |
| `biogrid_human_physical` | `two_hop` | 48 | `val` | `adamic_adar` | 0.596125 | 0.624004 |  | 0.00 |
| `biogrid_human_physical` | `two_hop` | 48 | `val` | `preferential_attachment` | 0.592550 | 0.590046 |  | 0.00 |
| `biogrid_human_physical` | `two_hop` | 48 | `test` | `common_neighbors` | 0.613416 | 0.632763 |  | 0.00 |
| `biogrid_human_physical` | `two_hop` | 48 | `test` | `jaccard` | 0.579137 | 0.606012 |  | 0.00 |
| `biogrid_human_physical` | `two_hop` | 48 | `test` | `adamic_adar` | 0.599543 | 0.629601 |  | 0.00 |
| `biogrid_human_physical` | `two_hop` | 48 | `test` | `preferential_attachment` | 0.594396 | 0.593906 |  | 0.00 |
| `biogrid_human_physical` | `two_hop` | 48 | `val` | `logistic_regression` | 0.661669 | 0.655446 | 0.031116 | 1.18 |
| `biogrid_human_physical` | `two_hop` | 48 | `test` | `logistic_regression` | 0.660714 | 0.655576 | 0.030009 | 1.18 |
| `biogrid_human_physical` | `two_hop` | 48 | `val` | `random_forest` | 0.768467 | 0.774237 | 0.027774 | 47.32 |
| `biogrid_human_physical` | `two_hop` | 48 | `test` | `random_forest` | 0.767266 | 0.773593 | 0.026106 | 47.32 |
| `biogrid_human_physical` | `two_hop` | 48 | `val` | `hist_gradient_boosting` | 0.771138 | 0.775504 | 0.017105 | 6.51 |
| `biogrid_human_physical` | `two_hop` | 48 | `test` | `hist_gradient_boosting` | 0.769805 | 0.774981 | 0.017797 | 6.51 |
| `biogrid_human_physical` | `two_hop` | 49 | `val` | `common_neighbors` | 0.611269 | 0.628098 |  | 0.00 |
| `biogrid_human_physical` | `two_hop` | 49 | `val` | `jaccard` | 0.577113 | 0.603095 |  | 0.00 |
| `biogrid_human_physical` | `two_hop` | 49 | `val` | `adamic_adar` | 0.596804 | 0.624363 |  | 0.00 |
| `biogrid_human_physical` | `two_hop` | 49 | `val` | `preferential_attachment` | 0.593249 | 0.590426 |  | 0.00 |
| `biogrid_human_physical` | `two_hop` | 49 | `test` | `common_neighbors` | 0.613702 | 0.633605 |  | 0.00 |
| `biogrid_human_physical` | `two_hop` | 49 | `test` | `jaccard` | 0.578164 | 0.604321 |  | 0.00 |
| `biogrid_human_physical` | `two_hop` | 49 | `test` | `adamic_adar` | 0.599628 | 0.630215 |  | 0.00 |
| `biogrid_human_physical` | `two_hop` | 49 | `test` | `preferential_attachment` | 0.595006 | 0.595368 |  | 0.00 |
| `biogrid_human_physical` | `two_hop` | 49 | `val` | `logistic_regression` | 0.661792 | 0.655329 | 0.031913 | 1.21 |
| `biogrid_human_physical` | `two_hop` | 49 | `test` | `logistic_regression` | 0.661976 | 0.657414 | 0.032838 | 1.21 |
| `biogrid_human_physical` | `two_hop` | 49 | `val` | `random_forest` | 0.766246 | 0.773017 | 0.025797 | 47.44 |
| `biogrid_human_physical` | `two_hop` | 49 | `test` | `random_forest` | 0.767397 | 0.774279 | 0.027318 | 47.44 |
| `biogrid_human_physical` | `two_hop` | 49 | `val` | `hist_gradient_boosting` | 0.770440 | 0.775077 | 0.016504 | 6.57 |
| `biogrid_human_physical` | `two_hop` | 49 | `test` | `hist_gradient_boosting` | 0.770778 | 0.776141 | 0.018095 | 6.57 |
| `biogrid_human_physical` | `two_hop` | 50 | `val` | `common_neighbors` | 0.608139 | 0.626631 |  | 0.00 |
| `biogrid_human_physical` | `two_hop` | 50 | `val` | `jaccard` | 0.574998 | 0.600931 |  | 0.00 |
| `biogrid_human_physical` | `two_hop` | 50 | `val` | `adamic_adar` | 0.593636 | 0.622669 |  | 0.00 |
| `biogrid_human_physical` | `two_hop` | 50 | `val` | `preferential_attachment` | 0.589136 | 0.587689 |  | 0.00 |
| `biogrid_human_physical` | `two_hop` | 50 | `test` | `common_neighbors` | 0.611437 | 0.631238 |  | 0.00 |
| `biogrid_human_physical` | `two_hop` | 50 | `test` | `jaccard` | 0.577072 | 0.603886 |  | 0.00 |
| `biogrid_human_physical` | `two_hop` | 50 | `test` | `adamic_adar` | 0.597716 | 0.628166 |  | 0.00 |
| `biogrid_human_physical` | `two_hop` | 50 | `test` | `preferential_attachment` | 0.592886 | 0.593395 |  | 0.00 |
| `biogrid_human_physical` | `two_hop` | 50 | `val` | `logistic_regression` | 0.661335 | 0.655116 | 0.030470 | 1.19 |
| `biogrid_human_physical` | `two_hop` | 50 | `test` | `logistic_regression` | 0.658580 | 0.653589 | 0.032107 | 1.19 |
| `biogrid_human_physical` | `two_hop` | 50 | `val` | `random_forest` | 0.767279 | 0.773574 | 0.027740 | 46.92 |
| `biogrid_human_physical` | `two_hop` | 50 | `test` | `random_forest` | 0.766956 | 0.774563 | 0.025898 | 46.92 |
| `biogrid_human_physical` | `two_hop` | 50 | `val` | `hist_gradient_boosting` | 0.770568 | 0.775433 | 0.018992 | 6.67 |
| `biogrid_human_physical` | `two_hop` | 50 | `test` | `hist_gradient_boosting` | 0.769629 | 0.775392 | 0.017826 | 6.67 |
| `biogrid_human_physical` | `two_hop` | 51 | `val` | `common_neighbors` | 0.611644 | 0.629446 |  | 0.00 |
| `biogrid_human_physical` | `two_hop` | 51 | `val` | `jaccard` | 0.577493 | 0.603380 |  | 0.00 |
| `biogrid_human_physical` | `two_hop` | 51 | `val` | `adamic_adar` | 0.597322 | 0.625647 |  | 0.00 |
| `biogrid_human_physical` | `two_hop` | 51 | `val` | `preferential_attachment` | 0.593119 | 0.591220 |  | 0.00 |
| `biogrid_human_physical` | `two_hop` | 51 | `test` | `common_neighbors` | 0.611610 | 0.630028 |  | 0.00 |
| `biogrid_human_physical` | `two_hop` | 51 | `test` | `jaccard` | 0.577208 | 0.604195 |  | 0.00 |
| `biogrid_human_physical` | `two_hop` | 51 | `test` | `adamic_adar` | 0.597471 | 0.626692 |  | 0.00 |
| `biogrid_human_physical` | `two_hop` | 51 | `test` | `preferential_attachment` | 0.593451 | 0.592077 |  | 0.00 |
| `biogrid_human_physical` | `two_hop` | 51 | `val` | `logistic_regression` | 0.662159 | 0.655887 | 0.031921 | 1.17 |
| `biogrid_human_physical` | `two_hop` | 51 | `test` | `logistic_regression` | 0.658673 | 0.653337 | 0.030968 | 1.17 |
| `biogrid_human_physical` | `two_hop` | 51 | `val` | `random_forest` | 0.765574 | 0.772087 | 0.026438 | 46.64 |
| `biogrid_human_physical` | `two_hop` | 51 | `test` | `random_forest` | 0.765636 | 0.772275 | 0.027041 | 46.64 |
| `biogrid_human_physical` | `two_hop` | 51 | `val` | `hist_gradient_boosting` | 0.769031 | 0.773764 | 0.015662 | 6.48 |
| `biogrid_human_physical` | `two_hop` | 51 | `test` | `hist_gradient_boosting` | 0.769053 | 0.773983 | 0.016057 | 6.48 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 42 | `val` | `common_neighbors` | 0.485780 | 0.515329 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 42 | `val` | `jaccard` | 0.397298 | 0.439214 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 42 | `val` | `adamic_adar` | 0.450297 | 0.499051 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 42 | `val` | `preferential_attachment` | 0.558250 | 0.548398 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 42 | `test` | `common_neighbors` | 0.488544 | 0.520052 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 42 | `test` | `jaccard` | 0.398920 | 0.441035 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 42 | `test` | `adamic_adar` | 0.454493 | 0.504733 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 42 | `test` | `preferential_attachment` | 0.560709 | 0.552860 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 42 | `val` | `logistic_regression` | 0.755898 | 0.725823 | 0.102472 | 0.78 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 42 | `test` | `logistic_regression` | 0.749036 | 0.720426 | 0.097919 | 0.78 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 42 | `val` | `random_forest` | 0.818634 | 0.834512 | 0.046496 | 24.21 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 42 | `test` | `random_forest` | 0.814176 | 0.830096 | 0.042436 | 24.21 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 42 | `val` | `hist_gradient_boosting` | 0.839644 | 0.853615 | 0.012782 | 4.00 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 42 | `test` | `hist_gradient_boosting` | 0.833694 | 0.848247 | 0.012820 | 4.00 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 43 | `val` | `common_neighbors` | 0.486298 | 0.517723 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 43 | `val` | `jaccard` | 0.398322 | 0.440356 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 43 | `val` | `adamic_adar` | 0.451418 | 0.501462 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 43 | `val` | `preferential_attachment` | 0.558267 | 0.548670 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 43 | `test` | `common_neighbors` | 0.489461 | 0.520026 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 43 | `test` | `jaccard` | 0.398888 | 0.440409 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 43 | `test` | `adamic_adar` | 0.454962 | 0.504421 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 43 | `test` | `preferential_attachment` | 0.560892 | 0.554115 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 43 | `val` | `logistic_regression` | 0.755571 | 0.725519 | 0.101756 | 0.69 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 43 | `test` | `logistic_regression` | 0.750851 | 0.721947 | 0.098016 | 0.69 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 43 | `val` | `random_forest` | 0.814475 | 0.830049 | 0.044305 | 24.75 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 43 | `test` | `random_forest` | 0.813658 | 0.829883 | 0.041908 | 24.75 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 43 | `val` | `hist_gradient_boosting` | 0.836180 | 0.849634 | 0.010538 | 4.02 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 43 | `test` | `hist_gradient_boosting` | 0.833724 | 0.848450 | 0.012601 | 4.02 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 44 | `val` | `common_neighbors` | 0.485951 | 0.513977 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 44 | `val` | `jaccard` | 0.397237 | 0.438202 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 44 | `val` | `adamic_adar` | 0.450772 | 0.497810 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 44 | `val` | `preferential_attachment` | 0.558658 | 0.547233 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 44 | `test` | `common_neighbors` | 0.487915 | 0.520330 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 44 | `test` | `jaccard` | 0.396278 | 0.439063 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 44 | `test` | `adamic_adar` | 0.453640 | 0.504985 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 44 | `test` | `preferential_attachment` | 0.563076 | 0.555795 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 44 | `val` | `logistic_regression` | 0.754367 | 0.723156 | 0.104584 | 0.57 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 44 | `test` | `logistic_regression` | 0.752951 | 0.723115 | 0.102310 | 0.57 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 44 | `val` | `random_forest` | 0.817911 | 0.833128 | 0.045180 | 24.41 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 44 | `test` | `random_forest` | 0.815439 | 0.830766 | 0.042947 | 24.41 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 44 | `val` | `hist_gradient_boosting` | 0.838979 | 0.852714 | 0.011151 | 3.96 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 44 | `test` | `hist_gradient_boosting` | 0.835464 | 0.849323 | 0.009817 | 3.96 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 45 | `val` | `common_neighbors` | 0.485975 | 0.515477 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 45 | `val` | `jaccard` | 0.398238 | 0.439501 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 45 | `val` | `adamic_adar` | 0.450754 | 0.499336 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 45 | `val` | `preferential_attachment` | 0.558354 | 0.548213 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 45 | `test` | `common_neighbors` | 0.489682 | 0.518803 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 45 | `test` | `jaccard` | 0.397656 | 0.439048 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 45 | `test` | `adamic_adar` | 0.455515 | 0.503219 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 45 | `test` | `preferential_attachment` | 0.563272 | 0.554501 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 45 | `val` | `logistic_regression` | 0.753500 | 0.722568 | 0.101894 | 0.67 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 45 | `test` | `logistic_regression` | 0.752638 | 0.724893 | 0.098143 | 0.67 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 45 | `val` | `random_forest` | 0.815406 | 0.830588 | 0.045699 | 24.55 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 45 | `test` | `random_forest` | 0.815789 | 0.831294 | 0.045885 | 24.55 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 45 | `val` | `hist_gradient_boosting` | 0.836608 | 0.850310 | 0.010117 | 3.91 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 45 | `test` | `hist_gradient_boosting` | 0.836463 | 0.851271 | 0.014668 | 3.91 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 46 | `val` | `common_neighbors` | 0.488187 | 0.518464 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 46 | `val` | `jaccard` | 0.399053 | 0.439810 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 46 | `val` | `adamic_adar` | 0.453514 | 0.502338 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 46 | `val` | `preferential_attachment` | 0.560993 | 0.551302 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 46 | `test` | `common_neighbors` | 0.486000 | 0.516641 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 46 | `test` | `jaccard` | 0.394398 | 0.436430 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 46 | `test` | `adamic_adar` | 0.451841 | 0.501256 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 46 | `test` | `preferential_attachment` | 0.561864 | 0.553462 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 46 | `val` | `logistic_regression` | 0.754642 | 0.724382 | 0.104988 | 0.68 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 46 | `test` | `logistic_regression` | 0.751918 | 0.720377 | 0.103089 | 0.68 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 46 | `val` | `random_forest` | 0.817091 | 0.832442 | 0.046274 | 23.59 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 46 | `test` | `random_forest` | 0.818057 | 0.832911 | 0.044766 | 23.59 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 46 | `val` | `hist_gradient_boosting` | 0.837060 | 0.851347 | 0.010832 | 3.91 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 46 | `test` | `hist_gradient_boosting` | 0.836538 | 0.850621 | 0.012875 | 3.91 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 47 | `val` | `common_neighbors` | 0.480164 | 0.511474 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 47 | `val` | `jaccard` | 0.392740 | 0.436403 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 47 | `val` | `adamic_adar` | 0.444931 | 0.495160 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 47 | `val` | `preferential_attachment` | 0.553584 | 0.544449 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 47 | `test` | `common_neighbors` | 0.489575 | 0.520421 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 47 | `test` | `jaccard` | 0.397912 | 0.439052 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 47 | `test` | `adamic_adar` | 0.455750 | 0.505315 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 47 | `test` | `preferential_attachment` | 0.562904 | 0.555254 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 47 | `val` | `logistic_regression` | 0.756905 | 0.724902 | 0.104759 | 0.68 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 47 | `test` | `logistic_regression` | 0.751827 | 0.722799 | 0.101523 | 0.68 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 47 | `val` | `random_forest` | 0.817966 | 0.833125 | 0.044844 | 25.23 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 47 | `test` | `random_forest` | 0.815130 | 0.831027 | 0.044741 | 25.23 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 47 | `val` | `hist_gradient_boosting` | 0.839084 | 0.852351 | 0.011577 | 4.14 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 47 | `test` | `hist_gradient_boosting` | 0.834524 | 0.849057 | 0.012158 | 4.14 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 48 | `val` | `common_neighbors` | 0.483882 | 0.515822 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 48 | `val` | `jaccard` | 0.394911 | 0.438966 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 48 | `val` | `adamic_adar` | 0.448856 | 0.499557 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 48 | `val` | `preferential_attachment` | 0.557495 | 0.548958 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 48 | `test` | `common_neighbors` | 0.486870 | 0.519161 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 48 | `test` | `jaccard` | 0.398430 | 0.440751 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 48 | `test` | `adamic_adar` | 0.452678 | 0.503792 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 48 | `test` | `preferential_attachment` | 0.559293 | 0.550949 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 48 | `val` | `logistic_regression` | 0.755450 | 0.724957 | 0.102585 | 0.76 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 48 | `test` | `logistic_regression` | 0.750347 | 0.719550 | 0.101010 | 0.76 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 48 | `val` | `random_forest` | 0.814479 | 0.830338 | 0.042569 | 23.81 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 48 | `test` | `random_forest` | 0.813056 | 0.829064 | 0.041604 | 23.81 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 48 | `val` | `hist_gradient_boosting` | 0.837971 | 0.851638 | 0.011721 | 3.94 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 48 | `test` | `hist_gradient_boosting` | 0.834274 | 0.848780 | 0.012837 | 3.94 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 49 | `val` | `common_neighbors` | 0.487679 | 0.516605 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 49 | `val` | `jaccard` | 0.397016 | 0.438353 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 49 | `val` | `adamic_adar` | 0.452258 | 0.500267 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 49 | `val` | `preferential_attachment` | 0.561449 | 0.551366 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 49 | `test` | `common_neighbors` | 0.487397 | 0.520159 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 49 | `test` | `jaccard` | 0.396513 | 0.438563 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 49 | `test` | `adamic_adar` | 0.453241 | 0.504770 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 49 | `test` | `preferential_attachment` | 0.561722 | 0.555126 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 49 | `val` | `logistic_regression` | 0.755434 | 0.727460 | 0.101545 | 0.78 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 49 | `test` | `logistic_regression` | 0.752322 | 0.723398 | 0.099608 | 0.78 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 49 | `val` | `random_forest` | 0.817216 | 0.832737 | 0.045285 | 24.20 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 49 | `test` | `random_forest` | 0.812899 | 0.828554 | 0.040867 | 24.20 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 49 | `val` | `hist_gradient_boosting` | 0.838658 | 0.852988 | 0.012435 | 3.94 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 49 | `test` | `hist_gradient_boosting` | 0.834788 | 0.849003 | 0.010808 | 3.94 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 50 | `val` | `common_neighbors` | 0.485706 | 0.516876 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 50 | `val` | `jaccard` | 0.398326 | 0.440416 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 50 | `val` | `adamic_adar` | 0.450840 | 0.500539 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 50 | `val` | `preferential_attachment` | 0.557553 | 0.548695 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 50 | `test` | `common_neighbors` | 0.488395 | 0.519035 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 50 | `test` | `jaccard` | 0.398193 | 0.439730 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 50 | `test` | `adamic_adar` | 0.454030 | 0.503196 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 50 | `test` | `preferential_attachment` | 0.560059 | 0.552520 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 50 | `val` | `logistic_regression` | 0.755051 | 0.724549 | 0.102950 | 0.57 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 50 | `test` | `logistic_regression` | 0.754205 | 0.724716 | 0.101226 | 0.57 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 50 | `val` | `random_forest` | 0.815305 | 0.831239 | 0.044658 | 24.37 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 50 | `test` | `random_forest` | 0.812908 | 0.828574 | 0.042276 | 24.37 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 50 | `val` | `hist_gradient_boosting` | 0.837504 | 0.851573 | 0.011925 | 4.03 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 50 | `test` | `hist_gradient_boosting` | 0.835538 | 0.849605 | 0.013193 | 4.03 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 51 | `val` | `common_neighbors` | 0.483065 | 0.515375 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 51 | `val` | `jaccard` | 0.394773 | 0.438565 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 51 | `val` | `adamic_adar` | 0.447938 | 0.498963 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 51 | `val` | `preferential_attachment` | 0.556650 | 0.547593 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 51 | `test` | `common_neighbors` | 0.488820 | 0.518976 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 51 | `test` | `jaccard` | 0.398475 | 0.439353 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 51 | `test` | `adamic_adar` | 0.454306 | 0.503193 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 51 | `test` | `preferential_attachment` | 0.562185 | 0.553688 |  | 0.00 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 51 | `val` | `logistic_regression` | 0.756965 | 0.726713 | 0.106262 | 0.62 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 51 | `test` | `logistic_regression` | 0.753081 | 0.721678 | 0.101714 | 0.62 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 51 | `val` | `random_forest` | 0.817481 | 0.833749 | 0.045713 | 24.37 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 51 | `test` | `random_forest` | 0.814518 | 0.830094 | 0.043414 | 24.37 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 51 | `val` | `hist_gradient_boosting` | 0.837969 | 0.852106 | 0.011237 | 4.42 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 51 | `test` | `hist_gradient_boosting` | 0.834345 | 0.848365 | 0.011677 | 4.42 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 42 | `val` | `common_neighbors` | 0.661363 | 0.686482 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 42 | `val` | `jaccard` | 0.620839 | 0.649922 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 42 | `val` | `adamic_adar` | 0.647634 | 0.692503 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 42 | `val` | `preferential_attachment` | 0.609414 | 0.610005 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 42 | `test` | `common_neighbors` | 0.661366 | 0.694742 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 42 | `test` | `jaccard` | 0.623527 | 0.658318 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 42 | `test` | `adamic_adar` | 0.649373 | 0.702332 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 42 | `test` | `preferential_attachment` | 0.607569 | 0.609555 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 42 | `val` | `logistic_regression` | 0.663999 | 0.677448 | 0.048245 | 0.34 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 42 | `test` | `logistic_regression` | 0.660820 | 0.680509 | 0.046945 | 0.34 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 42 | `val` | `random_forest` | 0.835731 | 0.848451 | 0.014167 | 12.32 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 42 | `test` | `random_forest` | 0.836416 | 0.850766 | 0.019535 | 12.32 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 42 | `val` | `hist_gradient_boosting` | 0.832026 | 0.844009 | 0.014144 | 2.53 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 42 | `test` | `hist_gradient_boosting` | 0.832951 | 0.846524 | 0.019422 | 2.53 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 43 | `val` | `common_neighbors` | 0.664000 | 0.694877 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 43 | `val` | `jaccard` | 0.626838 | 0.657236 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 43 | `val` | `adamic_adar` | 0.650009 | 0.701141 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 43 | `val` | `preferential_attachment` | 0.606618 | 0.608399 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 43 | `test` | `common_neighbors` | 0.664764 | 0.697419 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 43 | `test` | `jaccard` | 0.626715 | 0.659133 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 43 | `test` | `adamic_adar` | 0.652241 | 0.704799 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 43 | `test` | `preferential_attachment` | 0.610834 | 0.614507 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 43 | `val` | `logistic_regression` | 0.668140 | 0.682948 | 0.048499 | 0.34 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 43 | `test` | `logistic_regression` | 0.665767 | 0.683360 | 0.048740 | 0.34 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 43 | `val` | `random_forest` | 0.838225 | 0.850752 | 0.016834 | 12.42 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 43 | `test` | `random_forest` | 0.836953 | 0.850393 | 0.017676 | 12.42 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 43 | `val` | `hist_gradient_boosting` | 0.835530 | 0.847329 | 0.018004 | 2.57 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 43 | `test` | `hist_gradient_boosting` | 0.833628 | 0.846493 | 0.019535 | 2.57 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 44 | `val` | `common_neighbors` | 0.659507 | 0.687218 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 44 | `val` | `jaccard` | 0.620998 | 0.649442 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 44 | `val` | `adamic_adar` | 0.646877 | 0.693706 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 44 | `val` | `preferential_attachment` | 0.607521 | 0.608241 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 44 | `test` | `common_neighbors` | 0.667716 | 0.699692 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 44 | `test` | `jaccard` | 0.627258 | 0.659868 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 44 | `test` | `adamic_adar` | 0.655251 | 0.707283 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 44 | `test` | `preferential_attachment` | 0.611489 | 0.615881 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 44 | `val` | `logistic_regression` | 0.661496 | 0.676637 | 0.044499 | 0.34 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 44 | `test` | `logistic_regression` | 0.666140 | 0.684573 | 0.050396 | 0.34 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 44 | `val` | `random_forest` | 0.833743 | 0.846860 | 0.015018 | 13.25 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 44 | `test` | `random_forest` | 0.839440 | 0.852028 | 0.019837 | 13.25 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 44 | `val` | `hist_gradient_boosting` | 0.830859 | 0.843442 | 0.017596 | 2.60 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 44 | `test` | `hist_gradient_boosting` | 0.836141 | 0.848374 | 0.021363 | 2.60 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 45 | `val` | `common_neighbors` | 0.659607 | 0.691361 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 45 | `val` | `jaccard` | 0.621461 | 0.652063 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 45 | `val` | `adamic_adar` | 0.645208 | 0.697343 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 45 | `val` | `preferential_attachment` | 0.606307 | 0.609606 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 45 | `test` | `common_neighbors` | 0.665365 | 0.695787 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 45 | `test` | `jaccard` | 0.630478 | 0.661836 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 45 | `test` | `adamic_adar` | 0.652975 | 0.703357 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 45 | `test` | `preferential_attachment` | 0.604246 | 0.608476 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 45 | `val` | `logistic_regression` | 0.662887 | 0.680725 | 0.044096 | 0.32 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 45 | `test` | `logistic_regression` | 0.665156 | 0.683013 | 0.047350 | 0.32 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 45 | `val` | `random_forest` | 0.836136 | 0.849206 | 0.014881 | 12.47 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 45 | `test` | `random_forest` | 0.837491 | 0.850385 | 0.019079 | 12.47 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 45 | `val` | `hist_gradient_boosting` | 0.832830 | 0.845478 | 0.015646 | 2.51 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 45 | `test` | `hist_gradient_boosting` | 0.833771 | 0.846272 | 0.020797 | 2.51 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 46 | `val` | `common_neighbors` | 0.664299 | 0.693500 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 46 | `val` | `jaccard` | 0.623635 | 0.651626 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 46 | `val` | `adamic_adar` | 0.650156 | 0.699376 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 46 | `val` | `preferential_attachment` | 0.612653 | 0.614495 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 46 | `test` | `common_neighbors` | 0.661249 | 0.690956 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 46 | `test` | `jaccard` | 0.623253 | 0.653967 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 46 | `test` | `adamic_adar` | 0.648585 | 0.698209 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 46 | `test` | `preferential_attachment` | 0.608212 | 0.606993 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 46 | `val` | `logistic_regression` | 0.669781 | 0.682914 | 0.049273 | 0.35 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 46 | `test` | `logistic_regression` | 0.663013 | 0.677713 | 0.048810 | 0.35 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 46 | `val` | `random_forest` | 0.839004 | 0.851040 | 0.017594 | 12.70 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 46 | `test` | `random_forest` | 0.838421 | 0.850987 | 0.019583 | 12.70 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 46 | `val` | `hist_gradient_boosting` | 0.835603 | 0.847395 | 0.016946 | 2.68 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 46 | `test` | `hist_gradient_boosting` | 0.834533 | 0.846745 | 0.019685 | 2.68 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 47 | `val` | `common_neighbors` | 0.660913 | 0.690008 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 47 | `val` | `jaccard` | 0.626049 | 0.655839 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 47 | `val` | `adamic_adar` | 0.647042 | 0.695936 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 47 | `val` | `preferential_attachment` | 0.604362 | 0.604119 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 47 | `test` | `common_neighbors` | 0.665793 | 0.695891 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 47 | `test` | `jaccard` | 0.629016 | 0.656627 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 47 | `test` | `adamic_adar` | 0.652965 | 0.703356 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 47 | `test` | `preferential_attachment` | 0.607887 | 0.610559 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 47 | `val` | `logistic_regression` | 0.664940 | 0.681490 | 0.048273 | 0.33 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 47 | `test` | `logistic_regression` | 0.663632 | 0.680685 | 0.050648 | 0.33 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 47 | `val` | `random_forest` | 0.835081 | 0.847899 | 0.016311 | 12.67 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 47 | `test` | `random_forest` | 0.837291 | 0.850678 | 0.017811 | 12.67 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 47 | `val` | `hist_gradient_boosting` | 0.831557 | 0.843643 | 0.016187 | 2.55 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 47 | `test` | `hist_gradient_boosting` | 0.833392 | 0.845966 | 0.018686 | 2.55 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 48 | `val` | `common_neighbors` | 0.664909 | 0.693749 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 48 | `val` | `jaccard` | 0.626383 | 0.653512 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 48 | `val` | `adamic_adar` | 0.651176 | 0.699741 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 48 | `val` | `preferential_attachment` | 0.609441 | 0.610593 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 48 | `test` | `common_neighbors` | 0.665515 | 0.695683 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 48 | `test` | `jaccard` | 0.627379 | 0.658703 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 48 | `test` | `adamic_adar` | 0.652559 | 0.703055 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 48 | `test` | `preferential_attachment` | 0.610305 | 0.612911 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 48 | `val` | `logistic_regression` | 0.666864 | 0.681835 | 0.048050 | 0.33 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 48 | `test` | `logistic_regression` | 0.665511 | 0.682336 | 0.048471 | 0.33 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 48 | `val` | `random_forest` | 0.837440 | 0.849410 | 0.015711 | 12.06 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 48 | `test` | `random_forest` | 0.838800 | 0.851225 | 0.018717 | 12.06 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 48 | `val` | `hist_gradient_boosting` | 0.833852 | 0.844929 | 0.017616 | 2.55 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 48 | `test` | `hist_gradient_boosting` | 0.835324 | 0.847230 | 0.020408 | 2.55 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 49 | `val` | `common_neighbors` | 0.660413 | 0.691877 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 49 | `val` | `jaccard` | 0.622867 | 0.653171 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 49 | `val` | `adamic_adar` | 0.647106 | 0.698011 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 49 | `val` | `preferential_attachment` | 0.607424 | 0.610019 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 49 | `test` | `common_neighbors` | 0.662692 | 0.693974 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 49 | `test` | `jaccard` | 0.624853 | 0.657239 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 49 | `test` | `adamic_adar` | 0.650501 | 0.701581 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 49 | `test` | `preferential_attachment` | 0.607804 | 0.612984 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 49 | `val` | `logistic_regression` | 0.666051 | 0.683039 | 0.047352 | 0.33 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 49 | `test` | `logistic_regression` | 0.663756 | 0.681081 | 0.047716 | 0.33 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 49 | `val` | `random_forest` | 0.837010 | 0.850990 | 0.016952 | 13.23 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 49 | `test` | `random_forest` | 0.839000 | 0.852090 | 0.019174 | 13.23 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 49 | `val` | `hist_gradient_boosting` | 0.833142 | 0.846491 | 0.015646 | 2.80 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 49 | `test` | `hist_gradient_boosting` | 0.834608 | 0.847240 | 0.019009 | 2.80 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 50 | `val` | `common_neighbors` | 0.659811 | 0.692248 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 50 | `val` | `jaccard` | 0.620445 | 0.653672 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 50 | `val` | `adamic_adar` | 0.646063 | 0.698596 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 50 | `val` | `preferential_attachment` | 0.607254 | 0.610062 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 50 | `test` | `common_neighbors` | 0.664218 | 0.695819 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 50 | `test` | `jaccard` | 0.627631 | 0.657818 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 50 | `test` | `adamic_adar` | 0.652248 | 0.703506 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 50 | `test` | `preferential_attachment` | 0.607975 | 0.610366 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 50 | `val` | `logistic_regression` | 0.665112 | 0.682615 | 0.047696 | 0.34 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 50 | `test` | `logistic_regression` | 0.662169 | 0.679908 | 0.050268 | 0.34 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 50 | `val` | `random_forest` | 0.836460 | 0.849712 | 0.015589 | 12.61 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 50 | `test` | `random_forest` | 0.838166 | 0.851546 | 0.019744 | 12.61 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 50 | `val` | `hist_gradient_boosting` | 0.833015 | 0.845125 | 0.015337 | 2.48 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 50 | `test` | `hist_gradient_boosting` | 0.834402 | 0.846620 | 0.020904 | 2.48 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 51 | `val` | `common_neighbors` | 0.662669 | 0.692366 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 51 | `val` | `jaccard` | 0.624633 | 0.653182 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 51 | `val` | `adamic_adar` | 0.649068 | 0.698410 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 51 | `val` | `preferential_attachment` | 0.609908 | 0.612561 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 51 | `test` | `common_neighbors` | 0.668943 | 0.698727 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 51 | `test` | `jaccard` | 0.629570 | 0.659650 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 51 | `test` | `adamic_adar` | 0.656038 | 0.705722 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 51 | `test` | `preferential_attachment` | 0.610997 | 0.613822 |  | 0.00 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 51 | `val` | `logistic_regression` | 0.667641 | 0.682420 | 0.050549 | 0.33 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 51 | `test` | `logistic_regression` | 0.669545 | 0.686123 | 0.052440 | 0.33 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 51 | `val` | `random_forest` | 0.835643 | 0.849236 | 0.017906 | 12.16 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 51 | `test` | `random_forest` | 0.837238 | 0.850067 | 0.018620 | 12.16 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 51 | `val` | `hist_gradient_boosting` | 0.832092 | 0.844969 | 0.017697 | 2.57 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 51 | `test` | `hist_gradient_boosting` | 0.833964 | 0.845948 | 0.020337 | 2.57 |
