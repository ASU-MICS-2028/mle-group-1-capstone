---
summary: A neural network is layers of neurons; each neuron takes a weighted sum then applies an activation.
type: concept
tags: [neural-networks, foundations]
sources: [neural networks slides, lecture-10 recording]
---
# Neural network

A neural network is a family of models built to find **non-linear patterns** in data. The idea is borrowed loosely from the brain: a biological neuron receives signals through branches (dendrites), "fires" when the total signal passes a threshold, and passes a signal on.

An artificial neuron does two steps:

1. **Weighted sum**: multiply each input by its weight, add them, add a bias. z = w₁x₁ + w₂x₂ + … + b.
2. **Activation**: pass z through an activation function a = f(z), which decides how strongly the neuron "fires".

Neurons are arranged in layers:

- **Input layer**: the features (e.g. rainfall, soil moisture).
- **Hidden layers**: neurons between input and output. In a standard (fully connected) network, each neuron takes input from every neuron in the previous layer.
- **Output layer**: the prediction.

The activated output of a hidden layer is what NLP papers call a "hidden state". It carries what the layer has learned about the input on to the next layer.

Example: inputs x₁ = 1, x₂ = 2, weights 0.5 and −1, bias 0.3. Then z = 0.5 − 2 + 0.3 = −1.2. With ReLU, the output is 0; with sigmoid it is about 0.23.

## For the capstone
The course allows a small neural network only where the data justifies it, as a comparison against the classical models.

## Related
- [A single neuron is a linear model](single-neuron-is-a-linear-model.md)
- [Multilayer perceptron](multilayer-perceptron.md)
- [Activation functions](activation-functions.md)
- [Types of neural networks](types-of-neural-networks.md)
