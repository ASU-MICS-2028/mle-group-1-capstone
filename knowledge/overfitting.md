---
summary: Overfitting is memorising training noise - low training error, high validation error.
type: concept
tags: [model-selection, generalisation]
sources: [lecture-06 recording, lec5 slides, MIT 6.390 ch2]
---
# Overfitting

A model **overfits** when it fits the training data too closely, including its random noise, and so does worse on new data.

The tell-tale pattern (from the slides): **low training error, high validation error.**

Example: 10 points that roughly follow a straight line. A degree-9 polynomial can pass through every point exactly (zero training error), but it wiggles wildly between them and predicts new points badly. The straight line has some training error but predicts new points well.

What makes overfitting more likely, as discussed in class:
- few examples compared with the model's flexibility;
- very flexible models (deep trees, small k in kNN, high-degree polynomials), which bend towards outliers;
- many noisy or irrelevant features.

The lecturer stressed that it is handled **during** training and model selection, not patched afterwards. Tools:
- regularisation (ridge, lasso, penalties in logistic regression);
- limiting complexity (tree depth, minimum leaf size, pruning);
- ensembles that average many models (random forests);
- early stopping in boosting;
- good feature selection;
- choosing all of these by cross-validation.

The opposite failure is **underfitting**: the model is too simple to capture the real pattern, so both training and validation error are high.

## For the capstone
Compare training-period and 2023 scores for every model. LightGBM and random forest with deep trees on ~16 regions × 8 years of weeks can easily memorise particular flood weeks.

## Related
- [Generalisation](generalisation.md)
- [Bias-variance trade-off](bias-variance-tradeoff.md)
- [Ridge regression](ridge-regression.md)
- [Tree pruning and stopping rules](tree-pruning-and-stopping-rules.md)
