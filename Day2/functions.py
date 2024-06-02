def function_name():
    print("Hello, World!")

function_name()

#function with arguments
def function_name(name):
    print("Hello, " + name + "!")

function_name("John")

#function with return value
def function_name(name):
    return "Hello, " + name + "!"

print(function_name("John"))

#List as argument
list_names = ["John", "Jane", "Doe"]
def function_name(names):
    for name in names:
        print("Hello, " + name + "!")
function_name(list_names)

