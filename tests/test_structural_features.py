import numpy as np
import pytest

from biographbench.features import build_structural_features, log_degree_bins, one_hot, validate_structural_feature_bundle


def test_log_degree_bins_follow_policy_with_cap():
    degrees = np.asarray([0, 1, 2, 3, 4, 7, 8, 255, 256, 9999])

    bins = log_degree_bins(degrees, max_log_bin=8)

    assert bins.tolist() == [0, 1, 1, 2, 2, 3, 3, 8, 8, 8]


def test_build_structural_features_shapes_and_values():
    node_ids = np.asarray(["n0", "n1", "n2", "n3"])
    degrees = np.asarray([0, 1, 3, 8])

    bundle = build_structural_features(node_ids, degrees, max_log_bin=4)

    assert bundle.constant.shape == (4, 1)
    assert np.allclose(bundle.constant, 1.0)
    assert bundle.degree.reshape(-1).tolist() == [0.0, 1.0, 3.0, 8.0]
    assert np.allclose(bundle.log_degree.reshape(-1), np.log1p(degrees))
    assert bundle.log_degree_bin.tolist() == [0, 1, 2, 3]
    assert bundle.one_hot_log_degree.shape == (4, 5)
    assert np.array_equal(bundle.one_hot_log_degree.argmax(axis=1), bundle.log_degree_bin)
    assert validate_structural_feature_bundle(bundle) == []


def test_one_hot_rejects_invalid_indices():
    with pytest.raises(ValueError, match="outside valid class range"):
        one_hot(np.asarray([0, 3]), num_classes=3)


def test_build_structural_features_rejects_misaligned_degrees():
    with pytest.raises(ValueError, match="does not match node count"):
        build_structural_features(np.asarray(["a", "b"]), np.asarray([1]))
