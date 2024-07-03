import numpy as np

arr = np.arange(1,10)
print("Original array:")
print(f"{arr}\n")

print("Log at Base 2:")
print(np.log2(arr))

print("\nLog at Base 10:")
print(np.log10(arr))

print("\nNatural Log or Log at Base e:")
print(np.log(arr))

# Log at any base:
from math import log
nplog = np.frompyfunc(log, 2, 1)
print("\nLog at Base 5:")
print(nplog(arr, 5))