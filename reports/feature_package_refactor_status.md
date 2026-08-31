# Feature package refactor status

Date: 2026-08-05

## Objective

Convert the current structural feature policy into importable, testable, reusable package code without breaking the existing OBNB feature pipeline.

## Implemented package module

- `src/biographbench/features/structural.py`

The module now owns the common policy for:

- constant control features;
- raw degree scalar features;
- natural `log1p` degree scalar features;
- capped `floor(log2(degree + 1))` degree bins;
- one-hot log-degree features;
- feature bundle validation;
- manifest construction.

## Script migrated

The following script now calls `biographbench.features.build_structural_features`:

- `scripts/build_obnb_biogrid_gobp_features.py`

Dataset-specific logic remains in the script:

- loading OBNB BioGRID+GOBP;
- reading graph degrees from OBNB;
- writing `features.npz`;
- writing feature policy reports.

## Tests added

- `tests/test_structural_features.py`

The tests cover:

- exact log-degree binning with cap;
- expected shapes and values for all structural features;
- rejection of invalid one-hot indices;
- rejection of misaligned node and degree arrays.

## Verification

Executed successfully:

```powershell
python -m pytest -q
python scripts\build_obnb_biogrid_gobp_features.py
python scripts\validate_obnb_biogrid_gobp_features.py
```

Final test result:

```text
11 passed
```

The OBNB feature artifact was rebuilt and validated as aligned with the node-classification export.
