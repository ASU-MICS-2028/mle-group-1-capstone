---
summary: Shuffled splits overstate scores, most for flexible models that memorise units
type: result
tags: [validation, temporal-split, evaluation]
sources: [prosit-2 ADR 0010, prosit-2 ADR 0016, prosit-1 outputs/tables/leakage_audit.csv]
---
# Shuffled validation inflates scores

In Prosit 2 we scored the same models three ways (PR-AUC, logistic / LightGBM):

| Test | Logistic | LightGBM |
|---|---|---|
| Shuffled | 0.207 | **0.310** |
| Grouped by customer | 0.194 | 0.209 |
| Older → newer | **0.112** | 0.099 |

The shuffled test made LightGBM look best by a wide margin; it was recognising customers it had already seen. On future loans, the case that matters in deployment, the ranking flipped. In the final comparison, random forest and LightGBM led on shuffled (0.223, 0.238) but fell to 0.068 and 0.057 on future loans, against 0.108 for logistic regression.

We reported the shuffled score only to show how much it misleads, and divided PR-AUC by each block's base rate (lift) because base rates differed across time.

## For the capstone
Use the temporal split (train 2015–2022, tune 2023, test 2024–2025) as the headline. Report one shuffled run beside it to show the inflation; region-weeks from the same flood season are strongly correlated, so expect a big gap. Report lift as well as PR-AUC because flood frequency varies by year.

## Related
- [time-split-must-respect-when-labels-are-known.md](time-split-must-respect-when-labels-are-known.md)
- [simple-models-held-up-better-over-time.md](simple-models-held-up-better-over-time.md)
- [../knowledge/temporal-split.md](../knowledge/temporal-split.md)
