"""W05: three baselines through the harness. Scores 2023 (tune) and the rolling origin only; the test set is untouched.

    python src/baselines.py            # real table.parquet
    python src/baselines.py --synthetic
"""
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import average_precision_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import FunctionTransformer, StandardScaler

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from evaluate import evaluate, leave_one_region_out, rolling_origin, without_akosombo  # noqa: E402

RAIN = ["rain_1d_mm", "rain_3d_mm", "rain_7d_mm", "rain_14d_mm", "rain_30d_mm", "rain_max1d_7d_mm"]
OUT = ROOT / "learnings" / "tables"


def seasonal(train, pred):
    """Flood rate for this region and calendar month in the training years."""
    rate = train.groupby(["region_id", "month"]).flood.mean().rename("p")
    p = pred.join(rate, on=["region_id", "month"]).p
    return p.fillna(train.flood.mean()).to_numpy()


def rain_rule(train, pred):
    """Rank by rain over one window; the window is the one with the best PR-AUC in the training years."""
    best = max(RAIN, key=lambda c: average_precision_score(train.flood, train[c]))
    rain_rule.chosen = best
    return pred[best].to_numpy()  # a ranking score in mm, not a probability (Brier not defined)


def logistic(train, pred):
    """Logistic regression on log rain and soil moisture."""
    cols = RAIN + ["soil_moisture"]
    m = make_pipeline(FunctionTransformer(np.log1p), StandardScaler(), LogisticRegression(max_iter=1000))
    return m.fit(train[cols], train.flood).predict_proba(pred[cols])[:, 1]


MODELS = {"seasonal_rate": seasonal, "rain_rule": rain_rule, "logistic_rain": logistic}

if __name__ == "__main__":
    syn = "--synthetic" in sys.argv
    df = pd.read_parquet(ROOT / "data" / "processed" / ("table_synthetic.parquet" if syn else "table.parquet"))
    tag = "_synthetic" if syn else ""
    rows, roll, loro = [], [], []
    for name, fp in MODELS.items():
        rows.append({"model": name, "eval": "tune_2023", **evaluate(fp, df)})
        if name == "rain_rule":
            rows[-1]["note"] = f"window chosen on train: {rain_rule.chosen}"
        rows.append({"model": name, "eval": "tune_2023_without_akosombo", **evaluate(fp, without_akosombo(df))})
        roll.append(rolling_origin(fp, df).assign(model=name))
        loro.append({"model": name, "eval": "leave_one_region_out_2015_2023", **leave_one_region_out(fp, df, n_boot=200)})
    t, r, l = pd.DataFrame(rows), pd.concat(roll), pd.DataFrame(loro)
    OUT.mkdir(parents=True, exist_ok=True)
    t.round(4).to_csv(OUT / f"baselines{tag}.csv", index=False)
    r.round(4).to_csv(OUT / f"baselines_rolling_origin{tag}.csv", index=False)
    l.round(4).to_csv(OUT / f"baselines_leave_one_region_out{tag}.csv", index=False)
    show = ["model", "eval", "pr_auc", "pr_auc_lo", "pr_auc_hi", "roc_auc", "recall_at_3", "recall_at_3_lo", "recall_at_3_hi", "brier", "base_rate", "positives"]
    print(t[show].round(3).to_string(index=False))
    print(r.pivot(index="year", columns="model", values="pr_auc").round(3).assign(base_rate=r.groupby("year").base_rate.first().round(3)).to_string())
    print(l[["model", "pr_auc", "roc_auc", "recall_at_3"]].round(3).to_string(index=False))
