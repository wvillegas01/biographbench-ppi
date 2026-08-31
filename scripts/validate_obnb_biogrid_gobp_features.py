"""Validate OBNB BioGRID+GOBP feature artifacts."""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data" / "processed" / "obnb_biogrid_gobp"


def main() -> int:
    errors: list[str] = []
    dataset_manifest = json.loads((DATA_DIR / "manifest.json").read_text(encoding="utf-8"))
    feature_manifest = json.loads((DATA_DIR / "feature_manifest.json").read_text(encoding="utf-8"))
    arrays = np.load(DATA_DIR / "node_classification_arrays.npz", allow_pickle=False)
    features = np.load(DATA_DIR / "features.npz", allow_pickle=False)

    node_count = dataset_manifest["graph_nodes"]
    if feature_manifest["node_count"] != node_count:
        errors.append("feature manifest node count does not match dataset manifest")

    for name in ["constant", "degree", "log_degree", "one_hot_log_degree"]:
        matrix = features[name]
        if matrix.shape[0] != node_count:
            errors.append(f"{name} row count mismatch")
        if not np.isfinite(matrix).all():
            errors.append(f"{name} contains NaN or inf")

    if not np.array_equal(arrays["node_ids"], features["node_ids"]):
        errors.append("feature node_ids do not match node classification export")

    constant = features["constant"]
    if constant.shape[1] != 1 or not np.allclose(constant, 1.0):
        errors.append("constant feature is not all ones with shape N x 1")

    one_hot = features["one_hot_log_degree"]
    if one_hot.shape[1] != 9:
        errors.append("one_hot_log_degree should have 9 columns")
    if not np.allclose(one_hot.sum(axis=1), 1.0):
        errors.append("one_hot_log_degree rows do not sum to 1")
    if not np.all((one_hot == 0.0) | (one_hot == 1.0)):
        errors.append("one_hot_log_degree contains non-binary values")

    bins = features["log_degree_bin"]
    if bins.min() < 0 or bins.max() > 8:
        errors.append("log_degree_bin outside expected range 0..8")
    if not np.array_equal(one_hot.argmax(axis=1), bins):
        errors.append("one_hot argmax does not match log_degree_bin")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print("OK: OBNB BioGRID+GOBP features are valid and aligned with node export.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
