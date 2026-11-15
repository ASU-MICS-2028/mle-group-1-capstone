---
summary: A dataset is judged by how many examples it has and how much variety they cover.
type: concept
tags: [data, foundations]
sources: [lecture-05 recording]
---
# Dataset size and diversity

The lecturer described a dataset with two properties:

- **Size:** the number of examples (rows).
- **Diversity:** how different the examples are from each other, that is, how much of the possible range they cover.

Both limit what a model can learn. If all your houses are small two-bedroom flats in one town, the model cannot learn how price behaves for large houses elsewhere, however many flats you add. More rows of the same kind do not fix low diversity.

Features can be of mixed types in one example (numbers, categories like wind direction). Images, audio and text are also turned into numbers before training. Combining several of these types is called multimodal learning.

The lecturer also said the quality of the features you pick largely sets the quality of the model. Different groups may choose different features for the same problem, and that is fine if it is justified.

## For the capstone
Flood weeks are rare and cluster in a few regions and rainy months. Check how many positive region-weeks each region has. A region with almost no positives gives the model little to learn from, and the test years (2024–2025) may contain conditions not seen in 2015–2022.

## Related
- [Supervised learning](supervised-learning.md)
- [Class imbalance](class-imbalance.md)
- [Types of supervision](types-of-supervision.md)
