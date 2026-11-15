---
summary: One hidden layer with enough neurons and a non-linear activation can approximate any continuous function.
type: concept
tags: [neural-networks, theory, exam]
sources: [neural networks slides, lecture-10 recording]
---
# Universal approximation theorem

Cybenko (1989) showed that a feedforward network with:

- **one hidden layer**,
- **enough hidden neurons**, and
- a suitable **non-linear activation** (Cybenko used sigmoid; later work covers others such as ReLU and tanh)

can approximate any continuous function on a bounded region, as closely as you like.

In plain words: with enough neurons, even a shallow network can draw any smooth shape you need. This revived interest in neural networks after the XOR setback.

What the theorem does **not** say:

- It does not say how many neurons you need. It may be a huge number.
- It does not say training will find the right weights.
- It does not say the network will generalise to new data. A network that can fit anything can also overfit anything.

So "neural networks can learn anything" is a statement about what is possible, not about what happens with your 500 rows.

## For the capstone
Our data is small: 16 regions × about 11 years of weeks, with few flood weeks. The theorem is no reason to expect an NN to beat LightGBM here.

## Related
- [Multilayer perceptron](multilayer-perceptron.md)
- [Network depth and width](network-depth-and-width.md)
- [The XOR problem](xor-problem.md)
