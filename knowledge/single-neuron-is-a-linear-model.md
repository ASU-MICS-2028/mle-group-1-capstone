---
summary: One neuron with a linear (identity) activation is exactly a linear model; non-linear activation changes that.
type: concept
tags: [neural-networks, linear-models]
sources: [neural networks slides, lecture-10 recording]
---
# A single neuron is a linear model

The linear classifier from earlier lectures is f(x) = w₁x₁ + w₂x₂ + b. Points with f(x) ≥ 0 get class 1, the rest get class 0. The line f(x) = 0 is the decision boundary.

Draw that as a unit: inputs come in, each is multiplied by a weight, a bias is added, and the result goes out. That is a neuron. The slide's key line: a single neuron without a non-linear activation function is a linear model.

The lecturer explained it as "an activation of 1": the sum passes straight through, unchanged. The cleaner way to say it is the **identity activation**, f(z) = z.

- Identity activation → still a linear model.
- Non-linear activation (step, sigmoid, ReLU) → the lecturer calls this a **perceptron**.

Two corrections to keep in mind:

- Historically, "perceptron" means a neuron with a **step** activation (Rosenblatt, 1958). Calling any non-linear neuron a perceptron is the lecturer's loose usage.
- One neuron with a sigmoid is logistic regression. Its *output* is non-linear in the inputs, but its *decision boundary* is still a straight line. One neuron alone still cannot solve XOR.

## Related
- [Neural network](neural-network.md)
- [Linear classifier](linear-classifier.md)
- [Logistic regression](logistic-regression.md)
- [The XOR problem](xor-problem.md)
