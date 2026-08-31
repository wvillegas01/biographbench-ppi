# Full-Length Phase 1 PPI Manuscript Revision Log

Output document:

- `C:\Users\wilop\Dropbox\MPDI\2026\BioGraphBench\BioGraphBench_Frontiers_working_manuscript_PPI_revised_full_length.docx`

Purpose:

- Recover the original long manuscript architecture after the overly condensed PPI-only revision.
- Preserve the base article while correcting claims that became inconsistent after the completed Phase 1 PPI analysis.

## What Was Preserved

- Original article structure and front matter.
- Methodological workflow figure.
- OBNB/node-classification section as a secondary stress-test result.
- Five-table manuscript structure.
- References and standard Frontiers declarations.

## What Was Updated

- Title, running title, abstract, keywords, introduction contribution paragraph.
- Methods text for:
  - 10 predefined seeds.
  - Three PPI negative-sampling regimes: random, degree-matched, and two-hop.
  - node2vec-compatible random-walk baseline.
  - multi-seed statistical summaries.
- PPI Results text around:
  - 120 split contracts.
  - 1,680 classical-baseline rows.
  - 240 node2vec-compatible rows.
  - random-negative inflation.
  - degree-matched and two-hop difficulty.
  - model-ranking shifts.
  - calibration and runtime diagnostics.
- Discussion, limitations, future work, conclusion, and data availability.

## Figure/Table Structure

- Figures: 6 active inline figures.
  - Figure 1: methodological workflow, preserved.
  - Figure 2: HGB AUPRC seed distributions.
  - Figure 3: seed-paired negative-regime drops.
  - Figure 4: model-family regime profiles.
  - Figure 5: calibration and runtime diagnostics.
  - Figure 6: OBNB node-classification trade-offs, preserved and renumbered.
- Tables: 5 active tables.
  - Tables 1-2 preserve accepted task and scale structure.
  - Table 3 updated to multi-seed model/regime AUPRC.
  - Table 4 updated to HGB negative-regime sensitivity.
  - Table 5 preserves OBNB node-classification results.

## QA Performed

- DOCX package integrity check: passed.
- Active inline figures: 6.
- Active tables: 5.
- Empty table cells: 0.
- Conflict-string search:
  - `fixed-seed`: 0 hits.
  - `one seed`: 0 hits.
  - `single seed`: 0 hits.
  - `All results use seed 42`: 0 hits.
  - `Figure 7`: 0 hits.
  - `Table 6`: 0 hits.

## Visual QA Note

Full DOCX-to-PNG rendering could not be completed because the local render pipeline could not find LibreOffice/soffice. Structural QA was completed instead.
