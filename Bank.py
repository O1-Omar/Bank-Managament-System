# import Files and Libraries :
from Teller import Teller
from savingAccount import SavingAccount
from checkingAccount import CheckingAccount
from Customer import Customer
from tkinter import messagebox

# Craete Bank Class :
class Bank:
    # Init the class :
    def __init__(self, bank_id : str, bank_name : str, bank_location : str) -> None:
        
        # Init the paramaters :
        self.bank_id = bank_id
        self.bank_name = bank_name
        self.bank_location = bank_location 
        
        self.Customers = {}    # Create the dictionary to sotre Customers .
        self.tellers = {}      # Craete dictionary yo sotre tellers .
        
        # Craete One Manager to Manage the Bank System
        self.managers = {
            1020 : Teller(10001, "Omar Ibrahim", "6060", "Egypt, Giza", "01061408612", 1020)
        }

        # Craete Accounts to Manager Account (saving, Chekcing):
        self.managers[1020].Accounts["checking"] = CheckingAccount(1020, 50000)
        self.managers[1020].Accounts["saving"] = SavingAccount(1020, 1000, 10)    
    
    def createTeller(self, teller_id : int, teller_name : str, password : str, address : str, phone_number : int, account_number : int):
        """
            Function to create teller from bank class .
        """
        # if the account is already exists raise error, else => Craete Teller Account:
        if account_number in self.Customers:
            messagebox.showerror("Account Info", "Account number already exists.")
        else:
            self.tellers[account_number] = Teller(teller_id, teller_name, password, address, phone_number, account_number)


    def create_customer(self, cusotmer_id : int, customer_name : str, password : str, address : str, phone_number : int, account_number : int):
        """
            Function to create customer from bank class .
        """
        # if the account is already exists raise error, else => Craete Teller Account:
        if account_number in self.Customers:
            messagebox.showwarning("Account Info", "Account number already exists.")
        else:
            self.Customers[account_number] = Customer(cusotmer_id, customer_name, password, address, phone_number, account_number)
    
    def create_teller_account(self, account_number, account_type, initial_balance, initial_rate = None):
        """
            Function to create teller --Bank Account-- (Saving, Checking) from bank class.
        """
        # if the teller has not account, craete it :
        if account_type not in self.tellers[account_number].Accounts:
            # Check the type of the bank account :
            if account_type == "saving":
                self.tellers[account_number].Accounts["saving"] = SavingAccount(account_number, initial_balance, initial_rate)
            elif account_type == "checking":
                self.tellers[account_number].Accounts["checking"] = CheckingAccount(account_number, initial_balance)
            else:
                # raise error if the user entered in valid data :
                messagebox.showerror("Account Info", "Invalid account type .")
        else :
            # raise error if the account has already acount Bank .
            messagebox.showerror("Account Info", f"Account already Has {account_type} Account .")

    def create_account(self, account_number, account_type, initial_balance, initial_rate = None):
        """
            Function to create Customer --Bank Account-- (Saving, Checking) from bank class.
        """
        # if the Customer has not account, craete it :
        if account_type not in self.Customers[account_number].Accounts :
            # Check the type of the bank account :
            if account_type == "saving" :
                self.Customers[account_number].Accounts["saving"] = SavingAccount(account_number, initial_balance, initial_rate)
            elif account_type == "checking":
                self.Customers[account_number].Accounts["checking"] = CheckingAccount(account_number, initial_balance)
            else:
                # raise error if the user entered in valid data :
                messagebox.showerror("Account Info", "Invalid account type .")
        else :
            # raise error if the account has already acount Bank .
            messagebox.showerror("Account Info", f"Account already Has {account_type} Account .")

    def deposit_teller(self, account_number, amount):
        """
            Function to deposit money in teller checking account .
        """
        # Check if the teller has checking account or not :
        if "checking" in self.tellers[account_number].Accounts:
            # Deposit Money :
            self.tellers[account_number].Accounts["checking"].deposit(amount)
        else:
            messagebox.showerror("Account Info", "Account number does not exist .")

    def withdraw_teller(self, account_number, amount):
        """
            Function to Withdraw money in teller checking account .
        """
        # Check if the teller has checking account or not :
        if "checking" in self.tellers[account_number].Accounts:
            # Withdraw Money :
            self.tellers[account_number].Accounts["checking"].withdraw(amount)
        else:
            messagebox.showerror("Account Info", "Account number does not exist .")

    def deposit_saving_teller(self, account_number, amount):
        """
            Function to deposit money in teller saving account .
        """
        # Check if the teller has checking account or not :
        if "saving" in self.tellers[account_number].Accounts:
            # Deposit Money :
            self.tellers[account_number].Accounts["saving"].deposit(amount)
        else:
            messagebox.showerror("Account Info", "Account number does not exist .")

    def withdraw_saving_teller(self, account_number, amount):
        """
            Function to withdraw money in teller saving account .
        """
        # Check if the teller has checking account or not :
        if "saving" in self.tellers[account_number].Accounts:
            # Withdraw Money :
            self.tellers[account_number].Accounts["saving"].withdraw(amount)
        else:
            messagebox.showerror("Account Info", "Account number does not exist .")

    def deposit(self, account_number, amount):
        """
            Function to Deposit money in teller checking account .
        """
        # Check if the customer has checking account or not : 
        if "checking" in self.Customers[account_number].Accounts:
            # deposit Money :  
            self.Customers[account_number].Accounts["checking"].deposit(amount)
        else:
            messagebox.showerror("Account Info", "Account number does not exist .")

    def withdraw(self, account_number, amount):
        """
            Function to Withdraw money in teller checking account .
        """
        # Check if the customer has checking account or not :
        if "checking" in self.Customers[account_number].Accounts:
            # Withdraw Money :
            self.Customers[account_number].Accounts["checking"].withdraw(amount)
        else:
            messagebox.showerror("Account Info", "Account number does not exist .")

    def depositSaving(self, account_number, amount):
        """
            Function to Deposit money in teller saving account .
        """
        # Check if the customer has checking account or not :
        if "saving" in self.Customers[account_number].Accounts:
            # Deposit Money :
            self.Customers[account_number].Accounts["saving"].deposit(amount)
        else:
            messagebox.showerror("Account Info", "Account number does not exist .")

    def withdrawSaving(self, account_number, amount):
        """
            Function to Withdraw money in customer saving account .
        """
        # Check if the cusomer has checking account or not :
        if "saving" in self.Customers[account_number].Accounts:
            # Withdraw Money :
            self.Customers[account_number].Accounts["saving"].withdraw(amount)
        else:
            messagebox.showerror("Account Info", "Account number does not exist .")

    def check_balance(self, account_number):
        """
            Function to check balance in customers .
        """
        if "checking" in self.Customers[account_number].Accounts:
            return self.Customers[account_number].Accounts["checking"].balance
        else:
            messagebox.showerror("Account Info", "Account number does not exist .")
        return 0
