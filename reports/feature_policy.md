# Feature Policy

Fecha: 2026-08-05

## Decision

La feature principal inicial para `obnb_biogrid_gobp` sera `one_hot_log_degree`, acompanada por una feature constante como control.

## Politicas implementadas

| Feature | Dimension | Uso |
|---|---:|---|
| `constant` | 1 | Control sin informacion estructural explicita |
| `degree` | 1 | Baseline compacto con grado crudo |
| `log_degree` | 1 | Baseline compacto con grado suavizado |
| `one_hot_log_degree` | 9 | Feature principal inicial |

Formula:

```text
bin = min(floor(log2(degree + 1)), 8)
x = one_hot(bin)
```

## Distribucion de bins

| Bin | Nodos |
|---:|---:|
| 0 | 0 |
| 1 | 2386 |
| 2 | 1965 |
| 3 | 2387 |
| 4 | 2839 |
| 5 | 3263 |
| 6 | 3419 |
| 7 | 2206 |
| 8+ | 1300 |

## Degree Summary

- Min: `1`
- Median: `33.0`
- Mean: `78.6638`
- Max: `4145`

## Leakage Policy

Para este piloto de OBNB, el split es por nodos con study bias, no por aristas retenidas. Por tanto, el grafo OBNB se trata como entrada estructural del benchmark y el grado se calcula sobre ese grafo.

Para tareas de link prediction o cualquier split con aristas retenidas, esta regla cambia: toda feature estructural debe calcularse solo sobre el grafo de entrenamiento.

## Archivos

- `C:\Users\wilop\Dropbox\MPDI\2026\BioGraphBench\Auditoria\data\processed\obnb_biogrid_gobp\features.npz`
- `C:\Users\wilop\Dropbox\MPDI\2026\BioGraphBench\Auditoria\data\processed\obnb_biogrid_gobp\feature_manifest.json`
