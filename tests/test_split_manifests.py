from biographbench.paths import data_dir
from biographbench.validation import validate_split_manifest


def test_link_prediction_split_manifests_are_clean():
    processed = data_dir() / "processed"
    manifests = [
        processed / "string_human_physical_v12" / "split_manifest.json",
        processed / "biogrid_human_physical" / "splits" / "split_manifest.json",
        processed / "biogrid_human_physical_no_string_overlap" / "splits" / "split_manifest.json",
        processed / "string_human_physical_no_biogrid_overlap" / "splits" / "split_manifest.json",
    ]

    errors = []
    for manifest in manifests:
        errors.extend(validate_split_manifest(manifest))
    assert errors == []
