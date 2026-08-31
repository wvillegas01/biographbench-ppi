# Data Availability

BioGraphBench-PPI uses public source datasets from STRING, BioGRID, and OBNB. Raw third-party files are not redistributed in this repository. Users should obtain them from the original providers according to their licenses and terms of use.

This repository includes:

- source manifests and checksums where available;
- canonicalization and filtering scripts;
- split-generation scripts and validation tests;
- machine-readable split manifests;
- raw per-seed benchmark results produced by the retained baseline models;
- statistical summaries used in manuscript tables and figures;
- figure and table generation scripts.

Large split files containing per-seed positive and sampled-nonedge CSV files should be archived as a versioned release asset or Zenodo dataset/software artifact. The local source path for the full split package is:

`C:\Users\wilop\Dropbox\MPDI\2026\BioGraphBench\Auditoria\data\processed\phase1_ppi_multiseed_splits`

Before resubmission, replace repository placeholders in this file, `CITATION.cff`, `.zenodo.json`, and the manuscript with the active GitHub URL and Zenodo DOI.
