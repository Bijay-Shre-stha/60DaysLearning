class Vehicle:
    def __init__ (self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print(f"{self.brand} {self.model} is moving")
    
class Car(Vehicle):
    pass

class Boat(Vehicle):
    def move(self):
        print(f"{self.brand} {self.model} is sailing")
    
class Plane(Vehicle):
    def move(self):
        print(f"{self.brand} {self.model} is flying")

c1 = Car("Toyota", "Corolla")
b1 = Boat("Yamaha", "2000")
p1 = Plane("Boeing", "747")
for x in (c1, b1, p1):
    print("Vehicle: ", x.__class__.__name__)
    print("Brand: " , x.brand)
    print("Model: ", x.model)
    x.move()