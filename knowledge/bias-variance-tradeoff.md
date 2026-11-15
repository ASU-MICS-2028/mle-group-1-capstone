---
summary: Test error comes from a too-simple model (bias) or an unstable, data-hungry one (variance).
type: concept
tags: [model-selection, generalisation]
sources: [MIT 6.390 ch2, lec5 slides, lecture-07 recording, intro slides]
---
# Bias-variance trade-off

There are two different reasons a model can do badly on new data.

- **Bias** (the MIT notes call it *structural error*): no model in your family can fit the truth. Fitting a straight line to a curve is the classic case. More data does not help.
- **Variance** (*estimation error*): the family is flexible enough, but you lack the data to pin down the right member. Small changes in the training set give very different models. A deep decision tree is the classic case.

Making a model more flexible lowers bias but raises variance, and the reverse. The best model sits in between.

Knobs that move along the trade-off:
- more regularisation (bigger λ) → more bias, less variance;
- deeper trees, smaller k in kNN, higher polynomial degree → less bias, more variance;
- more training data → less variance.

How the ensembles use this (from the survey lecture):
- **Bagging / random forests** average many deep, low-bias trees to **cut variance**.
- **Boosting** adds many shallow, high-bias trees one after another to **cut bias**.

Example: predicting flood risk from rainfall alone with a straight line is high bias. A tree with one leaf per historical flood week is high variance.

**Slide caution (intro deck):** it fits a straight line, a degree-4 and a degree-25 polynomial to curved noisy data and reports MSEs of 0.29, 0.07 and 0.06. The degree-25 model having the lowest MSE only makes sense if these are *training* errors; on new data the overfit degree-25 curve would normally lose to degree 4. Read the slide as showing shapes of fit, not a fair comparison.

## Related
- [Overfitting](overfitting.md)
- [Generalisation](generalisation.md)
- [Bagging vs boosting](bagging-vs-boosting.md)
- [Ridge regression](ridge-regression.md)
