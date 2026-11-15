---
summary: A linear classifier computes a score and predicts the class from its sign; the boundary is a line.
type: concept
tags: [linear-models, classification]
sources: [lecture-06 recording, lec4 slides]
---
# Linear classifier

A linear classifier uses the same weighted sum as linear regression, but treats it as a **score** rather than the answer:

score = θᵀx (any real number: 20, −35, 0.4 …)
predicted class = +1 if score > 0, otherwise −1

The **decision boundary** is where the score is exactly 0. In 2 features that is a straight line; in 3 a flat plane; in more, a "hyperplane". The model does not move the data points. It only places the boundary.

The course labels the two classes −1 and +1. The lecturer's reason was that the classes then sit symmetrically, so neither looks "bigger". It also makes the margin formula y·score neat. In practice, libraries such as scikit-learn use 0/1 labels with no problem.

**Limit:** if the classes are interleaved so no straight boundary separates them, a linear classifier will make many mistakes. Options then are new features (interactions, squares), kernels (SVM), or non-linear models like trees.

Logistic regression is a linear classifier whose score is turned into a probability with the sigmoid.

## Related
- [Classification margin](classification-margin.md)
- [Logistic regression](logistic-regression.md)
- [Zero-one loss](zero-one-loss.md)
- [Support vector machine](support-vector-machine.md)
