---
summary: Molnar's Interpretable Machine Learning — free guide to explaining models (permutation importance, PDP, SHAP)
type: source
tags: [book, interpretability]
sources: [Molnar, Interpretable Machine Learning, https://christophm.github.io/interpretable-ml-book/]
---
# Book: Interpretable Machine Learning (Molnar)

Supplementary course text, free at https://christophm.github.io/interpretable-ml-book/. Chapter numbers change between editions, so cite by chapter name.

| Topic (chapter name) | Key idea (our paraphrase) | Capstone use |
|---|---|---|
| Interpretable models (linear, logistic, trees) | Coefficients and odds ratios read directly | Explaining the logistic model to NADMO |
| Permutation feature importance | Shuffle one feature on held-out data and measure the drop in score | Which inputs drive alerts; compare with impurity importance |
| Partial dependence / ICE | How the prediction moves as one feature changes | Show the rainfall–risk curve per region |
| Shapley values / SHAP | Fair split of one prediction among features | Per-region, per-week explanation on the dashboard ("rain over 7 days drove this") |
| Limits of interpretation | Correlated features make importances unstable | Rainfall windows are highly correlated; group them |

## For the capstone
Use permutation importance on the 2024–2025 test set to check whether built-up share or population (possible media-attention proxies) dominate the model.

## Related
- [Proxy variables](proxy-variables.md)
- [Decision tree split derivation](decision-tree-split-derivation.md)
- [Book: ISLR](book-islr.md)
