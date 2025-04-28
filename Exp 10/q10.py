
class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        if isinstance(account, _BankAccount):
            self.accounts.append(account)
        else:
            raise ValueError("Only BankAccount instances can be added")

    def remove_account(self, account):
        if account in self.accounts:
            self.accounts.remove(account)
        else:
            raise ValueError("Account not found in bank")

    def total_balance(self):
        return sum(acc._BankAccount__balance for acc in self.accounts)

class _BankAccount:
    def __init__(self, balance=0):
        self._BankAccount__balance = balance

account = _BankAccount(1000)
bank = Bank()
bank.add_account(account)
print("Total Bank Balance:", bank.total_balance())