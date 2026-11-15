---
summary: Regression uses a linear output, binary classification one sigmoid, multi-class a softmax.
type: rule
tags: [neural-networks, activation, exam]
sources: [neural networks slides, lecture-10 recording]
---
# Output-layer activation

The last layer's activation depends on what you are predicting.

**Regression** (a number, e.g. rainfall in mm): use a **linear** output (no activation). A squashing function would force the output into a fixed range. Sigmoid would cap a 20,000 prediction near 1; ReLU would block a needed negative value. Use a sigmoid only if the output must stay in an interval. The model is still non-linear overall, because the hidden layers have non-linear activations.

**Binary classification** (yes/no): one neuron with a **sigmoid**. It gives the probability of class 1. To get a hard yes/no, compare it with a threshold (0.5 by default).

**Multi-class classification** (one of several classes): one neuron per class with **softmax**. The outputs are probabilities that sum to 1. Predict the class with the highest probability. Example: scores for three cancer subtypes become 0.7, 0.2, 0.1, so predict subtype 1.

**Multi-label** (several classes can be true at once): treat each class separately, typically a sigmoid per class with its own threshold.

## For the capstone
Our task is binary (flood reported / not). Any model we use should output a probability, then a threshold chosen on the 2023 tuning year turns it into an alert.

## Related
- [Activation functions](activation-functions.md)
- [Multi-class vs multi-label classification](multiclass-vs-multilabel-classification.md)
- [Choosing a classification threshold](classification-threshold.md)
