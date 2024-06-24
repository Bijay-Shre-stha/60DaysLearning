## **Normal Distribution**

- Normal distribution is a continuous probability distribution function that is symmetrical on both sides of the mean.
- It fits the probability distribution of many events, eg. IQ Scores, Heartbeat etc.
- Two parameters are required to define a normal distribution:
  - **Mean(μ)**: The average value.
  - **Standard Deviation(σ)**: The dispersion of values from the mean.
- The `np.random.normal()` method is used to get a Normal Data Distribution.
- It takes three arguments:
  - `loc`: The mean of the distribution.
  - `scale`: The standard deviation of the distribution.
  - `size`: The shape of the returned array.
- `Note: The curve of a Normal Distribution is also known as the Bell Curve because of the bell-shaped curve.`

## **Binomial Distribution**

- Binomial Distribution is a Discrete Distribution.
- It describes the outcome of binary scenarios, eg. toss of a coin, it will either be head or tails.
- It has three parameters:
  - `n`: number of trials.
  - `p`: probability of occurence of each trial (e.g. for toss of a coin 0.5 each).
  - `size`: The shape of the returned array.
- The `np.random.binomial()` method is used to get a Binomial Distribution.
- It takes the `n`, `p` and `size` as shape of the array.

## **Summary**

- Normal Distribution is a continuous probability distribution.
- It is defined by the normal probability density function.
- It is the most important probability distribution in statistics.
- It is also called the Gaussian Distribution.
- It fits the probability distribution of many events, eg. IQ Scores, Heartbeat etc.
- Use the `np.random.normal()` method to get a Normal Data Distribution.
- Binomial Distribution is a Discrete Distribution.
- It describes the outcome of binary scenarios.
- It has three parameters: `n`, `p`, and `size`.
- Use the `np.random.binomial()` method to get a Binomial Distribution.
