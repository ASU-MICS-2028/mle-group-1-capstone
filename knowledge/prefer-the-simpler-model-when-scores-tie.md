---
summary: If a simple model matches complex ones on most metrics, ship the simple one.
type: lesson
tags: [model-selection, prosit-2, explainability]
sources: [lab-session-1 discussion]
---
# Prefer the simpler model when scores tie

In Prosit 2 we compared several models for loan default. Logistic regression matched the more complex models on most metrics and beat them on one. The brief also asked for a simple model. So the recommendation was logistic regression, not the most complex model.

The reasoning to state in a report:

- The goal is "a simple model that works", not the top leaderboard score.
- A simpler model is easier to explain, audit for fairness, and maintain.
- Small differences between models are often within noise on small datasets.
- Complexity must earn its place with a clear, repeatable gain.

When this holds, say so explicitly: "logistic regression was within X of the best model on PR-AUC and better on Y, so we chose it for transparency".

## For the capstone
If LightGBM only edges logistic regression on the 2023 tuning year, a NADMO-facing dashboard may be better served by logistic regression with readable coefficients. Decide using tuning-year results, then report test results for both.

## Related
- [Beat a naive baseline first](beat-a-naive-baseline-first.md)
- [Black-box models and explainability](black-box-models-and-explainability.md)
