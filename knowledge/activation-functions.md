---
summary: Activation functions add non-linearity; ReLU is the usual hidden-layer choice, sigmoid/softmax for outputs.
type: concept
tags: [neural-networks, activation]
sources: [neural networks slides, lecture-10 recording]
---
# Activation functions

Without activation functions a network is just a linear model, however many layers it has. Activations bring in non-linearity, which lets the network learn complex patterns.

Common ones:

- **Step**: output 1 if z ≥ 0, else 0. The original perceptron. Not used in training today because its slope is zero almost everywhere, so gradient descent gets no signal.
- **Sigmoid**: σ(z) = 1 / (1 + e^(−z)). Squashes any number into (0, 1). Example: σ(−2.5) ≈ 0.08. Used for probabilities.
- **ReLU** (rectified linear unit): max(0, z). Negative values become 0; positive values pass unchanged. The typical choice for **hidden layers**.
- **Leaky ReLU**: like ReLU but lets a small slope through for negatives, so neurons do not "die".
- **Softmax**: turns a vector of scores into probabilities that sum to 1. Used for multi-class outputs.
- **GELU** and **tanh** were also named.

Usually one activation is set per layer. A student asked if each neuron in a layer could have a different activation. The lecturer said it is possible but rarely done.

Note: a neuron's weighted sum z can be negative (weights and bias can be negative). The activation decides what happens to it.

## Related
- [Output-layer activation](output-layer-activation.md)
- [Neural network](neural-network.md)
- [Vanishing gradients](vanishing-gradients.md)
