---
summary: Train on a maths-friendly loss, report a human-readable metric, and make sure the two move together.
type: rule
tags: [evaluation, loss, lecturer-emphasis]
sources: [lecture-05 recording, lecture-07 recording, lec4 slides]
---
# Training loss vs evaluation metric

The lecturer stressed that a project has **two objectives**:

1. a **training loss** that the optimiser minimises. It is chosen because it is smooth and easy to differentiate (for example MSE, or log loss);
2. an **evaluation metric** that people actually care about and can read (for example RMSE in cedis, accuracy, precision, recall, F1, ROC-AUC). The lecturer called these "secondary objectives".

The rule: **the two must be correlated.** When the training loss goes down, the evaluation metric should get better. If they do not move together, you are optimising the wrong thing.

Why not train on the metric directly? Many useful metrics are step functions. Accuracy only changes when a prediction flips class, so it gives no slope for gradient descent to follow. So we train on a smooth stand-in (a surrogate) and judge on the metric.

Analogy from class: when marking a 50-question test, it is easier to count the wrong answers. Models are also judged by counting or measuring their errors.

## For the capstone
We train with log loss (logistic regression, LightGBM) but report PR-AUC, recall at a chosen alert threshold, and calibration. State both in the report and show that lower validation log loss went with better PR-AUC.

## Related
- [Zero-one loss](zero-one-loss.md)
- [Surrogate loss requirements](surrogate-loss-requirements.md)
- [Precision-recall AUC](precision-recall-auc.md)
- [RMSE and MAE](rmse-and-mae.md)
