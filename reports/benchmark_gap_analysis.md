# Benchmark Gap Analysis - BioGraphBench

Fecha de auditoria: 2026-08-04

## Tesis de posicionamiento

BioGraphBench debe diferenciarse como un benchmark multidimensional para redes biologicas reales. No debe competir solo por mayor AUROC/AUPRC, sino por auditar simultaneamente rendimiento, calibracion, robustez, explicabilidad, escalabilidad, estabilidad entre semillas y consistencia biologica.

La oportunidad principal no es "otro ranking de GNNs", sino un protocolo reproducible que haga visibles los trade-offs entre precision, confianza probabilistica, resistencia a perturbaciones, coste computacional y validez biologica.

## Matriz comparativa inicial

| Recurso existente | Dominio | Tareas | Datasets | Modelos | Robustez | Explicabilidad | Calibracion | Escalabilidad | Validacion biologica | Limitaciones observadas | Diferencia propuesta de BioGraphBench |
|---|---|---|---|---|---|---|---|---|---|---|---|
| OBNB | Network biology humana | Node classification | Redes de 15 fuentes; funciones, traits y enfermedades | Compatible con PyG/DGL; enfasis en datasets | No es eje central | No es eje central | No es eje central | Parcial, por loaders/framework | Parcial por etiquetas biologicas | Muy fuerte para node classification, pero no cubre de forma central link prediction heterogeneo, calibracion, robustez, explicabilidad y Pareto multidimensional | Usar OBNB como referencia y posible fuente, pero ampliar a link prediction/KG, calibracion, perturbaciones y validacion de explicaciones |
| OGB | Graph ML general | Node, link y graph property prediction | Diversos dominios; incluye `ogbl-biokg` y `ogbl-ppa` | Baselines y leaderboards estandarizados | No como dimension principal | No como dimension principal | No como dimension principal | Fuerte en datasets grandes | Limitada al dataset | Excelente estandar de loaders/evaluadores, pero no es un benchmark biologico multidimensional | Adoptar datasets/evaluadores donde convenga, anadiendo auditoria biologica, leakage checks, calibracion, robustez e interpretabilidad |
| OpenBioLink | Biomedical KG | Link prediction | OpenBioLink2020 y variantes | Framework de evaluacion de link prediction | Parcial via splits/leakage minimizado | No central | No central | Dataset grande | Parcial por entidades/rels biomedicas | Muy solido para KG link prediction, pero concentrado en una familia de tarea/dataset | Usarlo como candidato fuerte para KG, comparandolo con OGB BioKG y redes PPI homogeneas |
| GNN-Suite | Biomedical informatics | Cancer-driver gene node classification | STRING/BioGRID con PCAWG/PID/COSMIC | GCN, GAT, GIN, GraphSAGE, GCN2, GTN, HGCN, PHGCN, LR | No central | No central | No central | Parcial via Nextflow/Docker | Si, en cancer driver genes | Caso de uso fuerte pero estrecho: una tarea, splits 80/20, metrica primaria BACC, poca calibracion/robustez/explicabilidad | Extender la idea de reproducibilidad a multiples tareas y dimensiones, con controles de leakage mas estrictos |
| OgBench / OGBench Omics Graph Benchmark | Omics graph learning | Clasificacion biologica, principalmente graph/sample-level en omics | 4 datasets omics en Hugging Face | GNNs, MLP y sklearn baselines | No eje central inicial | No eje central | No eje central | Buena infraestructura moderna | Parcial por datasets omics | Se enfoca en omics graph-level/low-sample settings, no en redes biologicas como objetos principales de node/link prediction | BioGraphBench se centra en redes biologicas reales, node classification y link prediction, incluyendo homogeneas y heterogeneas |

## Fuentes verificadas

- OBNB: PMLR reporta que OBNB es una coleccion de datasets de node classification derivados de redes de 15 fuentes y tareas de funciones, traits y enfermedades; tambien indica paquete compatible con PyG/DGL y licencia MIT. URL: https://proceedings.mlr.press/v240/liu24a.html
- OGB: la documentacion oficial lista `ogbl-biokg` con 93,773 nodos, 5,088,434 aristas, tarea KG completion y metrica MRR; tambien provee loaders y evaluadores. URL: https://ogb.stanford.edu/docs/linkprop/
- OpenBioLink: el repositorio oficial lo define como recurso/framework para link prediction en grafos biomedicos heterogeneos; declara licencia MIT y variantes OpenBioLink2020 en Zenodo. URL: https://github.com/OpenBioLink/OpenBioLink
- GNN-Suite: el preprint lo presenta como framework modular con Nextflow para benchmarking GNN en biomedical informatics, aplicado a cancer-driver genes con STRING/BioGRID y 10 semillas. URL: https://arxiv.org/html/2505.10711v1
- OgBench: el leaderboard lo describe como Omics Graph Benchmark para GNN, neural networks y classical ML en datasets omics graph-structured. URL: https://ogbench.org/ y repositorio https://github.com/geometric-intelligence/ogbench
- BioGRID: el repositorio oficial de descargas indica que los datos son libres para uso academico y comercial bajo MIT. URL: https://downloads.thebiogrid.org/
- STRING: la pagina oficial de acceso indica version 12.0 actual desde 2023-07-26 y licencia Creative Commons BY 4.0 para datos y descargas. URL: https://string-db.org/cgi/access

## Vacio defendible para BioGraphBench

BioGraphBench sera novedoso si conserva esta combinacion:

1. Cobertura de al menos dos tareas: node classification y link prediction.
2. Cobertura de grafos homogeneos y heterogeneos.
3. Auditoria explicita de licencia, version, descarga, hashes, transformaciones y reproducibilidad.
4. Controles de leakage antes de entrenar modelos.
5. Evaluacion multidimensional: performance, calibracion, robustez, explicabilidad, escalabilidad y estabilidad.
6. Analisis de trade-offs sin indice compuesto prematuro.
7. Comparacion contra baselines no neuronales y contra redes aleatorizadas para responder si la estructura biologica aporta valor.

## Riesgos cientificos principales

- DisGeNET y otras fuentes de etiquetas pueden tener licencias cambiantes o restricciones comerciales. No se deben usar sin auditoria de version y terminos.
- Node classification puede inducir leakage si etiquetas, atributos o embeddings usan informacion posterior al split.
- Link prediction en grafos de conocimiento requiere filtrado de aristas inversas, relaciones triviales y negativos incompatibles.
- STRING contiene interacciones bidireccionales por defecto en varios archivos; hay que remover pares redundantes o documentar direccion segun tarea.
- BioGRID y STRING se solapan; si ambos se usan, hay que medir redundancia para evitar datasets casi duplicados.

## Decision inicial

Avanzar con una Fase 1 estricta: seleccionar 4 a 6 candidatos, validar acceso/licencia/tamano/tarea/leakage, y no iniciar GNNs hasta que al menos 4 datasets tengan procedimiento reproducible completo.
