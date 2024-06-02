name = "Doe"
age = 25
print("Hello, my name is %s and I am %d years old." % (name, age))


#List
names = ["John", "Doe"]
print("Hello, my name is %s %s." % (names[0], names[1]))

list = []
list.append("John")
list.append("Doe")
print("Hello, my name is %s %s." % (list[0], list[1]))

numList = [1, 2, 3]
print("NumList: %s" % numList)

def name(string):
    print("Hello, " + string + "!")
print("Enter your name: ")
name(input())