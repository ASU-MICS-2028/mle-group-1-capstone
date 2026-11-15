---
summary: All notebooks and the deployed app build features from one tested module
type: procedure
tags: [pipeline, code, deployment]
sources: [prosit-2 ADR 0004, prosit-2 AGENTS.md, prosit-2 ADR 0015]
---
# One shared feature module

In Prosit 2 four notebooks and the scoring service all needed the same features. If each built its own, they drift, and the deployed scorer computes features differently from training: a classic deployment bug. We made one module of plain functions:

- `train, test = build("data/...")` returns the full tables with every feature and the fold columns.
- Feature groups are named lists (`BASE`, `HISTORY`, ..., and the chosen `FEATURES`), so a notebook picks columns, never re-derives them.
- `preprocessor(FEATURES)` starts every model pipeline.
- Self-checks at the bottom: `python src/features.py` must print its "passed" lines before any change is committed. They used a made-up example row and also compared against a slow reference loop on real data (0 mismatches).
- Any change that alters a decision gets an ADR and a log line, because it affects everyone.

A class hierarchy was rejected as overkill for four people and two weeks.

## For the capstone
Put region-week construction, lagged rainfall/soil-moisture features, the label, and the temporal folds in `src/features.py` (or similar), with asserts for "features use only data up to week t−1" and "no week crosses a split". The Streamlit app imports the same functions.

## Related
- [fit-preprocessing-inside-the-fold.md](fit-preprocessing-inside-the-fold.md)
- [scorer-tests-catch-what-metrics-miss.md](scorer-tests-catch-what-metrics-miss.md)
