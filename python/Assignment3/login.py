# 4. Create a function: login(username, password)
# The function should check whether:
# Username = "admin"
# Password = "python123"de
# If both are correct, return:
# Login Successful
# If the username is incorrect, return:
# Invalid Username
# If the username is correct but the password is incorrect, return:
# Invalid Password


def login(username, password):
    if username == "admin" and password == "python123":
        return "Login Successful"
    else:
        if username != "admin":
            return "Invalid username"
        else:
            return "Invalid password"


username = input("enter the username:")
password = input("enter the password:")
print(login(username, password))
