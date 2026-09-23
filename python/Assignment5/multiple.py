class Teacher:
    def teach(self):
        print("this is teacher")


class Mentor:
    def guide(self):
        print("this is mentor")


class Tutor(Teacher, Mentor):
    def display(self):
        self.teach()
        self.guide()


d = Tutor()
d.display()
