"""
car.py
Defines a Car class with attributes and methods to simulate driving a car
Kyle Ponte
kponte@stevens.edu
11/6/25
"""
class Car:
    def __init__(self, make, model, mileage=0):
        self.make = make
        self.model = model
        self.mileage = mileage

    def drive(self, miles):
        if miles > 0: # only add positive miles
            self.mileage += miles

    def __str__(self):
        return f"{self.make} {self.model} with {self.mileage} miles"

# Create objects and update attributes
car1 = Car("Toyota", "Corolla", 15000)
car2 = Car("Honda", "Civic")

car1.drive(500)
car2.drive(1200)

print(car1)
print(car2)