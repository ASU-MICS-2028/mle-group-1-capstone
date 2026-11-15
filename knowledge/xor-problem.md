---
summary: No single straight line separates XOR's outputs, so one neuron fails and hidden layers are needed.
type: concept
tags: [neural-networks, history, exam]
sources: [neural networks slides, lecture-10 recording]
---
# The XOR problem

XOR ("exclusive or") outputs 1 when exactly one input is 1:

| x₁ | x₂ | XOR |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

Plot the four points. The 1s sit on one diagonal, the 0s on the other. No single straight line puts both 1s on one side and both 0s on the other. So one neuron (one line) cannot learn XOR.

Historically this simple failure fed doubts about perceptrons and contributed to a drop in funding and interest, one of the "AI winters" the lecturer mentioned.

The fix is to **stack neurons**. Use two hidden neurons, each drawing its own line. One line cuts off (0,0), the other cuts off (1,1). The output neuron then says "1 if the point is between the two lines". The slide shows a small network with weights of ±1 and biases −0.5 and −1.5 that does exactly this.

Lesson: hidden layers with non-linear activations let a network combine several simple boundaries into a complex one.

## Related
- [A single neuron is a linear model](single-neuron-is-a-linear-model.md)
- [Multilayer perceptron](multilayer-perceptron.md)
- [Universal approximation theorem](universal-approximation-theorem.md)
