class Base:
    def __init__ (self):
        self.a = "Hello World"
        # Private member
        self.__b = "Hello Python"

class Derived(Base):
    def __init__ (self):
        Base.__init__(self)
        print("Calling private member of base class: ", self.__b)
        print(self.__c)

obj1 = Base()
print(obj1.a)
# The following line will raise an error because __b is a private member
# print(obj1.__b)