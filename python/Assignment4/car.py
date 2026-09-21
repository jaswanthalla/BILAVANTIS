# 3. Car Class with Default Values
# Problem Statement:
# Build a Car class with attributes brand and model. Allow model to have a default value if not provided. Instantiate objects with and without specifying the model, then print their details.

# Problem: Allow model to have a default value if not provided


class Car:
    def __init__(self, brand, model="Unknown"):  # model defaults to "Unknown"
        self.brand = brand
        self.model = model

    def details(self):
        print(f"Car Brand: {self.brand}, Model: {self.model}")


# Creating objects
c1 = Car("Toyota", "Hilex")
c2 = Car("Tesla")

c1.details()
c2.details()
