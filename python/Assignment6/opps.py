from abc import abstractmethod


class Employee:
    company_name = "Bilvantis"

    def __init__(self, name, employee_id, salary):
        self.name = name
        self._employee_id = employee_id
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    @abstractmethod
    def calculate_bonus(self):
        if self.__salary >= 20000:
            self.__salary += 2000
            print(f"After bonus salary is {self.__salary}")
        else:
            print("Not eligible for bonus")

    def display_details(self):
        print(
            f"Name {self.name},Employee_id {self._employee_id},salary {self.__salary},company_name {Employee.company_name}"
        )

    @classmethod
    def change_company_name(cls, new_company_name):
        cls.company_name = new_company_name

    @staticmethod
    def is_valid_employee_id(employee_id):
        if employee_id.startswith("BTIN") and len(employee_id) == 7:
            return True
        else:
            return False


class Manager(Employee):
    def __init__(self, name, _employee_id, __salary, department, team_size):
        super().__init__(name, _employee_id, __salary)
        self.department = department
        self._team_size = team_size

    def calculate_bonus(self):
        salary = self.get_salary()
        if salary >= 20000:
            salary += 2000
            print(f"After bonus salary is {salary}")
        else:
            print("Not eligible for bonus")

    def display_details(self):
        print(
            f"Name {self.name},Employee_id {self._employee_id},salary {self.get_salary()},Department {self.department},Team_size {self._team_size},company_name {Employee.company_name}"
        )


class Developer(Employee):
    def __int__(
        self, name, employee_id, salary, programming_language, projects_completed
    ):
        super().__init__(name, employee_id, salary)
        self.programming_language = programming_language
        self._projects_completed = projects_completed

    def calculate_bonus(self):
        if self.__salary >= 20000:
            self.__salary += 2000
            print(f"After bonus salary is {self.__salary}")
        else:
            print("Not eligible for bonus")

    def display_details(self):
        print(
            f"Name {self.name},Employee_id {self._employee_id},salary {self.get_salary()},Programming_language {self.programming_language},Projects_completed {self._projects_completed},company_name {Employee.company_name}"
        )


obj = Employee("AJ", "BTIN009", 20000)
obj.display_details()
obj.calculate_bonus()
print(obj.name)
obj.change_company_name("Interactly")
obj.display_details()
print(obj.is_valid_employee_id("BTIN009"))


obj1 = Manager("Rajesh", "EMPI011", 50000, "CDE", 5)
obj1.display_details()
obj1.calculate_bonus()
