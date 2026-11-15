---
summary: Sample averages settle on the true average as n grows, but this does not remove bias.
type: concept
tags: [sampling, statistics]
sources: [probability & sampling slides]
---
# Law of large numbers

The **law of large numbers** says that as the sample size n grows, the sample average gets closer and closer to the true population average.

What it does **not** promise:
- a biased estimator will become unbiased;
- dependence between observations goes away;
- you converge to the quantity you *meant* to measure.

Example: toss a fair coin 10 times and you might get 70% heads; toss it 10,000 times and you will be very close to 50%. But if the coin is bent, more tosses only pin down the bent coin's rate more precisely.

## Related
- [Central limit theorem](central-limit-theorem.md)
- [Sampling bias](sampling-bias.md)
