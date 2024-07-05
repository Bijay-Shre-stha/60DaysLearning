import numpy as np
import matplotlib.pyplot as plt

# converting array with repeated values to a set
arr = np.array([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])
print(f"Array with repeated values: {arr}")
x = np.unique(arr)
print(f"Array converted to a set: {x}")

# union 
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([4, 5, 6, 7, 8])
x = np.union1d(arr1, arr2)
print(f"Union of the two arrays: {x}")

# intersection
x = np.intersect1d(arr1, arr2)
print(f"Intersection of the two arrays: {x}")

# difference
x = np.setdiff1d(arr1, arr2)
print(f"Difference between the two arrays: {x}")

# symmetric difference
x = np.setxor1d(arr1, arr2)
print(f"Symmetric difference between the two arrays: {x}")

