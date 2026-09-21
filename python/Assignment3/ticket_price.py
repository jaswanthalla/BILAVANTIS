# 9. Create: ticket_price(age, show_time)
# Rules:
# Age below 5       → Free
# Age 5–12          → ₹100
# Age 13–59         → ₹200
# Age 60 or above   → ₹120
# Additional rule:
# If the show is before `5 PM`, give a ₹30 discount.
# The discount should **not** be applied to free tickets.
# Example:
# ticket_price(25, 3)
# Output:
# 170


def ticket_price(age, show_time):
    if age < 5:
        return f"final ticket price {'free'}"
    else:
        if show_time < 5:
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
        return f"final ticket price {ticket_price}"


a = ticket_price(25, 3)
print(a)
