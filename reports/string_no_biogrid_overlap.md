# STRING No-BioGRID-Overlap Ablation

Fecha: 2026-08-04

## Objetivo

Crear una variante de STRING human physical excluyendo pares que se solapan con BioGRID filtrado, usando mapeo explicito STRING protein ID -> Entrez.

## Conteos

| Medida | Valor |
|---|---:|
| Aristas STRING originales no dirigidas | 738805 |
| Aristas removidas por solapamiento BioGRID | 424266 |
| Aristas restantes | 314539 |
| Nodos restantes | 16781 |
| Aristas restantes con mapeo Entrez incompleto | 7623 |

## Split piloto

| Split | Positivos | Negativos |
|---|---:|---:|
| Train | 251633 | 251633 |
| Validation | 31453 | 31453 |
| Test | 31453 | 31453 |

## Checks

- Errores de split: `None`
- Componentes originales: `26`
- Componentes en train: `26`
- Componentes preservados: `True`

## Decision

Esta ablation complementa la version BioGRID sin STRING. Debe interpretarse con cuidado: remover solapamiento en STRING depende del mapeo Entrez disponible y puede dejar pares no removidos si el mapeo es incompleto.
