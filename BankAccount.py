# Import files :
from tkinter import messagebox
class Account:

    # Init the class
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    
    def deposit(self, amount):
        """
            Function to deposit money in account .
        """
        self.balance += amount

    def withdraw(self, amount):
        """
            Function to withdraw the moeny in account .
        """
        if self.balance >= amount:
            self.balance -= amount
        else:
            messagebox.showerror("Account Info", "Insufficient funds.")

    def get_balance(self):
        """
            Function to return the balance of the account .
        """
        return self.balance
