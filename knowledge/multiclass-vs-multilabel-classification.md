---
summary: Multi-class picks exactly one class per example; multi-label allows several classes at once.
type: concept
tags: [classification, neural-networks]
sources: [neural networks slides, lecture-10 recording]
---
# Multi-class vs multi-label classification

**Multi-class**: each example belongs to exactly one of several classes. An image is a cat *or* a dog *or* a bird. Use softmax, whose outputs sum to 1, and pick the top one.

**Multi-label**: an example can belong to several classes at the same time. A photo can show a cat *and* a bed. A cell can show two cancer types. Here you need a separate yes/no decision per class, usually a sigmoid per class, each with its own threshold.

A student asked what softmax does when two classes tie (e.g. 0.35 and 0.35). In multi-class, you must still choose one, so a tie-break rule picks one (libraries take the first). If ties like this are common and both answers are genuinely right, the task is probably multi-label, not multi-class.

The slide learning objective mentions "two types of multi-class classification"; these are the two.

## For the capstone
Ours is plain binary, one label per region-week. If we later predicted flood *severity* levels (none, minor, major), that would be multi-class.

## Related
- [Output-layer activation](output-layer-activation.md)
- [Regression vs classification](regression-vs-classification.md)
