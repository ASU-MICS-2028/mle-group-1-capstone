"""W05: the one evaluation harness every model goes through (decision 0004).

    python src/evaluate.py      # self-checks

A model is a function fit_predict(train_df, predict_df) -> array of flood probabilities (or scores).
"""
from typing import Callable

import numpy as np
import pandas as pd
from sklearn.metrics import average_precision_score, brier_score_loss, roc_auc_score

TRAIN_END, TUNE_YEAR, TEST_START = "2022-12-31", 2023, "2024-01-01"
AKOSOMBO = ("2023-09-11", "2023-10-30")  # Mondays of the weeks touching the 15 Sep - 31 Oct 2023 spill
FitPredict = Callable[[pd.DataFrame, pd.DataFrame], np.ndarray]


def split(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """train 2015-2022, tune 2023, test 2024-2025. Use test ONCE, at the very end."""
    w = df.week_start
    return df[w <= TRAIN_END], df[w.dt.year == TUNE_YEAR], df[w >= TEST_START]


def recall_at_k(y, p, weeks, k: int = 3) -> float:
    """Alert budget: flag the k highest-scored regions each week. Share of flood region-weeks flagged."""
    d = pd.DataFrame({"y": np.asarray(y), "p": np.asarray(p), "w": np.asarray(weeks)})
    d["rank"] = d.groupby("w").p.rank(ascending=False, method="first")
    return float(d.loc[d["rank"] <= k, "y"].sum() / max(d.y.sum(), 1))


def _point(y, p, weeks, k):
    y, p = np.asarray(y), np.asarray(p)
    one_class = y.min() == y.max()
    prob = p.min() >= 0 and p.max() <= 1
    return {"pr_auc": np.nan if one_class else average_precision_score(y, p),
            "roc_auc": np.nan if one_class else roc_auc_score(y, p),
            f"recall_at_{k}": recall_at_k(y, p, weeks, k),
            "brier": brier_score_loss(y, p) if prob else np.nan,
            "base_rate": y.mean()}


def score(y, p, weeks, k: int = 3, n_boot: int = 1000, seed: int = 553) -> dict:
    """Point scores plus 95% bootstrap CIs, resampling whole weeks (regions in a week are correlated)."""
    y, p, weeks = np.asarray(y), np.asarray(p), np.asarray(weeks)
    out = _point(y, p, weeks, k)
    rng = np.random.default_rng(seed)
    uw = np.unique(weeks)
    idx = {w: np.flatnonzero(weeks == w) for w in uw}
    boots = []
    for _ in range(n_boot):
        pick = rng.choice(uw, len(uw), replace=True)
        rows = np.concatenate([idx[w] for w in pick])
        new_w = np.repeat(np.arange(len(pick)), [len(idx[w]) for w in pick])  # a week drawn twice counts twice
        boots.append(_point(y[rows], p[rows], new_w, k))
    b = pd.DataFrame(boots)
    for m in list(out):
        if m != "base_rate":
            out[f"{m}_lo"], out[f"{m}_hi"] = b[m].quantile(0.025), b[m].quantile(0.975)
    out["n"], out["positives"] = len(y), int(y.sum())
    return out


def evaluate(fit_predict: FitPredict, df: pd.DataFrame, on: str = "tune", **kw) -> dict:
    """Fit on train (train+tune when on='test'), score on tune or test."""
    train, tune, test = split(df)
    fit_on, target = (train, tune) if on == "tune" else (pd.concat([train, tune]), test)
    return score(target.flood, fit_predict(fit_on, target), target.week_start, **kw)


def without_akosombo(df: pd.DataFrame) -> pd.DataFrame:
    return df[~df.week_start.between(*AKOSOMBO)]


def rolling_origin(fit_predict: FitPredict, df: pd.DataFrame, years=range(2018, 2024), **kw) -> pd.DataFrame:
    """Train on 2015..Y-1, score year Y. Stops at 2023: the test years are never used."""
    kw.setdefault("n_boot", 200)
    rows = []
    for y in years:
        assert y < 2024, "rolling origin must not touch the test years"
        tr, te = df[df.week_start.dt.year < y], df[df.week_start.dt.year == y]
        rows.append({"year": y, **score(te.flood, fit_predict(tr, te), te.week_start, **kw)})
    return pd.DataFrame(rows)


def leave_one_region_out(fit_predict: FitPredict, df: pd.DataFrame, **kw) -> dict:
    """Train on 15 regions, predict the 16th, 2015-2023 only; score the pooled out-of-region predictions."""
    d = df[df.week_start < TEST_START]
    preds = pd.Series(np.nan, index=d.index)
    for r in d.region_id.unique():
        m = d.region_id == r
        preds[m] = fit_predict(d[~m], d[m])
    return score(d.flood, preds, d.week_start, **kw)


if __name__ == "__main__":
    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).parent))
    from synthetic import make

    df = make()
    tr, tu, te = split(df)
    assert len(tr) + len(tu) + len(te) == len(df)
    assert tr.week_start.max() < tu.week_start.min() and tu.week_start.max() < te.week_start.min()
    assert set(te.week_start.dt.year) == {2024, 2025} and set(tu.week_start.dt.year) == {2023}
    s = score(tu.flood, tu.flood.astype(float), tu.week_start, n_boot=50)
    assert s["pr_auc"] == 1 and s["roc_auc"] == 1 and s["brier"] == 0, s
    assert recall_at_k(tu.flood, tu.flood, tu.week_start, k=16) == 1
    # random scores: the 95% CI should cover AUC 0.5 in most of 20 tries (a single try misses ~1 in 20)
    cover = [(lambda r: r["roc_auc_lo"] < 0.5 < r["roc_auc_hi"])(
        score(tu.flood, np.random.default_rng(i).random(len(tu)), tu.week_start, n_boot=100)) for i in range(20)]
    assert sum(cover) >= 16, sum(cover)
    seen = []
    rolling_origin(lambda a, b: (seen.append(b.week_start.max()), np.zeros(len(b)))[1], df)
    assert max(seen) < pd.Timestamp(TEST_START)
    print("passed: splits disjoint and ordered, perfect predictor = 1.0, random CI covers 0.5, test years untouched")
