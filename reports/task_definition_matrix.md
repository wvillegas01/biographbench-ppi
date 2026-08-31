# BioGraphBench Task Definition Matrix

Date: 2026-08-05

## Purpose

This matrix defines the current MVP benchmark tasks that are sufficiently audited to be used in the BioGraphBench article draft.

The organizing principle is:

> BioGraphBench does not start with models; it starts with trust.

The table below separates accepted MVP tasks from candidates that remain useful but are not yet benchmark-ready.

## Accepted MVP Tasks

| Task ID | Dataset | Type | Nodes | Target | Split | Features/Input | Metrics | Best Current Baseline | Paper Role |
|---|---|---|---:|---|---|---|---|---|---|
| `lp_string_physical` | `string_human_physical_v12` | Binary undirected link prediction | 18,767 | Missing physical PPI | 80/10/10, spanning-forest train protection | Train-graph pair heuristics | AUROC, AUPRC, Brier, NLL, ECE10 | HistGradientBoosting: AUROC 0.941380, AUPRC 0.950931 | Main task |
| `lp_biogrid_physical` | `biogrid_human_physical` | Binary undirected link prediction | 20,376 | Missing physical PPI | 80/10/10, spanning-forest train protection | Train-graph pair heuristics | AUROC, AUPRC, Brier, NLL, ECE10 | HistGradientBoosting: AUROC 0.942187, AUPRC 0.943193 | Main task |
| `lp_biogrid_no_string_overlap` | `biogrid_human_physical_no_string_overlap` | Binary undirected link prediction | 19,591 | Missing physical PPI after STRING overlap removal | 80/10/10, spanning-forest train protection | Train-graph pair heuristics | AUROC, AUPRC, Brier, NLL, ECE10 | HistGradientBoosting: AUROC 0.944687, AUPRC 0.942283 | Overlap ablation |
| `lp_string_no_biogrid_overlap` | `string_human_physical_no_biogrid_overlap` | Binary undirected link prediction | 16,781 | Missing physical PPI after BioGRID overlap removal | 80/10/10, spanning-forest train protection | Train-graph pair heuristics | AUROC, AUPRC, Brier, NLL, ECE10 | HistGradientBoosting: AUROC 0.955332, AUPRC 0.963088 | Overlap ablation |
| `nc_obnb_biogrid_gobp` | `obnb_biogrid_gobp` | Multilabel node classification | 19,765 | GOBP labels per gene | OBNB train/val/test node masks | `constant`, `degree`, `log_degree`, `one_hot_log_degree` | Macro AUROC, Macro AUPRC, Micro-F1, Macro-F1 | Threshold-tuned logistic regression: AUROC 0.530988, AUPRC 0.014365, Micro-F1 0.025313 | Secondary challenge task |

## Link Prediction Protocol

The accepted link-prediction tasks share one reproducible policy:

- undirected positive edges;
- seeded 80/10/10 split;
- validation and test positives sampled only from non-forest edges;
- spanning forest protected in training positives;
- balanced negative sampling;
- negatives sampled from node pairs absent from the full positive graph;
- no overlap between positive/negative and train/validation/test splits;
- no self-loops;
- ordered undirected pairs;
- train graph preserves the original number of connected components.

This protocol is now implemented in:

- `src/biographbench/splits/link_prediction.py`

## Feature Protocol

The accepted node-classification task uses explicitly documented structural features:

- `constant`;
- `degree`;
- `log_degree`;
- `one_hot_log_degree`;
- `log_degree_bin`.

For `obnb_biogrid_gobp`, degree features are computed from the OBNB benchmark graph because the split is over nodes rather than an edge-holdout protocol. For any future edge-holdout task, structural features must be computed from the training graph only.

This protocol is now implemented in:

- `src/biographbench/features/structural.py`

## Baseline Interpretation

The current MVP establishes a strong but cautious baseline story:

- PPI link prediction is highly structured; classical heuristics and supervised models over pair heuristics are already strong.
- The overlap-aware ablations are essential because STRING and BioGRID share 423,528 Entrez-mapped pairs.
- Node classification is much harder and strongly imbalanced; threshold tuning and AUPRC are more informative than F1 at a fixed 0.5 threshold.
- The GCN pilot verifies infrastructure but should not yet be framed as a final competitive result.

## Candidate Tasks Not Yet Accepted

| Candidate | Current Status | Reason Not Accepted Yet | Next Action |
|---|---|---|---|
| `openbiolink2020_hq_directed` | Downloaded and quality audited | Negatives include 54 same-relation reverse hits against positives; inverse-relation semantics need review | Build relation-inverse audit and filtered KG protocol |
| `ogbl_biokg` | Download URL verified | Not downloaded or locally processed in this MVP | Download, inspect, audit official split leakage |
| `obnb_string_gobp` | Candidate identified | Not exported or compared against OBNB BioGRID+GOBP yet | Export and compare feasibility/readiness |

## Decision

The current article should use five accepted MVP tasks:

- two main PPI link-prediction tasks;
- two overlap-aware PPI ablation tasks;
- one harder multilabel node-classification task.

This is enough to support the paper's core claim: BioGraphBench is primarily an auditable benchmark design, not a race to train a fast GNN.
