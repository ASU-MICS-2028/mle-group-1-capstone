---
summary: Impurity importance comes free from trees; permutation importance is more reliable; neither is causal.
type: concept
tags: [trees, interpretability, feature-selection]
sources: [lecture-07 recording, lec5 slides]
---
# Feature importance

Tree models give a sense of which features matter.

- **Impurity-based importance:** add up how much each feature reduced Gini or entropy across all its splits (and all trees). Comes free with training. The lecturer pointed out that features chosen early, near the root, are the most informative. A student asked whether this could guide feature selection, and the lecturer said yes.
- **Permutation importance:** shuffle one feature's column on validation data and measure how much the score drops. A big drop means the model relied on it. Slower, but more reliable, especially with correlated features.

Pitfalls:
- impurity importance favours features with many distinct values (continuous or high-cardinality), even if they are noise;
- with two correlated features, importance gets split between them, so each looks weaker than it is;
- importance is **for screening, not causal claims** (slide 21). "Rainfall is important" does not prove rainfall causes the floods in the data; it could be a proxy;
- if you use importance to select features, do it inside each training fold, or you leak information.

Global importance tells you what matters on average. To explain a single prediction you need per-case methods (for example SHAP values, or the weight × value terms of a linear model).

## For the capstone
Report permutation importance on 2023 for LightGBM and random forest, and compare with logistic-regression coefficients. Agreement across models is a good sign for the defence.

## Related
- [Decision tree](decision-tree.md)
- [Random forest](random-forest.md)
- [Black-box models and explainability](black-box-models-and-explainability.md)
- [Lasso regression](lasso-regression.md)
