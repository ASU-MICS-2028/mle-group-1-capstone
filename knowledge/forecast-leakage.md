---
summary: Using rain observed during the predicted week gives great scores for a tool no one could run
type: concept
tags: [flood, leakage, validation]
sources: [Flood options report §6, proposal Option B (ref CHIRPS-GEFS)]
---
# Forecast leakage

When predicting floods in week $w$, rainfall *during* week $w$ is the strongest predictor — but at decision time (start of week $w$) it has not fallen yet. Including it produces excellent scores for a tool nobody could actually use. This is temporal leakage at the feature level, separate from shuffled-CV leakage.

**Rules:**
- Features use only data available **up to the prediction date** (rain to day $t-1$, soil moisture at $t-1$, floods in previous weeks).
- Leave a gap around the prediction date, because news dates may lag the flood (27% of events span more than one day).
- If forecast rain is wanted, use a real forecast product (CHIRPS-GEFS) as it was issued, and show both results: "observed rain only" and "with forecast rain".
- Observed future rain may appear only as an explicitly labelled upper bound (an oracle), never as the headline.
- Never use the year as a feature; never fit scalers or encoders on test years.

Report the before/after scores if a leak is found.

## For the capstone
Compute each feature with an explicit "as-of" date and add a test that fails if any feature date ≥ the label week's start.

## Related
- [Temporal leakage in cross-validation](temporal-leakage-in-cross-validation.md)
- [Leakage audit with before/after numbers](leakage-audit-before-after.md)
- [CHIRPS-GEFS](chirps-gefs.md)
- [Flood problem formulation](flood-problem-formulation.md)
