# Split package refactor status

Date: 2026-08-05

## Objective

Convert the current link-prediction split policy into importable, testable, reusable package code without breaking the existing scripts pipeline.

## Implemented package module

- `src/biographbench/splits/link_prediction.py`

The module now owns the common policy for:

- undirected edge normalization;
- adjacency construction;
- connected component counting;
- spanning forest protection;
- train/validation/test positive split construction;
- balanced negative sampling;
- split overlap, self-loop, and ordering validation;
- split manifest construction.

## Scripts migrated

The following scripts now call `biographbench.splits.build_link_prediction_split`:

- `scripts/build_string_pilot_splits.py`
- `scripts/build_biogrid_pilot_splits.py`
- `scripts/build_biogrid_no_string_overlap.py`
- `scripts/build_string_no_biogrid_overlap.py`

Dataset-specific logic remains in the scripts:

- raw file loading;
- metadata preservation;
- CSV writing;
- report writing.

## Tests added

- `tests/test_link_prediction_split_core.py`

The tests cover:

- preservation of original component count through spanning forest protection;
- negative edges not overlapping positives or other negatives;
- explicit failure when requested holdout would violate the forest policy.

## Verification

Executed successfully:

```powershell
python scripts\build_string_pilot_splits.py
python scripts\validate_string_pilot_split.py
python scripts\build_biogrid_pilot_splits.py
python scripts\validate_biogrid_pilot_split.py
python scripts\build_biogrid_no_string_overlap.py
python scripts\validate_biogrid_no_string_overlap.py
python scripts\build_string_no_biogrid_overlap.py
python scripts\validate_string_no_biogrid_overlap.py
python -m pytest -q
```

Final test result:

```text
7 passed
```

## Note

The local Windows environment did not have `make` available, so the Makefile targets were executed through their underlying Python commands.
