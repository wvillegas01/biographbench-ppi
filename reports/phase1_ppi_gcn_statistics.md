# Phase 1 PPI GCN Statistics

Test split only. GCN propagation uses train-positive graph only. Training used 10 epochs and up to 100,000 positive and 100,000 negative training pairs per seed.

| Dataset | Negatives | n | AUPRC mean | SD | CI95 low | CI95 high | AUROC mean | Brier | ECE-10 | Train s |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `biogrid_human_physical` | `degree_matched` | 10 | 0.499964 | 0.000018 | 0.499950 | 0.499977 | 0.499927 | 0.500000 | 0.500000 | 4.53 |
| `biogrid_human_physical` | `random` | 10 | 0.525598 | 0.010278 | 0.518245 | 0.532951 | 0.548375 | 0.499650 | 0.499817 | 3.99 |
| `biogrid_human_physical` | `two_hop` | 10 | 0.500099 | 0.000086 | 0.500037 | 0.500160 | 0.500198 | 0.499998 | 0.499999 | 5.25 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 10 | 0.500015 | 0.000070 | 0.499965 | 0.500066 | 0.500030 | 0.499997 | 0.499997 | 2.97 |
| `biogrid_human_physical_no_string_overlap` | `random` | 10 | 0.590818 | 0.025546 | 0.572544 | 0.609093 | 0.652224 | 0.497361 | 0.498597 | 3.65 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 10 | 0.501155 | 0.000571 | 0.500747 | 0.501564 | 0.502301 | 0.499940 | 0.499965 | 3.36 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 10 | 0.500344 | 0.000596 | 0.499918 | 0.500770 | 0.500539 | 0.499562 | 0.499337 | 1.78 |
| `string_human_physical_no_biogrid_overlap` | `random` | 10 | 0.717051 | 0.030608 | 0.695155 | 0.738946 | 0.792237 | 0.475688 | 0.485954 | 2.27 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 10 | 0.515327 | 0.005404 | 0.511461 | 0.519193 | 0.528014 | 0.498846 | 0.498883 | 1.87 |
| `string_human_physical_v12` | `degree_matched` | 10 | 0.499725 | 0.000105 | 0.499650 | 0.499800 | 0.499452 | 0.499996 | 0.499994 | 4.25 |
| `string_human_physical_v12` | `random` | 10 | 0.534888 | 0.013599 | 0.525160 | 0.544617 | 0.564563 | 0.498958 | 0.499430 | 3.46 |
| `string_human_physical_v12` | `two_hop` | 10 | 0.500621 | 0.000461 | 0.500291 | 0.500951 | 0.501235 | 0.499957 | 0.499969 | 3.77 |
