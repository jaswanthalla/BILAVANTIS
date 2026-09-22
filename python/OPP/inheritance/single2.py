class Vehicle:
    def drive(self):
        print("The vehicle is moving")


class Car(Vehicle):
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type

    def drive(self):
        print(f"The car is moving using {self.fuel_type}")


a = Vehicle()
a.drive()

b = Car("petrol")
a.drive()
b.drive()
