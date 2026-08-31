# BioGraphBench Article Results Plan

Date: 2026-08-05

## Working Structure

The article will use five main sections:

1. Introduction
2. Benchmark Audit and Design
3. Accepted Tasks and Reproducibility Protocol
4. Baseline Results
5. Discussion, Limitations, and Roadmap

## Section 1: Introduction

Purpose:
motivate why BioGraphBench is needed and state the central claim: trustworthy biomedical graph benchmarks require auditability before model training.

Main points:

- biomedical graph learning benchmarks can hide leakage through split policy, negative sampling, relation inverses, or dataset overlap;
- BioGraphBench prioritizes reproducibility and leakage controls;
- the MVP defines five accepted tasks with validated artifacts;
- link prediction baselines are already strong, so future GNN claims need serious comparisons;
- node classification remains difficult and imbalanced.

Planned table:

- Table 1: Contributions.

Planned figure:

- Figure 1: BioGraphBench audit-first workflow.

## Section 2: Benchmark Audit and Design

Purpose:
show that accepted tasks come from a dataset audit rather than arbitrary dataset selection.

Main points:

- compare existing benchmark coverage;
- document candidate datasets and inclusion/exclusion decisions;
- highlight OpenBioLink as useful but not yet accepted because inverse-relation semantics need review;
- highlight STRING/BioGRID overlap as a reason for ablation tasks.

Planned tables:

- Table 2: Existing benchmark coverage and BioGraphBench gap.
- Table 3: Dataset candidate audit.

Planned figure:

- Figure 2: Dataset audit pipeline.

## Section 3: Accepted Tasks and Reproducibility Protocol

Purpose:
define the official MVP benchmark tasks.

Accepted tasks:

- `lp_string_physical`
- `lp_biogrid_physical`
- `lp_biogrid_no_string_overlap`
- `lp_string_no_biogrid_overlap`
- `nc_obnb_biogrid_gobp`

Planned tables:

- Table 4: Accepted BioGraphBench MVP tasks.
- Table 5: Leakage and reproducibility controls.

Planned figure:

- Figure 3: STRING-BioGRID overlap and ablation design.

## Section 4: Baseline Results

Purpose:
present the numerical evidence from the MVP.

Subsection 4.1:
Link prediction baselines.

Main message:
PPI link prediction is strongly shaped by graph topology. Classical heuristics and supervised pair-heuristic baselines already set a high bar.

Subsection 4.2:
Node classification baselines.

Main message:
OBNB BioGRID+GOBP is difficult and highly imbalanced. Fixed-threshold F1 is weak; threshold tuning and AUPRC are more informative.

Planned tables:

- Table 6: Best link prediction results.
- Table 7: Node classification results.

Planned figures:

- Figure 4: Link prediction AUROC/AUPRC by task.
- Figure 5: Node classification challenge.

## Section 5: Discussion, Limitations, and Roadmap

Purpose:
interpret the findings cautiously and define what remains before a final benchmark release.

Main points:

- the current MVP supports an audit-first benchmark claim;
- current results should not be framed as final GNN performance;
- multiple seeds and stronger modular GNN baselines are still needed;
- OpenBioLink and OGB BioKG remain future KG extensions;
- biological external features require separate license and leakage audits.

Planned table:

- Table 8: Limitations and next actions.

Optional planned figure:

- Figure 6: BioGraphBench roadmap.

## Current Writing Decision

The manuscript should be framed as:

> BioGraphBench: Auditing Reproducibility and Leakage in Biomedical Graph Learning Benchmarks

The article should not be framed as a model-performance paper yet. The strongest contribution is the benchmark audit, task definition, leakage controls, reproducible artifacts, and baseline evidence.
