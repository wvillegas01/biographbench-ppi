from pathlib import Path


def project_root() -> Path:
    """Return the audit repository root from the installed source tree."""
    return Path(__file__).resolve().parents[2]


def data_dir() -> Path:
    return project_root() / "data"


def reports_dir() -> Path:
    return project_root() / "reports"


def results_dir() -> Path:
    return project_root() / "results"


def require_file(path: Path) -> Path:
    if not path.is_file():
        raise FileNotFoundError(f"Required file is missing: {path}")
    return path


def require_dir(path: Path) -> Path:
    if not path.is_dir():
        raise FileNotFoundError(f"Required directory is missing: {path}")
    return path
