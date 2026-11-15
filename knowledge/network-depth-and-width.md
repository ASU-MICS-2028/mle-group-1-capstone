---
summary: Depth is layer count, width is neurons per layer; both add capacity, need more data and risk overfitting.
type: concept
tags: [neural-networks, hyperparameters, overfitting, lecturer-emphasis]
sources: [neural networks slides, lecture-10 recording, lecture-11 recording]
---
# Network depth and width

- **Depth** = number of layers. "Deep learning" means many layers.
- **Width** = number of neurons in a layer.

Both increase the number of parameters, so both make the model more complex. The lecturer asked students to relate this to **bias and variance**, and said "you should know these things intuitively".

Effects of more depth:

- often better accuracy on complex data;
- slower learning;
- risk of overfitting;
- risk of **vanishing gradients**.

Effects of more width on a small dataset: each neuron learns its own piece of the input, so many neurons on few examples memorise noise. Overfitting again. The rule: grow the dataset as you grow width.

How layers divide the work, for images: early layers learn general features (edges), later layers learn specific details. Too many layers means learning minute details of the training set, which is overfitting.

Diagnosis: if the model overfits, try reducing depth or width. If the data is simple and small, start with a narrow, shallow network. Use EDA to judge how complex the data really is.

Depth, width and activation are **hyperparameters**: set before training, not learned.

## Related
- [Multilayer perceptron](multilayer-perceptron.md)
- [Vanishing gradients](vanishing-gradients.md)
- [Parameters vs hyperparameters](hyperparameters.md)
- [Generalisation](generalisation.md)
