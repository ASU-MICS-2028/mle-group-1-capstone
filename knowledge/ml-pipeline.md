---
summary: The standard ordered steps from a vague problem to a deployed ML model.
type: procedure
tags: [foundations, pipeline]
sources: [intro slides, Terms notes, lecture-01 recording]
---
# The ML pipeline

The *pipeline* is the usual route through an ML project. The intro slides list these steps (the slides number "Step 9" twice; renumbered here):

1. **Problem formulation** – what exactly are we predicting, and what counts as success?
2. **Data collection** – databases, APIs, sensors, public datasets.
3. **Data preprocessing / cleaning** – missing values, duplicates, wrong formats.
4. **Exploratory data analysis (EDA)** – summaries and plots to understand the data.
5. **Feature engineering** – turn raw columns into useful model inputs.
6. **Data splitting** – train / validation / test.
7. **Model selection** – choose candidate algorithms.
8. **Model training** – fit the model's internal numbers (parameters) to the training data.
9. **Model evaluation** – measure performance on data the model has not seen.
10. **Hyperparameter tuning** – adjust settings you choose yourself (e.g. tree depth).
11. **Deployment** – put the model where real users get predictions.

It is not a straight line. Evaluation often sends you back to cleaning or features. Also, the order in a slide list hides a trap: anything that *learns from data* (scaling, imputing, encoding) must be fitted after the split, on training data only. See [split first, fit on train](split-first-fit-on-train.md).

The lecturer stressed step 11: a model that only lives in a notebook is not end-to-end.

## For the capstone
Our repo should mirror these steps: Groundsource labels + CHIRPS/ERA5/terrain features → cleaning → EDA → features → temporal split → baselines and models → evaluation on 2024–2025 → Streamlit dashboard.

## Related
- [Problem formulation](problem-formulation.md)
- [Data collection](data-collection.md)
- [Exploratory data analysis](exploratory-data-analysis.md)
- [Train, validation and test sets](train-validation-test-split.md)
- [The capstone must be end-to-end](end-to-end-pipeline-requirement.md)
