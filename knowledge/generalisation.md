---
summary: A model is only useful if it works on new data, not just the data it trained on.
type: concept
tags: [foundations, evaluation]
sources: [intro slides]
---
# Generalisation

*Generalisation* means performing well on new examples the model has never seen. It is the whole point of ML.

The slides use handwritten digits: everyone writes "7" differently, so a model that memorised the training images is useless. It has to learn what makes a 7 a 7.

Two ways to fail:
- **Underfitting** – the model is too simple and misses the real pattern even on training data.
- **Overfitting** – the model is too flexible and learns the noise of the training data, so it does badly on new data.

That is why we judge a model on held-out data (a test set), never on the training data.

## For the capstone
"New data" for us means *future* weeks. We train on 2015–2022 and test on 2024–2025, which checks that the model generalises forward in time, not just to random rows.

## Related
- [Bias-variance trade-off](bias-variance-tradeoff.md)
- [Train, validation and test sets](train-validation-test-split.md)
- [Temporal split](temporal-split.md)
