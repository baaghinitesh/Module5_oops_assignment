# 10. Implement encapsulation in a `BankAccount class with private attributes for `balance` and `account_number". Include methods for deposit, withdrawal, and balance inquiry.

class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.__account_number = account_number  # Private attribute
        self.__balance = initial_balance        # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: ₹{amount:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: ₹{amount:.2f}")
        else:
            print("Withdrawal amount must be positive and less than or equal to the current balance.")
        print(f"Acount balance : {self.__balance:.2f}")

    def get_balance(self):
        return self.__balance

    def get_account_number(self):
        return self.__account_number


if __name__ == "__main__":
    account = BankAccount("123456789", 1000)

    print(f"Account Number: {account.get_account_number()}")
    print(f"Initial Balance: ₹{account.get_balance():.2f}")

    account.deposit(200)
    print(f"Balance after deposit: ₹{account.get_balance():.2f}")

    account.withdraw(150)
    print(f"Balance after withdrawal: ₹{account.get_balance():.2f}")

    account.withdraw(1200)  
