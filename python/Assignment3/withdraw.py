# 13. Create: withdraw(balance, amount)
# Rules:
# * Amount must be greater than `0`.
# * Amount must be a multiple of `100`.
# * Minimum balance after withdrawal must be ₹500.
# * Withdrawal cannot exceed the available balance.
# Return an appropriate message for each situation.
# Example:
# Balance: ₹5000
# Withdrawal: ₹2000
# Output:
# Withdrawal successful
# Remaining balance: ₹3000


def withdraw(balance, amount):
    if amount <= 0:
        return "Invalid amount"
    if amount % 100 != 0:
        return "Amount must be multiple of 100"
    if balance - amount < 500:
        return "Minimum balance of ₹500 must be maintained"
    if amount > balance:
        return "Insufficient balance"
    balance -= amount
    return f"Withdrawal successful\nRemaining balance: ₹{balance}"


print(withdraw(5000, 2000))
