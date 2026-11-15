---
summary: Without a penalty, logistic regression on separable data pushes weights to infinity and becomes overconfident.
type: concept
tags: [regularisation, logistic-regression]
sources: [MIT 6.390 ch4]
---
# Why logistic regression needs regularisation

If the training classes can be split perfectly by a line, plain logistic regression never finishes. Making the weights bigger makes the sigmoid steeper, which pushes every training probability closer to exactly 0 or 1 and lowers the log loss a little more. So the weights grow without limit.

The result is a model that claims near-total certainty about a sharp boundary, even in empty regions where it has seen no data. Its probabilities are useless and it reacts strongly to small changes in the training set.

Adding a ridge penalty λ‖θ‖² stops this. The weights stay finite, the probabilities stay moderate, and the fit is more stable.

This also happens in a softer form when a few features almost separate the classes, which is common with many features and few positive examples.

scikit-learn's `LogisticRegression` applies an L2 penalty by default (`C=1.0`). Tune `C` rather than switching it off.

## For the capstone
With few flood weeks per region and many features, near-separation is likely. Keep the penalty on, tune C on 2023, and check calibration of the output probabilities.

## Related
- [Logistic regression](logistic-regression.md)
- [Ridge regression](ridge-regression.md)
- [Probability calibration](probability-calibration.md)
