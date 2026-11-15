---
summary: A datasheet answers seven groups of questions so users can judge a dataset's fitness and biases
type: source
tags: [fairness, documentation, reading, data]
sources: [Gebru et al. 2021, Datasheets for Datasets, Communications of the ACM 64(12), doi:10.1145/3458723, https://arxiv.org/abs/1803.09010]
---
# Datasheets for datasets (Gebru et al. 2021)

Electronic parts come with datasheets describing how they were made and where they should not be used; datasets should too. The **creator** answers a fixed set of questions so the **user** can decide whether the data fit their task and can see hidden biases and legal limits. The questions are a guide, not a form: skip what does not apply, and "unknown" is an acceptable, honest answer.

**Seven question groups:**
1. **Motivation** — why, by whom, funded by whom.
2. **Composition** — what a row is, how many, sample or complete, representativeness, label, missing data, noise, sensitive data, subpopulations.
3. **Collection process** — how and when acquired, who collected, consent, ethical review.
4. **Preprocessing/cleaning/labelling** — what was done, raw data kept, code available.
5. **Uses** — past uses, other possible uses, risks of unfair treatment, **tasks it should not be used for**.
6. **Distribution** — how shared, licence, IP restrictions.
7. **Maintenance** — who maintains, errata, updates, versions.

## For the capstone
Write one datasheet for our derived region-week table, with a section on Groundsource itself. Key honest answers: labels were extracted from news by an LLM (Gemini); one event = a news-derived polygon and date; coverage rises sharply over time; Accra is over-represented; local-language and radio coverage is unknown; precision estimates vary (75% in one abstract); CC BY 4.0. Composition should give the positive rate per region.

## Related
- [Groundsource dataset](groundsource-dataset.md)
- [News label bias](news-label-bias.md)
- [Model cards](model-cards.md)
- [Ethics and fairness review pack](ethics-and-fairness-review-pack.md)
