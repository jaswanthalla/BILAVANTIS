# 3. Create a function: calculate_grade(marks)
# Rules:
# 90–100 → A
# 80–89  → B
# 70–79  → C
# 60–69  → D
# Below 60 → F
# If the marks are less than `0` or greater than `100`, return:
# Invalid Marks


def calculate_grade(marks):
    if marks < 0 or marks > 100:
        return "Invalid marks"
    else:
        if 100 >= marks >= 90:
            return "A"
        elif 89 >= marks >= 80:
            return "B"
        elif 79 >= marks >= 70:
            return "c"
        elif 69 >= marks >= 60:
            return "D"
        else:
            return "F"


print(calculate_grade(10))
