class Base:
    def __init__(self):
        # Protected member
        self._a = 2

class Derived(Base):
    def __init__(self):
        # Calling constructor of Base class
        Base.__init__(self)
        print("Calling protected member of base class: ", self._a)

        # Modify the protected member
        self._a = 3
        print("Modified protected member of base class: ", self._a)

obj1 = Derived()
obj2 = Base()

print("Accessing protected member of obj1: ", obj1._a)
print("Accessing protected member of obj2: ", obj2._a)