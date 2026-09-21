# 12. Create: is_valid_date(day, month, year)
# Check whether the given date is valid.
# Consider:
# * Months with 30 days
# * Months with 31 days
# * February
# * Leap years
# Examples:
# 29/02/2024 → Valid
# 29/02/2023 → Invalid
# 31/04/2025 → Invalid
# 31/12/2025 → Valid
# **Challenge:** Do not use any date/time library.


def is_valid_date(day, month, year):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        days_in_month[1] = 29

    if month < 1 or month > 12:
        return False

    if day < 1 or day > days_in_month[month - 1]:
        return False

    return True


print(is_valid_date(29, 2, 2024))
