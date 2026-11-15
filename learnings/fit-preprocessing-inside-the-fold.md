---
summary: Every imputer, scaler, encoder, sampler and calibrator is fitted only on training rows
type: procedure
tags: [leakage, pipeline, scikit-learn]
sources: [prosit-1 notebook §7–8, prosit-2 AGENTS.md ML rules, prosit-2 ADR 0010]
---
# Fit preprocessing inside the fold

A median, a mean, a category list or a calibration curve is something learned from data. If it's computed on all rows before splitting, the test set has already leaked in. The fix we used in both prosits is to put every learned step inside one scikit-learn `Pipeline`, so cross-validation refits it from scratch in each training fold.

```python
pre = ColumnTransformer([
    ("num", Pipeline([("imp", SimpleImputer(strategy="median")),
                      ("sc", StandardScaler())]), num_cols),
    ("cat", OneHotEncoder(handle_unknown="ignore"), cat_cols),
])
model = Pipeline([("pre", pre), ("clf", LogisticRegression(max_iter=1000))])
cross_val_score(model, X, y, cv=splits, scoring="average_precision")
```

Rules that came with it:
- Split first, then do anything that learns.
- SMOTE and calibrators go inside the fold too.
- In Prosit 2 one function (`preprocessor(FEATURES)`) started every model, so no notebook could rebuild the steps differently.

## For the capstone
Rainfall anomalies, soil-moisture percentiles and region baselines are all learned statistics. Compute them from training years (2015–2022) only, inside the pipeline or in a function that takes the training window as an argument, then apply them to 2023 and 2024–2025.

## Related
- [one-shared-feature-module.md](one-shared-feature-module.md)
- [audit-leaks-by-building-the-cheating-version.md](audit-leaks-by-building-the-cheating-version.md)
- [../knowledge/data-leakage.md](../knowledge/data-leakage.md)
