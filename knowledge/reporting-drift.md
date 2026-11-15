---
summary: Rising online news makes later years look floodier; train from 2015, drop the year, validate forward in time
type: concept
tags: [flood, labels, drift, validation]
sources: [Flood options report §3, §6]
---
# Reporting drift

Groundsource Ghana counts climb from 2 events in 2012 to 333 in 2022. Some of that is more flooding, but much is probably **more online news being published and indexed**. The label's meaning drifts over time: the same rainstorm is more likely to become a "flood event" in 2022 than in 2012.

Risks: a model given the year (or anything that tracks it) learns "later = more floods"; base rates differ between train (2015–2022) and test (2024–2025), so calibration can break; apparent trends in flood frequency may be reporting artefacts.

**Responses:**
- Train from **2015** onward, where coverage is steadier.
- **Never use the year** as a feature.
- Use **temporal validation** (train past, test future, plus rolling windows) so drift shows up as degraded test performance instead of hiding in shuffled folds.
- Report the positive rate per year and check calibration on the test years.
- Avoid claiming flood frequency is rising from these labels alone.

## For the capstone
Plot events per year in the EDA, mark the 2015 cut-off, and discuss drift in Limitations.

## Related
- [News label bias](news-label-bias.md)
- [Forecast leakage](forecast-leakage.md)
- [Temporal leakage in cross-validation](temporal-leakage-in-cross-validation.md)
- [Groundsource dataset](groundsource-dataset.md)
