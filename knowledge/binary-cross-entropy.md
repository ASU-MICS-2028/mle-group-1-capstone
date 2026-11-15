---
summary: Binary cross-entropy punishes confident wrong probabilities hard; it is the standard loss for yes/no outputs.
type: concept
tags: [loss, classification, neural-networks]
sources: [neural networks slides, lecture-11 recording]
---
# Binary cross-entropy (log loss)

For a true label y (0 or 1) and a predicted probability ŷ, the loss for one example is:

L = −[ y log(ŷ) + (1 − y) log(1 − ŷ) ]

Average this over all examples in the batch.

Only one term is active at a time:

- If y = 1, the loss is −log(ŷ). ŷ = 0.9 gives about 0.11. ŷ = 0.1 gives about 2.3.
- If y = 0, the loss is −log(1 − ŷ).

So the loss is small when the model is right and confident, and very large when it is wrong and confident. That is exactly what the slide asks for: punish the network more when it is wrong *and* sure.

Notes:

- The log is the natural log (base e) in libraries. The class got stuck on log(0): as ŷ approaches 0 for a true positive, the loss heads to infinity. Libraries clip ŷ slightly away from 0 and 1 to avoid this.
- It is the same loss as logistic regression's.
- **Limitation** (slide): on imbalanced data the model can lean toward the majority class.

For multi-class problems, categorical cross-entropy does the same with softmax outputs: −log of the probability given to the true class.

## Related
- [Classification loss functions compared](classification-loss-functions-compared.md)
- [Logistic regression](logistic-regression.md)
- [Accuracy misleads on imbalanced data](accuracy-misleads-on-imbalanced-data.md)
