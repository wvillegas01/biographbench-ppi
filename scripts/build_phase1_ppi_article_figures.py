"""Build manuscript-ready quantitative figures and tables for Phase 1 PPI."""

from __future__ import annotations

import math
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


ROOT = Path(__file__).resolve().parents[1]
RESULTS_DIR = ROOT / "results" / "phase1"
ARTICLE_DIR = ROOT / "Articulo"
FIGURES_DIR = ARTICLE_DIR / "figures"
TABLES_DIR = ARTICLE_DIR / "tables"

CLASSICAL_PATH = RESULTS_DIR / "ppi_link_prediction_baselines.csv"
NODE2VEC_PATH = RESULTS_DIR / "ppi_node2vec_link_prediction.csv"

DATASET_LABELS = {
    "string_human_physical_v12": "STRING",
    "biogrid_human_physical": "BioGRID",
    "biogrid_human_physical_no_string_overlap": "BioGRID no-STRING",
    "string_human_physical_no_biogrid_overlap": "STRING no-BioGRID",
}

DATASET_ORDER = [
    "string_human_physical_v12",
    "biogrid_human_physical",
    "string_human_physical_no_biogrid_overlap",
    "biogrid_human_physical_no_string_overlap",
]

NEGATIVE_LABELS = {
    "random": "Random",
    "degree_matched": "Degree-matched",
    "two_hop": "Two-hop",
}

NEGATIVE_ORDER = ["random", "degree_matched", "two_hop"]

MODEL_LABELS = {
    "logistic_regression": "LogReg",
    "random_forest": "RF",
    "hist_gradient_boosting": "HGB",
    "node2vec_walk_logreg": "node2vec",
}

MODEL_ORDER = ["logistic_regression", "random_forest", "hist_gradient_boosting", "node2vec_walk_logreg"]

PALETTE = {
    "random": "#4C78A8",
    "degree_matched": "#F58518",
    "two_hop": "#54A24B",
    "logistic_regression": "#7F7F7F",
    "random_forest": "#4C78A8",
    "hist_gradient_boosting": "#E45756",
    "node2vec_walk_logreg": "#72B7B2",
}


def read_results() -> pd.DataFrame:
    classical = pd.read_csv(CLASSICAL_PATH)
    node2vec = pd.read_csv(NODE2VEC_PATH)
    node2vec = node2vec.assign(model_family="embedding")
    shared = [
        "dataset",
        "negative_strategy",
        "seed",
        "split",
        "model",
        "model_family",
        "auroc",
        "auprc",
        "brier",
        "nll",
        "ece_10",
        "train_seconds",
        "inference_seconds",
        "num_train",
        "num_eval",
    ]
    node2vec["train_seconds"] = node2vec["walk_seconds"] + node2vec["embedding_seconds"] + node2vec["decoder_seconds"]
    data = pd.concat([classical[shared], node2vec[shared]], ignore_index=True)
    data["dataset_label"] = data["dataset"].map(DATASET_LABELS)
    data["negative_label"] = data["negative_strategy"].map(NEGATIVE_LABELS)
    data["model_label"] = data["model"].map(MODEL_LABELS).fillna(data["model"])
    return data


def test_rows(data: pd.DataFrame) -> pd.DataFrame:
    return data[data["split"] == "test"].copy()


def mean_ci(values: pd.Series) -> pd.Series:
    values = values.astype(float)
    n = values.count()
    mean = values.mean()
    sd = values.std(ddof=1) if n > 1 else 0.0
    ci = 1.96 * sd / math.sqrt(n) if n > 1 else 0.0
    return pd.Series(
        {
            "n": n,
            "mean": mean,
            "sd": sd,
            "ci95_low": mean - ci,
            "ci95_high": mean + ci,
        }
    )


def save_summary_tables(data: pd.DataFrame) -> None:
    TABLES_DIR.mkdir(parents=True, exist_ok=True)
    subset = test_rows(data)
    model_subset = subset[subset["model"].isin(MODEL_ORDER)]
    summary = (
        model_subset.groupby(["dataset", "dataset_label", "negative_strategy", "negative_label", "model", "model_label"])[
            "auprc"
        ]
        .apply(mean_ci)
        .unstack()
        .reset_index()
    )
    summary.to_csv(TABLES_DIR / "table_phase1_model_regime_auprc.csv", index=False)

    pivot = summary.pivot_table(
        index=["dataset", "dataset_label", "model", "model_label"],
        columns="negative_strategy",
        values="mean",
    ).reset_index()
    pivot["drop_random_to_degree_matched"] = pivot["random"] - pivot["degree_matched"]
    pivot["drop_random_to_two_hop"] = pivot["random"] - pivot["two_hop"]
    pivot.to_csv(TABLES_DIR / "table_phase1_negative_regime_drops.csv", index=False)

    md_lines = [
        "# Phase 1 Final Quantitative Tables",
        "",
        "Table A reports test AUPRC mean, SD, and 95% CI across 10 seeds for each dataset, negative regime, and model family.",
        "",
        "Table B reports the AUPRC reduction from random negatives to degree-matched and two-hop negatives.",
        "",
        "- `table_phase1_model_regime_auprc.csv`",
        "- `table_phase1_negative_regime_drops.csv`",
    ]
    (TABLES_DIR / "README.md").write_text("\n".join(md_lines) + "\n", encoding="utf-8")


def annotate_panel(ax: plt.Axes, label: str) -> None:
    ax.text(-0.08, 1.04, label, transform=ax.transAxes, fontsize=12, fontweight="bold", va="bottom")


def figure_hgb_distributions(data: pd.DataFrame) -> Path:
    hgb = test_rows(data[data["model"] == "hist_gradient_boosting"])
    complete = hgb[hgb["dataset"].isin(DATASET_ORDER[:2])]
    overlap = hgb[hgb["dataset"].isin(DATASET_ORDER[2:])]
    path = FIGURES_DIR / "fig1_hgb_auprc_seed_distributions.png"

    fig, axes = plt.subplots(1, 2, figsize=(13.5, 5.2), sharey=True)
    for ax, subset, title, label in [
        (axes[0], complete, "Complete PPI graphs", "A"),
        (axes[1], overlap, "Cross-database no-overlap graphs", "B"),
    ]:
        sns.violinplot(
            data=subset,
            x="dataset_label",
            y="auprc",
            hue="negative_strategy",
            hue_order=NEGATIVE_ORDER,
            palette=PALETTE,
            inner=None,
            linewidth=0.9,
            cut=0,
            ax=ax,
        )
        sns.stripplot(
            data=subset,
            x="dataset_label",
            y="auprc",
            hue="negative_strategy",
            hue_order=NEGATIVE_ORDER,
            dodge=True,
            palette=PALETTE,
            size=3.2,
            alpha=0.75,
            linewidth=0.25,
            edgecolor="black",
            ax=ax,
        )
        ax.set_title(title)
        ax.set_xlabel("")
        ax.set_ylabel("Test AUPRC" if ax is axes[0] else "")
        ax.grid(axis="y", alpha=0.25)
        annotate_panel(ax, label)
        handles, labels = ax.get_legend_handles_labels()
        ax.legend(handles[:3], [NEGATIVE_LABELS[x] for x in NEGATIVE_ORDER], title="Negatives", frameon=False)
    fig.suptitle("HGB performance distributions across 10 seeds", y=1.02, fontsize=14, fontweight="bold")
    fig.tight_layout()
    fig.savefig(path, dpi=350, bbox_inches="tight")
    plt.close(fig)
    return path


def figure_negative_drops(data: pd.DataFrame) -> Path:
    hgb = test_rows(data[data["model"] == "hist_gradient_boosting"])
    pivot = hgb.pivot_table(index=["dataset", "dataset_label", "seed"], columns="negative_strategy", values="auprc").reset_index()
    for col in ["degree_matched", "two_hop"]:
        pivot[f"drop_{col}"] = pivot["random"] - pivot[col]

    path = FIGURES_DIR / "fig2_hgb_negative_regime_drops.png"
    fig, axes = plt.subplots(1, 2, figsize=(13.5, 5.2), sharex=True)
    for ax, col, title, label in [
        (axes[0], "drop_degree_matched", "Random minus degree-matched", "A"),
        (axes[1], "drop_two_hop", "Random minus two-hop", "B"),
    ]:
        plot_rows = []
        for dataset in DATASET_ORDER:
            values = pivot[pivot["dataset"] == dataset][col]
            stats = mean_ci(values)
            plot_rows.append(
                {
                    "dataset": dataset,
                    "dataset_label": DATASET_LABELS[dataset],
                    "mean": stats["mean"],
                    "ci95_low": stats["ci95_low"],
                    "ci95_high": stats["ci95_high"],
                }
            )
        plot_df = pd.DataFrame(plot_rows)
        y = np.arange(len(plot_df))
        ax.errorbar(
            plot_df["mean"],
            y,
            xerr=[plot_df["mean"] - plot_df["ci95_low"], plot_df["ci95_high"] - plot_df["mean"]],
            fmt="o",
            color="#333333",
            ecolor="#333333",
            elinewidth=1.4,
            capsize=4,
        )
        for yi, row in zip(y, plot_df.to_dict("records")):
            seed_values = pivot[pivot["dataset"] == row["dataset"]][col]
            ax.scatter(seed_values, np.full(seed_values.shape, yi), s=20, alpha=0.45, color="#4C78A8")
            ax.text(row["ci95_high"] + 0.006, yi, f"{row['mean']:.3f}", va="center", fontsize=9)
        ax.axvline(0, color="#777777", linewidth=0.9, linestyle="--")
        ax.set_yticks(y)
        ax.set_yticklabels(plot_df["dataset_label"])
        ax.invert_yaxis()
        ax.set_title(title)
        ax.set_xlabel("AUPRC difference")
        ax.grid(axis="x", alpha=0.25)
        annotate_panel(ax, label)
    fig.suptitle("Seed-paired performance change induced by harder negative sampling", y=1.02, fontsize=14, fontweight="bold")
    fig.tight_layout()
    fig.savefig(path, dpi=350, bbox_inches="tight")
    plt.close(fig)
    return path


def figure_model_ranking(data: pd.DataFrame) -> Path:
    subset = test_rows(data[data["model"].isin(MODEL_ORDER)])
    summary = (
        subset.groupby(["dataset", "dataset_label", "negative_strategy", "model", "model_label"])["auprc"]
        .mean()
        .reset_index()
    )
    path = FIGURES_DIR / "fig3_model_family_regime_profiles.png"
    fig, axes = plt.subplots(2, 2, figsize=(13.5, 8.6), sharey=False)
    axes = axes.ravel()
    for ax, dataset, label in zip(axes, DATASET_ORDER, ["A", "B", "C", "D"]):
        local = summary[summary["dataset"] == dataset]
        for model in MODEL_ORDER:
            series = local[local["model"] == model].set_index("negative_strategy").reindex(NEGATIVE_ORDER)
            ax.plot(
                [NEGATIVE_LABELS[x] for x in NEGATIVE_ORDER],
                series["auprc"],
                marker="o",
                linewidth=1.8,
                color=PALETTE[model],
                label=MODEL_LABELS[model],
            )
            last_y = float(series["auprc"].iloc[-1])
            ax.text(
                len(NEGATIVE_ORDER) - 1 + 0.03,
                last_y,
                MODEL_LABELS[model],
                ha="left",
                va="center",
                fontsize=8,
                color=PALETTE[model],
            )
        ax.set_title(DATASET_LABELS[dataset])
        ax.set_xlabel("")
        ax.set_ylabel("Mean test AUPRC")
        ax.grid(axis="y", alpha=0.25)
        ax.set_ylim(max(0.55, local["auprc"].min() - 0.06), min(1.0, local["auprc"].max() + 0.04))
        annotate_panel(ax, label)
    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="lower center", ncol=4, frameon=False)
    fig.suptitle("Model-family profiles across negative-sampling regimes", y=1.01, fontsize=14, fontweight="bold")
    fig.tight_layout(rect=[0, 0.06, 1, 1])
    fig.savefig(path, dpi=350, bbox_inches="tight")
    plt.close(fig)
    return path


def figure_calibration_scalability(data: pd.DataFrame) -> Path:
    subset = test_rows(data[data["model"].isin(MODEL_ORDER)])
    path = FIGURES_DIR / "fig4_calibration_and_runtime.png"
    fig, axes = plt.subplots(1, 2, figsize=(13.5, 5.2))

    calibrated = subset.dropna(subset=["ece_10"])
    sns.boxplot(
        data=calibrated,
        x="model_label",
        y="ece_10",
        hue="negative_label",
        hue_order=[NEGATIVE_LABELS[x] for x in NEGATIVE_ORDER],
        palette={NEGATIVE_LABELS[key]: value for key, value in PALETTE.items() if key in NEGATIVE_LABELS},
        ax=axes[0],
        fliersize=1.8,
        linewidth=0.9,
    )
    axes[0].set_title("Calibration error by model and regime")
    axes[0].set_xlabel("")
    axes[0].set_ylabel("ECE-10")
    axes[0].grid(axis="y", alpha=0.25)
    axes[0].legend(title="Negatives", frameon=False)
    annotate_panel(axes[0], "A")

    runtime = subset.copy()
    runtime["train_seconds_plot"] = runtime["train_seconds"].clip(lower=0.001)
    sns.boxplot(
        data=runtime,
        x="model_label",
        y="train_seconds_plot",
        order=[MODEL_LABELS[m] for m in MODEL_ORDER],
        color="#DDDDDD",
        fliersize=0,
        linewidth=0.9,
        ax=axes[1],
    )
    sns.stripplot(
        data=runtime,
        x="model_label",
        y="train_seconds_plot",
        order=[MODEL_LABELS[m] for m in MODEL_ORDER],
        hue="dataset_label",
        hue_order=[DATASET_LABELS[d] for d in DATASET_ORDER],
        dodge=True,
        jitter=0.18,
        size=3.2,
        alpha=0.65,
        edgecolor="black",
        linewidth=0.25,
        ax=axes[1],
    )
    axes[1].set_yscale("log")
    axes[1].set_title("Training-time distribution by model")
    axes[1].set_xlabel("")
    axes[1].set_ylabel("Training seconds, log scale")
    axes[1].grid(axis="y", alpha=0.25, which="both")
    axes[1].legend(title="Dataset", frameon=False, fontsize=8, title_fontsize=9)
    annotate_panel(axes[1], "B")

    fig.suptitle("Calibration and computational cost diagnostics", y=1.02, fontsize=14, fontweight="bold")
    fig.tight_layout()
    fig.savefig(path, dpi=350, bbox_inches="tight")
    plt.close(fig)
    return path


def write_figure_index(paths: list[Path]) -> None:
    lines = [
        "# Phase 1 PPI Article Figures",
        "",
        "All figures are generated from raw Phase 1 result CSV files and saved as 350 dpi PNG.",
        "",
        "| Figure | File | Article role |",
        "|---|---|---|",
        "| Fig. 1 | `fig1_hgb_auprc_seed_distributions.png` | Distribution of HGB test AUPRC across seeds, split by complete and no-overlap graphs. |",
        "| Fig. 2 | `fig2_hgb_negative_regime_drops.png` | Seed-paired AUPRC loss from random negatives to harder negative regimes. |",
        "| Fig. 3 | `fig3_model_family_regime_profiles.png` | Model-family ranking shifts across negative-sampling contracts. |",
        "| Fig. 4 | `fig4_calibration_and_runtime.png` | Calibration and computational-cost diagnostics. |",
        "",
        "Generated files:",
    ]
    lines.extend(f"- `{path}`" for path in paths)
    (FIGURES_DIR / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    sns.set_theme(style="whitegrid", context="paper", font_scale=1.05)
    plt.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "axes.edgecolor": "#333333",
            "axes.linewidth": 0.8,
            "figure.facecolor": "white",
            "axes.facecolor": "white",
            "savefig.facecolor": "white",
        }
    )
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    TABLES_DIR.mkdir(parents=True, exist_ok=True)

    data = read_results()
    save_summary_tables(data)
    paths = [
        figure_hgb_distributions(data),
        figure_negative_drops(data),
        figure_model_ranking(data),
        figure_calibration_scalability(data),
    ]
    write_figure_index(paths)
    for path in paths:
        print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
