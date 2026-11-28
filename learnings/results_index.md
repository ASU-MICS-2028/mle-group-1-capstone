# Results index

Every saved result, including failures and rejected options. A number that isn't listed here doesn't go in the report or the slides.

| File | What it shows | Made by (workstream) | Date |
|---|---|---|---|
| [tables/w01_label_options.csv](tables/w01_label_options.csv) | 8 label rules compared: positives, rate, train/test rate, regions with no positive. Chosen: centroid + start + keep all, 585 positives (6.4%) | W01 | 2026-11-23 |
| [figures/w01_label_eda.png](figures/w01_label_eda.png) | Events per year (120 in 2015 → 333 in 2022), per month (peaks Jun and Sep–Oct), share of weeks flagged per region (Greater Accra 21.6%, Ahafo 0%) | W01 | 2026-11-23 |
| [figures/w02_monthly_rain_by_region.png](figures/w02_monthly_rain_by_region.png) · [tables/w02_monthly_rain_by_region.csv](tables/w02_monthly_rain_by_region.csv) | Mean monthly CHIRPS rain per region, 2015–2025: two rainy seasons in the south (peaks Jun, Oct), one in the north (peak Aug–Sep). Sanity check for W02 features | W02 | 2026-11-22 |
| [tables/baselines.csv](tables/baselines.csv) | 3 baselines on 2023 (tune), with and without the Akosombo weeks, with 95% week-bootstrap CIs. Seasonal rate PR-AUC 0.25, rain rule 0.18, logistic 0.18; base rate 0.109 | W05 | 2026-11-23 |
| [tables/baselines_rolling_origin.csv](tables/baselines_rolling_origin.csv) | The same baselines, trained on 2015..Y-1 and scored on Y, for 2018–2023. Seasonal rate best in 4 of 6 years | W05 | 2026-11-23 |
| [tables/baselines_leave_one_region_out.csv](tables/baselines_leave_one_region_out.csv) | Train on 15 regions, predict the 16th (2015–2023). Rain rule 0.17, logistic 0.14; seasonal 0.04 (cannot transfer, as designed) | W05 | 2026-11-23 |
| [figures/report_fig1_labels.png](figures/report_fig1_labels.png) | Report Figure 1: reports per year (123 in 2015 → 333 in 2022), % of weeks flooded by month (peak June 14%, September 12%) and by region (Greater Accra 22%, Ahafo none) | W12 | 2026-11-28 |
| [figures/report_fig2_pipeline.png](figures/report_fig2_pipeline.png) | Report Figure 2: pipeline diagram, sources → build scripts → 9,184-row table → evaluation, models and dashboard | W12 | 2026-11-28 |
