# import the libraries and files :
from datetime import datetime
from Loan import Loan

class Customer:
    # Init the Calss :
    def __init__(self, cusotmer_id : int, cusotmer_name : str, password : str, address : str, phone_number : int, account_number : int) -> None:
        self.account_id = cusotmer_id
        self.account_name = cusotmer_name
        self.password = password
        self.address = address
        self.phone_number= phone_number
        self.account_number = account_number
        # Set the created date of account : 
        self.date_created = datetime.now().strftime("%a %b %Y")
        # Set the created Time of account :
        self.time_created = datetime.now().strftime("%I:%M:%S %p")
        # dictionary to sotre accounts of customer [Saving , account]
        """
            How data Stored in Accounts Dictionary ?
            {
                "account_number" : Object() =>> can may be {SavingAccount, Checking Account}
            }

            Ex : 
                {   
                    "1145" : SavingAccount()
                }

            Explanation :
                "1145" == > the Account Number os Customer .
                SavingAccount ==> the object .

        """
        self.Accounts = {}

        # Craete the events list to show in transction data :
        self.events = []
        
        # Craete loans list to store the loans of the customer :
        self.loans = []
    
    def applayForLoan(self, loan_type : str, amount : int):
        """
            Function To applay loan .
        """
        self.loans.append(Loan(self.account_number, loan_type,  amount))

    def deposit(self, bank, amount):
        """
            Function To deposit money .
        """
        bank.deposit(self.account_number, amount)

    def withdraw(self, bank, amount):
        """
            Function To withdraw money .
        """
        bank.withdraw(self.account_number, amount)

    def depositSaving(self, bank, amount):
        """
            Function To deposit money in saving account.
        """
        bank.depositSaving(self.account_number, amount)

    def withdrawSaving(self, bank, amount):
        """
            Function To withdraw money in saving account.
        """
        bank.withdrawSaving(self.account_number, amount)

    def check_balance(self, bank):
        """
            Function To return the value of check balance .
        """
        return bank.check_balance(self.account_number)