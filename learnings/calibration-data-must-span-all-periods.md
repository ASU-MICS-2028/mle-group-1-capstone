---
summary: Calibrating on only the newest slice priced everyone at that slice's base rate
type: result
tags: [calibration, temporal-split, deployment]
sources: [prosit-2 ADR 0017, prosit-2 ADR 0016 update 29 Oct]
---
# Calibration data must span all periods

Prosit 2's first saved final model was Platt-calibrated on the newest 20% of dates. On the full data that slice was one high-default period (9% default, about 2,600 loans). The result: low-risk older loans were priced at 4.9% against a real 1.3%, and the model declined **89%** of applicants. The validation tests hadn't shown it because they calibrated each time block separately; the bug only existed in the saved artefact.

We compared five options (none, newest 20% of dates, newest 20% of rows, random 25%, out-of-fold from 5 grouped folds). Cost per loan was within noise for all of them on the future blocks, but the newest-dates option had the worst log loss (0.095 vs about 0.080) and broke on the full refit. We switched to Platt fitted on **out-of-fold scores from all periods**: declines fell to 19% and older loans were priced at 1.3% (actual 1.3%).

Lesson: test the artefact you actually ship, not only the validation procedure, and look at its decision rate before trusting it.

## For the capstone
If the final model is refit on 2015–2023 and calibrated, fit the calibrator on out-of-fold predictions across all those years, not just on 2023 (one wet or dry year would skew it). Before the dashboard goes live, check the share of region-weeks it alerts on per year.

## Related
- [calibrate-before-applying-a-cost-cutoff.md](calibrate-before-applying-a-cost-cutoff.md)
- [scorer-tests-catch-what-metrics-miss.md](scorer-tests-catch-what-metrics-miss.md)
- [../knowledge/probability-calibration.md](../knowledge/probability-calibration.md)
