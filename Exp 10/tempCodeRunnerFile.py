class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance
    
    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited: {amount}")
    
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Insufficient balance")
    
    def check_balance(self):
        print(f"Balance: {self.__balance}")

account = BankAccount(1000)
account.deposit(500)
account.withdraw(200)
account.check_balance()