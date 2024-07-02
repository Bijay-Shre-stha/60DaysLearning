x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]
z = []

for i, j in zip(x,y):
    z.append(i+j)
print(z)

# Using numpy
import numpy as np
x = np.array([1, 2, 3, 4, 5])
y = np.array([10, 20, 30, 40, 50])
# while adding two numpy arrays, it will add element wise and there is no comma  in between the elements of the array because it is a numpy array and not a list
z = np.add(x, y)
print(z)

# Create a custom ufunc that takes two arrays and returns the sum of the squares of their elements.

def sum_of_squares(x, y):
    return x**2 + y**2

sum_of_squares = np.frompyfunc(sum_of_squares, 2, 1)
x = np.array([1, 2, 3, 4, 5])
y = np.array([6, 7, 8, 9, 2])
z = sum_of_squares(x, y)
print(z)