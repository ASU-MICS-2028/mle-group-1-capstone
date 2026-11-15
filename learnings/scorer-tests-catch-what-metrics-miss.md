---
summary: Unit tests on the deployed scorer found gaps that aggregate metrics never showed
type: result
tags: [deployment, testing, robustness]
sources: [prosit-2 ADR 0022, prosit-2 learnings/12_scorer, prosit-2 tests/test_scorer.py]
---
# Scorer tests catch what metrics miss

Prosit 2's scoring function (application in; probability, decision and top 3 reasons out) had 18 tests. Good metrics hadn't revealed what the tests did:

- **A made-up applicant who defaulted on all 3 earlier loans was approved** at 1.9% risk. The model's weights on past defaults were tiny because few labelled loans followed a default. We added a rule (2+ past defaults or a 50%+ default rate → decline), checked it changed nothing on history, and kept it.
- **Unseen categories.** We hid each of 6 product types from training and scored them as new; declining unseen types was cheapest. Single types were badly mispriced (one: 2.6% actual vs 15.7% predicted).
- **Input validation.** The scorer rejects bad input and lists every problem; unknown fields are refused so sensitive fields can't slip in.
- **A label that lied.** About 1,900 rows labelled "repeat" had no earlier loan on record, so "first-timer" was defined from the data, not the label.
- Whole test set run through: all 18,594 accepted; median 29 ms per call; about 1.6 s to load.

## For the capstone
Write `tests/` for the Streamlit back end: a region-week with missing rainfall, an out-of-range value, a new year, extreme rain in a dry region, all 16 regions present. Run the whole 2024–2025 table through it and record latency.

## Related
- [one-shared-feature-module.md](one-shared-feature-module.md)
- [calibration-data-must-span-all-periods.md](calibration-data-must-span-all-periods.md)
- [faithful-reason-codes-from-a-linear-model.md](faithful-reason-codes-from-a-linear-model.md)
