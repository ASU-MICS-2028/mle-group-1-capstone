---
summary: ML is software that improves at a task from examples instead of hand-written rules.
type: concept
tags: [foundations, definition]
sources: [lecture-01 recording, intro slides]
---
# What machine learning is

Machine learning (ML) is the part of artificial intelligence where a program learns patterns from example data and then uses them to make predictions about new data. Nobody writes the rules by hand. The lecturer's short version: ML is "learning by examples".

Two classic definitions appear on the slides:

- **Arthur Samuel (1959):** ML lets computers learn without being explicitly programmed.
- **Tom Mitchell (1998):** a program learns from experience **E** on a task **T**, judged by a performance measure **P**, if its score P on T gets better as it gets more E.

Mitchell's version is useful because it forces you to name all three parts. If you cannot say what T, E and P are, the problem is not yet an ML problem.

Small example: T = "say if an email is spam"; E = a pile of emails already marked spam or not; P = the share of new emails sorted correctly.

## For the capstone
T = predict whether a Ghana region will have at least one news-reported flood in a given week. E = region-weeks from 2015–2022 with known labels. P = a metric on the held-out 2024–2025 weeks (for rare floods, recall/precision or PR-AUC, not plain accuracy).

## Related
- [When to use machine learning](when-to-use-machine-learning.md)
- [Problem formulation](problem-formulation.md)
- [The ML pipeline](ml-pipeline.md)
- [Generalisation](generalisation.md)
