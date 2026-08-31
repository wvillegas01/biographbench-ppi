# Node Classification Threshold Tuning

Fecha: 2026-08-05

Umbrales por tarea seleccionados en validation para maximizar F1 y aplicados a test.

| Modelo | Split | Macro AUROC | Macro AUPRC | Micro-F1 | Macro-F1 | Precision | Recall | Threshold median |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| `logistic_regression` | `val` | 0.570703 | 0.019143 | 0.035027 | 0.047150 | 0.018083 | 0.555940 | 0.5150 |
| `logistic_regression` | `test` | 0.530988 | 0.014365 | 0.025313 | 0.024530 | 0.013053 | 0.416216 | 0.5150 |
| `mlp` | `val` | 0.515486 | 0.016806 | 0.028097 | 0.038796 | 0.014350 | 0.668397 | 0.0200 |
| `mlp` | `test` | 0.488016 | 0.012944 | 0.021706 | 0.024501 | 0.011027 | 0.687838 | 0.0200 |
| `gcn` | `val` | 0.506155 | 0.019271 | 0.031475 | 0.037644 | 0.016162 | 0.598616 | 0.4200 |
| `gcn` | `test` | 0.493559 | 0.015926 | 0.021249 | 0.021220 | 0.010814 | 0.605405 | 0.4200 |
