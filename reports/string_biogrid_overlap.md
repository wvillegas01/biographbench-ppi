# STRING-BioGRID Overlap Audit

Fecha: 2026-08-04

## Objetivo

Medir si STRING human physical y BioGRID human physical filtrado son datasets independientes o si comparten una fraccion sustancial de pares biologicos.

## Mapeo usado

STRING usa IDs de proteina tipo `9606.ENSP...`; BioGRID filtrado usa Entrez Gene IDs. Para evitar resolucion silenciosa, solo se usaron aliases Entrez explicitos en STRING:

- `Ensembl_HGNC_entrez_id`
- `UniProt_DR_GeneID`

## Resultados

| Medida | Valor |
|---|---:|
| Proteinas STRING con mapeo Entrez | 19336 |
| Nodos STRING fisicos | 18767 |
| Nodos STRING fisicos con Entrez | 18564 |
| Pares STRING crudos no dirigidos | 738805 |
| Pares STRING sin mapeo Entrez completo | 7623 |
| Pares STRING con mapeo Entrez ambiguo | 16659 |
| Pares STRING Entrez tras mapeo | 766284 |
| Pares BioGRID Entrez | 961531 |
| Pares solapados | 423528 |
| Ratio de STRING cubierto por BioGRID | 0.552704 |
| Ratio de BioGRID cubierto por STRING | 0.440473 |
| Jaccard de pares Entrez | 0.324720 |

## Decision metodologica

STRING y BioGRID no deben tratarse automaticamente como datasets independientes. El solapamiento debe reportarse y, para experimentos comparativos, conviene crear al menos una ablacion:

1. BioGRID completo filtrado;
2. BioGRID excluyendo pares presentes en STRING;
3. STRING completo;
4. STRING excluyendo pares presentes en BioGRID, cuando el mapeo Entrez sea confiable.

Esto evita inflar la evidencia de generalizacion cuando dos datasets comparten muchas interacciones.

## Archivos generados

- `C:\Users\wilop\Dropbox\MPDI\2026\BioGraphBench\Auditoria\data\processed\string_biogrid_overlap\overlap_entrez_edges.csv`
- `C:\Users\wilop\Dropbox\MPDI\2026\BioGraphBench\Auditoria\data\processed\string_biogrid_overlap\overlap_manifest.json`
