---
summary: Gather relevant real data, and record where it came from, how and who it misses.
type: procedure
tags: [pipeline, data]
sources: [intro slides, Terms notes, lecture-01 recording, lecture-02 recording]
---
# Data collection

Step two of the pipeline: gather data relevant to the problem. The slides list common sources: databases (queried with SQL), APIs, and sensors / IoT devices. Public datasets and surveys are others.

Points from the lectures:
- The lecturer wants **real data**, not toy datasets, in course work.
- Each dataset should come with a **data dictionary** (what each column means). The readings include *Datasheets for Datasets*, a standard way to document where data came from and its limits.
- How the data were collected decides how much you can trust estimates from it (see sampling). Ask who or what is missing.
- Check each source's licence and any restrictions (e.g. not uploading restricted data to AI tools).

"Collect as much as possible" (from the Terms notes) is only half right: relevant and representative beats large.

## For the capstone
Sources: Groundsource (flood labels from news), CHIRPS (rainfall), ERA5-Land (soil moisture), terrain and built-up land layers. Record version, download date, licence and known gaps of each in the datasheet.

## Related
- [Datasheets for datasets](datasheets-for-datasets.md)
- [Sampling bias](sampling-bias.md)
- [Data integration](data-integration.md)
- [AI-use policy](ai-use-policy.md)
- [The ML pipeline](ml-pipeline.md)
