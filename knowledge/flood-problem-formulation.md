---
summary: Approved Option B spec — weekly region-level flood-report classifier with temporal split
type: concept
tags: [flood, problem-formulation, capstone]
sources: [Flood options report §4 F1, MLE Group 1 proposal Option B, instructor approval 9 Nov 2026]
---
# Flood problem formulation (Option B, approved)

- **Decision:** should a NADMO regional office (or assembly) prepare staff, supplies and public warnings this week?
- **ML task:** supervised binary classification, framed as weekly forecasting with temporal validation.
- **Unit:** region-week, Ghana's 16 regions, 2015–2025 (9,184 rows, 585 positive = 6.4%).
- **Label:** 1 if at least one Groundsource news-reported flood falls in that region in the coming week. A week counts once however many events.
- **Features:** rainfall over the past 1, 3, 7, 14, 30 days (CHIRPS); antecedent soil moisture (ERA5-Land); season; terrain (Copernicus DEM); river density; built-up share and land-cover change (GHSL/Dynamic World); floods in recent weeks. **The year is never a feature.**
- **Models:** baselines (seasonal average; simple rainfall threshold), logistic regression, random forest, LightGBM, SVM.
- **Validation:** train 2015–2022, tune 2023, test 2024–2025; plus rolling windows; plus held-out regions to test transfer (Roberts et al. 2017, doi:10.1111/ecog.02881).
- **Metrics:** PR-AUC, recall at a fixed number of alerts (alert budget), calibration curves.
- **Research add-on (F2):** how much land-change features add beyond rainfall.
- **Artefact:** Streamlit dashboard of each region's risk this week.

The model predicts **reported** floods, not floods; say so everywhere.

## For the capstone
This is the scope we are held to. Any change (e.g. Greater Accra only, district level) needs instructor agreement.

## Related
- [Groundsource dataset](groundsource-dataset.md)
- [Flood decision and stakeholders](flood-decision-and-stakeholders.md)
- [Flood cost of errors](flood-cost-of-errors.md)
- [Forecast leakage](forecast-leakage.md)
- [Train/validation/test split](train-validation-test-split.md)
- [Land-change added value](land-change-added-value.md)
