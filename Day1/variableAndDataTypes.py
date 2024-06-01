#Integers
int = 7
print(int)

#Floats
myFloat = 7.0
print(myFloat)
myFloat = float(7)
print(myFloat)

#Strings
string = 'Hello World!'
print(string)
string = "Hello World!"
print(string)

useDoubleQuotes = "I'm using double quotes"
print(useDoubleQuotes)

#simultaneously
a,b = 5,6
print("Simultaneously:", a, b)

#Mixing operators between numbers and strings is not supported
#This will not work!
# one = 1
# two = 2
# hello = "hello"

# print(one + two + hello)

#Fix it by converting the integers into strings
one = 1
two = 2
hello = "hello"

print(str(one) + str(two) + hello)


#Complex Numbers
complexNumber = 1 + 2j
z = 1j   # complex

print(complexNumber)
print(type(z))