---
summary: Gradient descent finds good parameters by repeatedly stepping downhill on the loss.
type: concept
tags: [optimisation]
sources: [lecture-06 recording, lec4 slides, MIT 6.390 ch3, lecture-11 recording]
---
# Gradient descent

Gradient descent is a general way to find the parameters that make a loss small.

Picture standing on a hill in fog and wanting to reach the valley. You feel which way the ground slopes and take a small step downhill. Repeat until the ground is flat.

The algorithm:
1. Start with random parameters θ.
2. Compute the **gradient** of the loss: one partial derivative per parameter. It points uphill.
3. Step the other way: θ ← θ − α · gradient. α is the **learning rate** (step size).
4. Repeat until θ barely changes between steps (smaller than a tiny tolerance ε). This is **convergence**.

At the bottom the gradient is zero, so the updates stop by themselves.

If the loss is **convex** (one bowl, like MSE or log loss), the bottom you reach is the best possible one. If not (neural networks), you might stop in a local dip.

Why bother when linear regression has a formula? Gradient descent needs no matrix inverse, scales to many features, and works for models with no formula at all (logistic regression, neural networks). It may stop at "good enough" rather than the exact optimum.

The lecturer named fancier optimisers that follow the same idea: Adam, AdamW and RMSProp.

In neural networks the same idea applies, but there are many parameters and each one's effect depends on the layers after it. Backpropagation computes all the gradients; an optimiser then takes the step (lecture 11).

## Related
- [Backpropagation](backpropagation.md)
- [Optimisers](optimisers.md)
- [Learning rate](learning-rate.md)
- [Batch, stochastic and mini-batch gradient descent](batch-stochastic-minibatch-gradient-descent.md)
- [Convexity and local minima](convexity-and-local-minima.md)
- [Normal equation](normal-equation.md)
