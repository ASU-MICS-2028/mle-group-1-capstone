---
summary: A good classification training loss must decrease with the margin, be convex and be differentiable.
type: concept
tags: [loss, classification]
sources: [lec4 slides, lecture-06 recording]
---
# What a good surrogate loss needs

Because the 0-1 loss cannot be trained on, we replace it with a **surrogate**: a smooth stand-in that roughly tracks it. The slides list three requirements for the surrogate, written as a function g(z) of the margin z = y·score:

1. **Decreasing:** a better margin (more correct, more confident) gives a lower loss. Badly wrong points cost more.
2. **Convex:** one bowl shape, so gradient descent reaches the global best.
3. **Differentiable:** a slope exists everywhere, so gradient descent can compute steps.

The candidates compared in class were the linear (perceptron), exponential and logistic losses. Logistic loss meets all three and also behaves well with outliers, which is why it won.

The hinge loss used by SVMs is convex and decreasing but has a kink at z = 1. That is fine in practice (it has a "sub-gradient"), but it is not strictly differentiable there.

Remember: the surrogate must still correlate with the metric you report, as the lecturer insisted.

## Related
- [Zero-one loss](zero-one-loss.md)
- [Classification loss functions compared](classification-loss-functions-compared.md)
- [Convexity and local minima](convexity-and-local-minima.md)
- [Training loss vs evaluation metric](training-loss-vs-evaluation-metric.md)
