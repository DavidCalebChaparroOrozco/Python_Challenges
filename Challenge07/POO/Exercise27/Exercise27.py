"""
Define a parent class called Vehicle and two child classes called Car and Bike,
which inherit from the parent class Vehicle.
The parent class must have the following attributes and methods.

Vehicle (Parent class):
-Attributes (color, wheels)
-Methods ( __init__() and __str__ )

Car (Daughter Class of Vehicle) (In addition to the attributes and methods inherited from Vehicle):
-Attributes ( speed (km/hr) )
-Methods ( __init__() and __str__() )

Bicycle (Child Class of Vehicle) (In addition to Vehicle attributes and inherited methods):
-Attributes ( type (urban/mountain/etc )
-Methods ( __init__() and __str__() )
"""

class Vehicle():
    def __init__(self, color, wheels):
        self.color = color
        self.wheels = wheels

    def __str__(self):
        return 'Color: ' + self.color + ', Wheels: ' + str(self.wheels)

class Car(Vehicle):
    def __init__(self, color, wheels, speed):
        super().__init__(color, wheels)
        self.speed = speed

    def __str__(self):
        return super().__str__() + ', speed(km/hr): ' + str(self.speed)

class Bicycle(Vehicle):
    def __init__(self, color, wheels, type):
        super().__init__(color, wheels)
        self.type = type

    def __str__(self):
        return super().__str__() + ', Type:' + self.type

# Create an object of class Vehicle
vehicle1 = Vehicle('Red', 4)
print(vehicle1)

# Create an object the class daughter Car
car1 = Car('Blue', 4, 150)
print(car1)

# Create an object the class daughter Bicycle
Bicycle1 = Bicycle('White', 2, 'Urban')
print(Bicycle1)