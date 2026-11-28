"""Forecast experiment (W02, decision 0004): how much would knowing this week's rain help?

    python src/forecast_experiment.py

`rain_thisweek_mm` is the rain that actually fell during the week being predicted. Nobody has it on Monday,
so the score with it is an upper bound: what a perfect rain forecast could add. It is never used in the main model.
Each model is scored twice, without and with that column, on 2023 (tune) and on the rolling origin 2018-2023.
The 2024-2025 test years are not touched.
"""
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import average_precision_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import FunctionTransformer, StandardScaler

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from evaluate import _point, rolling_origin, split, without_akosombo  # noqa: E402

RAIN = ["rain_1d_mm", "rain_3d_mm", "rain_7d_mm", "rain_14d_mm", "rain_30d_mm", "rain_max1d_7d_mm"]
FX = "rain_thisweek_mm"
OUT = ROOT / "learnings" / "tables"


def logistic(cols):
    def fp(train, pred):
        m = make_pipeline(FunctionTransformer(np.log1p), StandardScaler(), LogisticRegression(max_iter=1000))
        return m.fit(train[cols], train.flood).predict_proba(pred[cols])[:, 1]
    return fp


def forest(cols):
    """Rain plus where and when: region (one-hot), month, floods in the previous 4 weeks."""
    def fp(train, pred):
        X = lambda d: pd.get_dummies(d[cols + ["month", "floods_prev_4w", "region_id"]], columns=["region_id"])  # noqa: E731
        Xt = X(train)
        m = RandomForestClassifier(n_estimators=300, min_samples_leaf=20, class_weight="balanced", random_state=553, n_jobs=-1)
        return m.fit(Xt, train.flood).predict_proba(X(pred).reindex(columns=Xt.columns, fill_value=0))[:, 1]
    return fp


BASE = RAIN + ["soil_moisture"]
PAIRS = {  # name: (without this week's rain, with it)
    "logistic_rain_soil": (logistic(BASE), logistic(BASE + [FX])),
    "forest_rain_region_month": (forest(BASE), forest(BASE + [FX])),
}


def paired(y, p0, p1, weeks, k=3, n_boot=1000, seed=553):
    """Scores without (p0) and with (p1), and the 95% week-bootstrap range of the difference (same resamples for both)."""
    y, p0, p1, weeks = map(np.asarray, (y, p0, p1, weeks))
    a, b = _point(y, p0, weeks, k), _point(y, p1, weeks, k)
    rng = np.random.default_rng(seed)
    uw = np.unique(weeks)
    idx = {w: np.flatnonzero(weeks == w) for w in uw}
    d = {"pr_auc": [], f"recall_at_{k}": []}
    for _ in range(n_boot):
        pick = rng.choice(uw, len(uw), replace=True)
        rows = np.concatenate([idx[w] for w in pick])
        nw = np.repeat(np.arange(len(pick)), [len(idx[w]) for w in pick])
        a_, b_ = _point(y[rows], p0[rows], nw, k), _point(y[rows], p1[rows], nw, k)
        for m in d:
            d[m].append(b_[m] - a_[m])
    out = {"n": len(y), "positives": int(y.sum()), "base_rate": round(float(y.mean()), 4)}
    for m in d:
        out[f"{m}_without"], out[f"{m}_with"] = round(a[m], 4), round(b[m], 4)
        out[f"{m}_gain"] = round(b[m] - a[m], 4)
        out[f"{m}_gain_lo"], out[f"{m}_gain_hi"] = (round(float(q), 4) for q in np.quantile(d[m], [0.025, 0.975]))
    return out


def tune_rows(df):
    rows = []
    for label, data in [("tune_2023", df), ("tune_2023_without_akosombo", without_akosombo(df))]:
        train, tune, _ = split(data)
        for name, (f0, f1) in PAIRS.items():
            rows.append({"model": name, "eval": label, **paired(tune.flood, f0(train, tune), f1(train, tune), tune.week_start)})
    return pd.DataFrame(rows)


def rolling(df):
    out = []
    for name, (f0, f1) in PAIRS.items():
        for tag, f in [("without", f0), ("with", f1)]:
            r = rolling_origin(f, df, n_boot=20)[["year", "pr_auc", "recall_at_3", "base_rate"]]
            out.append(r.assign(model=name, this_week_rain=tag))
    return pd.concat(out, ignore_index=True)


def load():
    p = ROOT / "data" / "processed"
    df = pd.read_parquet(p / "table.parquet").merge(pd.read_parquet(p / "weather_forecast_experiment.parquet"),
                                                    on=["region_id", "week_start"], how="left", validate="1:1")
    assert df[FX].notna().all() and len(df) == 9184
    return df


if __name__ == "__main__":
    # self-check: a feature equal to the label must show a large, clearly positive gain
    df = load()
    cheat = df.assign(**{FX: df.flood * 100.0})
    tr, tu, _ = split(cheat)
    s = paired(tu.flood, logistic(BASE)(tr, tu), logistic(BASE + [FX])(tr, tu), tu.week_start, n_boot=50)
    assert s["pr_auc_with"] > 0.95 and s["pr_auc_gain_lo"] > 0, s
    assert average_precision_score(tu.flood, tu[FX]) == 1

    t, r = tune_rows(df), rolling(df)
    OUT.mkdir(parents=True, exist_ok=True)
    t.to_csv(OUT / "forecast_experiment.csv", index=False)
    r.round(4).to_csv(OUT / "forecast_experiment_rolling_origin.csv", index=False)
    show = ["model", "eval", "pr_auc_without", "pr_auc_with", "pr_auc_gain", "pr_auc_gain_lo", "pr_auc_gain_hi",
            "recall_at_3_without", "recall_at_3_with", "recall_at_3_gain_lo", "recall_at_3_gain_hi"]
    print(t[show].to_string(index=False))
    piv = r.pivot_table(index="year", columns=["model", "this_week_rain"], values="pr_auc").round(3)
    print(piv.to_string())
    print("mean over 2018-2023:\n", piv.mean().round(3).to_string())
