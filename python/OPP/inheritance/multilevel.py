class Animal:
    def eat(self):
        print("animal")


class Mammal(Animal):
    def walk(self):
        print("mammal")
        self.eat()


class Dog(Mammal):
    def bark(self):
        print("dog")
        self.walk()


d = Dog()
d.bark()
