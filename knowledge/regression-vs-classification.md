---
summary: Regression predicts a number; classification predicts a category.
type: concept
tags: [foundations, supervised-learning]
sources: [intro slides, Terms notes, lecture-05 recording, lec4 slides]
---
# Regression vs classification

Both are kinds of *supervised learning* (learning from examples that come with the right answer).

- **Regression** predicts a continuous number. Examples: a house price, tomorrow's temperature, millimetres of rain.
- **Classification** predicts a category (a class). Examples: spam / not spam, disease positive / negative. With two classes it is *binary* classification.

The type decides the metrics. Regression uses errors such as MSE (mean squared error) or RMSE (its square root). Classification uses accuracy, precision, recall and F1.

The lecturer stressed that the same domain can be framed either way, depending on how the label is defined: house *price* is regression, house *type* (studio, bungalow) is classification. You can also chain them: predict an exam score, then bin it into "low / medium / high".

Many classifiers actually output a probability (e.g. 0.27 chance of the positive class) and you pick a threshold to turn it into yes/no.

## For the capstone
Our task is binary classification (flood week or not). We could have predicted a flood *count* instead (regression or a count model), but a yes/no alert matches how NADMO would act.

## Related
- [Supervised learning](supervised-learning.md)
- [Bernoulli distribution](bernoulli-distribution.md)
- [Problem formulation](problem-formulation.md)
- [Logistic regression](logistic-regression.md)
- [RMSE and MAE](rmse-and-mae.md)
