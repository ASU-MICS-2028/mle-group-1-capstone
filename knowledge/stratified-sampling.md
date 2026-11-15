---
summary: Stratified sampling splits the population into groups and samples from every group.
type: concept
tags: [sampling]
sources: [probability & sampling slides, lecture-03 recording]
---
# Stratified sampling

Three basic ways to draw a sample:

- **Simple random sampling** – every unit has the same chance, drawn independently. Clean theory, but expensive when units are scattered.
- **Stratified sampling** – split the population into groups (**strata**), e.g. regions or urban/rural, and draw a sample from **every** group. Every group is guaranteed to appear. More precise when groups differ, but you must know the groups in advance.
- **Cluster sampling** – see [Cluster sampling](cluster-sampling.md).

Stratified samples often deliberately over-sample small groups, which is why they need sampling weights to describe the whole population.

The same idea appears in ML as a **stratified split**: keep the share of each class the same in train and test. The lecturer suggested stratified splits for Prosit 1.

## For the capstone
A random stratified split is wrong for us (time order matters), but we can still check that every region and both classes appear in each of the train/tune/test periods.

## Related
- [Cluster sampling](cluster-sampling.md)
- [Sampling weights](sampling-weights.md)
- [Train, validation and test sets](train-validation-test-split.md)
