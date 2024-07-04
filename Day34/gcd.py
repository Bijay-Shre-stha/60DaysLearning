import numpy as np

num1 = 10
num2 = 15

gcd = np.gcd(num1, num2)
print(f"GCD of {num1} and {num2} is: {gcd}")

arr1 = np.array([3, 6, 9])
print(f"GCD of arr1: {np.gcd.reduce(arr1)}")

arr2 = np.arange(1, 11)
print(f"GCD of arr2: {np.gcd.reduce(arr2)}")
