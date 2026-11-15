---
summary: Linear, exponential and logistic losses compared; logistic loss is the default for binary classification.
type: concept
tags: [loss, classification, lecturer-emphasis]
sources: [lecture-06 recording, lecture-07 recording, lec4 slides]
---
# Linear vs exponential vs logistic loss

All three are functions of the margin z = y·score.

- **Linear / perceptron loss** max(0, −z): zero when right; when wrong, grows in a straight line with how wrong. Example: y = +1, score −20 gives loss 20. Problem: a few far-off outliers can dominate training. (The slide's graph actually shows plain −z, which keeps *rewarding* points already far on the right side; the max(0, ·) version on the same slide does not. The criticism fits the plain version better.)
- **Exponential loss** e^(−z): explodes for badly wrong points (e^20 is huge). One mislabelled point can drag the model around and make training unstable. AdaBoost uses this loss.
- **Logistic loss (binary cross-entropy)** log(1 + e^(−z)): large for wrong points, but the log keeps it calm; it fades towards zero for confidently right points, so effort goes to mistakes and borderline points. On the slide's scenarios (overlapping classes, one big and one small class) it did clearly better than linear loss. Small correction: the slide says it is zero for correct points; it only *approaches* zero.

The lecturer's conclusion, repeated in the next lecture: **logistic loss is usually the best choice for binary classification**, and the lecturer said students would "play with" these losses in the next prosit. Be ready to justify the loss you used.

## For the capstone
Logistic regression and LightGBM (`objective=binary`) both use logistic loss. SVM uses hinge loss, which is one reason its scores need calibration.

## Related
- [Classification margin](classification-margin.md)
- [Logistic regression](logistic-regression.md)
- [Hinge loss and soft margin](hinge-loss-and-soft-margin.md)
- [Surrogate loss requirements](surrogate-loss-requirements.md)
