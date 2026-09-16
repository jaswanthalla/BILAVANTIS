# 3. Accept marks for a student and display the grade according to the following:

# | Marks    | Grade |
# | -- | -- |
# | 90–100   | A     |
# | 80–89    | B     |
# | 70–79    | C     |
# | 60–69    | D     |
# | Below 60 | F     |

# Also check whether the entered marks are valid. 
# For example, marks below `0` or above `100` should be treated as invalid.

marks = int(input("enter a number:"))

if marks < 0 or marks > 100:
    print("invalid marks")
else:
    print("valid marks")
    if marks >= 90 and marks <= 100:
        print("A")
    elif marks >= 80 and marks <= 89:
        print("B")
    elif marks >= 70 and marks <= 79:
        print("C")
    elif marks >= 60 and marks <= 69:
        print("D")
    else:
        print("F")


