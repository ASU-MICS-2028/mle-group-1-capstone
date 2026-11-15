---
summary: Choose a model by its boundary shape, assumptions, cost, interpretability and data needs, then let validation decide.
type: procedure
tags: [model-selection, lecturer-emphasis]
sources: [lecture-07 recording, lec5 slides]
---
# Choosing a supervised model

The lecturer gave a list of questions to ask about any algorithm:
- What shape of decision boundary can it draw (line, tree splits, kernel curve, neighbourhood, probability distribution)?
- How is it trained (formula, greedy splits, gradient descent, nothing)?
- What does it assume about the data?
- Training cost vs prediction cost.
- **Interpretability:** can you trace a decision (white box) or not (black box)? Linked in class to fairness and explainable AI.
- How does it scale with more rows and more features?
- How robust is it to noise, outliers and missing values?
- How much data does it need?

The survey slides turn this into a rough guide:
- need explanations → decision tree (or logistic regression);
- tabular data, best accuracy → gradient boosting (XGBoost, LightGBM, CatBoost);
- robust with little tuning → random forest;
- text, tiny data → naive Bayes;
- many features, clean margin → SVM;
- quick small-data baseline → kNN;
- **always keep logistic regression as a baseline**;
- unsure → try 2–3 candidates and let cross-validation decide.

The slides end with **"no free lunch"**: no algorithm is best on every problem. Match the method to your data size, dimensionality, assumptions and deployment needs.

## For the capstone
Put a one-row-per-model table in the report: boundary, training, assumptions, interpretability, cost, and the 2023 score. It answers "why these five models?" before it is asked.

## Related
- [Supervised learning recipe](supervised-learning-pipeline.md)
- [Black-box models and explainability](black-box-models-and-explainability.md)
- [Beat a naive baseline first](beat-a-naive-baseline-first.md)
- [Start simple, add complexity only if it helps](start-simple-add-complexity-only-if-it-helps.md)
