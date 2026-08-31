# Contexto del manuscrito 1966469

Fecha de revisión local: 2026-08-31

## Archivo revisado

- `C:\Users\wilop\Dropbox\MPDI\2026\BioGraphBench\1966469_Manuscript.DOCX`

Nota de ruta: la carpeta indicada por el usuario, `C:\Users\wilop\Dropbox\MPDI\2026\BioGraphBench\1966469\_Manuscript`, no existe localmente. El archivo encontrado es `1966469_Manuscript.DOCX` directamente dentro de `BioGraphBench`.

## Estado estructural

- Documento Word valido como paquete OOXML: si.
- Tamano: 3,142,594 bytes.
- Metadatos Word:
  - Paginas: 18.
  - Palabras: 7,998.
  - Caracteres: 51,274.
  - Template: `frontiers_template.dotx`.
  - Ultima modificacion registrada: 2026-08-13.
- Extraccion con `python-docx`:
  - Parrafos: 159.
  - Tablas: 5.
  - Figuras inline: 6.
  - Celdas vacias en tablas: 0.
  - Comentarios Word (`comments.xml`): no encontrados.
  - Inserciones con texto en control de cambios: 0.
  - Eliminaciones en control de cambios: 0.

## Estructura principal

- Title: `BioGraphBench-PPI enables audit-first evaluation of negative-sampling contracts and structural baselines in protein interaction networks`
- Running title: `Audit-first PPI link prediction`
- Abstract
- Introduction
- Materials and Methods
  - Audit-first benchmark design
  - Data sources and canonicalization
  - Task definitions and fixed partitions
  - Structural features and link-prediction baselines
  - Multilabel node-classification baselines
  - Evaluation, calibration, and reproducibility
- Results
  - Accepted tasks and benchmark scale
  - Strong structural baselines for PPI link prediction
  - Calibration and computational cost distinguish supervised baselines
  - Functional node classification remains difficult
  - Empirical requirements for future graph models
- Discussion
- Conclusion
- Statements
- References

## Figuras y tablas

Figuras detectadas:

- Figure 1: workflow metodologico audit-first.
- Figure 2: distribuciones HGB AUPRC por semilla.
- Figure 3: diferencias pareadas por regimen de negativos.
- Figure 4: perfiles por familia de modelos y regimen de negativos.
- Figure 5: calibracion y costo computacional.
- Figure 6: OBNB BioGRID+GOBP como stress test secundario.

Tablas detectadas:

- Table 1: tareas aceptadas en el framework BioGraphBench.
- Table 2: escala y particiones positivas.
- Table 3: AUPRC media por dataset, negativos y modelo.
- Table 4: sensibilidad HGB a contratos de negativos.
- Table 5: resultados OBNB BioGRID+GOBP multilabel node classification.

## Mensaje cientifico actual

El manuscrito esta correctamente enfocado como `BioGraphBench-PPI`, no como benchmark general de network bioinformatics. La tesis empirica central es que los resultados de PPI link prediction dependen fuertemente del contrato de negativos:

- `random` negatives producen desempeno alto y estable.
- `degree-matched` negatives reducen atajos por grado.
- `two-hop` negatives introducen dificultad local y cambian rankings de modelos.
- HGB y RF son baselines estructurales fuertes.
- node2vec-compatible aporta un baseline de embedding no-GNN.
- OBNB se mantiene como stress test secundario, no como contribucion principal.

## Puntos que probablemente seran sensibles ante revisores

- No hay modelos GNN competitivos de link prediction implementados en el manuscrito enviado; se reconocen como trabajo futuro.
- `two-hop` es un hard-negative local, pero no reemplaza un muestreo community-matched o temporal.
- node2vec-compatible es auditable, pero no esta presentado como node2vec exhaustivamente tuneado.
- OBNB permanece en el manuscrito, pero debe defenderse como stress test secundario para no diluir el foco PPI.
- El articulo reporta confianza/dispersion y comparaciones pareadas, pero en el texto no aparece literalmente `Wilcoxon`; aparece como `paired seed-wise comparisons`. Si los revisores piden pruebas estadisticas explicitas, conviene reforzar esta parte.
- Algunas captions de figuras aparecen estructuralmente como parrafos `Normal` aunque el texto y la numeracion son correctos. Si se va a reentregar el DOCX, conviene normalizar estilos de captions antes del envio.

## Observaciones editoriales/revisores

No se encontraron localmente archivos de observaciones, decision editorial, reviewer comments, response letter o rebuttal dentro de `C:\Users\wilop\Dropbox\MPDI\2026\BioGraphBench`. Cuando el usuario pegue o suba esas observaciones, deben mapearse contra este manuscrito exacto.

## QA visual

Se intento renderizar el DOCX a PNG/PDF con el renderer del plugin de documentos. El intento fallo porque el entorno local no encuentra LibreOffice/`soffice`. Por tanto, solo se completo QA estructural, no revision visual pagina por pagina.
