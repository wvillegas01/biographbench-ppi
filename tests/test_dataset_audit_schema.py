from biographbench.paths import reports_dir
from biographbench.validation import validate_dataset_audit_csv


def test_dataset_audit_has_required_schema_and_content():
    errors = validate_dataset_audit_csv(reports_dir() / "dataset_audit.csv")
    assert errors == []
