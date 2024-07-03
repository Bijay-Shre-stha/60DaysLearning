import numpy as np

# Create an array of 10 random numbers from 0 to 10
arr = np.random.rand(10) * 10
print("Original array:")
print(f"{arr}\n")

print("Truncate the decimal values from the random numbers:")
print(np.trunc(arr))

print("\nFix the decimal values from the random numbers:")
print(np.fix(arr))

print("\nRound the decimal values from the random numbers:")
print(np.round(arr))

print("\nFloor the decimal values from the random numbers:")
print(np.floor(arr))

print("\nCeil the decimal values from the random numbers:")
print(np.ceil(arr))
