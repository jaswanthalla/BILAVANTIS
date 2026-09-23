# 1. Banking System — Inheritance + Method Overriding

# Create a Banking System with:

# BankAccount as the parent class with:

# account_number
# holder_name
# balance
# deposit()
# withdraw()

# Create child classes:
# SavingsAccount
# CurrentAccount

# Each account should have different withdrawal rules.
# Override the withdraw() method in child classes.
# Create multiple account objects and perform transactions.


# class BankAccount:
#     def __init__(self, account_number, holder_name, balance):
#         self.account_number = account_number
#         self.holder_name = holder_name
#         self.balance = balance

#     def deposit(self, deposited_amount):
#         if deposited_amount > 0:
#             self.balance += deposited_amount
#             print(f"updated amount:{self.balance}")
#         else:
#             print(f"No Deposits :{self.balance}")

#     def withdraw(self, withdraw_amount):
#         if withdraw_amount <= self.balance:
#             self.balance -= withdraw_amount
#             print(f"Remaining balance {self.balance}")
#         else:
#             print("Insufficient funds")


# class SavingsAccount(BankAccount):
#     def withdraw(self, withdraw_amount):
#         return super().withdraw(withdraw_amount)


# class CurrentAccount(BankAccount):
#     def withdraw(self, withdraw_amount):
#         return super().withdraw(withdraw_amount)


# bank = SavingsAccount(123, "2", 30000)
# bank.withdraw(20)
# bank.deposit(3000)


class BankAccount:
    def __init__(self, account_number, holder_name, balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, deposited_amount):
        if deposited_amount > 0:
            self.balance += deposited_amount
            print(
                f"{self.holder_name} deposited {deposited_amount}. Updated balance: {self.balance}"
            )
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, withdraw_amount):
        if withdraw_amount <= self.balance:
            self.balance -= withdraw_amount
            print(
                f"{self.holder_name} withdrew {withdraw_amount}. Remaining balance: {self.balance}"
            )
        else:
            print("Insufficient funds.")


class SavingsAccount(BankAccount):
    def withdraw(self, withdraw_amount):
        if withdraw_amount > 10000:
            print(
                f"{self.holder_name}: Cannot withdraw more than 10,000 in one transaction!"
            )
        elif withdraw_amount <= self.balance:
            self.balance -= withdraw_amount
            print(
                f"{self.holder_name} withdrew {withdraw_amount}. Remaining balance: {self.balance}"
            )
        else:
            print("Insufficient funds.")


class CurrentAccount(BankAccount):
    def withdraw(self, withdraw_amount):
        total_deduction = withdraw_amount
        if total_deduction <= self.balance:
            self.balance -= total_deduction
            print(
                f"{self.holder_name} withdrew {withdraw_amount} . Remaining balance: {self.balance}"
            )
        else:
            print("Insufficient funds for withdrawal.")


s1 = SavingsAccount(101, "Jashwanth", 20000)
c1 = CurrentAccount(102, "Anu", 15000)

s1.withdraw(12000)
s1.withdraw(8000)

c1.withdraw(5000)
c1.withdraw(14000)
