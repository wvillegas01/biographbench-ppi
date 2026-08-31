# Phase 1 PPI Manuscript Revision Log

Output document:

- `C:\Users\wilop\Dropbox\MPDI\2026\BioGraphBench\BioGraphBench_Frontiers_working_manuscript_PPI_revised.docx`

Backup of the pre-revision manuscript:

- `C:\Users\wilop\Dropbox\MPDI\2026\BioGraphBench\BioGraphBench_Frontiers_working_manuscript.before_phase1_ppi_revision.docx`

## Surgical Changes Applied

- Refocused the title, running title, abstract, keywords, introduction, discussion, and conclusion on the PPI-focused Camino A.
- Removed central claims based on fixed seed 42 and replaced them with the completed Phase 1 protocol:
  - 10 seeds: 42-51.
  - Three negative-sampling contracts: random, degree-matched, and two-hop.
  - Classical structural baselines plus node2vec-compatible random-walk baseline.
  - Calibration, runtime diagnostics, confidence intervals, paired tests, and effect sizes.
- Rebuilt the Results section around four quantitative claims:
  - Four auditable PPI tasks and 120 split contracts.
  - Random negatives inflate apparent performance.
  - Degree-matched and two-hop negatives change task difficulty.
  - Model rankings depend on the negative-sampling contract.
- Replaced the old figure set with four new quantitative PNG figures:
  - HGB seed distributions.
  - Paired negative-regime drops.
  - Model-family regime profiles.
  - Calibration and runtime diagnostics.
- Rebuilt manuscript tables:
  - Table 1: accepted PPI tasks.
  - Table 2: PPI scale and per-seed positive partitions.
  - Table 3: mean test AUPRC by model and negative regime.
  - Table 4: HGB sensitivity to negative-sampling contracts.
- Removed the node-classification result section, Figure 5, Table 5, and OBNB as an empirical result so the manuscript does not overclaim beyond the focused PPI study.

## QA Performed

- DOCX package integrity check: passed.
- Active inline figures: 4.
- Active tables: 4.
- Empty table cells: 0.
- Conflict-string search:
  - `seed 42`: 0 manuscript hits.
  - `fixed-seed`: 0 manuscript hits.
  - `single seed`: 0 manuscript hits.
  - `Figure 5`: 0 manuscript hits.
  - `Table 5`: 0 manuscript hits.
  - `node-classification`: 0 manuscript hits.

## Visual QA Note

Full DOCX-to-PNG rendering could not be completed because the local render pipeline could not find a LibreOffice or soffice executable. Structural QA was completed instead.
