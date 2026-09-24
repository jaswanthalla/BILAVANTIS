from abc import ABC, abstractmethod


# Base class: Person
class Person(ABC):
    school_name = "Madhu Vidyalayam"  # shared by everyone

    def __init__(self, name, age, id_number):
        self.name = name  # public
        self._id_number = id_number  # protected
        self.__age = age  # private

    # Encapsulation: age is private, so we use getter/setter
    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        if new_age > 0:
            self.__age = new_age
        else:
            print("Age must be positive!")

    # Abstract method: subclasses must explain their role
    @abstractmethod
    def role_description(self):
        pass

    # Normal instance method
    def display_details(self):
        print(
            f"Name: {self.name}, ID: {self._id_number}, Age: {self.__age}, School: {Person.school_name}"
        )

    #Class method: changes school name for everyone
    @classmethod
    def change_school_name(cls, new_name):
        cls.school_name = new_name

    #Static method: checks if an ID looks valid
    @staticmethod
    def is_valid_id(id_number):
        return id_number.startswith("SCH") and len(id_number) == 6


#Child class: Teacher
class Teacher(Person):
    def __init__(self, name, age, id_number, subject, classes_handled):
        super().__init__(name, age, id_number)
        self.subject = subject
        self._classes_handled = classes_handled

    def role_description(self):
        print(f"I teach {self.subject}")

    def display_details(self):
        super().display_details()
        print(f"Subject: {self.subject}, Classes handled: {self._classes_handled}")

    def calculate_bonus(self):
        bonus = self._classes_handled * 1000
        print(f"Teacher bonus: {bonus}")


# Child class: Student
class Student(Person):
    def __init__(self, name, age, id_number, grade, projects_completed):
        super().__init__(name, age, id_number)
        self.grade = grade
        self._projects_completed = projects_completed

    def role_description(self):
        print(f"I am a student in grade {self.grade}")

    def display_details(self):
        super().display_details()
        print(f"Grade: {self.grade}, Projects completed: {self._projects_completed}")

    def calculate_bonus(self):
        bonus = self._projects_completed * 500
        print(f"Student bonus: {bonus}")


# -------------------------
# Main Program
# -------------------------
if __name__ == "__main__":
    # Create some teachers and students
    teacher1 = Teacher("Alice", 35, "SCH001", "Math", 5)
    teacher2 = Teacher("Charlie", 40, "SCH002", "Science", 4)
    student1 = Student("Bob", 15, "SCH003", "10th", 3)
    student2 = Student("Daisy", 14, "SCH004", "9th", 2)
    student3 = Student("Ethan", 16, "SCH005", "11th", 4)

    # Show details
    teacher1.display_details()
    student1.display_details()

    # Show bonuses
    teacher1.calculate_bonus()
    student1.calculate_bonus()

    # Encapsulation demo
    print("Bob's age (via getter):", student1.get_age())
    student1.set_age(16)  # valid
    student1.set_age(-5)  # invalid

    # Static method demo
    print("Is SCH123 a valid ID?", Person.is_valid_id("SCH123"))

    # Class method demo
    Person.change_school_name("Sunrise Academy")
    teacher1.display_details()  # notice school name changed

    # Polymorphism demo
    people = [teacher1, teacher2, student1, student2, student3]
    for person in people:
        person.role_description()  # same call, different output
        person.display_details()
        person.calculate_bonus()
        print("---")
