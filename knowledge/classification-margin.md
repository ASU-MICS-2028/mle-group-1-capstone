---
summary: The margin y times score is positive when correct, negative when wrong, and its size shows confidence.
type: concept
tags: [classification, loss]
sources: [lec4 slides, lecture-06 recording]
---
# Classification margin

With labels y ∈ {−1, +1} and a raw score h(x), the **margin** is

z = y · h(x)

One number now tells you two things:

| true y | score | z | meaning |
|---|---|---|---|
| +1 | +5 | +5 | right, confident |
| +1 | +0.2 | +0.2 | right, only just |
| +1 | −3 | −3 | wrong |
| −1 | −4 | +4 | right, confident |
| −1 | +2 | −2 | wrong |

- z > 0: correct. z < 0: wrong.
- Large positive z: correct and sure. Very negative z: badly wrong.

All the classification losses in the course are written as a function of z: the 0-1 loss is 1 when z < 0; the linear (perceptron) loss is max(0, −z); the logistic loss is log(1 + e^(−z)); the exponential loss is e^(−z); the SVM hinge loss is max(0, 1 − z).

A good training loss should go *down* as z goes up.

Note: in SVMs "margin" also means the width of the gap between the boundary and the nearest points. Same family of idea, slightly different use.

## Related
- [Linear classifier](linear-classifier.md)
- [Classification loss functions compared](classification-loss-functions-compared.md)
- [Surrogate loss requirements](surrogate-loss-requirements.md)
