# Phase 1 PPI Negative-Sampling Impact

All values are test AUPRC means over 10 seeds. Degree-matched negatives preserve an approximate endpoint degree-bin distribution of positive pairs.

| Dataset | HGB random | HGB degree-matched | Absolute drop | Relative drop | RF random | RF degree-matched |
|---|---:|---:|---:|---:|---:|---:|
| `biogrid_human_physical` | 0.942885 | 0.770470 | 0.172415 | 18.3% | 0.942270 | 0.771189 |
| `biogrid_human_physical_no_string_overlap` | 0.942256 | 0.683591 | 0.258665 | 27.5% | 0.940877 | 0.686539 |
| `string_human_physical_no_biogrid_overlap` | 0.964154 | 0.915642 | 0.048512 | 5.0% | 0.963660 | 0.915105 |
| `string_human_physical_v12` | 0.950261 | 0.881324 | 0.068937 | 7.3% | 0.949844 | 0.880517 |

## Manuscript Takeaway

Across all four PPI tasks, replacing uniformly sampled random negatives with degree-matched negatives reduced HGB test AUPRC. The reduction was modest for STRING without BioGRID but substantial for BioGRID tasks, especially BioGRID without STRING. This directly supports the revised article thesis: high PPI link-prediction performance under balanced random negatives partly reflects topological separability induced by the negative-sampling protocol.
