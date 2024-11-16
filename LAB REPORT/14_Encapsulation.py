# BankAccount Class

class BankAccount:
    def __init__(self):
        self.__balance = 0  # Private variable for account balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: ${amount:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: ${amount:.2f}")
        else:
            print("Withdrawal amount exceeds current balance or is invalid.")

    def check_balance(self):
        return f"Current Balance: ${self.__balance:.2f}"


# Example usage
account = BankAccount()
account.deposit(100)
account.withdraw(150)  # Attempt to withdraw more than the balance
print(account.check_balance())
