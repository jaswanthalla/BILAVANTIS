class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Employee(Person):
    def __init__(self, name, age, emp_id, basic_salary):
        super().__init__(name, age)
        self.emp_id = emp_id
        self.basic_salary = basic_salary

    def calculate_salary(self):
        return self.basic_salary


class Manager(Employee):
    def __init__(self, name, age, emp_id, basic_salary, bonus, team_size):
        super().__init__(name, age, emp_id, basic_salary)
        self.bonus = bonus
        self.team_size = team_size

    def calculate_salary(self):
        return self.basic_salary + self.bonus


emp = Employee("AJ", 28, "101", 40000)
mgr = Manager("Rajesh", 35, "201", 60000, 15000, 5)

print(f"Employee: {emp.name}, Salary: {emp.calculate_salary()}")
print(f"Manager: {mgr.name}, Salary: {mgr.calculate_salary()}")

f= open("Assignment_questions.txt")
print(f.read())