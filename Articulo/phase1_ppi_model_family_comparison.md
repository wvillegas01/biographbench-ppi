# Phase 1 PPI Model-Family Comparison

All values are test AUPRC means over 10 seeds. The node2vec-compatible baseline uses auditable random-walk embeddings with a logistic edge decoder.

| Dataset | Negatives | Logistic regression | Random forest | HGB | node2vec-compatible |
|---|---|---:|---:|---:|---:|
| `biogrid_human_physical` | `degree_matched` | 0.716246 | 0.771189 | 0.770470 | 0.697622 |
| `biogrid_human_physical` | `random` | 0.934672 | 0.942270 | 0.942885 | 0.873371 |
| `biogrid_human_physical` | `two_hop` | 0.654315 | 0.772939 | 0.774382 | 0.638958 |
| `biogrid_human_physical_no_string_overlap` | `degree_matched` | 0.593875 | 0.686539 | 0.683591 | 0.724663 |
| `biogrid_human_physical_no_string_overlap` | `random` | 0.932833 | 0.940877 | 0.942256 | 0.898468 |
| `biogrid_human_physical_no_string_overlap` | `two_hop` | 0.722290 | 0.830226 | 0.849272 | 0.604805 |
| `string_human_physical_no_biogrid_overlap` | `degree_matched` | 0.888887 | 0.915105 | 0.915642 | 0.903597 |
| `string_human_physical_no_biogrid_overlap` | `random` | 0.959790 | 0.963660 | 0.964154 | 0.940531 |
| `string_human_physical_no_biogrid_overlap` | `two_hop` | 0.681930 | 0.851016 | 0.846741 | 0.735606 |
| `string_human_physical_v12` | `degree_matched` | 0.864446 | 0.880517 | 0.881324 | 0.804031 |
| `string_human_physical_v12` | `random` | 0.945644 | 0.949844 | 0.950261 | 0.876736 |
| `string_human_physical_v12` | `two_hop` | 0.752718 | 0.857063 | 0.856382 | 0.730962 |

## Manuscript Takeaway

The added random-walk baseline strengthens the comparison because it does not rely only on local handcrafted edge scores. HGB and RF remain strongest in most STRING and complete BioGRID settings, but node2vec-compatible embeddings become competitive under the harder BioGRID no-STRING degree-matched regime. This pattern supports a focused PPI article: model rankings are conditional on the graph source and negative-sampling contract, not merely on the nominal task definition.
