---
summary: Parameters are learned from data; hyperparameters are settings you choose before training.
type: concept
tags: [model-selection, hyperparameters]
sources: [lecture-06 recording, lecture-07 recording, MIT 6.390 ch2, lec5 slides, lecture-11 recording]
---
# Parameters vs hyperparameters

- **Parameters** are the numbers the model learns from the training data: the weights in linear and logistic regression, the split points in a tree.
- **Hyperparameters** are settings you choose before training, which control how learning happens.

Examples from the course:
- learning rate α in gradient descent;
- regularisation strength λ (or C);
- maximum depth and minimum leaf size of a tree;
- number of trees, features per split (random forest);
- learning rate and number of trees (boosting);
- C, kernel and γ (SVM);
- k in kNN and in k-means;
- smoothing α in naive Bayes.

The MIT notes make a useful point: each hyperparameter setting is effectively a **different learning algorithm**. Tuning means trying several and keeping the one that does best on validation data.

The firm rule from the lectures: hyperparameters are chosen on validation data or by cross-validation, **never on the test set**.

**Neural-network view (lecture 11).** "Parameters" is the umbrella term for everything training can update: weights *and* biases. All weights are parameters, but not all parameters are weights. Some parameters are deliberately kept fixed: when you reuse a pretrained network you **freeze** some layers, and those become *non-learnable* parameters. Batch-normalisation mean and variance are also called non-learnable parameters. Depth, width and activation choice are hyperparameters: set before training and never changed by the optimiser.

## Related
- [Network depth and width](network-depth-and-width.md)
- [Hyperparameter tuning](hyperparameter-tuning.md)
- [Train, validation and test sets](train-validation-test-split.md)
- [K-fold cross-validation](k-fold-cross-validation.md)
