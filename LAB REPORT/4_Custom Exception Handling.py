# Insufficient Funds Exception
class InsufficientFundsError(Exception):
    def __init__(self, message="Insufficient funds for this withdrawal."):
        self.message = message
        super().__init__(self.message)

# Bank Account Class
class BankAccount:
    def __init__(self, balance, min_balance):
        self.balance = balance
        self.min_balance = min_balance

    def withdraw(self, amount):
        if self.balance - amount < self.min_balance:
            raise InsufficientFundsError()
        self.balance -= amount
        return self.balance

# Testing the BankAccount and InsufficientFundsError
if __name__ == "__main__":
    account = BankAccount(1000, 100)
    
    try:
        print("Current Balance:", account.balance)
        account.withdraw(950)
    except InsufficientFundsError as e:
        print(e)

    try:
        account.withdraw(900)
    except InsufficientFundsError as e:
        print(e)
