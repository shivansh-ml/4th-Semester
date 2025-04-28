class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}, New Balance: {self.balance}")
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: {amount}, New Balance: {self.balance}")
        else:
            print("Insufficient balance")
    
    def get_balance(self):
        return self.balance

class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance=0, interest_rate=0.02):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate
    
    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest Added: {interest}, New Balance: {self.balance}")

savings = SavingsAccount("SA12345", 1000, 0.05)
savings.deposit(500)
savings.add_interest()
savings.withdraw(200)
savings.get_balance()
