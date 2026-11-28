"""W12: figures for the technical report, in the report colours.

    python src/report_figures.py      # needs data/processed/labels.parquet

Writes learnings/figures/report_fig1_labels.png and report_fig2_pipeline.png (6.5 in wide, for a Letter page).
"""
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib import font_manager as fm  # noqa: E402
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch  # noqa: E402
import pandas as pd  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from synthetic import REGIONS  # noqa: E402

FIG = ROOT / "learnings" / "figures"
RED, MAROON, INK, MUTED, TINT, GOLD = "#C9482E", "#6E1A30", "#2A1A20", "#76666B", "#FDF2EA", "#F6BE52"

for f in Path.home().joinpath("Library/Fonts").glob("Poppins-*.ttf"):  # the report font, if installed
    fm.fontManager.addfont(str(f))
plt.rcParams.update({
    "font.family": ["Poppins", "DejaVu Sans"], "font.size": 8, "axes.edgecolor": "#D9C9C0", "axes.labelcolor": MUTED,
    "xtick.color": MUTED, "ytick.color": MUTED, "axes.spines.top": False, "axes.spines.right": False,
    "axes.titlesize": 9, "axes.titlecolor": INK, "axes.titleweight": "bold", "axes.titlelocation": "left",
})


def fig1_labels():
    lab = pd.read_parquet(ROOT / "data" / "processed" / "labels.parquet")
    per_year = lab.groupby(lab.week_start.dt.year).n_events.sum()
    per_month = lab.groupby(lab.week_start.dt.month).flood.mean() * 100
    per_region = (lab.groupby("region_id").flood.mean() * 100).rename(index=REGIONS).sort_values()
    assert per_year.sum() == lab.n_events.sum() and len(per_region) == 16

    fig, ax = plt.subplots(1, 3, figsize=(7.6, 2.9), gridspec_kw={"width_ratios": [1.15, 1, 1.1]})
    ax[0].bar(per_year.index.astype(str), per_year.values, color=RED, width=0.7)
    ax[0].set_title("Reports per year")
    for x, v in zip(per_year.index.astype(str), per_year.values):
        if x in ("2015", "2022", "2025"):
            ax[0].text(x, v + 6, f"{v}", ha="center", fontsize=7, color=INK)
    ax[0].set_xticks(["2015", "2018", "2021", "2024"])

    months = list("JFMAMJJASOND")
    ax[1].bar(range(12), per_month.values, color=RED, width=0.7)
    ax[1].set_xticks(range(12), months, fontsize=7)
    ax[1].set_title("% of weeks flooded, by month")
    for i in (5, 8):
        ax[1].text(i, per_month.values[i] + 0.4, f"{per_month.values[i]:.0f}%", ha="center", fontsize=7, color=INK)

    colors = [MAROON if n == "Greater Accra" else (MUTED if v == 0 else RED) for n, v in per_region.items()]
    ax[2].barh(per_region.index, per_region.values, color=colors, height=0.7)
    ax[2].set_title("% of weeks flooded, by region", loc="right")
    ax[2].tick_params(axis="y", labelsize=6.5)
    ax[2].text(per_region.max() + 0.5, 15, f"{per_region.max():.0f}%", va="center", fontsize=7, color=INK)
    ax[2].text(0.5, 0, "none", va="center", fontsize=6.5, color=MUTED)
    for a in ax:
        a.grid(axis="y" if a is not ax[2] else "x", color="#EFE4DD", linewidth=0.6)
        a.set_axisbelow(True)
    fig.tight_layout(w_pad=1.2)
    fig.savefig(FIG / "report_fig1_labels.png", dpi=220)
    return per_year, per_month, per_region


def fig2_pipeline():
    fig, ax = plt.subplots(figsize=(7.6, 2.9))
    ax.set_xlim(0, 100); ax.set_ylim(0, 42); ax.axis("off")

    def box(x, y, w, h, title, sub, fill=TINT, fg=INK):
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.3,rounding_size=1.6", fc=fill, ec="none"))
        ax.text(x + w / 2, y + h * 0.64, title, ha="center", va="center", fontsize=7.5, fontweight="bold", color=fg)
        ax.text(x + w / 2, y + h * 0.28, sub, ha="center", va="center", fontsize=6, color=fg if fill != TINT else MUTED)

    def arrow(x0, y0, x1, y1):
        ax.add_patch(FancyArrowPatch((x0, y0), (x1, y1), arrowstyle="-|>", mutation_scale=8, color=MUTED, lw=0.9))

    sources = [("Groundsource", "news-reported floods"), ("geoBoundaries", "16 region borders"),
               ("CHIRPS", "daily satellite rain"), ("ERA5-Land", "daily soil moisture")]
    for i, (t, s) in enumerate(sources):
        box(1, 33 - i * 10, 17, 7, t, s)
    ax.text(9.5, 41.5, "Sources", ha="center", fontsize=7, color=MUTED)

    box(24, 28, 23, 9, "labels.py", "flood = a report starts\nin the region that week")
    box(24, 4, 23, 9, "weather.py", "rain and soil moisture\nfrom days before Monday")
    ax.text(35.5, 41.5, "Build (with self-checks)", ha="center", fontsize=7, color=MUTED)
    arrow(18.6, 36.5, 23.4, 34.0)   # Groundsource -> labels
    arrow(18.6, 26.5, 23.4, 30.5)   # regions -> labels
    arrow(18.6, 26.5, 23.4, 12.0)   # regions -> weather
    arrow(18.6, 16.5, 23.4, 9.0)    # CHIRPS -> weather
    arrow(18.6, 6.5, 23.4, 6.5)     # ERA5 -> weather

    box(52, 16, 17, 9, "build_table.py", "9,184 region-weeks", fill=MAROON, fg="white")
    arrow(47.6, 32.5, 51.4, 23.0)
    arrow(47.6, 8.5, 51.4, 18.0)

    box(74, 28, 25, 9, "evaluate.py", "train 2015–22 · tune 2023\ntest 2024–25 once")
    box(74, 4, 25, 13, "Models, dashboard", "baselines, ≥ 4 models,\nweekly risk by region")
    arrow(69.6, 21.5, 73.4, 31.5)
    arrow(86.5, 27.4, 86.5, 17.6)
    ax.text(86.5, 41.5, "Evaluate and use", ha="center", fontsize=7, color=MUTED)
    fig.savefig(FIG / "report_fig2_pipeline.png", dpi=220, bbox_inches="tight", pad_inches=0.05)


if __name__ == "__main__":
    y, m, r = fig1_labels()
    assert y[2015] == 123 and y[2022] == 333 and m.idxmax() == 6 and r.idxmin() == "Ahafo", (y, m, r)
    fig2_pipeline()
    print("wrote report_fig1_labels.png and report_fig2_pipeline.png")
