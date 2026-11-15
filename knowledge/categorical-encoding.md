---
summary: Turn categories into numbers with one-hot, ordinal, label or target encoding.
type: concept
tags: [preprocessing, feature-engineering]
sources: [intro slides, lecture-02 recording]
---
# Categorical encoding

Most models need numbers, so text categories must be encoded.

- **One-hot encoding** – one 0/1 column per category. Red = [1,0,0], Blue = [0,1,0], Green = [0,0,1]. Safe default. (The slide has a typo giving Green as [0,1,0], the same as Blue.)
- **Label encoding** – one integer per category (Red=1, Blue=2, Green=3). It invents a fake order (is Green "bigger" than Red?), which misleads linear models. Trees cope better.
- **Ordinal encoding** – integers when a real order exists: small < medium < large.
- **Target encoding** – replace each category with the average target for it (e.g. city → average house price). Powerful but it **uses the label**, so it must be computed on training data only (inside each CV fold), or it leaks the answer. The slide does not warn about this.

For Prosit 1 the lecturer asked for simple encoding, e.g. one-hot.

Too many categories one-hot encoded → many sparse columns (see curse of dimensionality).

## For the capstone
Region (16 values) can be one-hot encoded. Avoid target-encoding region on all years: a region's historical flood rate must come from training years only.

## Related
- [Feature engineering](feature-engineering.md)
- [Target leakage](target-leakage.md)
- [Curse of dimensionality](curse-of-dimensionality.md)
