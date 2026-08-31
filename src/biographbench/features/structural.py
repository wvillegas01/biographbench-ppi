from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Dict

import numpy as np


@dataclass(frozen=True)
class StructuralFeatureBundle:
    node_ids: np.ndarray
    constant: np.ndarray
    degree: np.ndarray
    log_degree: np.ndarray
    one_hot_log_degree: np.ndarray
    log_degree_bin: np.ndarray
    max_log_bin: int

    def arrays(self) -> Dict[str, np.ndarray]:
        return {
            "node_ids": self.node_ids,
            "constant": self.constant,
            "degree": self.degree,
            "log_degree": self.log_degree,
            "one_hot_log_degree": self.one_hot_log_degree,
            "log_degree_bin": self.log_degree_bin,
        }

    def degree_summary(self) -> Dict[str, object]:
        degrees = self.degree.reshape(-1)
        return {
            "min": int(degrees.min()),
            "median": float(np.median(degrees)),
            "mean": float(degrees.mean()),
            "max": int(degrees.max()),
        }

    def manifest(
        self,
        dataset_id: str,
        feature_file: Path,
        source_graph: str,
        source_label: str,
        version: str,
        leakage_note: str,
    ) -> Dict[str, object]:
        bin_counts = np.bincount(self.log_degree_bin, minlength=self.max_log_bin + 1)
        return {
            "dataset_id": dataset_id,
            "feature_file": str(feature_file),
            "source_graph": source_graph,
            "source_label": source_label,
            "version": version,
            "node_count": int(self.node_ids.shape[0]),
            "policies": {
                "constant": {
                    "shape": list(self.constant.shape),
                    "description": "Control feature: all nodes receive value 1.",
                },
                "degree": {
                    "shape": list(self.degree.shape),
                    "description": "Raw graph degree scalar.",
                },
                "log_degree": {
                    "shape": list(self.log_degree.shape),
                    "description": "Natural log1p graph degree scalar.",
                },
                "one_hot_log_degree": {
                    "shape": list(self.one_hot_log_degree.shape),
                    "formula": f"bin = min(floor(log2(degree + 1)), {self.max_log_bin})",
                    "bin_count": self.max_log_bin + 1,
                    "bin_counts": bin_counts.tolist(),
                },
            },
            "degree_summary": self.degree_summary(),
            "leakage_note": leakage_note,
        }


def one_hot(indices: np.ndarray, num_classes: int) -> np.ndarray:
    if indices.ndim != 1:
        raise ValueError("one_hot expects a 1D array of indices")
    if indices.size and (indices.min() < 0 or indices.max() >= num_classes):
        raise ValueError("one_hot index outside valid class range")
    output = np.zeros((indices.shape[0], num_classes), dtype=np.float32)
    output[np.arange(indices.shape[0]), indices] = 1.0
    return output


def log_degree_bins(degrees: np.ndarray, max_log_bin: int = 8) -> np.ndarray:
    degree_vector = np.asarray(degrees).reshape(-1)
    if np.any(degree_vector < 0):
        raise ValueError("degrees must be non-negative")
    bins = np.floor(np.log2(degree_vector.astype(np.float64) + 1)).astype(np.int64)
    return np.clip(bins, 0, max_log_bin)


def build_structural_features(
    node_ids: np.ndarray,
    degrees: np.ndarray,
    max_log_bin: int = 8,
) -> StructuralFeatureBundle:
    node_ids = np.asarray(node_ids, dtype=str).reshape(-1)
    degree_vector = np.asarray(degrees, dtype=np.int64).reshape(-1)
    if degree_vector.shape[0] != node_ids.shape[0]:
        raise ValueError(f"degree length {degree_vector.shape[0]} does not match node count {node_ids.shape[0]}")

    bins = log_degree_bins(degree_vector, max_log_bin=max_log_bin)
    constant = np.ones((node_ids.shape[0], 1), dtype=np.float32)
    degree_scalar = degree_vector.astype(np.float32).reshape(-1, 1)
    log_degree_scalar = np.log1p(degree_vector).astype(np.float32).reshape(-1, 1)
    one_hot_log_degree = one_hot(bins, max_log_bin + 1)

    return StructuralFeatureBundle(
        node_ids=node_ids,
        constant=constant,
        degree=degree_scalar,
        log_degree=log_degree_scalar,
        one_hot_log_degree=one_hot_log_degree,
        log_degree_bin=bins,
        max_log_bin=max_log_bin,
    )


def validate_structural_feature_bundle(bundle: StructuralFeatureBundle) -> list:
    errors = []
    n_nodes = bundle.node_ids.shape[0]
    for name, matrix in (
        ("constant", bundle.constant),
        ("degree", bundle.degree),
        ("log_degree", bundle.log_degree),
        ("one_hot_log_degree", bundle.one_hot_log_degree),
    ):
        if matrix.shape[0] != n_nodes:
            errors.append(f"{name} row count mismatch")
        if not np.isfinite(matrix).all():
            errors.append(f"{name} contains non-finite values")

    if bundle.constant.shape != (n_nodes, 1) or not np.allclose(bundle.constant, 1.0):
        errors.append("constant feature is not all ones with shape N x 1")
    if bundle.degree.shape != (n_nodes, 1):
        errors.append("degree feature is not N x 1")
    if bundle.log_degree.shape != (n_nodes, 1):
        errors.append("log_degree feature is not N x 1")
    if bundle.one_hot_log_degree.shape != (n_nodes, bundle.max_log_bin + 1):
        errors.append("one_hot_log_degree has unexpected shape")
    if not np.allclose(bundle.one_hot_log_degree.sum(axis=1), 1.0):
        errors.append("one_hot_log_degree rows do not sum to 1")
    if not np.all((bundle.one_hot_log_degree == 0.0) | (bundle.one_hot_log_degree == 1.0)):
        errors.append("one_hot_log_degree contains non-binary values")
    if bundle.log_degree_bin.size and (bundle.log_degree_bin.min() < 0 or bundle.log_degree_bin.max() > bundle.max_log_bin):
        errors.append("log_degree_bin outside expected range")
    if not np.array_equal(bundle.one_hot_log_degree.argmax(axis=1), bundle.log_degree_bin):
        errors.append("one_hot argmax does not match log_degree_bin")
    return errors
