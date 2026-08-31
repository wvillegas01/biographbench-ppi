# Reproducibility Guide

## Environment

Recommended setup:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e .[dev,gnn,obnb]
```

The manuscript experiments were prepared with pinned Python packages listed in `requirements-lock.txt`. GNN pilots require PyTorch.

## Core Audit Pipeline

```powershell
make validate
make test
```

## PPI Link-Prediction Baselines

Classical and node2vec-compatible baselines:

```powershell
python scripts/run_phase1_ppi_node2vec.py --resume
```

GCN link-prediction baseline prepared for reviewer-requested extension:

```powershell
python scripts/run_phase1_ppi_gcn_link_prediction.py --resume
```

The GCN script builds the propagation graph only from train-positive edges, computes node features from the same graph, and evaluates the same PPI datasets, negative-sampling contracts, seeds, and metrics used by the retained baselines.

## Article Tables And Figures

```powershell
python Articulo/generate_figures.py
```

Generated outputs are stored under `Articulo/figures` and `Articulo/tables`.
