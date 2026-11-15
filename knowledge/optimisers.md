---
summary: Optimisers such as momentum and Adam turn gradients into better steps than plain gradient descent.
type: concept
tags: [neural-networks, optimisation]
sources: [neural networks slides, lecture-11 recording]
---
# Optimisers

Backpropagation gives the gradient. An **optimiser** decides how big a step to take and in which exact direction.

Plain gradient descent uses one learning rate for every weight: w ← w − α × gradient.

The slides say that in practice we use optimisers that:

- give each parameter its **own learning rate**, depending on how much that parameter's gradient varies;
- use **past history** of gradients, so steps keep moving in a consistent direction and do not zig-zag.

This makes training faster and more stable. Common names (the slide only shows an animation): momentum, RMSProp, Adam. Adam combines both ideas and is the usual default.

Analogy: plain gradient descent is a walker who looks at the slope under their feet each step. Momentum is a ball rolling downhill that keeps some speed. Adam is a ball that also adjusts its stride on steep versus gentle ground.

scikit-learn's `MLPClassifier` uses Adam by default (`solver='adam'`).

## Related
- [Gradient descent](gradient-descent.md)
- [Learning rate](learning-rate.md)
- [Neural network training loop](neural-network-training-loop.md)
