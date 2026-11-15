---
id: 0004
status: Accepted
date: 2026-11-09
owner: Team (in the proposal) · confirmed by the instructor's reason for choosing B
issue: "W05"
---
# 0004 · Split by time: train 2015–2022, tune 2023, test 2024–2025

## Context
The instructor chose this project *because* it allows a real past→future split ([0002](0002-project-flood-early-warning.md)). Reporting also grows over time: 2 events in 2012 against 333 in 2022. A random split would mix future reporting habits into training.

## Decision
- **Train** on weeks starting 2015-01-05 to 2022-12-26. **Tune** (choose models, thresholds and calibration) on 2023. **Test** once, at the end, on 2024–2025.
- **No feature may use information from on or after `week_start`.** Rain from the week being predicted counts as a *forecast* feature. That gets a separate experiment, clearly labelled.
- **Never use `year` as a feature.** Data before 2015 is never used for training.
- **Extra checks:**
  - rolling-origin evaluation (train up to year *Y*, test *Y*+1);
  - leave-one-region-out, to test whether the model transfers to other regions.
- **Metrics:**
  - PR-AUC (the positive rate is about 6%);
  - recall at a fixed weekly alert budget (e.g. the top 3 regions each week);
  - calibration;
  - bootstrap 95% CIs over weeks.
- **2023 Akosombo spill weeks** (15 Sep–31 Oct): report results with and without them.

## Consequences
- The 2024–2025 test set is touched **once**. Every tuning choice uses 2023 or the rolling windows.
- These settings are the evaluation harness's contract (W05). The baselines and every model use the same code.
