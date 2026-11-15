---
summary: Dimensionality reduction re-describes each point with far fewer numbers while keeping most information.
type: concept
tags: [unsupervised, dimensionality-reduction]
sources: [unsupervised slides, lecture-08 recording]
---
# Dimensionality reduction

You have n points, each with d features. Dimensionality reduction finds a new description of each point with k numbers, where k is much smaller than d. The new description is called an **embedding**.

Why do it:

- **Visualisation**: with k = 2 or 3 you can plot the data.
- **Less overfitting**: fewer inputs give the model fewer ways to memorise noise. The slides frame this as a kind of regularisation.
- **Speed and storage**: fewer columns train and store faster.
- **Removing redundancy**: many real features are correlated and repeat each other.

More features are not always better. With thousands of features, many may be noise that the model still tries to fit.

Clustering versus dimensionality reduction (a slide learning objective): clustering is for **discovering groups** of rows; dimensionality reduction is for **compressing** the columns.

The method covered in the course is **PCA**. The lecturer also mentioned autoencoders (a neural network that squeezes data through a narrow middle layer) and his own work dropping unimportant frequencies from images.

## For the capstone
Our feature set is small (rainfall, soil moisture, terrain, built-up land), so we probably do not need reduction for modelling. A 2-D PCA plot of region-weeks coloured by flood/no-flood could still be a useful EDA figure.

## Related
- [Principal component analysis](principal-component-analysis.md)
- [Unsupervised learning](unsupervised-learning.md)
- [Curse of dimensionality](curse-of-dimensionality.md)
