import numpy as np

def add(x, y):
    return x + y

myAdd = np.frompyfunc(add, 2, 1)
x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]
z = myAdd(x, y)
print(z)
# type
print(type(myAdd))
print(type(np.concatenate))

if type(myAdd) == np.ufunc:
    print("myAdd is a ufunc")
else:
    print("myAdd is not a ufunc")

# making project with ufunc (calculating the distance between two points)

def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def subtract(x, y):
    return x - y

add = np.frompyfunc(add, 2, 1)
multiply = np.frompyfunc(multiply, 2, 1)
divide = np.frompyfunc(divide, 2, 1)
subtract = np.frompyfunc(subtract, 2, 1)

while True:
    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))
    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))

    distance = np.sqrt(add(multiply(subtract(x2, x1), subtract(x2, x1)), multiply(subtract(y2, y1), subtract(y2, y1))))
    print("The distance between the two points is: ", distance)
    choice = input("Do you want to continue? (y/n): ")
    if choice == 'n':
        break