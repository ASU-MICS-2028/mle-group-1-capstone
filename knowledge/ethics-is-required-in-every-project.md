---
summary: The lecturer expects a bias, fairness and ethics discussion in every ML project.
type: rule
tags: [course-rules, ethics, fairness]
sources: [lecture-01 recording]
---
# Ethics is required in every project

In lecture 1 the lecturer called the bias/fairness/ethics outcome "very important". His reasoning, in plain terms:

- Real datasets already contain bias, because of how and from whom they were collected.
- If you take such data as it is and train on it, the model learns and repeats that bias.
- So every ML project should include a discussion of ethics and a plan to reduce harm, not an afterthought.

He gave examples from the readings: *Gender Shades* (face classifiers that worked worse on darker-skinned women) and surveillance systems built abroad that flag Black people more often. Suggested tools: *Datasheets for Datasets* and *Model Cards*.

Small example: a model trained only on city hospital records will look good on city patients and quietly fail on rural ones.

## For the capstone
Our labels are news reports, so regions with less media coverage (often rural, northern) may look "safer" than they are. A per-region error check and an honest caveat in the dashboard are the minimum.

## Related
- [Sampling bias](sampling-bias.md)
- [Types of supervision](types-of-supervision.md)
- [Capstone learning outcomes](capstone-learning-outcomes.md)
