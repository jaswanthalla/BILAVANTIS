class School:
    school_name = "Madhu Vidyalayam"

    @classmethod
    def show_school(cls):  # class method
        print("School Name:", cls.school_name)


School.show_school()
