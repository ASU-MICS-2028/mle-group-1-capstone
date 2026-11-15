---
summary: Barocas, Hardt & Narayanan's Fairness and Machine Learning — free book behind our fairness criteria
type: source
tags: [book, fairness]
sources: [Barocas, Hardt & Narayanan, Fairness and Machine Learning, MIT Press 2023, https://fairmlbook.org]
---
# Book: Fairness and Machine Learning (FML)

Barocas, Hardt & Narayanan, MIT Press 2023. Supplementary course text, free at https://fairmlbook.org.

| Chapter | Key ideas (our paraphrase) | Capstone use |
|---|---|---|
| Classification (ch. 3, https://fairmlbook.org/classification.html) | Most fairness definitions reduce to independence, separation or sufficiency; with unequal base rates they conflict; removing a sensitive column does not remove it (redundant encodings); worked credit-score example comparing thresholding rules | Choosing and justifying a primary fairness criterion across regions; proxy analysis |
| Later chapters (causality, testing discrimination, datasets) | Broader context on measurement and data collection | Background for the Datasheet and the news-label-bias discussion |

## For the capstone
Our "groups" are regions and urban/rural areas with very different label rates (Greater Accra 21.6% of weeks vs ~6.4% nationally), so the impossibility results apply directly: a calibrated model will have unequal error rates by region.

## Related
- [Fairness definitions](fairness-definitions.md)
- [Fairness impossibility](fairness-impossibility.md)
- [Proxy variables](proxy-variables.md)
- [Capstone resources](capstone-resources.md)
