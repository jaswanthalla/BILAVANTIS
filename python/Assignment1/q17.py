# 17.Create a list containing marks of six students.
# Display:
# * First mark
# * Last mark
# * Highest mark
# * Lowest mark
# * Total marks
# * Number of students 

marks = [60, 70, 80, 90, 75, 85]

first_mark = marks[0]
print(first_mark)

last_mark = marks[-1]
print(last_mark)

highest_marks = max(marks)
print(highest_marks)

lowest_marks = min(marks)
print(lowest_marks)

total_marks = sum(marks)
print(total_marks)

students = len(marks)
print(students)
