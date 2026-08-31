.PHONY: download inspect quality node-audit node-export node-features string-split biogrid-filter biogrid-split overlap ablations baselines ppi-gcn gnn-pilot validate test readiness reproduce

PYTHON := python

download:
	$(PYTHON) scripts/download_initial_datasets.py

inspect:
	$(PYTHON) scripts/inspect_raw_datasets.py

quality:
	$(PYTHON) scripts/audit_string_quality.py
	$(PYTHON) scripts/audit_openbiolink_quality.py
	$(PYTHON) scripts/audit_biogrid_quality.py

node-audit:
	$(PYTHON) scripts/audit_obnb_node_classification.py

node-export:
	$(PYTHON) scripts/export_obnb_biogrid_gobp.py
	$(PYTHON) scripts/validate_obnb_biogrid_gobp.py

node-features:
	$(PYTHON) scripts/build_obnb_biogrid_gobp_features.py
	$(PYTHON) scripts/validate_obnb_biogrid_gobp_features.py

string-split:
	$(PYTHON) scripts/build_string_pilot_splits.py
	$(PYTHON) scripts/validate_string_pilot_split.py

biogrid-filter:
	$(PYTHON) scripts/build_biogrid_filtered_physical.py
	$(PYTHON) scripts/validate_biogrid_filtered_physical.py

biogrid-split:
	$(PYTHON) scripts/build_biogrid_pilot_splits.py
	$(PYTHON) scripts/validate_biogrid_pilot_split.py

overlap:
	$(PYTHON) scripts/audit_string_biogrid_overlap.py

ablations:
	$(PYTHON) scripts/build_biogrid_no_string_overlap.py
	$(PYTHON) scripts/validate_biogrid_no_string_overlap.py
	$(PYTHON) scripts/build_string_no_biogrid_overlap.py
	$(PYTHON) scripts/validate_string_no_biogrid_overlap.py

baselines:
	$(PYTHON) scripts/run_link_prediction_heuristics.py
	$(PYTHON) scripts/run_link_prediction_supervised.py
	$(PYTHON) scripts/run_node_classification_baseline.py
	$(PYTHON) scripts/build_baseline_summary.py

gnn-pilot:
	$(PYTHON) scripts/run_node_classification_gnn.py
	$(PYTHON) scripts/run_node_classification_threshold_tuning.py
	$(PYTHON) scripts/build_baseline_summary.py

ppi-gcn:
	$(PYTHON) scripts/run_phase1_ppi_gcn_link_prediction.py --resume

validate:
	$(PYTHON) scripts/validate_dataset_audit.py
	$(PYTHON) scripts/validate_string_pilot_split.py
	$(PYTHON) scripts/validate_biogrid_filtered_physical.py
	$(PYTHON) scripts/validate_biogrid_pilot_split.py
	$(PYTHON) scripts/validate_biogrid_no_string_overlap.py
	$(PYTHON) scripts/validate_string_no_biogrid_overlap.py
	$(PYTHON) scripts/validate_obnb_biogrid_gobp.py
	$(PYTHON) scripts/validate_obnb_biogrid_gobp_features.py

test:
	$(PYTHON) -m pytest -q

readiness:
	$(PYTHON) scripts/build_pilot_readiness_report.py

reproduce: download inspect quality node-audit node-export node-features string-split biogrid-filter biogrid-split overlap ablations validate readiness
