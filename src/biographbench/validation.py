import csv
from pathlib import Path
from typing import Dict, Iterable, List

import numpy as np

from biographbench.io import load_json


DATASET_AUDIT_REQUIRED_COLUMNS = {
    "dataset_id",
    "dataset_name",
    "source",
    "official_url",
    "license",
    "download_status",
    "preprocessing_status",
    "eligible",
    "exclusion_reason",
}


def validate_dataset_audit_csv(path: Path) -> List[str]:
    errors: List[str] = []
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        fieldnames = set(reader.fieldnames or [])
        missing = sorted(DATASET_AUDIT_REQUIRED_COLUMNS - fieldnames)
        if missing:
            errors.append(f"missing columns: {', '.join(missing)}")

        rows = list(reader)
        if not rows:
            errors.append("dataset audit has no rows")

        for index, row in enumerate(rows, start=2):
            for column in DATASET_AUDIT_REQUIRED_COLUMNS:
                if column in row and not str(row[column]).strip():
                    errors.append(f"row {index}: empty {column}")
    return errors


def validate_split_manifest(path: Path) -> List[str]:
    errors: List[str] = []
    manifest = load_json(path)
    if manifest.get("split_errors"):
        errors.append(f"{path}: split_errors is not empty")
    for key in ("train_pos", "val_pos", "test_pos"):
        value = manifest.get(key)
        if not isinstance(value, int) or value <= 0:
            errors.append(f"{path}: invalid {key}={value!r}")
    for key in ("train_neg", "val_neg", "test_neg"):
        if key in manifest and manifest[key] != manifest.get(key.replace("_neg", "_pos")):
            errors.append(f"{path}: {key} does not match positive split size")
    return errors


def validate_required_files(paths: Iterable[Path]) -> List[str]:
    return [f"missing file: {path}" for path in paths if not path.is_file()]


def validate_obnb_feature_bundle(feature_path: Path, arrays_path: Path) -> List[str]:
    errors: List[str] = []
    features = np.load(feature_path)
    arrays = np.load(arrays_path)

    x = features["one_hot_log_degree"]
    y = arrays["y"]
    train_mask = arrays["train_mask"]
    val_mask = arrays["val_mask"]
    test_mask = arrays["test_mask"]

    if x.shape[0] != y.shape[0]:
        errors.append(f"feature rows {x.shape[0]} != label rows {y.shape[0]}")
    if x.shape[0] == 0 or x.shape[1] == 0:
        errors.append(f"empty feature matrix shape={x.shape}")
    if not np.isfinite(x).all():
        errors.append("feature matrix contains non-finite values")

    for name, mask in (("train_mask", train_mask), ("val_mask", val_mask), ("test_mask", test_mask)):
        if mask.shape[0] != x.shape[0]:
            errors.append(f"{name} length {mask.shape[0]} != feature rows {x.shape[0]}")
        if mask.dtype != np.bool_:
            errors.append(f"{name} is not boolean")

    overlap = (train_mask.astype(int) + val_mask.astype(int) + test_mask.astype(int)) > 1
    if overlap.any():
        errors.append("train/val/test masks overlap")
    if train_mask.sum() == 0 or val_mask.sum() == 0 or test_mask.sum() == 0:
        errors.append("one or more node classification splits are empty")
    return errors
