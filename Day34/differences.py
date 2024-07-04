import numpy as np

arr1 = np.array([10, 15, 25, 5])
arr2 = np.array([10, 15, 25, 5, 0])
print(f"arr1: {arr1}")
print(f"arr2: {arr2}")

diffArr = np.diff(arr1)
print(f"Difference of arr1: {diffArr}")

discreteDiffArr = np.diff(arr2, n=2)
print(f"Discrete Difference of arr2: {discreteDiffArr}")

editArr = np.ediff1d(arr1)
print(f"Element-wise difference of arr1: {editArr}")

editArr2 = np.ediff1d(arr2, to_end=[10, 20])
print(f"Element-wise difference of arr2: {editArr2}")

gradientArr = np.gradient(arr1)
print(f"Gradient of arr1: {gradientArr}")
