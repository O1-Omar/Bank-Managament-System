from datetime import datetime
class Teller:
    def __init__(self, teller_id : int, teller_name : str, password : str, address : str, phone_number : int, account_number : int) -> None:
        self.account_id = teller_id
        self.account_name = teller_name
        self.password = password
        self.address = address
        self.phone_number= phone_number
        self.account_number = account_number
        self.date_created = datetime.now().strftime("%a %b %Y")
        self.time_created = datetime.now().strftime("%I:%M:%S %p")
        self.Accounts = {}
        self.events = []

    def deposit(self, bank, amount):
        bank.deposit_teller(self.account_number, amount)

    def withdraw(self, bank, amount):
        bank.withdraw_teller(self.account_number, amount)
    
    def depositSaving(self, bank, amount):
        bank.deposit_saving_teller(self.account_number, amount)

    def withdrawSaving(self, bank, amount):
        bank.withdraw_saving_teller(self.account_number, amount)

    def checkingCustomer(self, bank_system, account_number):
        if account_number in bank_system.Customers:
            return True
        return False

    def openAccount(self, bank_system, account_number, account):
        bank_system.Customers[account_number].Accounts[account_number] = account

    def closeAccount(self, bank_system, account_number):
        del bank_system.Customers[account_number]

