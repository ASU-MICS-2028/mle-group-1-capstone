---
summary: Batch, stochastic and mini-batch gradient descent differ in how many examples each update uses.
type: concept
tags: [optimisation]
sources: [lecture-06 recording, lec4 slides, MIT 6.390 ch3, neural networks slides]
---
# Batch, stochastic and mini-batch gradient descent

The three versions differ only in how many training examples are used to compute each gradient step.

- **Batch gradient descent:** uses the whole training set for every step. Steps are smooth and stable, but each one is slow when there are many rows.
- **Stochastic gradient descent (SGD):** uses one randomly chosen example per step. Each step is very cheap but noisy, so the path zig-zags. On average it still heads downhill and does converge, especially if the step size shrinks over time.
- **Mini-batch gradient descent:** uses a small group of B examples (say 32 or 256) per step. It balances stability and speed and runs well on GPUs. SGD is the special case B = 1. This is where the term "batch size" comes from.

Example: with 10,000 rows, one pass over the data (an **epoch**) is 1 step for batch GD, 10,000 steps for SGD, and about 40 steps for mini-batches of 256.

## Related
- [Gradient descent](gradient-descent.md)
- [Learning rate](learning-rate.md)
