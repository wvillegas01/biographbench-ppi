# BioGRID Human Physical Pilot Link Prediction Split

Fecha: 2026-08-04

## Objetivo

Construir un split piloto reproducible para BioGRID humano fisico filtrado, sin entrenar modelos todavia.

## Politica aplicada

1. Usar pares Entrez no dirigidos ya filtrados a interacciones fisicas humano-humano.
2. Preservar un bosque generador para que train conserve los componentes originales.
3. Generar negativos desde pares Entrez no conectados en el grafo completo.
4. Guardar pares siempre ordenados para evitar fuga inversa.
5. Usar seed fija `42`.

## Conteos

| Split | Positivos | Negativos |
|---|---:|---:|
| Train | 769225 | 769225 |
| Validation | 96153 | 96153 |
| Test | 96153 | 96153 |

## Checks

| Check | Resultado |
|---|---|
| Overlap entre splits | OK |
| Self-loops | OK |
| Fuga inversa por pares ordenados | OK |
| Componentes originales | 1 |
| Componentes en train | 1 |
| Componentes preservados | True |

Errores detectados:

```text
None
```

## Archivos generados

- `train_pos.csv`
- `val_pos.csv`
- `test_pos.csv`
- `train_neg.csv`
- `val_neg.csv`
- `test_neg.csv`
- `split_manifest.json`

## Nota metodologica

Este split permite comparar baselines iniciales contra STRING en una segunda red PPI homogenea. Antes de declarar independencia biologica entre ambos datasets, falta medir solapamiento entre BioGRID Entrez y STRING protein IDs mediante una tabla de mapeo.
