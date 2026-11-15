---
summary: Train a classifier to tell old from new data; high AUC means expect transfer failure
type: procedure
tags: [distribution-shift, transfer, monitoring]
sources: [prosit-2 ADR 0019, prosit-2 learnings/10_transfer]
---
# Check domain shift with a domain classifier

Prosit 2 trained on Kenyan loans and deployed in Ghana. Steps we used to measure how different the target was:

1. **Domain classifier:** label source rows 0 and target rows 1, fit a classifier on the features, report ROC-AUC. Include a **control** (source test vs source train), which should be about 0.50. Ours: 1.00 with all features, 0.95–0.97 even without the obvious ones; control 0.50. No overlap.
2. **PSI per feature** (population stability index; below 0.1 stable, 0.1–0.25 some shift, above 0.25 large). Only two features were stable; loan type scored 17.
3. **Importance weights** (from the domain classifier) only help where the domains overlap. Effective sample size fell to 19 of 68,464 rows uncapped, 2,757 at best cap, and every weighted model got worse. We rejected weighting.
4. **Labels needed:** subsample the source to estimate how many target labels make an accuracy check meaningful (about 5,000).
5. **Trust gates** in the decision: what must be true before automatic use (recalibration, monthly PSI, observed vs predicted rate).

## For the capstone
Run a domain classifier for 2015–2022 vs 2024–2025 and per-feature PSI on rainfall and soil moisture (wetter years, new sensors, growing Groundsource coverage). Put monthly PSI and observed-vs-predicted flood rate in the Model Card's monitoring section.

## Related
- [features-that-encode-the-period-hurt-on-the-future.md](features-that-encode-the-period-hurt-on-the-future.md)
- [calibration-data-must-span-all-periods.md](calibration-data-must-span-all-periods.md)
- [../knowledge/model-transfer-across-places.md](../knowledge/model-transfer-across-places.md)
