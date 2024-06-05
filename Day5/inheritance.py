class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printName(self):
        print(self.firstname, self.lastname)


x = Person("John", "Doe")
x.printName()


#using pass keyword to avoid error
class Student(Person):
    pass

s1 = Student("Mike", "Olsen")
print("Printing name of student")
s1.printName()

#using __init__() method
class Employee(Person):
    def __init__ (self, fname , lname):
        Person.__init__(self, fname, lname)
e1 = Employee("John ", "Doe")
print("Printing name of Employee")
e1.printName()

#using super() method
class Teacher(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
t1 = Teacher("Mike", "Olsen")
print("Printing name of Teacher")
t1.printName()

#using super() method with more arguments
class Teacher(Person):
    def __init__(self, fname, lname, age):
        super().__init__(fname, lname)
        self.age = age
t2 = Teacher("Mike", "Olsen", age=40)
print("Printing name of Teacher with age")
t2.printName()
print(t2.age)

#using super() method with adding method
class Teacher(Person):
    def __init__(self, fname, lname, age):
        super().__init__(fname, lname)
        self.age = age
    def printNameWithAge(self):
        print("My name is", self.firstname, self.lastname, "and I am", self.age, "years old")
t3 = Teacher("Jack", "Olsen", age=40)
print("Printing name of Teacher with age method")
t3.printNameWithAge()