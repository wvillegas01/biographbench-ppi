"""Validate exported OBNB BioGRID+GOBP node-classification artifact."""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data" / "processed" / "obnb_biogrid_gobp"


def main() -> int:
    errors: list[str] = []
    manifest = json.loads((DATA_DIR / "manifest.json").read_text(encoding="utf-8"))
    arrays = np.load(DATA_DIR / "node_classification_arrays.npz", allow_pickle=False)

    y = arrays["y"]
    y_mask = arrays["y_mask"].astype(bool)
    train = arrays["train_mask"].astype(bool)
    val = arrays["val_mask"].astype(bool)
    test = arrays["test_mask"].astype(bool)
    node_ids = arrays["node_ids"]
    label_ids = arrays["label_ids"]

    expected_shape = tuple(manifest["y_shape"])
    if y.shape != expected_shape:
        errors.append(f"y shape mismatch: manifest={expected_shape} observed={y.shape}")
    if y_mask.shape != tuple(manifest["y_mask_shape"]):
        errors.append("y_mask shape mismatch")
    if len(node_ids) != manifest["graph_nodes"]:
        errors.append("node_ids length mismatch")
    if len(label_ids) != manifest["label_tasks"]:
        errors.append("label_ids length mismatch")
    if y.shape[0] != len(node_ids) or y.shape[1] != len(label_ids):
        errors.append("array dimensions do not match node/label ids")

    if np.any(train & val) or np.any(train & test) or np.any(val & test):
        errors.append("train/val/test masks overlap")
    split_union = train | val | test
    if int(split_union.sum()) != manifest["split_counts"]["train"] + manifest["split_counts"]["val"] + manifest["split_counts"]["test"]:
        errors.append("split union count mismatch")
    if int(train.sum()) != manifest["split_counts"]["train"]:
        errors.append("train count mismatch")
    if int(val.sum()) != manifest["split_counts"]["val"]:
        errors.append("val count mismatch")
    if int(test.sum()) != manifest["split_counts"]["test"]:
        errors.append("test count mismatch")

    if not np.all((y == 0) | (y == 1)):
        errors.append("y contains values outside {0,1}")
    if np.any(y.astype(bool) & ~y_mask):
        errors.append("positive label exists where y_mask is false")

    positives_per_task = y.sum(axis=0)
    observed_per_task = y_mask.sum(axis=0)
    negatives_per_task = observed_per_task - positives_per_task
    if int(positives_per_task.min()) < 50:
        errors.append("a task has fewer than 50 positives")
    if int(negatives_per_task.min()) <= 0:
        errors.append("a task has no negatives")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print("OK: OBNB BioGRID+GOBP export has valid arrays, disjoint masks, and expected label counts.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
