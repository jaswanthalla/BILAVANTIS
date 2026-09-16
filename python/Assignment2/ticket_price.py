# 7. Write a program that calculates a movie ticket price based on age and show timing.

# Rules:

# | Condition       | Ticket Price |
# |  | --: |
# | Age below 5     |         Free |
# | Age 5–12        |         ₹100 |
# | Age 13–59       |         ₹200 |
# | Age 60 or above |         ₹120 |

# Additionally:

# * If the show is before 5 PM, give a ₹30 discount.
# * If the person is below 5 years, the ticket remains free.
# * Display the final ticket price.

# Example:
# Enter age: 25
# Enter show time: 3
# Final ticket price: ₹170

age = int(input("enter your age:"))
time = int(input("enter the show time:"))

if age < 5:
    print(f"final ticket price {'free'}")
else:
    if time < 5:
        if 5 <= age <= 12:
            ticket_price = 100 - 30

        elif 13 <= age <= 59:
            ticket_price = 200 - 30

        else:
            ticket_price = 120 - 30

    else:
        if 5 <= age <= 12:
            ticket_price = 100

        elif 13 <= age <= 59:
            ticket_price = 200

        else:
            ticket_price = 120
    print(f"final ticket price {ticket_price}")
