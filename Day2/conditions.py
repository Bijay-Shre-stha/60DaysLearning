x = 2
print(x == 2) 
print(x == 3)
print(x < 3)
print(x > 1)
print(x != 1)


#Boolean operators
name = "Hello"
age = 20
if name != "Hello" and age == 20:
    print("Your name is Hello, and you are 20 years old.")
else:
    print("You are not Hello, and you are not 20 years old.")

#In operator
name = "Hello"
if name in ["Hello", "World"]:
    print("Hello is in the list")
else:
    print("Hello is not in the list")

#Not in operator
name = "Hello"
if name not in ["John", "World"]:
    print("Hello is not in the list")
else:
    print("Hello is in the list")

#Is operator
x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)
print(x is y)

#Not operator
print(not False)
print((not False) == (False))

#Elif statement
name = "Hello"
age = 20
if name == "Hello" and age == 20:
    print("Your name is Hello, and you are 20 years old.")
elif name == "Hello":
    print("Your name is Hello")
else:
    print("You are not Hello, and you are not 20 years old.")

#Short hand if
if name == "Hello": print("Hello")
else: print("World")
