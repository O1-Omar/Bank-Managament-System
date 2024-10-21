# Import File and library:
from BankAccount import Account

class SavingAccount(Account):
    # Init the class :
    def __init__(self, account_number, initial_balance, initial_rate) -> None:
        super().__init__(account_number, initial_balance)
        self.initial_rate = initial_rate
        
    
    def deposit(self, amount):
        """
            Function to Deposit Money .
        """
        super().deposit(amount)

    def withdraw(self, amount):
        """
            Function To Withdraw .
        """
        super().withdraw(amount)
    
    def addIntersetrate(self):
        """
            Function to add interest rate .
        """
        interest_value = self.initial_rate * self.balance
        self.deposit(interest_value)


    def getBalance(self):
        """
            Function to return balance .
        """
        return self.balance