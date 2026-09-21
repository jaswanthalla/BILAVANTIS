# 15. Create the following functions:
# calculate_total(m1, m2, m3)
# calculate_average(total)
# calculate_grade(average)
# check_result(m1, m2, m3)
# display_result(name, m1, m2, m3)
# Rules:
# A student passes only if:
# * Each subject mark is at least `35`.
# * Overall average is at least `40`.
# Grade:
# 90+     → A
# 80–89   → B
# 70–79   → C
# 60–69   → D
# 40–59   → E
# Below 40 → F
# `display_result()` should call the other functions and produce:
# Student Name: Rahul
# Total: 255
# Average: 85
# Result: PASS
# Grade: B


def calculate_total(m1, m2, m3):
    return m1 + m2 + m3


def calculate_average(total):
    return total / 3


def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    elif average >= 40:
        return "E"
    else:
        return "F"


def check_result(m1, m2, m3):
    total = calculate_total(m1, m2, m3)
    average = calculate_average(total)
    if m1 >= 35 and m2 >= 35 and m3 >= 35 and average >= 40:
        return "PASS"
    else:
        return "FAIL"


def display_result(name, m1, m2, m3):
    total = calculate_total(m1, m2, m3)
    average = calculate_average(total)
    grade = calculate_grade(average)
    result = check_result(m1, m2, m3)
    print(f"Student Name: {name}")
    print(f"Total: {total}")
    print(f"Average: {average}")
    print(f"Result: {result}")
    print(f"Grade: {grade}")


display_result("Rahul", 85, 90, 80)
