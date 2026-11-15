---
summary: Every supervised algorithm follows four steps - hypothesis space, loss, optimiser, validation.
type: procedure
tags: [supervised-learning, model-selection]
sources: [lecture-07 recording, lec5 slides]
---
# The supervised learning recipe

The lecturer showed that every supervised algorithm, from linear regression to boosting, is built from the same four choices:

1. **Hypothesis space** – the family of functions the model is allowed to be. "All straight lines", "all trees of depth 5", "all kernel boundaries". One fitted model is one member of that family, picked by its parameters.
2. **Loss** – how wrongness is measured (MSE, log loss, hinge loss, impurity).
3. **Optimiser** – how the best member is found: a closed-form formula, gradient descent, greedy splitting, or no training at all (kNN just stores the data).
4. **Validation** – check the result generalises, ideally with k-fold cross-validation, before a single final test.

Why validate? Answers from class that the lecturer endorsed: to watch performance during training, to choose between models, and to tune hyperparameters, so the model works on data it has never seen.

This view makes algorithms easy to compare. Logistic regression = linear functions + log loss + gradient descent. Decision tree = axis-aligned splits + impurity + greedy splitting. Same recipe, different ingredients.

This is narrower than the whole project [ML pipeline](ml-pipeline.md); it is what happens inside the "train and select a model" steps.

## For the capstone
For each model in the report (baselines, logistic regression, random forest, LightGBM, SVM), state the four ingredients in one table row. It makes the comparison and the defence much easier.

## Related
- [ML pipeline](ml-pipeline.md)
- [Hyperparameters](hyperparameters.md)
- [K-fold cross-validation](k-fold-cross-validation.md)
- [Choosing a model](choosing-a-model.md)
