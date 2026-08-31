# STRING Human Physical v12.0 - Quality Audit

Fecha de auditoria: 2026-08-04

## Resumen

| Medida | Valor |
|---|---:|
| Filas crudas dirigidas | 1477610 |
| Aristas dirigidas unicas | 1477610 |
| Duplicados dirigidos exactos | 0 |
| Self-loops | 0 |
| Aristas no dirigidas tras colapsar A-B/B-A | 738805 |
| Filas simetricas excedentes | 738805 |
| Nodos | 18767 |
| Componentes conectados | 5 |
| Nodos en componente principal | 18758 |
| Ratio componente principal | 0.999520 |
| Densidad no dirigida | 0.00419559 |
| Grado medio | 78.7345 |
| Grado mediano | 39 |
| Grado maximo | 2943 |
| Score minimo | 150 |
| Score mediano | 292.0 |
| Score maximo | 999 |

## Interpretacion

STRING physical viene como tabla de asociaciones proteina-proteina con pares simetricos. Para una tarea PPI no dirigida, el grafo debe colapsar `A-B` y `B-A` en una sola arista, conservando el mayor `combined_score` observado.

No se observan self-loops ni duplicados dirigidos exactos en la tabla cruda. La red es muy conectada: el componente principal contiene casi todos los nodos, por lo que es viable construir splits de link prediction preservando conectividad.

## Propuesta de tarea sin leakage

Tarea inicial: link prediction no dirigida en STRING human physical v12.0.

Politica propuesta:

1. Colapsar pares simetricos antes de construir el grafo final.
2. Remover self-loops si aparecieran en futuras versiones.
3. Separar aristas positivas de validacion/test antes de calcular cualquier feature estructural.
4. Mantener una version de entrenamiento conectada, evitando que el split fragmente excesivamente el componente principal.
5. Generar negativos solo entre pares de proteinas no conectadas en el grafo completo auditado.
6. Usar los mismos negativos para todos los modelos comparables dentro de cada seed.
7. Reportar AUROC y AUPRC; por desbalance, priorizar AUPRC.

## Riesgos abiertos

- STRING es una red de asociaciones con evidencia integrada, no interacciones experimentales puras.
- Los scores derivan de multiples fuentes de evidencia; si se usan como features o pesos, deben separarse de la etiqueta de existencia de arista.
- Hay que decidir si el umbral minimo de confianza sera 150, 400, 700 u otro, y reportarlo como ablacion o configuracion fija.
