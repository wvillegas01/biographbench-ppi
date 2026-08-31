# BioGraphBench package skeleton status

Date: 2026-08-05

This audit workspace now includes a minimal installable Python package under `src/biographbench`.

## What was formalized

- Python package metadata in `pyproject.toml`.
- Runtime dependency declarations in `requirements.txt`.
- Environment pin snapshot for the audited MVP in `requirements-lock.txt`.
- Importable path and validation helpers in `src/biographbench`.
- Artifact integrity tests in `tests`.

## Current package boundary

The package does not yet replace the existing `scripts/` pipeline. At this stage it provides a stable validation layer around the reproducible artifacts already produced by the audit.

The next engineering step is to migrate script logic into package modules incrementally, starting with split generation and feature construction because those are the strongest reproducibility contracts.
