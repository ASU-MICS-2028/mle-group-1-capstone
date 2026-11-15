---
summary: A convex loss has one bowl-shaped minimum, so gradient descent cannot get stuck in a worse dip.
type: concept
tags: [optimisation]
sources: [lecture-06 recording, lec4 slides, MIT 6.390 ch4]
---
# Convexity and local minima

A function is **convex** if it is shaped like a single bowl: draw a straight line between any two points on the curve and the line never goes below the curve.

Why it matters: on a convex loss, the only place where the slope is zero is the global minimum. So gradient descent (with a sensible step size) always ends at the best answer.

- MSE for linear regression is convex.
- Log loss for logistic regression is convex.
- Hinge loss (SVM) is convex.

A **non-convex** loss has several dips. A zero slope may just be a **local minimum**, a dip that is not the lowest point. Neural network losses are like this, and so is the k-means objective. The result then depends on where you start, which is why random seeds and repeated runs matter there.

The lecturer listed convexity as one of three wishes for a good classification training loss (with "decreasing in the margin" and "differentiable"). In passing the lecturer also said a decreasing loss is automatically convex. That is not true in general; they are separate properties.

## Related
- [Gradient descent](gradient-descent.md)
- [Surrogate loss requirements](surrogate-loss-requirements.md)
- [Logistic regression](logistic-regression.md)
