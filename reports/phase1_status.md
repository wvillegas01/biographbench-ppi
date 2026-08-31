# Phase 1 Status: PPI Multi-Seed and Negative Sampling

## Completed

- Generated 120 compressed split contracts:
  - 4 PPI datasets
  - 3 negative-sampling regimes: `random`, `degree_matched`, `two_hop`
  - 10 seeds: 42-51
- Validated all split manifests:
  - 120/120 present
  - 12 dataset/strategy contexts
  - 10 seeds per context
  - 0 split errors
- Ran classical Phase 1 baselines for all contexts:
  - common neighbors
  - Jaccard
  - Adamic-Adar
  - preferential attachment
  - logistic regression
  - random forest
  - histogram gradient boosting
- Ran a node2vec-compatible random-walk embedding baseline for all contexts:
  - 4 PPI datasets
  - 3 negative-sampling regimes
  - 10 seeds
  - validation and test splits
- Produced 1680 raw classical-baseline result rows:
  - 4 datasets x 3 strategies x 10 seeds x 7 models x 2 splits
- Produced 240 node2vec-compatible raw result rows:
  - 4 datasets x 3 strategies x 10 seeds x 1 model x 2 splits
- Generated statistical summaries:
  - mean
  - standard deviation
  - 95% confidence intervals
  - paired Wilcoxon tests versus HGB
  - paired effect size

## Key Finding

Degree-matched negatives substantially reduce PPI link-prediction performance compared with random negatives. This validates the critical concern that uniformly sampled non-edges make the task structurally easier.

| Dataset | HGB random AUPRC | HGB degree-matched AUPRC | Absolute drop | Relative drop |
|---|---:|---:|---:|---:|
| `biogrid_human_physical` | 0.942885 | 0.770470 | 0.172415 | 18.3% |
| `biogrid_human_physical_no_string_overlap` | 0.942256 | 0.683591 | 0.258665 | 27.5% |
| `string_human_physical_no_biogrid_overlap` | 0.964154 | 0.915642 | 0.048512 | 5.0% |
| `string_human_physical_v12` | 0.950261 | 0.881324 | 0.068937 | 7.3% |

## Distance-Two Hard Negatives

The `two_hop` regime samples non-edges that share at least one neighbor in the training-positive graph. This gives a distance-aware hard-negative protocol without using validation/test positives to define negative hardness.

| Dataset | HGB two-hop AUPRC | RF two-hop AUPRC | node2vec two-hop AUPRC |
|---|---:|---:|---:|
| `biogrid_human_physical` | 0.774382 | 0.772939 | 0.638958 |
| `biogrid_human_physical_no_string_overlap` | 0.849272 | 0.830226 | 0.604805 |
| `string_human_physical_no_biogrid_overlap` | 0.846741 | 0.851016 | 0.735606 |
| `string_human_physical_v12` | 0.856382 | 0.857063 | 0.730962 |

## node2vec-compatible Baseline

The random-walk embedding baseline adds a stronger non-GNN comparator than local heuristics alone. HGB and RF remain stronger in most contexts, but node2vec-compatible embeddings are competitive in the harder BioGRID no-STRING degree-matched setting.

| Dataset | Negatives | node2vec AUPRC | Best classical AUPRC |
|---|---|---:|---:|
| `biogrid_human_physical` | `random` | 0.873371 | 0.942885 |
| `biogrid_human_physical` | `degree_matched` | 0.697622 | 0.771189 |
| `biogrid_human_physical` | `two_hop` | 0.638958 | 0.774382 |
| `biogrid_human_physical_no_string_overlap` | `random` | 0.898468 | 0.942256 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 0.724663 | 0.686539 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 0.604805 | 0.849272 |
| `string_human_physical_no_biogrid_overlap` | `random` | 0.940531 | 0.964154 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 0.903597 | 0.915642 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 0.735606 | 0.851016 |
| `string_human_physical_v12` | `random` | 0.876736 | 0.950261 |
| `string_human_physical_v12` | `degree_matched` | 0.804031 | 0.881324 |
| `string_human_physical_v12` | `two_hop` | 0.730962 | 0.857063 |

## Outputs

- Splits:
  - `data/processed/phase1_ppi_multiseed_splits/`
- Raw results:
  - `results/phase1/ppi_link_prediction_baselines.csv`
  - `results/phase1/ppi_node2vec_link_prediction.csv`
- Statistical report:
  - `reports/phase1_ppi_statistics.md`
  - `reports/phase1_ppi_statistics.json`
  - `reports/phase1_ppi_node2vec_statistics.md`
  - `reports/phase1_ppi_node2vec_statistics.json`
- Manuscript-oriented summary:
  - `Articulo/phase1_ppi_negative_sampling_impact.md`
  - `Articulo/phase1_ppi_negative_sampling_impact.csv`
  - `Articulo/phase1_ppi_model_family_comparison.md`
  - `Articulo/phase1_ppi_model_family_comparison.csv`

## Remaining Within Phase 1

- Convert Phase 1 results into updated manuscript tables and figures.
