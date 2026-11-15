---
summary: Semi-supervised learning uses a few labelled examples plus many unlabelled ones.
type: concept
tags: [foundations, types-of-learning]
sources: [intro slides]
---
# Semi-supervised learning

Semi-supervised learning sits between supervised and unsupervised learning. You have a **small labelled set** and a **large unlabelled set**. The labels guide what the model learns from the unlabelled data.

Example from the slides: cluster all the data first (unsupervised), then use the few labelled points to name each cluster (supervised).

It is useful when labelling is expensive, e.g. a doctor has to read each scan.

## Related
- [Types of supervision](types-of-supervision.md)
- [Supervised learning](supervised-learning.md)
- [Unsupervised learning](unsupervised-learning.md)
