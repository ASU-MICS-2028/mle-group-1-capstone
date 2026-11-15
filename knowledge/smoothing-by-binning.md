---
summary: Binning smooths noise by sorting values into bins and replacing each by its bin mean.
type: procedure
tags: [preprocessing, cleaning]
sources: [preprocessing & leakage slides, lecture-04 recording]
---
# Smoothing noisy data by binning

**Binning** reduces small random errors (noise):
1. **Sort** the values.
2. Split them into equal-size bins.
3. Replace each value with its bin's mean (or median, or nearest bin edge).

Worked example from the slides. Sorted: 4, 8, 9, 15, 21, 21, 24, 25, 26, 28, 29, 34. Bins of four:
- 4, 8, 9, 15 → mean 9
- 21, 21, 24, 25 → mean 22.75
- 26, 28, 29, 34 → mean 29.25

Why sort first: if the large value 34 landed in a bin with 4, 8 and 9, it would be replaced by about 14 and badly distorted. In a sorted bin of similar values it only moves to about 29.

Does it lose information? The lecturer's answer: individual values change, but the feature keeps its overall pattern while the model learns less from noise.

Other smoothing methods named: regression (fit a trend and use it) and clustering. A related idea, **discretisation**, turns a continuous feature into labelled ranges (e.g. age → young / middle-aged / senior).

## Related
- [Dirty data](dirty-data.md)
- [Outlier detection](outlier-detection.md)
- [Feature engineering](feature-engineering.md)
