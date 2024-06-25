## **Poisson Distribution**

- Poisson Distribution is a discrete probability distribution that expresses the probability of a given number of events occurring in a fixed interval of time or space.
- It is used for independent events which occur at a constant rate within a given interval of time.
- It has two parameters:
  - `lam`: rate or known number of occurences e.g. 2 for above problem.
  - `size`: The shape of the returned array.
- The `np.random.poisson()` method is used to get a Poisson Distribution.

## **Uniform Distribution**

- Uniform Distribution is a distribution that has a constant probability.
- It is also known as Rectangular Distribution.
- All values have an equal chance of occuring.
- It has three parameters:
  - `a`: Lower bound - default 0.0.
  - `b`: Upper bound - default 1.0.
  - `size`: The shape of the returned array.
- The `np.random.uniform()` method is used to get a Uniform Distribution.

## **Summary**

- Poisson Distribution is a discrete probability distribution.
- It expresses the probability of a given number of events occurring in a fixed interval of time or space.
- Use the `np.random.poisson()` method to get a Poisson Distribution.
- Uniform Distribution is a constant probability distribution.
- Use the `np.random.uniform()` method to get a Uniform Distribution.
