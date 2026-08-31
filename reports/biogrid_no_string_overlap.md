# BioGRID No-STRING-Overlap Ablation

Fecha: 2026-08-04

## Objetivo

Crear una variante de BioGRID humano fisico filtrado excluyendo todos los pares Entrez que tambien aparecen en STRING human physical tras mapeo explicito a Entrez.

## Conteos

| Medida | Valor |
|---|---:|
| Aristas BioGRID filtradas originales | 961531 |
| Aristas removidas por solapamiento STRING | 423528 |
| Aristas restantes | 538003 |
| Nodos restantes | 19591 |

## Split piloto

| Split | Positivos | Negativos |
|---|---:|---:|
| Train | 430403 | 430403 |
| Validation | 53800 | 53800 |
| Test | 53800 | 53800 |

## Checks

- Errores de split: `None`
- Componentes originales: `4`
- Componentes en train: `4`
- Componentes preservados: `True`

## Decision

Esta ablation permite evaluar BioGRID sin el solapamiento directo observado con STRING. Es una pieza clave para no exagerar claims de generalizacion entre redes PPI.
