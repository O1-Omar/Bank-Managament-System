# Bank Management System
This is a Bank Management System built using Python's Tkinter library, providing a graphical interface to manage basic banking operations. 
The system supports three types of users: Customer, Teller, and Manager, each with specific roles and permissions.

- Features :
  * General Features:
    + Simple and user-friendly GUI.
    + Account creation, login, and management for different types of users.
  * Customer Features:
    + View account details.
    + Deposit and withdraw money.
    + Check account balance.
  * Teller Features:
    + Create new customer accounts.
    +  Perform deposits, withdrawals, and transfers on behalf of customers.
    + View and manage customer accounts.
  * Manager Features:
    + View and manage teller and customer accounts.
    + Generate reports for account activity.
    + Add or remove tellers and monitor teller activities.
- Technologies Used :
  * Python: The programming language used for logic and functionality.
  * Tkinter: GUI library for building the user interface.
- Requirements :
  * Python 3.x
  * Tkinter (usually included in standard Python installation)

# Contribution
  Contributions are welcome! If you find any issues or would like to add new features, feel free to submit a pull request.
# User Roles and Permissions
1. Customer
  The Customer role allows users to perform basic banking functions. Customers have access to the following features:
    - Deposit funds: Add money to their bank account.
    - Withdraw funds: Remove money from their bank account.
    - View transaction log: Access a record of past transactions, including deposits and withdrawals.
2. Teller
  The Teller role includes all permissions granted to a customer, along with additional management capabilities:
  - Add a customer: Register new customers into the system.
  - Close a customer account: Terminate an existing customer account.
  - View all customers: Display a list of all registered customers.
  - Edit customer information: Modify customer details.
  - Manage customer loans: Add and manage loan information for customers.
  - Edit teller information: Modify information related to fellow tellers.
    
3. Manager (Teller)
  The Manager role has full administrative privileges, including all teller operations and additional managerial functions:
  - Edit teller details: Modify the details of any teller in the system.
  - Add a teller: Register a new teller.
  - Deposit/withdraw in teller accounts: Perform transactions on teller accounts.
  - Full administrative access: Can manage all teller and customer data.

# Default Bank Accounts
Upon installation, the system comes with pre-configured accounts for testing purposes. Below are the default account details:

* Manager:
  Name: Omar Ibrahim
  Password: 6060
  Account Number: 1020
* Tellers:
  - Teller 1:
    Name: Mohammed
    Password: mohammed_123
    Account Number: 1010
  - Teller 2:
    Name: Ahmed
    Password: ahmed_123
    Account Number: 1030
* Customers:
  - Customer 1:
    Name: Ahmed Ibrahim
    Password: 14015016
    Account Number: 1219
  - Customer 2:
    Name: Abdo Ibrahim
    Password: 522522
    Account Number: 1211

