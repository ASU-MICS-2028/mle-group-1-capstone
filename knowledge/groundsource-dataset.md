---
summary: Groundsource — Google's news-derived global flood events (CC BY 4.0); 2,688 Ghana events, our label source
type: source
tags: [data, flood, labels, groundsource]
sources: [Flood options report §3 and §5, Zenodo record 18647054, Mayo et al. 2026 doi:10.31223/x5rr2k, EGU26-3253 doi:10.5194/egusphere-egu26-3253, Google Research blog]
---
# Groundsource dataset

**What it is.** Flood events extracted from news articles using Google's Gemini model, each with a polygon and dates. 2,646,302 events worldwide, 2000 to early 2026, ~667 MB. Licence **CC BY 4.0**. Status: **downloaded and counted** by the team.
- Data: https://zenodo.org/records/18647054. Confirmed via the Zenodo API on 2026-11-15: one file, `groundsource_2026.parquet` (667,122,400 bytes), licence `cc-by-4.0`, v1 snapshot.
- Preprint: Mayo R, Zlydenko O, Bootbool M, et al. (2026), EarthArXiv, doi:10.31223/x5rr2k
- Abstract: Zlydenko et al. (2026), EGU26-3253, doi:10.5194/egusphere-egu26-3253
- Blog: https://research.google/blog/introducing-groundsource-turning-news-reports-into-data-with-gemini/

**Ghana counts** (team's count, polygon centre inside geoBoundaries ADM1 regions): **2,688 events, June 2006 – January 2026; 2,305 in 2015–2025.** Greater Accra holds 1,014 (38%); Oti, Bono, Ahafo and Western North together 56. Only 2 events in 2012 vs 333 in 2022. Peaks in June and Sept–Oct (two rainy seasons). 3 June 2015 is the busiest day (61 events, 44 in Greater Accra); 15 Sep–31 Oct 2023 (Akosombo spillage) has 108, 52 in Volta. Median polygon ~2.6 km², ~11% exceed 500 km² (likely whole-town/district mentions). 27% of events span more than one day.

**How rare is the label (2015–2025)?**

| Unit | Positives | Total | Rate |
|---|---|---|---|
| Region-week (16 regions) | 585 | 9,184 | 6.4% |
| Region-day | 821 | 64,288 | 1.3% |
| Greater Accra weeks | 124 | 574 | 21.6% |
| Greater Accra days | 205 | 4,018 | 5.1% |

**Accuracy.** The figures don't agree. Google's launch blog says that in manual review, **60%** of extracted events were accurate in both location and timing. The EGU26 abstract gives about **75%** precision. Google also reports that it caught 85–100% of severe GDACS-recorded floods in 2020–2026. Plan for roughly 1 in 3 events being wrong somewhere, and let our audit (W04) settle it for Ghana. Read the preprint and hand-audit a sample (~100 events planned).

**Not verified:** centroid assignment puts multi-region events in one region; boundaries simplified; no hand-check of Ghana events yet; language coverage in Ghana unknown.

## For the capstone
Label = at least one event in a region-week. Count a week once even if a storm produced many events.

## Related
- [News label bias](news-label-bias.md)
- [Reporting drift](reporting-drift.md)
- [Flood problem formulation](flood-problem-formulation.md)
- [geoBoundaries](geoboundaries.md)
- [Datasheets for datasets](datasheets-for-datasets.md)
