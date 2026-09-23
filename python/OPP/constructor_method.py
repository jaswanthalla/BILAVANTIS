class Car:
    def __init__(self, brand, model):  # constructor
        self.brand = brand
        self.model = model


c = Car("Toyota", "hilex")
print(c.brand, c.model)
