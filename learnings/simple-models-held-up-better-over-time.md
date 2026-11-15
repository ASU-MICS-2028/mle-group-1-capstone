---
summary: On future data, regularised logistic regression beat random forest and LightGBM
type: result
tags: [model-selection, temporal-split, logistic-regression]
sources: [prosit-2 ADR 0016, prosit-2 ADR 0012, prosit-2 learnings/07_classification]
---
# Simple models held up better over time

Prosit 2's final comparison on future loans (PR-AUC): majority baseline 0.018, logistic regression **0.108**, random forest 0.068, LightGBM 0.057, k-NN 0.064, pruned tree 0.053. As lift (PR-AUC ÷ base rate): logistic 7.6, random forest 3.9, LightGBM 3.5. Logistic beat random forest in all 4 time blocks, by +0.039 on average, above our noise floor.

On the external leaderboard (mostly same-period data, LightGBM's best case) logistic and LightGBM tied (gap 0.003, inside noise).

Why it happened, as far as we could tell: the trees fitted period-specific patterns that didn't carry forward, while the linear model's weaker but steadier signals did. It also gave faithful, hand-checkable explanations for free.

This is one dataset, not a law, so the lesson is to *test* the simple model on the time split before assuming the boosted one wins.

## For the capstone
Keep logistic regression as a serious candidate, not just a baseline. If LightGBM wins on 2023, check whether the margin beats the noise floor and holds in each year of 2024–2025 separately before choosing it for the dashboard.

## Related
- [shuffled-validation-inflates-scores.md](shuffled-validation-inflates-scores.md)
- [measure-the-noise-floor-before-claiming-a-win.md](measure-the-noise-floor-before-claiming-a-win.md)
- [faithful-reason-codes-from-a-linear-model.md](faithful-reason-codes-from-a-linear-model.md)
