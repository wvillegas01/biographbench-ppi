# BioGRID Human Physical Filtered Dataset

Fecha: 2026-08-04

## Objetivo

Crear una version filtrada y auditable de BioGRID Homo sapiens para una futura tarea de link prediction PPI homogenea.

## Politica de filtrado

1. Mantener solo `Experimental System Type == physical`.
2. Mantener solo interacciones humano-humano: `Organism ID Interactor A == 9606` y `Organism ID Interactor B == 9606`.
3. Excluir filas sin Entrez Gene ID.
4. Excluir self-loops.
5. Colapsar pares Entrez no dirigidos.
6. Conservar `evidence_count`, `publication_count`, sistemas experimentales y throughput como metadatos.

## Conteos

| Medida | Valor |
|---|---:|
| Filas crudas | 1404902 |
| Filas de evidencia conservadas | 1264295 |
| Nodos Entrez unicos | 20376 |
| Aristas no dirigidas unicas | 961531 |
| Densidad | 0.00463209 |
| Evidencia minima por arista | 1 |
| Evidencia media por arista | 1.3149 |
| Evidencia maxima por arista | 666 |

## Exclusiones

- `not_human_human`: 112057
- `not_physical`: 19450
- `self_loop`: 9100

## Sistemas experimentales principales

- `Affinity Capture-MS`: 674918
- `Proximity Label-MS`: 178274
- `Two-hybrid`: 113988
- `Affinity Capture-Western`: 84724
- `Co-fractionation`: 73949
- `Reconstituted Complex`: 42034
- `Cross-Linking-MS (XL-MS)`: 30206
- `Affinity Capture-RNA`: 25419
- `Biochemical Activity`: 13103
- `Protein-RNA`: 8973
- `Co-localization`: 5154
- `Protein-peptide`: 3659
- `FRET`: 2480
- `Affinity Capture-Luminescence`: 2010
- `Co-purification`: 1675
- `Co-crystal Structure`: 1620
- `PCA`: 1364
- `Far Western`: 734
- `Surface Display`: 11

## Throughput

- `High Throughput`: 1032911
- `Low Throughput`: 224542
- `High Throughput|Low Throughput`: 6842

## Archivos generados

- `C:\Users\wilop\Dropbox\MPDI\2026\BioGraphBench\Auditoria\data\processed\biogrid_human_physical\edges_entrez_undirected.csv`
- `C:\Users\wilop\Dropbox\MPDI\2026\BioGraphBench\Auditoria\data\processed\biogrid_human_physical\filter_manifest.json`

## Decision

Esta version filtrada es mucho mas adecuada que BioGRID crudo para una tarea PPI homogenea. Todavia falta construir splits de link prediction y medir solapamiento biologico con STRING mediante una capa de mapeo de identificadores.
