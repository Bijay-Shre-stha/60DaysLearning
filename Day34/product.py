import numpy as np

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])
print(f"arr1: {arr1}")
print(f"arr2: {arr2}")

x= np.prod(arr1)
y= np.prod(arr2)
print(f"Product of arr1: {x}")
print(f"Product of arr2: {y}")

arrProd = np.prod([arr1, arr2])
print(f"Product of arr1 and arr2: {arrProd}")

arrOverAxis = np.prod([arr1, arr2], axis=1)
print(f"Product of arr1 and arr2 over axis 1: {arrOverAxis}")

arrCumProd = np.cumprod(arr1)
print(f"Cumulative product of arr1: {arrCumProd}")