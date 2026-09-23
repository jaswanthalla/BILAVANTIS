# 4. Car Management System

# Design a Car parent class with appropriate variables and methods representing real-world car functionality.

# Requirements:

# Define suitable instance variables using self.
# Create multiple methods inside the Car class.
# Create appropriate child classes that inherit from the Car class.
# Use super() wherever required.
# Override methods in the child classes where appropriate.
# Create objects for the child classes.
# Execute all relevant parent and child methods.
# Display the output for each method execution.
# Clearly demonstrate how inheritance and method overriding work in your implementation.


class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self):
        print(self.brand, self.model, "is starting")

    def drive(self):
        print(self.brand, self.model, "is driving")

    def stop(self):
        print(self.brand, self.model, "has stopped")


class ElectricCar(Car):
    def __init__(self, brand, model, battery):
        super().__init__(brand, model)
        self.battery = battery

    def drive(self):
        print(self.brand, self.model, "is driving silently with battery:", self.battery)


class SportsCar(Car):
    def __init__(self, brand, model, speed):
        super().__init__(brand, model)
        self.speed = speed

    def drive(self):
        print(self.brand, self.model, "is driving fast at speed:", self.speed)


ecar = ElectricCar("Tesla", "Model 3", "75 kWh")
scar = SportsCar("Ferrari", "F8", "340 km/h")

ecar.start()
ecar.drive()
ecar.stop()

print("-----")

scar.start()
scar.drive()
scar.stop()
