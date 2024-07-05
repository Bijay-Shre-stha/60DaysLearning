import numpy as np
import matplotlib.pyplot as plt

x = np.sin(np.pi/2)
print(f"The sin of 90 degrees is {x}")

# converting degrees to radians

arr = np.array([90, 180, 270, 360])
deg2rad= np.deg2rad(arr)
print(f"The radian values of the angles are {deg2rad}")

# converting radians to degrees

arr = np.array([np.pi/2, np.pi, 1.5*np.pi, 2*np.pi])
rad2deg = np.rad2deg(arr)
print(f"The degree values of the angles are {rad2deg}")

# angles

x = np.arcsin(1.0)
print(f"The arcsin of 1 is {x}")

# angles of each value in the array

arr = np.array([1, -1, 0.1])
x = np.arcsin(arr)
print(f"The arcsin of the array is {x}")

# hypotenuse

base = 3
perpendicular = 4
hypotenuse = np.hypot(base, perpendicular)
print(f"The hypotenuse of the triangle is {hypotenuse}")

# plot the sine function

x = np.linspace(0, 2*np.pi)
y = np.sin(x)
plt.title("Sine function")
plt.plot(x, y)
plt.show()
