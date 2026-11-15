---
summary: The ethics pack needs a Datasheet, Model Card, disaggregated results, proxy analysis, regulatory mapping and a mitigation
type: rule
tags: [capstone, brief, ethics, fairness]
sources: [capstone brief §2 LO5, §5, lecture-09 recording]
---
# Ethics and fairness review pack

A separate group deliverable, due with the repo in Week 14, presented in slot 4 of the talk. It must contain:

1. **Datasheet** for the dataset (Gebru et al. 2021 questions).
2. **Model Card** for the final model (Mitchell et al. 2019 sections).
3. **Disaggregated fairness results** — metrics broken down by relevant groups, not just one overall number.
4. **Proxy analysis** — which features could stand in for a sensitive or structural attribute.
5. **Regulatory mapping** — which laws or rules apply and how the system meets them.

LO5 adds two items the pack should visibly include: a **harm analysis** and **at least one concrete mitigation** (ideally with before/after numbers).

## For the capstone
"Groups" here are regions, and urban vs rural areas, not people. The central fairness issue is unequal visibility in news-based labels: report results per region, test whether built-up share and population act as proxies for media attention, and apply a mitigation such as per-region alert thresholds.

**Discrepancy to note.** In the lecture-9 briefing the lecturer described datasheets and model cards as "suggested considerations", not compulsory. The written brief lists them as required parts of the pack. Follow the brief (the stricter source) and include both.

## Related
- [Datasheets for datasets](datasheets-for-datasets.md)
- [Model cards](model-cards.md)
- [Disaggregated evaluation](disaggregated-evaluation.md)
- [Proxy variables](proxy-variables.md)
- [Regulatory mapping](regulatory-mapping.md)
- [Flood ethics concerns](flood-ethics-concerns.md)
