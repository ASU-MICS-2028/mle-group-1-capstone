---
summary: An MLP is a feedforward network with one or more hidden layers of non-linear neurons.
type: concept
tags: [neural-networks, mlp]
sources: [neural networks slides, lecture-10 recording, lecture-11 recording]
---
# Multilayer perceptron (MLP)

A multilayer perceptron stacks neurons into layers: input → one or more hidden layers → output. Data flows one way, left to right, with no loops. That is why it is also called a **feedforward** network.

Each hidden neuron takes a weighted sum of *all* outputs of the previous layer, adds a bias, and applies a non-linear activation. Its output becomes an input to every neuron in the next layer.

Why it works: each hidden neuron draws one simple boundary. Later layers combine those boundaries into curved, complex ones. That is how an MLP solves XOR and other problems a linear model cannot.

Why the activation must be non-linear: stacking linear layers just gives another linear function. Two linear steps, 2(3x) = 6x, collapse into one.

Design choices before training:

- **Depth**: number of hidden layers.
- **Width**: neurons per layer (layers may differ, e.g. 10, 5, 10).
- **Activation function** for each layer.

These are hyperparameters. Bigger networks can fit more complex patterns but need more data.

In scikit-learn this is `MLPClassifier`.

## For the capstone
If we add a small NN, an `MLPClassifier` with one or two small hidden layers on the same scaled features is the natural choice, compared on the same temporal split.

## Related
- [Neural network](neural-network.md)
- [The XOR problem](xor-problem.md)
- [Network depth and width](network-depth-and-width.md)
- [Universal approximation theorem](universal-approximation-theorem.md)
