from __future__ import annotations

import csv
import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(__file__).resolve().parents[1]
ARTICLE_DIR = ROOT / "Articulo"
FIG_DIR = ARTICLE_DIR / "figures"
REPORTS_DIR = ROOT / "reports"

STYLE = {
    "bg": "#ececf4",
    "grid": "#ffffff",
    "ink": "#202938",
    "muted": "#697386",
    "blue": "#1f77b4",
    "orange": "#ff7f0e",
    "green": "#2ca02c",
    "red": "#d62728",
    "purple": "#7b61b8",
    "teal": "#17a2a4",
    "gray": "#7b8494",
}

DATASET_ORDER = [
    "string_human_physical_v12",
    "biogrid_human_physical",
    "biogrid_human_physical_no_string_overlap",
    "string_human_physical_no_biogrid_overlap",
]

DATASET_LABELS = {
    "string_human_physical_v12": "STRING",
    "biogrid_human_physical": "BioGRID",
    "biogrid_human_physical_no_string_overlap": "BioGRID\nno STRING",
    "string_human_physical_no_biogrid_overlap": "STRING\nno BioGRID",
}

MODEL_LABELS = {
    "common_neighbors": "CN",
    "jaccard": "Jaccard",
    "adamic_adar": "AA",
    "preferential_attachment": "PA",
    "logistic_regression": "LogReg",
    "random_forest": "RF",
    "hist_gradient_boosting": "HGB",
}

HEURISTICS = ["common_neighbors", "jaccard", "adamic_adar", "preferential_attachment"]
SUPERVISED = ["logistic_regression", "random_forest", "hist_gradient_boosting"]
ALL_LP_MODELS = HEURISTICS + SUPERVISED


def setup() -> None:
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    plt.rcParams.update(
        {
            "figure.dpi": 150,
            "savefig.dpi": 320,
            "font.family": "DejaVu Sans",
            "font.size": 9,
            "axes.titlesize": 10,
            "axes.labelsize": 9,
            "legend.fontsize": 8,
            "xtick.labelsize": 8,
            "ytick.labelsize": 8,
        }
    )


def style_axis(ax) -> None:
    ax.set_facecolor(STYLE["bg"])
    ax.grid(True, color=STYLE["grid"], linewidth=1.0, alpha=0.85)
    ax.set_axisbelow(True)
    ax.spines[["top", "right"]].set_visible(False)
    ax.spines[["left", "bottom"]].set_color("#c0c5cf")
    ax.tick_params(colors=STYLE["ink"])
    ax.title.set_color(STYLE["ink"])
    ax.xaxis.label.set_color(STYLE["ink"])
    ax.yaxis.label.set_color(STYLE["ink"])


def save(fig: plt.Figure, filename: str) -> None:
    fig.savefig(FIG_DIR / filename, bbox_inches="tight", facecolor="white")
    plt.close(fig)


def read_csv_rows(path: Path):
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def lp_matrix(metric: str, models=ALL_LP_MODELS) -> np.ndarray:
    rows = read_csv_rows(REPORTS_DIR / "model_baseline_matrix.csv")
    matrix = np.zeros((len(models), len(DATASET_ORDER)))
    for i, model in enumerate(models):
        for j, dataset in enumerate(DATASET_ORDER):
            row = next(
                r
                for r in rows
                if r["task"] == "link_prediction" and r["dataset"] == dataset and r["model"] == model
            )
            matrix[i, j] = float(row[metric])
    return matrix


def figure_1_metric_profiles() -> None:
    x = np.arange(len(DATASET_ORDER))
    colors = {
        "logistic_regression": STYLE["blue"],
        "random_forest": STYLE["green"],
        "hist_gradient_boosting": STYLE["orange"],
    }
    markers = {"logistic_regression": "o", "random_forest": "s", "hist_gradient_boosting": "^"}
    rows = [r for r in read_json(REPORTS_DIR / "link_prediction_supervised.json") if r["split"] == "test"]

    fig, axes = plt.subplots(1, 2, figsize=(12.8, 4.8), sharex=True)
    fig.suptitle("Supervised link-prediction profiles across accepted PPI tasks", fontsize=12, weight="bold", color=STYLE["ink"])
    for ax, metric, title in zip(axes, ["auroc", "auprc"], ["A. Test AUROC", "B. Test AUPRC"]):
        style_axis(ax)
        for model in SUPERVISED:
            values = [
                float(next(r for r in rows if r["dataset"] == dataset and r["model"] == model)[metric])
                for dataset in DATASET_ORDER
            ]
            ax.plot(
                x,
                values,
                color=colors[model],
                marker=markers[model],
                linewidth=2.1,
                markersize=6,
                label=MODEL_LABELS[model],
            )
            for xi, value in zip(x, values):
                ax.text(xi, value + 0.0012, f"{value:.3f}", ha="center", fontsize=6.7, color=colors[model])
        ax.set_title(title)
        ax.set_ylim(0.928, 0.968)
        ax.set_ylabel("Score")
        ax.set_xticks(x)
        ax.set_xticklabels([DATASET_LABELS[d] for d in DATASET_ORDER])
    axes[1].legend(frameon=False, loc="lower right")
    save(fig, "figure_1_supervised_metric_profiles.png")


def add_violin_box(ax, matrix: np.ndarray, metric_name: str) -> None:
    style_axis(ax)
    groups = [matrix[i, :] for i in range(matrix.shape[0])]
    parts = ax.violinplot(groups, showmeans=False, showmedians=False, showextrema=False, widths=0.7)
    for idx, body in enumerate(parts["bodies"]):
        body.set_facecolor(STYLE["blue"] if idx < len(HEURISTICS) else STYLE["orange"])
        body.set_edgecolor("none")
        body.set_alpha(0.22)
    ax.boxplot(
        groups,
        widths=0.20,
        patch_artist=True,
        showfliers=False,
        medianprops={"color": STYLE["ink"], "linewidth": 1.2},
        boxprops={"facecolor": "white", "edgecolor": STYLE["ink"], "linewidth": 0.9},
        whiskerprops={"color": STYLE["ink"], "linewidth": 0.9},
        capprops={"color": STYLE["ink"], "linewidth": 0.9},
    )
    task_colors = [STYLE["blue"], STYLE["green"], STYLE["teal"], STYLE["purple"]]
    jitter = np.linspace(-0.10, 0.10, len(DATASET_ORDER))
    for i, values in enumerate(groups, start=1):
        for offset, value, color in zip(jitter, values, task_colors):
            ax.scatter(i + offset, value, s=26, color=color, edgecolor="white", linewidth=0.6, zorder=3)
    ax.set_xticks(np.arange(1, len(ALL_LP_MODELS) + 1))
    ax.set_xticklabels([MODEL_LABELS[m] for m in ALL_LP_MODELS], rotation=0)
    ax.set_ylabel(metric_name)
    ax.set_ylim(0.70 if "AUPRC" in metric_name else 0.78, 0.985)


def figure_2_model_distributions() -> None:
    auroc = lp_matrix("auroc")
    auprc = lp_matrix("auprc")
    fig, axes = plt.subplots(1, 2, figsize=(13.4, 5.2), sharex=True)
    fig.suptitle("Baseline score distributions across four PPI tasks", fontsize=12, weight="bold", color=STYLE["ink"])
    add_violin_box(axes[0], auroc, "A. Test AUROC")
    add_violin_box(axes[1], auprc, "B. Test AUPRC")
    axes[0].text(0.02, 0.04, "Blue violins: classical heuristics", transform=axes[0].transAxes, fontsize=8, color=STYLE["muted"])
    axes[1].text(0.02, 0.04, "Orange violins: supervised pair-heuristic models", transform=axes[1].transAxes, fontsize=8, color=STYLE["muted"])
    save(fig, "figure_2_baseline_distribution_violin_box.png")


def figure_3_gain_and_calibration() -> None:
    summary_rows = read_csv_rows(REPORTS_DIR / "model_baseline_matrix.csv")
    supervised_rows = [r for r in read_json(REPORTS_DIR / "link_prediction_supervised.json") if r["split"] == "test"]

    best_heuristic = {}
    hgb = {}
    for dataset in DATASET_ORDER:
        candidates = [
            r for r in summary_rows if r["task"] == "link_prediction" and r["dataset"] == dataset and r["model"] in HEURISTICS
        ]
        best = max(candidates, key=lambda r: float(r["auprc"]))
        best_heuristic[dataset] = (MODEL_LABELS[best["model"]], float(best["auprc"]))
        row = next(r for r in summary_rows if r["task"] == "link_prediction" and r["dataset"] == dataset and r["model"] == "hist_gradient_boosting")
        hgb[dataset] = float(row["auprc"])

    fig, axes = plt.subplots(1, 2, figsize=(13.2, 5.2))
    fig.suptitle("Added value and reliability of supervised pair-heuristic baselines", fontsize=12, weight="bold", color=STYLE["ink"])

    ax = axes[0]
    style_axis(ax)
    y = np.arange(len(DATASET_ORDER))
    for idx, dataset in enumerate(DATASET_ORDER):
        heuristic_name, heuristic_value = best_heuristic[dataset]
        hgb_value = hgb[dataset]
        ax.plot([heuristic_value, hgb_value], [idx, idx], color=STYLE["gray"], linewidth=2.0)
        ax.scatter(heuristic_value, idx, s=55, color=STYLE["blue"], edgecolor="white", zorder=2, label="Best heuristic" if idx == 0 else "")
        ax.scatter(hgb_value, idx, s=55, color=STYLE["orange"], edgecolor="white", zorder=3, label="HGB" if idx == 0 else "")
        ax.text((heuristic_value + hgb_value) / 2, idx + 0.16, f"+{hgb_value - heuristic_value:.3f}", ha="center", fontsize=8, color=STYLE["ink"])
        ax.text(heuristic_value - 0.002, idx - 0.18, heuristic_name, ha="right", fontsize=7, color=STYLE["blue"])
    ax.set_title("A. Gain over best heuristic")
    ax.set_yticks(y)
    ax.set_yticklabels([DATASET_LABELS[d].replace("\n", " ") for d in DATASET_ORDER])
    ax.set_xlabel("Test AUPRC")
    ax.set_xlim(0.875, 0.972)
    ax.legend(frameon=False, loc="lower right")

    ax = axes[1]
    style_axis(ax)
    model_styles = {
        "logistic_regression": ("LogReg", "o", STYLE["blue"]),
        "random_forest": ("RF", "s", STYLE["green"]),
        "hist_gradient_boosting": ("HGB", "^", STYLE["orange"]),
    }
    for model, (label, marker, color) in model_styles.items():
        subset = [r for r in supervised_rows if r["model"] == model]
        ax.scatter(
            [float(r["ece_10"]) for r in subset],
            [float(r["auprc"]) for r in subset],
            s=[45 + float(r["train_seconds"]) * 2.5 for r in subset],
            marker=marker,
            color=color,
            alpha=0.82,
            edgecolor="white",
            linewidth=0.8,
            label=label,
        )
    ax.axvline(0.01, color=STYLE["red"], linewidth=1.0, linestyle="--", alpha=0.7)
    ax.set_title("B. Calibration-performance trade-off")
    ax.set_xlabel("ECE-10, lower is better")
    ax.set_ylabel("Test AUPRC")
    ax.set_xlim(0, 0.065)
    ax.set_ylim(0.928, 0.968)
    ax.legend(frameon=False, loc="lower right")
    save(fig, "figure_3_gain_and_calibration_panels.png")


def figure_4_node_classification_panels() -> None:
    threshold_rows = [r for r in read_json(REPORTS_DIR / "node_classification_threshold_tuning.json") if r["split"] == "test"]
    logreg_rows = [r for r in read_json(REPORTS_DIR / "node_classification_logreg.json") if r["split"] == "test"]
    models = [
        ("Constant\nLogReg", next(r for r in logreg_rows if r["feature"] == "constant")),
        ("Degree-bin\nLogReg", next(r for r in threshold_rows if r["model"] == "logistic_regression")),
        ("MLP", next(r for r in threshold_rows if r["model"] == "mlp")),
        ("GCN", next(r for r in threshold_rows if r["model"] == "gcn")),
    ]
    x = np.arange(len(models))
    labels = [name for name, _ in models]

    fig, axes = plt.subplots(1, 2, figsize=(12.2, 4.9))
    fig.suptitle("OBNB BioGRID+GOBP node classification: discrimination and decision trade-offs", fontsize=12, weight="bold", color=STYLE["ink"])

    ax = axes[0]
    style_axis(ax)
    auroc = [float(row["macro_auroc"]) for _, row in models]
    auprc = [float(row["macro_auprc"]) for _, row in models]
    ax.plot(x, auroc, marker="o", color=STYLE["blue"], linewidth=2.0, label="Macro AUROC")
    ax2 = ax.twinx()
    ax2.plot(x, auprc, marker="s", color=STYLE["purple"], linewidth=2.0, label="Macro AUPRC")
    ax.set_title("A. Discrimination metrics")
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_ylabel("Macro AUROC")
    ax.set_ylim(0.45, 0.56)
    ax2.set_ylabel("")
    ax2.set_ylim(0.009, 0.018)
    ax2.tick_params(colors=STYLE["purple"])
    ax2.spines["right"].set_color("#c0c5cf")
    for xi, value in zip(x, auroc):
        ax.text(xi, value + 0.004, f"{value:.3f}", ha="center", fontsize=7, color=STYLE["blue"])
    for xi, value in zip(x, auprc):
        ax2.text(xi, value + 0.00035, f"{value:.3f}", ha="center", fontsize=7, color=STYLE["purple"])
    lines, labels_left = ax.get_legend_handles_labels()
    lines2, labels_right = ax2.get_legend_handles_labels()
    ax.legend(lines + lines2, labels_left + labels_right, frameon=False, loc="lower left")

    ax = axes[1]
    style_axis(ax)
    f1 = [float(row.get("micro_f1", 0)) for _, row in models]
    precision = [float(row.get("micro_precision", 0)) for _, row in models]
    recall = [float(row.get("micro_recall", row.get("micro_f1", 0))) for _, row in models]
    ax.plot(x, f1, marker="o", color=STYLE["orange"], linewidth=2.0, label="Tuned Micro-F1")
    ax.plot(x, precision, marker="^", color=STYLE["red"], linewidth=2.0, label="Precision")
    ax.plot(x, recall, marker="s", color=STYLE["green"], linewidth=2.0, label="Recall")
    ax.set_title("B. Threshold-tuned decision metrics")
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_ylabel("Score")
    ax.set_ylim(0, 0.75)
    ax.legend(frameon=False, loc="upper left")
    for series, color in [(f1, STYLE["orange"]), (recall, STYLE["green"])]:
        for xi, value in zip(x, series):
            ax.text(xi, value + 0.018, f"{value:.3f}", ha="center", fontsize=7, color=color)
    save(fig, "figure_4_node_classification_dual_panels.png")


def main() -> int:
    setup()
    figure_1_metric_profiles()
    figure_2_model_distributions()
    figure_3_gain_and_calibration()
    figure_4_node_classification_panels()
    print(f"Generated four two-panel scientific figures in {FIG_DIR}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
