---
summary: Anything learned from the test set contaminates every later score on it
type: lesson
tags: [evaluation, leakage, test-set]
sources: [prosit-2 ADR 0021, prosit-2 ADR 0013 limitations, prosit-2 learnings/07_classification]
---
# Never tune on the test set

Two Prosit 2 episodes:

- **Leaderboard probing.** With no labels for the target country, we submitted crafted files to the competition leaderboard to recover group-level default rates (totals only, after checking the rules allowed it). It was valuable evidence, but it came from the test set. Our ADR states that any later leaderboard score of a model built using those rates is contaminated; our three real scores were submitted before the probe, and we kept it that way.
- **A reused holdout.** The provisional model's limitations listed "the temporal holdout has been used for development". Once you have looked at a holdout to make choices, its score is no longer an unbiased estimate.

Practice we settled on: choose features, models, thresholds and fixes on older data only ("every setting is chosen on older loans only"), score the final choice once on the newest data, and record in the log when the test set was touched.

## For the capstone
2023 is the tune year: all selection, calibration and threshold choices happen there or earlier. Open 2024–2025 once, for the final models, and log the date. If anything is changed after seeing test results, say so in the report and treat the new test score as optimistic.

## Related
- [write-pass-rules-before-the-stress-test.md](write-pass-rules-before-the-stress-test.md)
- [time-split-must-respect-when-labels-are-known.md](time-split-must-respect-when-labels-are-known.md)
- [../knowledge/data-leakage.md](../knowledge/data-leakage.md)
