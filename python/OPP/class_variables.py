class Variable:
    class_variable = "class_variable"

    def add(self, a, b):
        print(a + b)


o1 = Variable()
o1.add(2, 4)
print(o1.class_variable)
