---
summary: Backpropagation sends the error backward through the network to get every weight's gradient.
type: concept
tags: [neural-networks, training, backpropagation, exam]
sources: [neural networks slides, lecture-11 recording]
---
# Backpropagation

Gradient descent needs the gradient of the loss with respect to every weight. In a network with many layers this is hard, because each weight's effect on the output passes through all the later layers. Backpropagation is the algorithm that computes all these gradients efficiently. It is what makes gradient descent practical for multi-layer networks.

The idea:

1. **Forward pass**: push the input through the network and get a prediction.
2. **Loss**: compare the prediction with the true label.
3. **Backward pass**: starting from the loss, work backward layer by layer. At each layer, ask how much each weight contributed to the error. The **chain rule** links each layer's effect to the next.
4. **Update**: change each weight a little in the direction that lowers the loss.

Without training, a network with random weights gives random predictions. With backpropagation, errors are measured, weight changes are computed, and predictions improve step by step.

Backpropagation computes gradients; it does not itself choose the step. The step is done by gradient descent or another optimiser.

A student asked how a "black box" can be trained at all. Answer: every intermediate number is visible and every update can be computed. "Black box" means we cannot easily explain *why* the final answer came out, not that the maths is hidden.

## Related
- [Chain rule in backpropagation](chain-rule-in-backpropagation.md)
- [Neural network training loop](neural-network-training-loop.md)
- [Gradient descent](gradient-descent.md)
- [Vanishing gradients](vanishing-gradients.md)
