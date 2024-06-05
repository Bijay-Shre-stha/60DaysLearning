#Looping through a list of objects and calling the same method on each object
class Car:
    def __init__ (self, brand, model):
        self.brand = brand
        self.model = model
    
    def start(self):
        print(f"{self.brand} {self.model} is starting")
    
class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def start(self):
        print(f"{self.brand} {self.model} is starting")

c1 = Car("Toyota", "Corolla")
b1 = Boat("Yamaha", "2000")
for x in (c1, b1):
    x.start()