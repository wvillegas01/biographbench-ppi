from biographbench.paths import data_dir
from biographbench.validation import validate_obnb_feature_bundle


def test_obnb_feature_bundle_is_aligned_with_labels_and_splits():
    base = data_dir() / "processed" / "obnb_biogrid_gobp"
    errors = validate_obnb_feature_bundle(base / "features.npz", base / "node_classification_arrays.npz")
    assert errors == []
