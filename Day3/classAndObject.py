#Creating Class
class Person:
    name = "John"

    def function(self):
        print("This is a message inside the class.")

#Creating Object
p1 = Person()
print(p1.name)
#Accessing Object Properties
p1.function()

#Modifying Object Properties
p1.name = "Jane"
print(p1.name)


#init() function
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Name",name, " & age: ", age)

p1 = Person("John", 36)

# Exercise
# class Vehicle:
#     name=""
#     name = ""
#     kind = ""
#     color = ""
#     value = ""
#     def description(self):
#         desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
#         return desc_str
# car1=Vehicle()
# car2=Vehicle()
# car1.name = "Fer"
# car1.kind = "convertible"
# car1.color = "red"
# car1.value = 60000.00
# car2.name = "Jump"
# car2.kind = "van"
# car2.color = "blue"
# car2.value = 10000.00

# print(car1.description())
# print(car2.description())