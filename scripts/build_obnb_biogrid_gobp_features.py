"""Build initial node features for OBNB BioGRID+GOBP.

Feature policies:
- constant: one scalar equal to 1 for every node.
- one_hot_log_degree: floor(log2(degree + 1)) capped to 8, one-hot encoded.

Degrees are computed from the OBNB BioGRID graph structure. For the current
OBNB node-classification pilot, the graph split is study-bias over nodes rather
than an edge holdout split, so the structural graph is treated as the benchmark
input. This policy is documented explicitly in reports/feature_policy.md.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
from obnb.dataset import OpenBiomedNetBench


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from biographbench.features import build_structural_features, validate_structural_feature_bundle

OBNB_ROOT = ROOT / "data" / "obnb"
OUT_DIR = ROOT / "data" / "processed" / "obnb_biogrid_gobp"
REPORTS_DIR = ROOT / "reports"

VERSION = "obnbdata-0.1.0"
GRAPH_NAME = "BioGRID"
LABEL_NAME = "GOBP"
MAX_LOG_BIN = 8


def build_features() -> dict[str, object]:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    dataset = OpenBiomedNetBench(
        root=str(OBNB_ROOT),
        graph_name=GRAPH_NAME,
        label_name=LABEL_NAME,
        version=VERSION,
        graph_as_feature=False,
    )

    node_ids = np.asarray(dataset.graph.node_ids, dtype=str)
    degrees = np.asarray(dataset.graph.degree(), dtype=np.int64).reshape(-1)
    bundle = build_structural_features(node_ids=node_ids, degrees=degrees, max_log_bin=MAX_LOG_BIN)
    errors = validate_structural_feature_bundle(bundle)
    if errors:
        raise RuntimeError(f"Invalid structural features: {errors}")

    np.savez_compressed(
        OUT_DIR / "features.npz",
        **bundle.arrays(),
    )

    manifest = bundle.manifest(
        dataset_id="obnb_biogrid_gobp",
        feature_file=OUT_DIR / "features.npz",
        source_graph=GRAPH_NAME,
        source_label=LABEL_NAME,
        version=VERSION,
        leakage_note="Computed from OBNB benchmark graph. For edge-holdout tasks, analogous structural features must be computed train-only.",
    )
    (OUT_DIR / "feature_manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    (REPORTS_DIR / "obnb_biogrid_gobp_features.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return manifest


def write_policy_report(manifest: dict[str, object]) -> None:
    bins = manifest["policies"]["one_hot_log_degree"]["bin_counts"]
    lines = [
        "# Feature Policy",
        "",
        "Fecha: 2026-08-05",
        "",
        "## Decision",
        "",
        "La feature principal inicial para `obnb_biogrid_gobp` sera `one_hot_log_degree`, acompanada por una feature constante como control.",
        "",
        "## Politicas implementadas",
        "",
        "| Feature | Dimension | Uso |",
        "|---|---:|---|",
        "| `constant` | 1 | Control sin informacion estructural explicita |",
        "| `degree` | 1 | Baseline compacto con grado crudo |",
        "| `log_degree` | 1 | Baseline compacto con grado suavizado |",
        "| `one_hot_log_degree` | 9 | Feature principal inicial |",
        "",
        "Formula:",
        "",
        "```text",
        f"bin = min(floor(log2(degree + 1)), {MAX_LOG_BIN})",
        "x = one_hot(bin)",
        "```",
        "",
        "## Distribucion de bins",
        "",
        "| Bin | Nodos |",
        "|---:|---:|",
    ]
    for idx, count in enumerate(bins):
        label = f"{idx}" if idx < MAX_LOG_BIN else f"{MAX_LOG_BIN}+"
        lines.append(f"| {label} | {count} |")

    degree_summary = manifest["degree_summary"]
    lines.extend(
        [
            "",
            "## Degree Summary",
            "",
            f"- Min: `{degree_summary['min']}`",
            f"- Median: `{degree_summary['median']}`",
            f"- Mean: `{degree_summary['mean']:.4f}`",
            f"- Max: `{degree_summary['max']}`",
            "",
            "## Leakage Policy",
            "",
            "Para este piloto de OBNB, el split es por nodos con study bias, no por aristas retenidas. Por tanto, el grafo OBNB se trata como entrada estructural del benchmark y el grado se calcula sobre ese grafo.",
            "",
            "Para tareas de link prediction o cualquier split con aristas retenidas, esta regla cambia: toda feature estructural debe calcularse solo sobre el grafo de entrenamiento.",
            "",
            "## Archivos",
            "",
            f"- `{manifest['feature_file']}`",
            f"- `{OUT_DIR / 'feature_manifest.json'}`",
        ]
    )
    (REPORTS_DIR / "feature_policy.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    manifest = build_features()
    write_policy_report(manifest)
    print(
        "Built OBNB BioGRID+GOBP features: "
        f"constant={manifest['policies']['constant']['shape']}, "
        f"one_hot_log_degree={manifest['policies']['one_hot_log_degree']['shape']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
