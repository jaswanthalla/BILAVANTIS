class bike:
    def __init__(self, name, model):
        self.name = name
        self.model = model


# we can create multiple objects for a class
obj = bike("RE", "Himalayan 411")
print(obj.name)
print(obj.model)
