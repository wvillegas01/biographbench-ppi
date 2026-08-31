# Dataset Downloadability Check

Fecha de revision: 2026-08-04

Objetivo: determinar cuales datasets candidatos pueden descargarse de forma completa, con fuente oficial o razonablemente primaria, antes de iniciar procesamiento o entrenamiento.

## Resumen ejecutivo

| Dataset | Descarga completa viable | Tamano aproximado | Metodo recomendado | Decision |
|---|---:|---:|---|---|
| OGB `ogbl-biokg` | Si | 963.3 MB ZIP | URL oficial en manifiesto OGB o loader `ogb` | Viable, pero requiere instalar `ogb` para loader reproducible |
| OpenBioLink2020 HQ directed | Si | 109.4 MB ZIP | Zenodo API/file | Viable y prioritario |
| BioGRID latest organism Tab3 | Si | 178.23 MB ZIP segun pagina | BioGRID latest release | Viable y prioritario; despues filtrar Homo sapiens |
| STRING human v12.0 links | Si | 79.3 MB gzip | STRING organism-specific download | Viable y prioritario |
| STRING human v12.0 detailed links | Si | 133.2 MB gzip | STRING organism-specific download | Viable si queremos evidencias/subscores |
| STRING human physical links | Si | 8.5 MB gzip | STRING organism-specific download | Muy viable para piloto pequeno |
| OBNB selected task | Probablemente si | Depende de red/label | Paquete `obnb` | Viable, pero requiere seleccionar tarea y auditar licencias fuente |
| DREAM4 in silico challenge | Si | 77.1 MB ZIP | GNW/SourceForge archive | Viable tecnicamente; no prioritario para MVP biologico real |
| DREAM5 Network Inference | Parcial / pendiente | 59.2 MB alternativa; oficial en Synapse | GNW alternative formats o Synapse | No asumir reproducible completo hasta probar Synapse/licencia |

## Detalle por dataset

### OGB `ogbl-biokg`

- Fuente: Open Graph Benchmark.
- URL de documentacion: https://ogb.stanford.edu/docs/linkprop/
- URL de descarga encontrada en manifiesto oficial OGB: https://snap.stanford.edu/ogb/data/linkproppred/biokg.zip
- Tamano por HEAD: 963,312,546 bytes.
- Licencia reportada por OGB para `ogbl-biokg`: CC-0.
- Estado local: `torch` esta instalado; `ogb` y `torch_geometric` no estan instalados.
- Decision: descargable completo. Para reproducibilidad conviene instalar `ogb` y usar `LinkPropPredDataset(name="ogbl-biokg")` o guardar la URL exacta del manifiesto OGB.

### OpenBioLink2020

- Fuente: Zenodo record 3834052.
- URL: https://zenodo.org/records/3834052
- Licencia del record Zenodo consultado por API: CC BY 4.0.
- Archivos principales:
  - `HQ_DIR.zip`: 109,387,184 bytes.
  - `HQ_UNDIR.zip`: 97,461,231 bytes.
  - `ALL_DIR.zip`: 700,146,163 bytes.
  - `ALL_UNDIR.zip`: 573,737,163 bytes.
- Decision: descargable completo. Recomendacion inicial: `HQ_DIR.zip`, porque es la variante dirigida de alta calidad y default para benchmarking segun el repositorio OpenBioLink.

### BioGRID

- Fuente: BioGRID Download File Repository.
- URL de latest release: https://downloads.thebiogrid.org/BioGRID/Latest-Release/
- Release actual observado: BioGRID 5.0.260, compilado el 2026-07-25.
- Licencia segun pagina de descarga: MIT, libre para uso academico y comercial.
- Archivos recomendados:
  - `BIOGRID-ORGANISM-LATEST.tab3.zip`: 178.23 MB segun pagina; contiene archivos separados por organismo.
  - `BIOGRID-ALL-LATEST.tab3.zip`: 172.59 MB segun pagina; contiene todo en un archivo.
- Decision: descargable completo. Recomendacion inicial: `BIOGRID-ORGANISM-LATEST.tab3.zip`, luego extraer Homo sapiens.

### STRING Homo sapiens v12.0

- Fuente: STRING download portal.
- URL: https://string-db.org/cgi/download?species_text=Homo+sapiens
- Licencia: CC BY 4.0 segun pagina oficial de acceso/licensing.
- Archivos confirmados por HEAD:
  - `9606.protein.links.v12.0.txt.gz`: 83,164,437 bytes.
  - `9606.protein.links.detailed.v12.0.txt.gz`: 139,634,808 bytes.
  - `9606.protein.physical.links.v12.0.txt.gz`: 8,954,065 bytes.
- Decision: descargable completo. Recomendacion inicial: descargar `physical.links` para piloto y `links.detailed` si queremos evidencias por canal.

### OBNB selected task

- Fuente: repositorio OBNB.
- URL: https://github.com/krishnanlab/obnb
- El README indica instalacion por `pip install obnb` y construccion de datasets via `OpenBiomedNetBench`.
- Estado: descargable probablemente completo mediante paquete y archivos archivados, pero no se debe cerrar hasta seleccionar una combinacion `graph_name`/`label_name` y auditar licencias fuente.
- Decision: candidato fuerte para node classification, pendiente de prueba de instalacion y seleccion de tarea.

### DREAM4 / DREAM5

- Fuente: GNW / DREAM challenge pages.
- URL GNW: https://gnw.sourceforge.net/dreamchallenge.html
- Archivos confirmados:
  - DREAM4 in silico challenge ZIP: 77,117,344 bytes.
  - DREAM5 alternative data formats ZIP: 59,163,708 bytes.
- Estado: DREAM4 tecnicamente descargable completo; DREAM5 oficial esta asociado a Synapse y requiere validacion aparte.
- Decision: DREAM4 es viable como benchmark regulatorio simulado; DREAM5 no debe entrar al MVP hasta resolver acceso/licencia oficial y gold standards.

## Ranking de descarga para la siguiente accion

1. STRING human physical links: pequeno, rapido, util para piloto.
2. OpenBioLink2020 `HQ_DIR.zip`: KG biomedico completo y manejable.
3. BioGRID organism Tab3: completo, formato recomendado, licencia clara.
4. STRING human detailed links: manejable y con evidencias.
5. OGB `ogbl-biokg`: viable, pero casi 1 GB y requiere instalar `ogb` para camino limpio.
6. OBNB selected task: primero seleccionar tarea y auditar licencias fuente.
7. DREAM4: tecnicamente facil, cientificamente menos prioritario si exigimos redes biologicas reales.

## Recomendacion

No descargar todo todavia en `reports/` ni mezclar datos con documentos. Si damos el siguiente paso, crear:

- `data/raw/`
- `data/manifests/`

y descargar primero solo:

1. STRING human physical links;
2. OpenBioLink `HQ_DIR.zip`;
3. BioGRID organism Tab3.

Con esos tres se prueba descarga, hash, descompresion, conteos y manifiestos sin comprometer demasiado disco.
