# import the base class Account to inherite from it :
from BankAccount import Account

class CheckingAccount(Account):
    # init the class :
    def __init__(self, account_number, initial_balance) -> None:
        super().__init__(account_number, initial_balance)
    
    def deposit(self, amount):
        """
            Function to Deposit money .
        """
        super().deposit(amount)

    def withdraw(self, amount):
        """
            Function to Withdraw money .
        """
        super().withdraw(amount)
    
    def getBalance(self):
        """
            Get the Balance .
        """
        return self.balance