import numpy as np
import matplotlib.pyplot as plt

x = np.sinh(np.pi/2)
print(f"The sinh of 90 degrees is {x}")

# cosh values for all of the values in arr
arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
cosh_arr = np.cosh(arr)
print(f"The cosh values of the angles are {cosh_arr}")

# finding the angles
x = np.arcsinh(1.0)
print(f"The arcsinh of 1 is {x}")

# angles of each value in the array
arr = np.array([0.1, 0.2, 0.5])
x = np.arctanh(arr)
print(f"The arctanh of the array is {x}")

# hyperbolic functions
x = np.tanh(np.pi/2)
print(f"The tanh of 90 degrees is {x}")

# plot the hyperbolic sine function
x = np.linspace(0, 2*np.pi)
y = np.sinh(x)
plt.title("Hyperbolic sine function")
plt.plot(x, y)
plt.show()
