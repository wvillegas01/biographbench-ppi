# BioGraphBench-PPI

BioGraphBench-PPI is an audit-first benchmark package for protein-protein interaction link prediction. Its main claim is not that one model family solves PPI prediction, but that reported link-prediction performance depends strongly on the sampled-nonedge contract used to define the task.

The repository contains scripts, manifests, validation checks, baseline outputs, statistical summaries, and manuscript figure/table generation code for the BioGraphBench-PPI study.

## Scope

The current benchmark focuses on four PPI link-prediction tasks derived from STRING and BioGRID:

- STRING human physical interactions;
- BioGRID human physical interactions;
- BioGRID with STRING-overlap pairs removed;
- STRING with BioGRID-overlap pairs removed.

Each task is evaluated with 10 seeds and three sampled-nonedge contracts: random, degree-matched, and two-hop.

## Repository Structure

- `src/biographbench/`: importable Python package for features, splits, I/O, and validation.
- `scripts/`: acquisition, canonicalization, split generation, baseline execution, validation, and reporting scripts.
- `tests/`: automated tests for split and manifest behavior.
- `data/manifests/`: source-data manifests.
- `data/processed/`: machine-readable processed-data manifests; large split CSV files are not versioned in Git.
- `results/`: retained raw benchmark result tables.
- `reports/`: audit reports and statistical summaries.
- `Articulo/`: manuscript tables, figures, captions, and result-section material.

## Installation

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e .[dev,gnn,obnb]
```

## Validation

```powershell
make validate
make test
```

## Baselines

Classical and random-walk baselines are retained in `results/phase1`.

The reviewer-requested GCN link-prediction extension is implemented as:

```powershell
python scripts/run_phase1_ppi_gcn_link_prediction.py --resume
```

The script builds the propagation graph exclusively from train-positive edges, derives node features only from that graph, and evaluates AUROC, AUPRC, Brier score, NLL, ECE-10, training time, and inference time.

## Data Availability

Raw STRING, BioGRID, and OBNB files must be obtained from their original providers according to their terms. This repository includes manifests and scripts required to recreate the processed artifacts. Large split files should be attached to the GitHub release or archived in Zenodo.

## Citation

Citation metadata is provided in `CITATION.cff`. Replace repository and DOI placeholders after the public GitHub repository and Zenodo release are created.
