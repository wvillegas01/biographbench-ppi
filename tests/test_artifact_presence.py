from biographbench.paths import data_dir, reports_dir
from biographbench.validation import validate_required_files


def test_core_audit_artifacts_exist():
    required = [
        reports_dir() / "benchmark_gap_analysis.md",
        reports_dir() / "dataset_audit.csv",
        reports_dir() / "pilot_dataset_readiness.md",
        reports_dir() / "baseline_summary.md",
        reports_dir() / "mvp_status_report.md",
        data_dir() / "processed" / "string_human_physical_v12" / "split_manifest.json",
        data_dir() / "processed" / "biogrid_human_physical" / "splits" / "split_manifest.json",
        data_dir() / "processed" / "obnb_biogrid_gobp" / "features.npz",
    ]
    assert validate_required_files(required) == []
