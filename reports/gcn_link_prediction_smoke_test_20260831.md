# GCN PPI Link-Prediction Smoke Test

Fecha: 2026-08-31

This smoke test verifies that the GCN-PPI script can load Phase 1 PPI splits, build the train-positive propagation graph, train a dot-product GCN, and report AUROC/AUPRC/calibration metrics. It used sampled train/evaluation pairs and must not be treated as manuscript evidence.

| Dataset | Negatives | Seed | Split | AUPRC | AUROC | Brier | ECE-10 | Train s |
|---|---|---:|---|---:|---:|---:|---:|---:|
| `string_human_physical_no_biogrid_overlap` | `random` | 42 | `val` | 0.520306 | 0.538972 | 0.498736 | 0.499298 | 0.21 |
| `string_human_physical_no_biogrid_overlap` | `random` | 42 | `test` | 0.519759 | 0.537950 | 0.499542 | 0.499762 | 0.21 |
