# 7. Create: check_password(password)
# The function should check the password length and return:
# "Strong"
# "Medium"
# "Weak"
# Rules:
# * Length less than 6 → Weak
# * Length 6–9 → Medium
# * Length 10 or more → Strong
# **Bonus:** Also check whether the password contains at least one digit.


def check_password(password):
    length = len(password)
    has_digit = any(a.isdigit() for a in password)
    if length < 6:
        return f"The password is Weak and contains atleast one digit {has_digit}"
    elif 6 <= length <= 9:
        return f"The password is Medium and contains atleast one digit {has_digit}"
    else:
        if length >= 10:
            return f"The password is Strong and contains atleast one digit {has_digit}"


password = input("enter the password:")
print(check_password(password))
