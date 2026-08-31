# Dataset Selection - Propuesta inicial

Fecha de auditoria: 2026-08-04

## Criterio de seleccion

La primera version debe cubrir:

- al menos 4 datasets abiertos;
- al menos 2 clases de redes biologicas;
- al menos 1 tarea de node classification;
- al menos 1 tarea de link prediction;
- al menos 1 grafo homogeneo;
- al menos 1 grafo heterogeneo;
- al menos 1 dataset suficientemente grande para escalabilidad.

## Candidatos recomendados para auditoria profunda

| Prioridad | Dataset | Rol propuesto | Tarea inicial | Tipo de grafo | Motivo |
|---|---|---|---|---|---|
| Alta | OGB `ogbl-biokg` | KG heterogeneo principal | Link prediction / KG completion | Heterogeneo | Loader/evaluador estandarizado, 93,773 nodos y 5,088,434 aristas segun OGB |
| Alta | OpenBioLink2020 directed high quality | KG heterogeneo alternativo | Link prediction | Heterogeneo | Benchmark biomedico dedicado, MIT, splits y variantes publicadas |
| Alta | BioGRID Homo sapiens | Red PPI/genetica curada | Link prediction y posible node classification con etiquetas externas | Homogeneo o multi-relacional simple | Descargas archivadas, MIT, buena trazabilidad de version |
| Alta | STRING Homo sapiens v12.0 | Asociaciones funcionales PPI | Link prediction, robustez, node classification con GO | Homogeneo ponderado | Gran escala, pesos/confianza, CC BY 4.0, filtros por organismo/confianza |
| Media | OBNB selected task | Node classification biologica | Node classification | Usualmente homogeneo | Cubre el hueco de etiquetas/tareas biologicas reproducibles |
| Media | DREAM4/DREAM5 | Red regulatoria | Link prediction regulatorio | Dirigido | Gold standards utiles, pero requiere mas auditoria de acceso/licencia/formato |

## Propuesta MVP

Seleccion provisional para llegar a 4 datasets:

1. `ogbl_biokg`: link prediction/KG completion heterogeneo.
2. `openbiolink2020_hq_directed`: link prediction heterogeneo.
3. `biogrid_human`: PPI/interacciones humanas homogeneas.
4. `string_human_v12`: PPI/asociaciones humanas ponderadas.

Para cumplir node classification sin forzar etiquetas dudosas, se abren dos rutas:

- Ruta A: incorporar una tarea OBNB ya reproducible como dataset de node classification.
- Ruta B: construir node classification sobre BioGRID/STRING con Gene Ontology u otra fuente abierta, despues de auditar licencia, version y fecha de corte.

Decision recomendada: usar Ruta A para el primer paper/MVP y dejar Ruta B como extension controlada, salvo que la auditoria de GO resulte muy limpia.

## Riesgos por dataset

### OGB `ogbl-biokg`

- Split oficial es random; hay que revisar si basta para evitar leakage biologico o si se requiere split adicional.
- KG heterogeneo: comparar modelos KG tradicionales y GNN heterogeneas, no solo GNN homogeneizadas.
- No tratar MRR oficial como comparable directamente con AUROC/AUPRC de otros datasets.

### OpenBioLink2020

- Dataset grande; validar requisitos de disco/memoria antes de prometer ejecucion completa.
- Aunque el benchmark minimiza leakage, BioGraphBench debe revalidar inversas, duplicados y negativos.
- Versiones y variantes deben quedar fijas desde Zenodo.

### BioGRID

- Seleccionar una version exacta y organismo.
- Separar interacciones fisicas/geneticas si la tarea lo requiere.
- Medir solapamiento con STRING para no duplicar evidencia.

### STRING

- Version 12.0; los archivos completos son enormes.
- Descargar por organismo y posiblemente por umbral de confianza.
- Documentar si se usan asociaciones funcionales, fisicas o subscores por evidencia.
- Licencia CC BY 4.0 exige atribucion y documentar cambios.

### OBNB

- Excelente para node classification, pero hay que seleccionar una tarea concreta.
- Auditar si los datos fuente y etiquetas permiten redistribucion o si solo se redistribuyen scripts/manifiestos.

### DREAM4/DREAM5

- Muy valioso para redes regulatorias, pero menos directo para el MVP.
- Confirmar acceso oficial, licencia y formato antes de incluir.

## Criterio de avance a Fase 2

No pasar a pipeline de datos completo hasta que 4 datasets tengan:

- URL oficial y procedimiento de descarga;
- version fija;
- licencia compatible;
- citacion;
- hashes o mecanismo de verificacion;
- conteos iniciales reproducibles;
- tarea predictiva definida;
- riesgos de leakage documentados;
- fila completa o justificada en `dataset_audit.csv`.
