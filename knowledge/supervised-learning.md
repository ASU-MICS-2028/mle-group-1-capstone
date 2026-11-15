---
summary: Supervised learning learns a mapping from inputs to outputs using labelled examples.
type: concept
tags: [supervised-learning, foundations]
sources: [lecture-05 recording, lec4 slides, lec5 slides, intro slides, lecture-01 recording]
---
# Supervised learning

Supervised learning means learning from examples that come with the right answer. Each **example** is a pair: the **features** (the inputs, such as house size and location) and the **label** (the answer, such as the sale price). The model looks at many such pairs and learns a rule that maps features to labels. Then it can predict the label for a new example it has never seen.

The lecturer called this "learning by example". It is "supervised" because the labels act like a teacher who marks every answer.

What the label looks like decides the task:
- a number (price, rainfall in mm) means **regression**;
- one of a fixed set of classes (spam / not spam) means **classification**.

Small example: you record the size and sale price of 20 houses in your area. A model fitted to those pairs can then suggest a price for your own 105 m² house.

If you have the features but no labels at all, the problem is no longer supervised. You can only look for groups or structure, which is unsupervised learning.

## For the capstone
Our examples are region-weeks. Features are rainfall, soil moisture, terrain and built-up land. The label is "at least one news-reported flood that week" from Groundsource, so this is supervised binary classification.

## Related
- [Regression vs classification](regression-vs-classification.md)
- [Types of supervision](types-of-supervision.md)
- [Supervised learning pipeline](supervised-learning-pipeline.md)
- [Dataset size and diversity](dataset-size-and-diversity.md)
- [Semi-supervised learning](semi-supervised-learning.md)
- [Unsupervised learning](unsupervised-learning.md)
