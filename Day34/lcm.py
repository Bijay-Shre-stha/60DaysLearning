import numpy as np

num1 = 10
num2 = 15

lcm = np.lcm(num1, num2)
print(f"LCM of {num1} and {num2} is: {lcm}")

arr1 = np.array([3, 6, 9])
print(f"LCM of arr1: {np.lcm.reduce(arr1)}")

arr2 = np.arange(1, 11)
print(f"LCM of arr2: {np.lcm.reduce(arr2)}")