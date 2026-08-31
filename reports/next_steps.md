# Next Steps

Fecha: 2026-08-05

## Prioridad 1

1. Convertir `Auditoria` en esqueleto de paquete `biographbench`.
2. Congelar entorno: `pyproject.toml`, `requirements-lock.txt` o `environment.yml`.
3. Mover scripts estables a modulos versionados.
4. Crear tests formales para leakage, splits, features y metricas.
5. Ejecutar 5 semillas en baselines principales.

## Prioridad 2

1. Cargar y auditar `ogbl-biokg`.
2. Resolver OpenBioLink inverse-relation review.
3. Implementar GCN/GraphSAGE/APPNP de forma modular.
4. Agregar calibracion posterior: temperature scaling o isotonic cuando aplique.
5. Agregar curvas de robustez iniciales para STRING/BioGRID.

## Prioridad 3

1. Interpretabilidad: GNNExplainer/Integrated Gradients cuando haya GNNs estables.
2. Escalabilidad: fracciones 10/25/50/75/100%.
3. Analisis estadistico con multiples semillas.
4. Figuras reproducibles.
