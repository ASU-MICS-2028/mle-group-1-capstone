---
summary: Supervised, unsupervised, self-supervised and weakly supervised learning differ in where labels come from.
type: concept
tags: [foundations, labels]
sources: [lecture-05 recording, lecture-08 recording]
---
# Types of supervision

The lecturer sorted kinds of learning by one question: **where do the labels come from, and can you trust them?**

- **Supervised:** every example has a good label. The model learns the input-to-label mapping.
- **Unsupervised:** no labels at all. The model groups similar examples (clustering) or compresses the data. It does not invent labels.
- **Self-supervised:** no human labels, so the model makes its own "pseudo-labels" from the data and trains on them. Large language models are an example: they hide a word and learn to predict it.
- **Weakly supervised:** labels exist but are few (say 10 of 100 houses have a price) or partly wrong (noisy). The model uses what it has to learn the whole picture.

Reinforcement learning (learning from rewards) was mentioned only in passing.

Example: you have size and location for 100 houses. With all prices, it is supervised. With no prices, it is unsupervised (cluster similar houses). With prices for only some, or prices you suspect are wrong, it is weakly supervised.

## For the capstone
Our Groundsource labels are weak. A flood only counts if a news outlet reported it, so quiet rural floods are missed (false "no flood" labels). Say this openly in the report and the defence.

## Related
- [Supervised learning](supervised-learning.md)
- [Dataset size and diversity](dataset-size-and-diversity.md)
