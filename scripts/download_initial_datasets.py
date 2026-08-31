"""Download the initial BioGraphBench audit datasets.

The script stores untouched source files in data/raw and writes one JSON
manifest per file in data/manifests with URL, size and SHA-256.
"""

from __future__ import annotations

import datetime as dt
import hashlib
import json
from pathlib import Path

import requests


ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "data" / "raw"
MANIFEST_DIR = ROOT / "data" / "manifests"


DATASETS = [
    {
        "dataset_id": "string_human_physical_v12",
        "filename": "9606.protein.physical.links.v12.0.txt.gz",
        "url": "https://stringdb-downloads.org/download/protein.physical.links.v12.0/9606.protein.physical.links.v12.0.txt.gz",
        "source": "STRING",
        "version": "12.0",
        "license": "CC BY 4.0",
    },
    {
        "dataset_id": "string_human_aliases_v12",
        "filename": "9606.protein.aliases.v12.0.txt.gz",
        "url": "https://stringdb-downloads.org/download/protein.aliases.v12.0/9606.protein.aliases.v12.0.txt.gz",
        "source": "STRING",
        "version": "12.0",
        "license": "CC BY 4.0",
    },
    {
        "dataset_id": "openbiolink2020_hq_directed",
        "filename": "HQ_DIR.zip",
        "url": "https://zenodo.org/api/records/3834052/files/HQ_DIR.zip/content",
        "source": "OpenBioLink / Zenodo",
        "version": "2020",
        "license": "CC BY 4.0",
    },
    {
        "dataset_id": "biogrid_organism_latest_tab3",
        "filename": "BIOGRID-ORGANISM-LATEST.tab3.zip",
        "url": "https://downloads.thebiogrid.org/Download/BioGRID/Latest-Release/BIOGRID-ORGANISM-LATEST.tab3.zip",
        "source": "BioGRID",
        "version": "5.0.260 latest release observed 2026-08-04",
        "license": "MIT",
    },
]


def download(dataset: dict[str, str]) -> dict[str, object]:
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    MANIFEST_DIR.mkdir(parents=True, exist_ok=True)

    output_path = RAW_DIR / dataset["filename"]
    temp_path = output_path.with_suffix(output_path.suffix + ".part")
    sha256 = hashlib.sha256()
    bytes_written = 0

    if output_path.exists():
        with output_path.open("rb") as handle:
            for chunk in iter(lambda: handle.read(1024 * 1024), b""):
                sha256.update(chunk)
                bytes_written += len(chunk)
        status = "already_present"
    else:
        with requests.get(dataset["url"], stream=True, timeout=60) as response:
            response.raise_for_status()
            with temp_path.open("wb") as handle:
                for chunk in response.iter_content(chunk_size=1024 * 1024):
                    if not chunk:
                        continue
                    handle.write(chunk)
                    sha256.update(chunk)
                    bytes_written += len(chunk)
        temp_path.replace(output_path)
        status = "downloaded"

    manifest = {
        "dataset_id": dataset["dataset_id"],
        "source": dataset["source"],
        "version": dataset["version"],
        "license": dataset["license"],
        "url": dataset["url"],
        "filename": dataset["filename"],
        "path": str(output_path),
        "download_date_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "status": status,
        "size_bytes": bytes_written,
        "sha256": sha256.hexdigest(),
    }

    manifest_path = MANIFEST_DIR / f"{dataset['dataset_id']}.json"
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return manifest


def main() -> int:
    for dataset in DATASETS:
        manifest = download(dataset)
        print(
            f"{manifest['status']}: {manifest['dataset_id']} "
            f"{manifest['size_bytes']} bytes sha256={manifest['sha256']}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
