---
summary: Initialise randomly, forward pass, compute loss, backpropagate, update, repeat until the loss stops improving.
type: procedure
tags: [neural-networks, training]
sources: [neural networks slides, lecture-11 recording]
---
# Neural network training loop

The steps from the slides:

1. **Initialise** weights and biases randomly.
2. **Forward pass**: compute every hidden neuron and the output ŷ for a batch of examples. Remember the activation at each neuron.
3. **Loss**: compare ŷ with the true y using a loss suited to the task (MSE or MAE for regression, binary cross-entropy for yes/no, categorical cross-entropy for multi-class). Average over the batch.
4. **Backpropagate**: compute the gradient of the loss with respect to every parameter.
5. **Update**: move each parameter a small step opposite to its gradient (gradient descent or another optimiser).
6. **Repeat** with new batches. Stop when the error stops improving or after a fixed number of updates.

The lecturer called step 5 the optimisation step and said there are better update rules than plain gradient descent.

Watch-out: "loss stops improving" should be judged on validation data, not training data, or you will train into overfitting. Stopping when validation loss rises is called early stopping (our addition).

## Related
- [Backpropagation](backpropagation.md)
- [Optimisers](optimisers.md)
- [Binary cross-entropy](binary-cross-entropy.md)
- [Batch, stochastic and mini-batch gradient descent](batch-stochastic-minibatch-gradient-descent.md)
