---
summary: Temporal leakage is using information from after the prediction time to predict earlier events.
type: concept
tags: [leakage, time-series]
sources: [preprocessing & leakage slides, lecture-04 recording]
---
# Temporal leakage

**Temporal leakage** is using information from **after** the prediction point to predict something earlier. The slide example: predicting Monday's purchase using a feature computed from Thursday's sales.

In the preprocessing lecture a student described a Prosit 1 case: net data from 2022 used to predict malaria outcomes from 2014 and 2017. The lecturer called this temporal leakage – the future predicting the past – and said it must be found and fixed.

How it sneaks in:
- random shuffling of time-ordered rows into train and test;
- rolling averages centred on a date instead of looking only backwards;
- features joined from a later snapshot of a database;
- filling gaps with values from later dates.

Fix: split **chronologically** (train on the past, test on the future) and build every feature only from data before the prediction moment.

## For the capstone
Our biggest risk. Use only trailing windows (e.g. rain in the 7 days *before* the week), and decide explicitly whether same-week rainfall is allowed (only if the alert uses a rainfall forecast, not observed totals).

## Related
- [Temporal split](temporal-split.md)
- [Temporal leakage in cross-validation](temporal-leakage-in-cross-validation.md)
- [Target leakage](target-leakage.md)
- [Leakage audit with before/after numbers](leakage-audit-before-after.md)
