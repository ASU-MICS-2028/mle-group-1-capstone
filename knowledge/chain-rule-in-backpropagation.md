---
summary: A weight's gradient is the product of local derivatives along the path from that weight to the loss.
type: derivation
tags: [neural-networks, backpropagation, calculus, exam]
sources: [neural networks slides, lecture-11 recording]
---
# Chain rule in backpropagation

The **chain rule**: if L depends on z, and z depends on w, then

dL/dw = (dL/dz) × (dz/dw)

In a network the chain is longer. Take a small chain: w₄ → z₄ → z₅ → L, where z₄ is a hidden neuron's output and z₅ is the network output. Then

∂L/∂w₄ = (∂L/∂z₅) × (∂z₅/∂z₄) × (∂z₄/∂w₄)

Each factor is a simple, local derivative. The intermediate terms seem to "cancel" when multiplied, which is a handy memory aid, though nothing is literally cancelled.

Work from the output backward. The factor ∂L/∂z₅ is computed once and reused for every earlier weight. That reuse is what makes backpropagation fast.

Doing this for every weight gives a **gradient vector**: one entry per parameter. Gradient descent then updates all weights at once:

w_new = w_old − α × ∂L/∂w

where α is the learning rate.

**Correction to the lecture.** While explaining partial derivatives, the board work said the gradient of f = x² + y² is "2x times 2y". That is wrong. The partial derivatives are ∂f/∂x = 2x and ∂f/∂y = 2y, and the gradient is the *vector* (2x, 2y). Multiplying happens along a chain (the chain rule), not across different variables.

## Related
- [Backpropagation](backpropagation.md)
- [Vanishing gradients](vanishing-gradients.md)
- [Gradient descent](gradient-descent.md)
