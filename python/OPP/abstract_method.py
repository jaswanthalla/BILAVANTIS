from abc import ABC, abstractmethod


class Calculation(ABC):  # Abstract class
    @abstractmethod
    def compute(self, a, b):
        pass


class Addition(Calculation):
    def compute(self, a, b):
        return a + b


class Subtraction(Calculation):
    def compute(self, a, b):
        return a - b


class Multiplication(Calculation):
    def compute(self, a, b):
        return a * b


add_obj = Addition()
sub_obj = Subtraction()
mul_obj = Multiplication()

print("Addition:", add_obj.compute(10, 5))
print("Subtraction:", sub_obj.compute(10, 5))
print("Multiplication:", mul_obj.compute(10, 5))
