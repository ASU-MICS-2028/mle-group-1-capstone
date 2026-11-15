---
summary: Neural networks are black boxes; you see every number but cannot trace why a decision was made.
type: concept
tags: [explainability, neural-networks, ethics]
sources: [lecture-11 recording, lecture-09 recording, lecture-07 recording, lec5 slides]
---
# Black-box models and explainability

A **black-box** model hides its reasoning. In a neural network you can print every weight and every intermediate output. What you cannot do is follow a clear path from input to decision. After the first layer, the original features (height, weight, rainfall) have already been mixed and transformed into something without a plain meaning.

A **white-box** model lets you trace the path. With a decision tree you can say: "flagged because rainfall > 80 mm and soil moisture > 0.4". With logistic regression you can read each coefficient.

Explainable AI (XAI) is an active research area that tries to open black boxes. Tools like SHAP (listed in the capstone resources) estimate how much each feature pushed one prediction up or down.

The lecturer tied explainability to documentation: model cards cover what the model does and how it can be explained.

In the supervised-learning survey the lecturer made interpretability one of the main criteria for choosing a model, linked it to fairness and bias, and used the example of having to explain why a model diagnosed a patient with cancer. If interpretability is the main concern, decision trees come out on top. The slides class boosting and kernel SVMs as black boxes too, not only neural networks.

Trade-off: black boxes sometimes predict a little better, but a decision-maker may not trust or act on an alert they cannot understand.

## For the capstone
Random forest and LightGBM sit in between (many trees, not traceable by hand). Pair them with SHAP or feature importance, and keep logistic regression as a readable reference model.

## Related
- [PCA limitations](pca-limitations.md)
- [Explain to non-technical audiences](explain-to-non-technical-audiences.md)
- [Ethics and fairness review pack](ethics-and-fairness-review-pack.md)
- [Decision tree](decision-tree.md)
- [Feature importance](feature-importance.md)
- [Choosing a model](choosing-a-model.md)
