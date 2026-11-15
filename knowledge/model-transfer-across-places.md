---
summary: A model trained mostly on one country or region may not hold in another with different data.
type: lesson
tags: [generalisation, distribution-shift, prosit-2, fairness]
sources: [lab-session-1 discussion, prosit-2 lecture notes]
---
# Model transfer across places

The Prosit 2 data was mostly Kenyan, with little Ghanaian data. Applying the Kenyan-trained model directly to Ghana still predicted a very high default rate. The strongest predictor (past repayment history) did not exist for Ghanaian applicants, so a strict model would have rejected everyone.

Lesson: when the training population differs from the deployment population, the model's patterns may not carry over. This is **distribution shift**. Check it rather than assume:

- compare feature distributions between the two places;
- report performance separately for each place;
- watch for features that are missing or behave differently in the new place.

Our Prosit 2 notes also suggested PCA or clustering plots to show whether the new place's points fall in regions the training data never covered.

## For the capstone
Our 16 regions differ a lot (e.g. Greater Accra's dense coverage vs northern regions). Report results per region, and check whether some regions have so few reported floods that the model is effectively trained on others.

## Related
- [Generalisation](generalisation.md)
- [Principal component analysis](principal-component-analysis.md)
- [Ethics and fairness review pack](ethics-and-fairness-review-pack.md)
