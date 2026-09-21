# Problem Statement:
# Define a BankAccount class with attributes account_number and balance. Implement methods deposit(amount) and withdraw(amount) to update the balance. Create objects for different accounts and perform transactions.


class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited amount {amount},Updated balance {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Insufficient funds!")


acc1 = BankAccount(1234, 20000)
acc1.deposit(500)
acc1.withdraw(15000)
