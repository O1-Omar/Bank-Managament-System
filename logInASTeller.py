# import Files and files :
from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime


class LogInAsTellerPage:
    # Init the class :
    def __init__(self, frame: Frame, logInPage, account_login_type : str, bank : object, account: object) -> None:
        self.frame = frame
        self.account = account
        self.bank = bank
        self.log_in_func = logInPage
        self.account_login_type = account_login_type

    def createWidgets(self):
        """
            create widgets and call it with teller log in .
        """
        # create the customer function :
        self.createBasicInformation()

        # create the basic (deposit, withdraw, transaction log, logout) buttons :
        self.createButtons()

    def createWidgetsAsManager(self):
        """
            Function to create widgets and call it with manager log in . 
        """
        # create the customer function :
        self.createBasicInformation()
        
        # create the basic (deposit, withdraw, transaction log, logout) buttons :
        self.createButtons()

        # create addtional buttons with manager log in :
        self.craeteButtonsAsManager()

    def craeteButtonsAsManager(self):
        """
            Function to create buttons in manager page .
        """

        # Create frame to put the teller managament buttons in it:
        self.frame_border = Frame(self.frame, highlightthickness=2, highlightbackground="grey", borderwidth=5, width=100, height=100, bg="white")
        
        # Create label :
        self.name_of_frame = Label(self.frame, text="Teller\nManagment:",font=("Arail", 10, "bold"), bg="white") 
        
        # Create button to show tellers:
        self.show_all_tellers_button = Button(self.frame_border, width=13, text="Show All Tellers", command = self.showAllTellers, fg="white", font=("Arial", 12, "bold"), background="green")
        self.show_all_tellers_button.grid(row=0, column=0, padx=2, pady=2)
        
        # Create Button to add teller and gird it:
        self.add_tellers_button = Button(self.frame_border, width=13, text="Add Teller", command = self.addTellerAcount, fg="white", font=("Arial", 12, "bold"), background="green")
        self.add_tellers_button.grid(row=0, column=1, padx=2, pady=2)

        # Create Button to edit teller and gird it:
        self.edit_tellers_button = Button(self.frame_border, width=13, text="Edit Teller", command = lambda : [self.editAccount("Teller")], fg="white", font=("Arial", 12, "bold"), background="green")
        self.edit_tellers_button.grid(row=0, column=2, padx=2, pady=2)

        # Create Button to deposit money of teller and gird it:
        self.deposit_tellers_button = Button(self.frame_border, width=13, text="Deposit Teller", command = lambda: [self.depositButton(self.bank.tellers)], fg="white", font=("Arial", 12, "bold"), background="blue")
        self.deposit_tellers_button.grid(row=0, column=3, padx=2, pady=2)

        # Create Button to with draw money of teller and gird it:
        self.withdraw_tellers_button = Button(self.frame_border, width=13, text="Withdraw Teller", command = lambda: [self.withdrawButton(self.bank.tellers)], fg="white", font=("Arial", 12, "bold"), background="blue")
        self.withdraw_tellers_button.grid(row=0, column=4, padx=2, pady=2)


        # make the veiw transaction button disabled in manager :
        self.veiw_transaction_button.config(state=DISABLED)
        
        # placing the sub frame and its name : 
        self.name_of_frame.place(x=5, y=550)
        self.frame_border.place(x=115, y=545)

    def createButtons(self):
        
        self.logout_button = Button(self.frame, width=20, text="Show All Customers", command = self.showAllCustomers, fg="white", font=("Arial", 12, "bold"), background="grey64")
        self.logout_button.place(x=10, y=100)

        self.withdraw_button = Button(self.frame, width=20, text="Add Account", command=self.addAccount, fg="white", font=("Arial", 12, "bold"), background="grey64")
        self.withdraw_button.place(x=10, y=150)
        
        self.withdraw_button = Button(self.frame, width=20, text="Edit Account", command=lambda : [self.editAccount("Customer")], fg="white", font=("Arial", 12, "bold"), background="grey64")
        self.withdraw_button.place(x=10, y=200)

        self.deposite_button = Button(self.frame, width=20, text="Close Account", command=self.closeAccount, fg="white", font=("Arial", 12, "bold"), background="grey64")
        self.deposite_button.place(x=10, y=250)


        self.deposite_button = Button(self.frame, width=20, text="Deposite", fg="white", font=("Arial", 12, "bold"), background="grey64", command = lambda: [self.depositButton(self.bank.Customers)])
        self.deposite_button.place(x=10, y=300)

        self.withdraw_button = Button(self.frame, width=20, text="Withdraw", fg="white", font=("Arial", 12, "bold"), background="grey64", command = lambda: [self.withdrawButton(self.bank.Customers)])
        self.withdraw_button.place(x=10, y=350)

        self.withdraw_button = Button(self.frame, width=20, text="Add Loan", command=self.addLoan, fg="white", font=("Arial", 12, "bold"), background="grey64")
        self.withdraw_button.place(x=10, y=400)
        
        self.veiw_transaction_button = Button(self.frame, width=20, text="Veiw Transaction Log", command=self.transactionButton, fg="white",font=("Arial", 12, "bold"), background="grey64")
        self.veiw_transaction_button.place(x=10, y=450)

        self.logout_button = Button(self.frame, width=20, text="Logout", command = self.logout, fg="white", font=("Arial", 12, "bold"), background="red2")
        self.logout_button.place(x=10, y=500)


    def addTellerAcount(self):
        """
            Function to create the widgets that apper when you press on  add teller .
        """
        # craete sub window :
        self.add_teller_page = Toplevel(self.frame)

        # set title of window :
        self.add_teller_page.title("Add Teller")

        # set size of window :
        self.add_teller_page.geometry("470x330")

        # set icon of the page ;
        self.add_teller_page.iconbitmap("images/bank.ico")

        # craete flags :
        self.account_type_checking_teller = True
        self.is_saving_taller_account = True
        
        # Create Lable info of  page :
        self.teller_page_label = Label(self.add_teller_page, text="Add Teller", font=("Arail", 15, "bold"))
        
        # Create teller id field :
        self.teller_id_label = Label(self.add_teller_page, text="Id : ", font=("Arail", 10, "bold"))
        self.teller_id_entry = Entry(self.add_teller_page, width=40)

        # Create teller name field :
        self.teller_name_label = Label(self.add_teller_page, text="Name : ", font=("Arail", 10, "bold"))
        self.teller_name_entry = Entry(self.add_teller_page, width=40)

        # Create teller password field :
        self.teller_password_label = Label(self.add_teller_page, text="Password : ", font=("Arail", 10, "bold"))
        self.teller_password_entry = Entry(self.add_teller_page, width=40)

        # Create teller address field :
        self.teller_address_label = Label(self.add_teller_page, text="Address : ", font=("Arail", 10, "bold"))
        self.teller_address_entry = Entry(self.add_teller_page, width=40)

        # Create teller phone number :
        self.teller_phone_number_label = Label(self.add_teller_page, text="Phone number :", font=("Arail", 10, "bold"))
        self.teller_phone_number_entry = Entry(self.add_teller_page, width=40)

        # Create teller account number :
        self.teller_account_number_label = Label(self.add_teller_page, text="Account Number :", font=("Arail", 10, "bold"))
        self.teller_account_number_entry = Entry(self.add_teller_page, width=40)

        # Create the init balance field:
        self.teller_init_balance_label = Label(self.add_teller_page, text="Balance :", font=("Arail", 10, "bold"))
        self.teller_init_balance_entry = Entry(self.add_teller_page, width=40)

        # Create the account type field :
        self.teller_account_type_label = Label(self.add_teller_page, text="Account Type (default checking):", font=("Arail", 10, "bold"))
        self.teller_account_type_button = Checkbutton(self.add_teller_page, text="Saving", command=self.createEnteryForSavingTeller)

        # Create the interset rate field :
        self.teller_interset_rate_label = Label(self.add_teller_page, text="Interset Rate :", font=("Arail", 10, "bold"))
        self.teller_interset_rate_entry = Entry(self.add_teller_page, width=40)

        # Create the submit add button:
        self.submit_add_teller_button = Button(self.add_teller_page, text="Submit Adding", bg="green", fg="white", font=("Arial", 10, "bold"), command = lambda : [self.addTeller(), self.add_teller_page.destroy()])

        # Grid :
        self.teller_page_label.grid(row=0, column=1, columnspan=5, pady=10)
        self.teller_id_label.grid(row = 1, column=1)
        self.teller_id_entry.grid(row = 1, column=2)
        self.teller_name_label.grid(row = 2, column=1)
        self.teller_name_entry.grid(row = 2, column=2)
        self.teller_password_label.grid(row = 3, column=1)
        self.teller_password_entry.grid(row = 3, column=2)
        self.teller_address_label.grid(row = 4, column=1)
        self.teller_address_entry.grid(row = 4, column=2)
        self.teller_phone_number_label.grid(row = 5, column=1)
        self.teller_phone_number_entry.grid(row = 5, column=2)
        self.teller_account_number_label.grid(row = 6, column=1)
        self.teller_account_number_entry.grid(row = 6, column=2)
        self.teller_init_balance_label.grid(row = 7, column=1)
        self.teller_init_balance_entry.grid(row = 7, column=2)
        self.teller_account_type_label.grid(row = 8, column=1)
        self.teller_account_type_button.grid(row = 8, column=2)
        self.submit_add_teller_button.grid(row = 10, column=1, columnspan=5, pady=10)

        # run the page :
        self.add_teller_page.mainloop()

    def addTeller(self):
        """
            Function run when you press on submit add teller .
        """
        # Try to handle if the user fill all feilds or not .
        try :
            # Get the data from the entries :
            id_ = int(self.teller_id_entry.get())
            name = self.teller_name_entry.get()
            password = self.teller_password_entry.get()
            address = self.teller_address_entry.get()
            phone_number = self.teller_phone_number_entry.get()
            account_number = int(self.teller_account_number_entry.get())
            balance = int(self.teller_init_balance_entry.get())

            # check if the feilds if fill or not :
            if len(str(id_)) > 0 and len(name) > 0 and len(password) > 0 and len(address) > 0 and len(phone_number) > 0 and len(str(account_number)) > 0 and len(str(balance)) > 0:
                
                # Check if the account is not already found :
                if account_number not in self.bank.tellers :
                    
                    # Add Teller Account :
                    self.bank.createTeller(id_, name, password, address, phone_number, account_number)
                    
                    # check if the user choose the checking account or saving
                    if self.account_type_checking_teller :
                        
                        # Create checking teller account :  
                        self.bank.create_teller_account(account_number, "checking", balance)
                        
                        # Show Message with done :
                        messagebox.showinfo("Account Info", "Account has been added.")
                    else :

                        # If the user choose saving get the interset rate : 
                        init_rate = int(self.teller_interset_rate_entry.get())

                        # Create Saving teller account :
                        self.bank.create_teller_account(account_number, "saving", balance, init_rate)
                        
                        # Show Message with done:
                        messagebox.showinfo("Account Info", "Account has been added.")
                else :
                    # Show Error if the account is found :
                    messagebox.showerror("Account Info", "Account number already exists.")
            else :
                # Show error if the account if fields arn not filled : 
                messagebox.showerror("Account Info", "Fields must be filled .")
        except :
            # Show error if the id, account if are not filled :
            messagebox.showerror("Account Info", "Fields must be filled .")

    def createEnteryForSavingTeller(self):
        """
            Function to grid and grid forget the interest rate lable and entry
        """
        # If the user choose the saving account :
        if self.is_saving_taller_account :
            # Show the lable and entry :
            self.teller_interset_rate_label.grid(row=9, column=1)
            self.teller_interset_rate_entry.grid(row=9, column=2)
            
            # clear flags :
            self.is_saving_taller_account = False
            self.account_type_checking_teller = False

        else:
            # Hide the lable and entry :
            self.teller_interset_rate_label.grid_forget()
            self.teller_interset_rate_entry.grid_forget()

            # set flags :
            self.is_saving_taller_account = True
            self.account_type_checking_teller = True

    def transactionButton(self):
        """
            Function to create trnasction Log Page .
        """
        # Create sub window :
        self.transaction_window = Toplevel(self.frame)

        # Set size of the window :
        self.transaction_window.geometry("600x450")

        # Create label info :
        self.transaction_label = Label(self.transaction_window, text="Transaction Log:", font=("Arail", 13, "bold"))
        
        # Packing the info label:
        self.transaction_label.pack(pady=10)

        # Create Text box to show all transaction log :
        self.transaction_text_box = Text(self.transaction_window, width=75, height=25)
        
        # Packing the transation text box
        self.transaction_text_box.pack()

        # get data from the account events 
        for line in self.account.events:
            
            # Insert data
            self.transaction_text_box.insert(END, f"{line}\n")

        # Run the page : 
        self.transaction_window.mainloop()

    def withdrawButton(self, account_object):
        self.withdraw_page = Toplevel(self.frame)
        self.withdraw_page.title("Withdraw Money")
        self.withdraw_page.iconbitmap("images/bank.ico")
        self.is_withdraw_in_saving_account = IntVar()

        self.deposit_account_label = Label(self.withdraw_page, text="Account Number : ", font=("Arail", 10, "bold"))
        self.deposit_account_entry = Entry(self.withdraw_page, width=40)

        self.deposit_amount_label = Label(self.withdraw_page, text="Amount : ", font=("Arail", 10, "bold"))
        self.deposit_amount_entry = Entry(self.withdraw_page, width=40)

        self.withdraw_saving_amount_label = Label(self.withdraw_page, text="Account Type (default checking) ", font=("Arail", 10, "bold"))
        self.customer_withdraw_account_type_button = Checkbutton(self.withdraw_page, text="Saving", variable= self.is_withdraw_in_saving_account)

        self.submit_deposit_customer_button = Button(self.withdraw_page, text="Submit Withdraw", bg="green", fg="white", font=("Arial", 10, "bold"), command =lambda : [self.withdrawSubmit(account_object), self.withdraw_page.destroy()])

        self.deposit_account_label.grid(row = 1, column=1)
        self.deposit_account_entry.grid(row = 1, column=2)
        self.deposit_amount_label.grid(row = 2, column=1)
        self.deposit_amount_entry.grid(row = 2, column=2)
        self.withdraw_saving_amount_label.grid(row = 3, column=1)
        self.customer_withdraw_account_type_button.grid(row = 3, column=2)
        self.submit_deposit_customer_button.grid(row=4, column=1, columnspan=20, pady=10)
        self.withdraw_page.mainloop()
        
    def withdrawSubmit(self, account_object):
        try :
            account_number = int(self.deposit_account_entry.get())
            amount = int(self.deposit_amount_entry.get())
        except :
            messagebox.showerror("Account Info", "Fields must be filled .")
        is_saving = self.is_withdraw_in_saving_account.get()
        try :
            if account_number in account_object:
                time = datetime.now().strftime("%I:%M:%S %p")
                date = datetime.now().strftime("%a %b %Y")
                if is_saving :
                    if amount < account_object[account_number].Accounts['saving'].balance :
                        account_object[account_number].events.append(f"* Withdraw (Saving): -{amount}, New Balance : {account_object[account_number].Accounts['saving'].balance - amount} .\n\t- Date : {date} .\n\t- Time : {time} .\n\tThe process was done by (Teller / Manager): {self.account.account_name} .")
                        account_object[account_number].withdrawSaving(self.bank, amount)
                        messagebox.showinfo("Successful Submit", "Done .")
                    else :
                        messagebox.showinfo("Error", "Insufficient funds .")
                else :
                    if amount < account_object[account_number].Accounts['checking'].balance :
                        
                        account_object[account_number].events.append(f"* Withdraw (Checking): -{amount}, New Balance : {account_object[account_number].Accounts['checking'].balance - amount} .\n\t- Date : {date} .\n\t- Time : {time} .\n\tThe process was done by (Teller / Manager): {self.account.account_name} .")
                        account_object[account_number].withdraw(self.bank, amount)
                        messagebox.showinfo("Successful Submit", "Done .")
                    else :
                        messagebox.showerror("Error", "Insufficient funds .")
            else :
                messagebox.showerror("Error", "Account Not Found .")
        except:
            messagebox.showerror("Error", "Bank Account Not Found .")

    def depositButton(self, account_object):
        self.deposit_page = Toplevel(self.frame)
        self.deposit_page.title("Deposit Money")
        self.deposit_page.iconbitmap("images/bank.ico")
        self.is_deposit_in_saving_account = IntVar(self.deposit_page)

        self.deposit_account_label = Label(self.deposit_page, text="Account Number : ", font=("Arail", 10, "bold"))
        self.deposit_account_entry = Entry(self.deposit_page, width=40)

        self.deposit_amount_label = Label(self.deposit_page, text="Amount : ", font=("Arail", 10, "bold"))
        self.deposit_amount_entry = Entry(self.deposit_page, width=40)

        self.deposit_saving_amount_label = Label(self.deposit_page, text="Account Type (default checking) ", font=("Arail", 10, "bold"))
        self.customer_account_type_button = Checkbutton(self.deposit_page, text="Saving", variable= self.is_deposit_in_saving_account)

        self.submit_deposit_customer_button = Button(self.deposit_page, text="Submit Despsoit", bg="green", fg="white", font=("Arial", 10, "bold"), command = lambda : [self.depositSubmit(account_object), self.deposit_page.destroy()])

        self.deposit_account_label.grid(row = 1, column=1)
        self.deposit_account_entry.grid(row = 1, column=2)
        self.deposit_amount_label.grid(row = 2, column=1)
        self.deposit_amount_entry.grid(row = 2, column=2)
        self.deposit_saving_amount_label.grid(row = 3, column=1)
        self.customer_account_type_button.grid(row = 3, column=2)
        self.submit_deposit_customer_button.grid(row=4, column=1, columnspan=20, pady=10)
        self.deposit_page.mainloop()
        
    def depositSubmit(self, account_object):
        try :
            account_number = int(self.deposit_account_entry.get())
            amount = int(self.deposit_amount_entry.get())
        except :
            messagebox.showerror("Account Info", "Fields must be filled .")

        is_saving = self.is_deposit_in_saving_account.get()

        try :
            if account_number in account_object:
                time = datetime.now().strftime("%I:%M:%S %p")
                date = datetime.now().strftime("%a %b %Y")
                if is_saving :
                    account_object[account_number].events.append(f"* Diposit (Saving): +{amount}, New Balance : {amount + account_object[account_number].Accounts['saving'].balance} .\n\t- Date : {date} .\n\t- Time : {time} .\n\t- The process was done by (Teller / Manager): {self.account.account_name} .")
                    account_object[account_number].depositSaving(self.bank, amount)
                    messagebox.showinfo("Successful Submit", "Done .")
                else :
                    account_object[account_number].events.append(f"* Diposit (Checking): +{amount}, New Balance : {amount + account_object[account_number].Accounts['checking'].balance} .\n\t- Date : {date} .\n\t- Time : {time} .\n\t- The process was done by (Teller / Manager): {self.account.account_name} .")
                    account_object[account_number].deposit(self.bank, amount)
                    messagebox.showinfo("Successful Submit", "Done .")
            else :
                messagebox.showerror("Error", "Account Not Found .")
        except:
            messagebox.showerror("Error", "Bank Account Not Found .")
    def addLoan(self):
        self.add_loan_page = Toplevel(self.frame)
        self.add_loan_page.title("Add Loan")
        self.add_loan_page.geometry("390x250")
        self.add_loan_page.iconbitmap("images/bank.ico")
        self.account_type_checking = True
        self.is_saving_account = True
        self.loan_was_selected = StringVar(self.add_loan_page)
        self.options_loan_list = [
            "Personal Loan",
            "Home Loan (Mortgage)",
            "Car Loan (Auto Loan)",
            "Student Loan (Education Loan)",
            "Business Loan",
            "Payday Loan",
            "Credit Card Loan (Cash Advance)",
            "Debt Consolidation Loan",
            "Payday Alternative Loan (PAL)",
            "Secured Loan",
            "Unsecured Loan"
        ]

        self.loan_page_label = Label(self.add_loan_page, text="Add Loan", font=("Arail", 15, "bold"))

        self.loan_account_number_label = Label(self.add_loan_page, text="Account Number : ", font=("Arail", 10, "bold"))
        self.loan_account_number_entry = Entry(self.add_loan_page, width=40)

        self.loan_ammount_number = Label(self.add_loan_page, text="Amount : ", font=("Arail", 10, "bold"))
        self.loan_ammount_entry = Entry(self.add_loan_page, width=40)

        self.loan_type_label = Label(self.add_loan_page, text="Loan type : ", font=("Arail", 10, "bold"))
        self.opentions_loan_menu = OptionMenu(self.add_loan_page, self.loan_was_selected, *self.options_loan_list)
        

        self.submit_add_customer_button = Button(self.add_loan_page, text="Submit Adding", bg="green", fg="white", font=("Arial", 10, "bold"), command = self.addCustomerLoan)

        self.loan_page_label.grid(row=0, column=1, columnspan=5, pady=10)
        self.loan_account_number_label.grid(row = 1, column=1)
        self.loan_account_number_entry.grid(row = 1, column=2)
        self.loan_ammount_number.grid(row = 2, column=1)
        self.loan_ammount_entry.grid(row = 2, column=2)
        self.loan_type_label.grid(row = 3, column=1)
        self.opentions_loan_menu.grid(row = 3, column=2)
        self.submit_add_customer_button.grid(row = 4, column=1, columnspan=5, pady=10)

        self.add_loan_page.mainloop()

    def addCustomerLoan(self):
        account_number = int(self.loan_account_number_entry.get())
        type = self.loan_was_selected.get()
        amount = int(self.loan_ammount_entry.get())
        if account_number in self.bank.Customers:
            self.bank.Customers[account_number].applayForLoan(type, amount)
            messagebox.showinfo("Successful", f"Successfully added the {type}")
        else :
            messagebox.showerror("Account Info", "Account number not found.")
    def showAllCustomers(self):
        self.show_all_customer_page = Toplevel(self.frame)
        self.show_all_customer_page.title("All Customers")
        self.show_all_customer_page.geometry("850x600")

        
        self.value_was_selected = StringVar(self.show_all_customer_page)
        self.value_was_selected.set("Choose :")
        self.options_list = [
            "Id",
            "Name",
            "Address",
            "Phone Number",
            "Account Number",
            "Date Created",
            "Accounts"
        ]

        

        self.search_button = Button(self.show_all_customer_page, bg="green", fg="white", font=("Arial", 10, "bold"), text="Search", command = self.search_button_action_customer)
        self.reest_button = Button(self.show_all_customer_page, bg="red", fg="white", font=("Arial", 10, "bold"), text="Reset", command = self.reset_button_action)
        self.search_entry = Entry(self.show_all_customer_page)
        self.search_label = Label(self.show_all_customer_page, text="Search Value")
        self.opentions_menu = OptionMenu(self.show_all_customer_page,self.value_was_selected,*self.options_list)
        self.tree_veiw = ttk.Treeview(self.show_all_customer_page, height=23, columns=("Account Id", "Account Name", "Address", "Phone Number", "Account Number", "Date Craeted", "Time Craeted", "Accounts"))
        
        self.tree_veiw.column("#0", width=50)
        self.tree_veiw.column("Account Id", width=100)
        self.tree_veiw.column("Account Name", width=100)
        self.tree_veiw.column("Address", width=100)
        self.tree_veiw.column("Phone Number", width=100)
        self.tree_veiw.column("Account Number", width=100)
        self.tree_veiw.column("Date Craeted", width=100)
        self.tree_veiw.column("Time Craeted", width=100)
        self.tree_veiw.column("Accounts", width=100)

        self.tree_veiw.heading("#0", text="N")
        self.tree_veiw.heading("Account Id", text="Account Id")
        self.tree_veiw.heading("Account Name", text="Account Name")
        self.tree_veiw.heading("Address", text="Address")
        self.tree_veiw.heading("Phone Number", text="Phone Number")
        self.tree_veiw.heading("Account Number", text="Account Number")
        self.tree_veiw.heading("Date Craeted", text="Date Craeted")
        self.tree_veiw.heading("Time Craeted", text="Time Craeted")
        self.tree_veiw.heading("Accounts", text="N-Accounts")

        self.show_customer_tree_view()
    
        self.opentions_menu.place(x = 200, y = 50)
        self.search_label.place(x = 350, y = 32)
        self.search_entry.place(x = 350, y = 55)
        self.search_button.place(x = 500, y = 50)
        self.reest_button.place(x = 560, y = 50)
        self.tree_veiw.place(y = 120)
        self.show_all_customer_page.mainloop()

    def show_customer_tree_view(self):
        count = 0
        for account_number in self.bank.Customers:
            self.tree_veiw.insert(
                "",
                END,
                text=f"{count+1}",
                values=(f"{self.bank.Customers[account_number].account_id}", 
                        f"{self.bank.Customers[account_number].account_name}",
                        f"{self.bank.Customers[account_number].address}",
                        f"{self.bank.Customers[account_number].phone_number}",
                        f"{self.bank.Customers[account_number].account_number}",
                        f"{self.bank.Customers[account_number].date_created}",
                        f"{self.bank.Customers[account_number].time_created}",
                        f"{len(self.bank.Customers[account_number].Accounts)}")
            )
            count += 1

    def reset_button_action(self):
        self.delete_elements_tree_view()
        self.show_customer_tree_view()

    def search_button_action_customer(self):
        self.delete_elements_tree_view()
        count = 0
        search_value_entry = self.search_entry.get()
        type_of_search = self.value_was_selected.get()


        if type_of_search == "Id" :
            for account_number in self.bank.Customers:
                if self.bank.Customers[account_number].account_id == int(search_value_entry) :
                    self.tree_veiw.insert(
                        "",
                        END,
                        text=f"1",
                        values=(f"{self.bank.Customers[account_number].account_id}", 
                                f"{self.bank.Customers[account_number].account_name}",
                                f"{self.bank.Customers[account_number].address}",
                                f"{self.bank.Customers[account_number].phone_number}",
                                f"{self.bank.Customers[account_number].account_number}",
                                f"{self.bank.Customers[account_number].date_created}",
                                f"{self.bank.Customers[account_number].time_created}",
                                f"{len(self.bank.Customers[account_number].Accounts)}")
                    )
        elif type_of_search == "Name" :
            for account_number in self.bank.Customers:
                if str(search_value_entry) in self.bank.Customers[account_number].account_name :
                    self.tree_veiw.insert(
                        "",
                        END,
                        text=f"{count+1}",
                        values=(f"{self.bank.Customers[account_number].account_id}", 
                                f"{self.bank.Customers[account_number].account_name}",
                                f"{self.bank.Customers[account_number].address}",
                                f"{self.bank.Customers[account_number].phone_number}",
                                f"{self.bank.Customers[account_number].account_number}",
                                f"{self.bank.Customers[account_number].date_created}",
                                f"{self.bank.Customers[account_number].time_created}",
                                f"{len(self.bank.Customers[account_number].Accounts)}")
                    )
                count += 1
        elif type_of_search == "Phone Number" :
            for account_number in self.bank.Customers:
                if str(search_value_entry) == self.bank.Customers[account_number].phone_number :
                    self.tree_veiw.insert(
                        "",
                        END,
                        text=f"1",
                        values=(f"{self.bank.Customers[account_number].account_id}", 
                                f"{self.bank.Customers[account_number].account_name}",
                                f"{self.bank.Customers[account_number].address}",
                                f"{self.bank.Customers[account_number].phone_number}",
                                f"{self.bank.Customers[account_number].account_number}",
                                f"{self.bank.Customers[account_number].date_created}",
                                f"{self.bank.Customers[account_number].time_created}",
                                f"{len(self.bank.Customers[account_number].Accounts)}")
                    )
        elif type_of_search == "Address" :
            for account_number in self.bank.Customers:
                if str(search_value_entry) in self.bank.Customers[account_number].address :
                    self.tree_veiw.insert(
                        "",
                        END,
                        text=f"{count+1}",
                        values=(f"{self.bank.Customers[account_number].account_id}", 
                                f"{self.bank.Customers[account_number].account_name}",
                                f"{self.bank.Customers[account_number].address}",
                                f"{self.bank.Customers[account_number].phone_number}",
                                f"{self.bank.Customers[account_number].account_number}",
                                f"{self.bank.Customers[account_number].date_created}",
                                f"{self.bank.Customers[account_number].time_created}",
                                f"{len(self.bank.Customers[account_number].Accounts)}")
                    )
                count += 1
        elif type_of_search == "Account Number" :
            search_value_entry = int(search_value_entry)
            if int(search_value_entry) in self.bank.Customers:
                self.tree_veiw.insert(
                    "",
                    END,
                    text=f"1",
                    values=(f"{self.bank.Customers[search_value_entry].account_id}", 
                            f"{self.bank.Customers[search_value_entry].account_name}",
                            f"{self.bank.Customers[search_value_entry].address}",
                            f"{self.bank.Customers[search_value_entry].phone_number}",
                            f"{self.bank.Customers[search_value_entry].account_number}",
                            f"{self.bank.Customers[search_value_entry].date_created}",
                            f"{self.bank.Customers[search_value_entry].time_created}",
                            f"{len(self.bank.Customers[search_value_entry].Accounts)}")
                    )
        elif type_of_search == "Accounts" :
            for account_number in self.bank.Customers:
                if int(search_value_entry) == len(self.bank.Customers[account_number].Accounts) :
                    self.tree_veiw.insert(
                        "",
                        END,
                        text=f"{count+1}",
                        values=(f"{self.bank.Customers[account_number].account_id}", 
                                f"{self.bank.Customers[account_number].account_name}",
                                f"{self.bank.Customers[account_number].address}",
                                f"{self.bank.Customers[account_number].phone_number}",
                                f"{self.bank.Customers[account_number].account_number}",
                                f"{self.bank.Customers[account_number].date_created}",
                                f"{self.bank.Customers[account_number].time_created}",
                                f"{len(self.bank.Customers[account_number].Accounts)}")
                    )
                count += 1
        elif type_of_search == "Date Created" :
            for account_number in self.bank.Customers:
                if str(search_value_entry) in self.bank.Customers[account_number].date_created :
                    self.tree_veiw.insert(
                        "",
                        END,
                        text=f"{count+1}",
                        values=(f"{self.bank.Customers[account_number].account_id}", 
                                f"{self.bank.Customers[account_number].account_name}",
                                f"{self.bank.Customers[account_number].address}",
                                f"{self.bank.Customers[account_number].phone_number}",
                                f"{self.bank.Customers[account_number].account_number}",
                                f"{self.bank.Customers[account_number].date_created}",
                                f"{self.bank.Customers[account_number].time_created}",
                                f"{len(self.bank.Customers[account_number].Accounts)}")
                    )
                count += 1
    
    def showAllTellers(self):
        self.show_all_tellers_page = Toplevel(self.frame)
        self.show_all_tellers_page.title("All Tellers")
        self.show_all_tellers_page.geometry("850x600")

        self.value_was_selected_teller = StringVar(self.show_all_tellers_page)
        self.value_was_selected_teller.set("Choose :")
        options_list = [
            "Id",
            "Name",
            "Address",
            "Phone Number",
            "Account Number",
            "Date Created",
            "Accounts"
        ]

        

        self.search_button = Button(self.show_all_tellers_page, bg="green", fg="white", font=("Arial", 10, "bold"), text="Search", command = self.search_button_action)
        self.reest_button = Button(self.show_all_tellers_page, bg="red", fg="white", font=("Arial", 10, "bold"), text="Reset", command = lambda : [self.reset_button_action_tellers(), self.show_customer_tree_view_tellers])
        self.search_entry = Entry(self.show_all_tellers_page)
        self.search_label = Label(self.show_all_tellers_page, text="Search Value")
        self.opentions_menu = OptionMenu(self.show_all_tellers_page,self.value_was_selected_teller,*options_list)
        self.tree_veiw = ttk.Treeview(self.show_all_tellers_page, height=23, columns=("Account Id", "Account Name", "Address", "Phone Number", "Account Number", "Date Craeted", "Time Craeted", "Accounts"))
        
        self.tree_veiw.column("#0", width=50)
        self.tree_veiw.column("Account Id", width=100)
        self.tree_veiw.column("Account Name", width=100)
        self.tree_veiw.column("Address", width=100)
        self.tree_veiw.column("Phone Number", width=100)
        self.tree_veiw.column("Account Number", width=100)
        self.tree_veiw.column("Date Craeted", width=100)
        self.tree_veiw.column("Time Craeted", width=100)
        self.tree_veiw.column("Accounts", width=100)

        self.tree_veiw.heading("#0", text="N")
        self.tree_veiw.heading("Account Id", text="Account Id")
        self.tree_veiw.heading("Account Name", text="Account Name")
        self.tree_veiw.heading("Address", text="Address")
        self.tree_veiw.heading("Phone Number", text="Phone Number")
        self.tree_veiw.heading("Account Number", text="Account Number")
        self.tree_veiw.heading("Date Craeted", text="Date Craeted")
        self.tree_veiw.heading("Time Craeted", text="Time Craeted")
        self.tree_veiw.heading("Accounts", text="N-Accounts")

        self.show_customer_tree_view_tellers()
    
        self.opentions_menu.place(x = 200, y = 50)
        self.search_label.place(x = 350, y = 32)
        self.search_entry.place(x = 350, y = 55)
        self.search_button.place(x = 500, y = 50)
        self.reest_button.place(x = 560, y = 50)
        self.tree_veiw.place(y = 120)
        self.show_all_tellers_page.mainloop()

    def show_customer_tree_view_tellers(self):
        count = 0

        for account_number in self.bank.tellers:
            self.tree_veiw.insert(
                "",
                END,
                text=f"{count+1}",
                values=(f"{self.bank.tellers[account_number].account_id}", 
                        f"{self.bank.tellers[account_number].account_name}",
                        f"{self.bank.tellers[account_number].address}",
                        f"{self.bank.tellers[account_number].phone_number}",
                        f"{self.bank.tellers[account_number].account_number}",
                        f"{self.bank.tellers[account_number].date_created}",
                        f"{self.bank.tellers[account_number].time_created}",
                        f"{len(self.bank.tellers[account_number].Accounts)}")
            )   
    def delete_elements_tree_view(self):
        for item in self.tree_veiw.get_children():
            self.tree_veiw.delete(item)

    def reset_button_action_tellers(self):
        self.delete_elements_tree_view()
        self.show_customer_tree_view_tellers()


    def search_button_action(self):
        self.delete_elements_tree_view()
        count = 0
        search_value_entry = self.search_entry.get()
        type_of_search = self.value_was_selected_teller.get()


        if type_of_search == "Id" :
            for account_number in self.bank.tellers:
                if self.bank.tellers[account_number].account_id == int(search_value_entry) :
                    self.tree_veiw.insert(
                        "",
                        END,
                        text=f"1",
                        values=(f"{self.bank.tellers[account_number].account_id}", 
                                f"{self.bank.tellers[account_number].account_name}",
                                f"{self.bank.tellers[account_number].address}",
                                f"{self.bank.tellers[account_number].phone_number}",
                                f"{self.bank.tellers[account_number].account_number}",
                                f"{self.bank.tellers[account_number].date_created}",
                                f"{self.bank.tellers[account_number].time_created}",
                                f"{len(self.bank.tellers[account_number].Accounts)}")
                    )
        elif type_of_search == "Name" :
            for account_number in self.bank.tellers:
                if str(search_value_entry) in self.bank.tellers[account_number].account_name :
                    self.tree_veiw.insert(
                        "",
                        END,
                        text=f"{count+1}",
                        values=(f"{self.bank.tellers[account_number].account_id}", 
                                f"{self.bank.tellers[account_number].account_name}",
                                f"{self.bank.tellers[account_number].address}",
                                f"{self.bank.tellers[account_number].phone_number}",
                                f"{self.bank.tellers[account_number].account_number}",
                                f"{self.bank.tellers[account_number].date_created}",
                                f"{self.bank.tellers[account_number].time_created}",
                                f"{len(self.bank.tellers[account_number].Accounts)}")
                    )
        elif type_of_search == "Phone Number" :
            for account_number in self.bank.tellers:
                if str(search_value_entry) == self.bank.tellers[account_number].phone_number :
                    self.tree_veiw.insert(
                        "",
                        END,
                        text=f"1",
                        values=(f"{self.bank.tellers[account_number].account_id}", 
                                f"{self.bank.tellers[account_number].account_name}",
                                f"{self.bank.tellers[account_number].address}",
                                f"{self.bank.tellers[account_number].phone_number}",
                                f"{self.bank.tellers[account_number].account_number}",
                                f"{self.bank.tellers[account_number].date_created}",
                                f"{self.bank.tellers[account_number].time_created}",
                                f"{len(self.bank.tellers[account_number].Accounts)}")
                    )
        elif type_of_search == "Address" :
            for account_number in self.bank.tellers:
                if str(search_value_entry) in self.bank.tellers[account_number].address :
                    self.tree_veiw.insert(
                        "",
                        END,
                        text=f"{count+1}",
                        values=(f"{self.bank.tellers[account_number].account_id}", 
                                f"{self.bank.tellers[account_number].account_name}",
                                f"{self.bank.tellers[account_number].address}",
                                f"{self.bank.tellers[account_number].phone_number}",
                                f"{self.bank.tellers[account_number].account_number}",
                                f"{self.bank.tellers[account_number].date_created}",
                                f"{self.bank.tellers[account_number].time_created}",
                                f"{len(self.bank.tellers[account_number].Accounts)}")
                    )
        elif type_of_search == "Account Number" :
            search_value_entry = int(search_value_entry)
            if int(search_value_entry) in self.bank.tellers:
                self.tree_veiw.insert(
                    "",
                    END,
                    text=f"1",
                    values=(f"{self.bank.tellers[search_value_entry].account_id}", 
                            f"{self.bank.tellers[search_value_entry].account_name}",
                            f"{self.bank.tellers[search_value_entry].address}",
                            f"{self.bank.tellers[search_value_entry].phone_number}",
                            f"{self.bank.tellers[search_value_entry].account_number}",
                            f"{self.bank.tellers[search_value_entry].date_created}",
                            f"{self.bank.tellers[search_value_entry].time_created}",
                            f"{len(self.bank.tellers[search_value_entry].Accounts)}")
                    )
        elif type_of_search == "Accounts" :
            for account_number in self.bank.tellers:
                if int(search_value_entry) == len(self.bank.tellers[account_number].Accounts) :
                    self.tree_veiw.insert(
                        "",
                        END,
                        text=f"{count+1}",
                        values=(f"{self.bank.tellers[account_number].account_id}", 
                                f"{self.bank.tellers[account_number].account_name}",
                                f"{self.bank.tellers[account_number].address}",
                                f"{self.bank.tellers[account_number].phone_number}",
                                f"{self.bank.tellers[account_number].account_number}",
                                f"{self.bank.tellers[account_number].date_created}",
                                f"{self.bank.tellers[account_number].time_created}",
                                f"{len(self.bank.tellers[account_number].Accounts)}")
                    )
        elif type_of_search == "Date Created" :
            for account_number in self.bank.tellers:
                if str(search_value_entry) in self.bank.tellers[account_number].date_created :
                    self.tree_veiw.insert(
                        "",
                        END,
                        text=f"{count+1}",
                        values=(f"{self.bank.tellers[account_number].account_id}", 
                                f"{self.bank.tellers[account_number].account_name}",
                                f"{self.bank.tellers[account_number].address}",
                                f"{self.bank.tellers[account_number].phone_number}",
                                f"{self.bank.tellers[account_number].account_number}",
                                f"{self.bank.tellers[account_number].date_created}",
                                f"{self.bank.tellers[account_number].time_created}",
                                f"{len(self.bank.tellers[account_number].Accounts)}")
                    )

    def addAccount(self):
        self.add_account_page = Toplevel(self.frame)
        self.add_account_page.title("Add Account")
        self.add_account_page.geometry("470x330")
        self.add_account_page.iconbitmap("images/bank.ico")
        self.account_type_checking = True
        self.is_saving_account = True

        self.customer_page_label = Label(self.add_account_page, text="Add Customer", font=("Arail", 15, "bold"))
        
        self.customer_id_label = Label(self.add_account_page, text="Id : ", font=("Arail", 10, "bold"))
        self.customer_id_entry = Entry(self.add_account_page, width=40)

        self.customer_name_label = Label(self.add_account_page, text="Name : ", font=("Arail", 10, "bold"))
        self.customer_name_entry = Entry(self.add_account_page, width=40)

        self.customer_password_label = Label(self.add_account_page, text="Password : ", font=("Arail", 10, "bold"))
        self.customer_password_entry = Entry(self.add_account_page, width=40)

        self.customer_address_label = Label(self.add_account_page, text="Address : ", font=("Arail", 10, "bold"))
        self.customer_address_entry = Entry(self.add_account_page, width=40)

        self.customer_phone_number_label = Label(self.add_account_page, text="Phone number :", font=("Arail", 10, "bold"))
        self.customer_phone_number_entry = Entry(self.add_account_page, width=40)

        self.customer_account_number_label = Label(self.add_account_page, text="Account Number :", font=("Arail", 10, "bold"))
        self.customer_account_number_entry = Entry(self.add_account_page, width=40)

        self.customer_init_balance_label = Label(self.add_account_page, text="Balance :", font=("Arail", 10, "bold"))
        self.customer_init_balance_entry = Entry(self.add_account_page, width=40)

        self.customer_account_type_label = Label(self.add_account_page, text="Account Type (default checking):", font=("Arail", 10, "bold"))
        self.customer_account_type_button = Checkbutton(self.add_account_page, text="Saving", command=self.createEnteryForSaving)

        self.customer_interset_rate_label = Label(self.add_account_page, text="Interset Rate :", font=("Arail", 10, "bold"))
        self.customer_interset_rate_entry = Entry(self.add_account_page, width=40)

        self.submit_add_customer_button = Button(self.add_account_page, text="Submit Adding", bg="green", fg="white", font=("Arial", 10, "bold"), command = self.addCustomer)

        self.customer_page_label.grid(row=0, column=1, columnspan=5, pady=10)
        self.customer_id_label.grid(row = 1, column=1)
        self.customer_id_entry.grid(row = 1, column=2)
        self.customer_name_label.grid(row = 2, column=1)
        self.customer_name_entry.grid(row = 2, column=2)
        self.customer_password_label.grid(row = 3, column=1)
        self.customer_password_entry.grid(row = 3, column=2)
        self.customer_address_label.grid(row = 4, column=1)
        self.customer_address_entry.grid(row = 4, column=2)
        self.customer_phone_number_label.grid(row = 5, column=1)
        self.customer_phone_number_entry.grid(row = 5, column=2)
        self.customer_account_number_label.grid(row = 6, column=1)
        self.customer_account_number_entry.grid(row = 6, column=2)
        self.customer_init_balance_label.grid(row = 7, column=1)
        self.customer_init_balance_entry.grid(row = 7, column=2)
        self.customer_account_type_label.grid(row = 8, column=1)
        self.customer_account_type_button.grid(row = 8, column=2)
        self.submit_add_customer_button.grid(row = 10, column=1, columnspan=5, pady=10)

        self.add_account_page.mainloop()
    
    def editAccount(self, account_type):
        self.edit_account_page = Toplevel(self.frame)
        self.edit_account_page.title("Edit Account")
        self.edit_account_page.iconbitmap("images/bank.ico")
        self.edit_account_page.geometry("400x250")


        self.customer_page_label = Label(self.edit_account_page, text=f"Edit {account_type}", font=("Arail", 15, "bold"))
        
        self.customer_account_number_label = Label(self.edit_account_page, text="Account Number :", font=("Arail", 10, "bold"))
        self.customer_account_number_entry = Entry(self.edit_account_page, width=40)

        self.customer_id_label = Label(self.edit_account_page, text="Id : ", font=("Arail", 10, "bold"))
        self.customer_id_entry = Entry(self.edit_account_page, width=40)

        self.customer_name_label = Label(self.edit_account_page, text="Name : ", font=("Arail", 10, "bold"))
        self.customer_name_entry = Entry(self.edit_account_page, width=40)

        self.customer_password_label = Label(self.edit_account_page, text="Password : ", font=("Arail", 10, "bold"))
        self.customer_password_entry = Entry(self.edit_account_page, width=40)

        self.customer_address_label = Label(self.edit_account_page, text="Address : ", font=("Arail", 10, "bold"))
        self.customer_address_entry = Entry(self.edit_account_page, width=40)

        self.customer_phone_number_label = Label(self.edit_account_page, text="Phone number :", font=("Arail", 10, "bold"))
        self.customer_phone_number_entry = Entry(self.edit_account_page, width=40)

        self.customer_account_number_new_label = Label(self.edit_account_page, text="Account Number New:", font=("Arail", 10, "bold"))
        self.customer_account_number_new_entry = Entry(self.edit_account_page, width=40)

        if account_type == "Teller" :
            self.submit_edit_customer_button = Button(self.edit_account_page, text="Submit Edit", bg="green", fg="white", font=("Arial", 10, "bold"), command = lambda : [self.editTeller(), self.edit_account_page.destroy()])
        else :
            self.submit_edit_customer_button = Button(self.edit_account_page, text="Submit Edit", bg="green", fg="white", font=("Arial", 10, "bold"), command = lambda : [self.editCustomer(), self.edit_account_page.destroy()])

        self.customer_page_label.grid(row = 0, column=1, columnspan=20, pady=10)
        self.customer_account_number_label.grid(row = 1, column=1)
        self.customer_account_number_entry.grid(row = 1, column=2)
        self.customer_id_label.grid(row = 2, column=1)
        self.customer_id_entry.grid(row = 2, column=2)
        self.customer_name_label.grid(row = 3, column=1)
        self.customer_name_entry.grid(row = 3, column=2)
        self.customer_password_label.grid(row = 4, column=1)
        self.customer_password_entry.grid(row = 4, column=2)
        self.customer_address_label.grid(row = 5, column=1)
        self.customer_address_entry.grid(row = 5, column=2)
        self.customer_phone_number_label.grid(row = 6, column=1)
        self.customer_phone_number_entry.grid(row = 6, column=2)
        self.customer_account_number_new_label.grid(row = 7, column=1)
        self.customer_account_number_new_entry.grid(row = 7, column=2)
        self.submit_edit_customer_button.grid(row = 8, column=1, columnspan=20, pady=10)
    
        self.edit_account_page.mainloop()


    def createEnteryForSaving(self):
        if self.is_saving_account :
            self.customer_interset_rate_label.grid(row=9, column=1)
            self.customer_interset_rate_entry.grid(row=9, column=2)
            self.is_saving_account = False
            self.account_type_checking = False

        else:
            self.customer_interset_rate_label.grid_forget()
            self.customer_interset_rate_entry.grid_forget()
            self.is_saving_account = True
            self.account_type_checking = True


    def addCustomer(self):
        """
            Function to create Customer .
        """
        try :
            # Get the Data .
            id_ = int(self.customer_id_entry.get())
            name = self.customer_name_entry.get()
            password = self.customer_password_entry.get()
            address = self.customer_address_entry.get()
            phone_number = self.customer_phone_number_entry.get()
            account_number = int(self.customer_account_number_entry.get())
            balance = int(self.customer_init_balance_entry.get())

            # if teh fields are filled :
            if len(str(id_)) > 0 and len(name) > 0 and len(password) > 0 and len(address) > 0 and len(phone_number) > 0 and len(str(account_number)) > 0 and len(str(balance)) > 0:
                
                # if the customer is not found in Customers .
                if account_number not in self.bank.Customers :
                    
                    # Create New Customer :
                    self.bank.create_customer(id_, name, password, address, phone_number, account_number)
                    
                    # Check the user is choosed "checking" or "Saving"
                    if self.account_type_checking :
                        
                        # Craete checking account .
                        self.bank.create_account(account_number, "checking", balance)
                        
                        # show info with : 
                        messagebox.showinfo("Account Info", "Account has been added.")
                    else :
                        # get the inital rate :
                        init_rate = int(self.customer_interset_rate_entry.get())
                        
                        # Create saving account : 
                        self.bank.create_account(account_number, "saving", balance, init_rate)
                        
                        # show info with done :
                        messagebox.showinfo("Account Info", "Account has been added.")
                else :
                    # Show Error :
                    messagebox.showerror("Account Info", "Account number already exists.")
            else :
                # Shoe Error :
                messagebox.showerror("Account Info", "Fields must be filled .")
        except:
            # Show Error :
            messagebox.showerror("Account Info", "Fields must be filled Correctly.")

    def editCustomer(self):
        """
            Fucntion to edit on Customer .
        """
        try :
            # Get the data From User :
            account_number = int(self.customer_account_number_entry.get())
            id_ = self.customer_id_entry.get()
            name = self.customer_name_entry.get()
            password = self.customer_password_entry.get()
            address = self.customer_address_entry.get()
            phone_number = self.customer_phone_number_entry.get()
            account_number_new = self.customer_account_number_new_entry.get()

            # Check if the user in accounts and if any entry has any data, information will updated:
            if account_number in self.bank.Customers :
                if len(id_) > 0 :
                    self.bank.Customers[account_number].account_id = int(id_)
                if len(name) > 0 :
                    self.bank.Customers[account_number].account_name = name
                if len(password) > 0:
                    self.bank.Customers[account_number].password = password
                if len(address) > 0:
                    self.bank.Customers[account_number].address = address
                if len(phone_number) > 0:
                    self.bank.Customers[account_number].phone_number = phone_number
                if len(account_number_new) > 0:
                    self.bank.Customers[account_number].account_number = int(account_number_new)
                    self.bank.Customers[int(account_number_new)] = self.bank.Customers.pop(account_number)
                
                # Show Error :
                messagebox.showinfo("Account Info", "Done .")
            else :
                # Show Error :
                messagebox.showerror("Account Info", "Account number Not Found.")
        except:
            # Show error when get fallid data :
            messagebox.showerror("Account Info", "Error when assgin data, try again")
    def editTeller(self):
        """
            Function to edit the teller
        """
        try :
            # Get the data From User :
            account_number = int(self.customer_account_number_entry.get())
            id_ = self.customer_id_entry.get()
            name = self.customer_name_entry.get()
            password = self.customer_password_entry.get()
            address = self.customer_address_entry.get()
            phone_number = self.customer_phone_number_entry.get()
            account_number_new = self.customer_account_number_new_entry.get()

            # Check if the user in accounts and if any entry has any data, information will updated:
            if account_number in self.bank.tellers:
                if len(id_) > 0 :
                    self.bank.tellers[account_number].account_id = int(id_)
                if len(name) > 0 :
                    self.bank.tellers[account_number].account_name = name
                if len(password) > 0:
                    self.bank.tellers[account_number].password = password
                if len(address) > 0:
                    self.bank.tellers[account_number].address = address
                if len(phone_number) > 0:
                    self.bank.tellers[account_number].phone_number = phone_number
                if len(account_number_new) > 0:
                    self.bank.tellers[account_number].account_number = int(account_number_new)
                    self.bank.tellers[int(account_number_new)] = self.bank.tellers.pop(account_number)
                
                # Show Message with Done :
                messagebox.showinfo("Account Info", "Done .")
            else :
                # Show Error :
                messagebox.showerror("Account Info", "Account number Not Found.")
        except:
            # Show error when get fallid data :
            messagebox.showerror("Account Info", "Error when assgin data, try again")

    def closeAccount(self):
        """
            Function to close account .
        """
        try : 
            # get the acount number .
            account_number = int(simpledialog.askstring("Delete Account", "Enter Account Number:"))
            
            # If the account found .
            if account_number in self.bank.Customers:
                # Close the account .
                self.account.closeAccount(self.bank, account_number)
                
                # Show Message with done : 
                messagebox.showinfo("Account deleted", "Account has been deleted .")
            else :
                # Show Error when account not found
                messagebox.showerror("Error", "Account Not Found .")
        except:
            pass

    def logout(self):
        """
            Function to log out .
        """
        # Clear The widgets of frame :
        self.clearAllInsideFrame()
        
        # Call the function to craete log in page : 
        self.log_in_func()

    def createBasicInformation(self):
        self.clearAllInsideFrame()  # Clear previous widgets

        # resize the frame again :
        self.frame.config(width=850, height=600)
        
        # Craete Bank Photo :
        self.bank_photo = PhotoImage(file = "images/bank2.png").subsample(2) # zoom out the photo
        
        # Create Label to store the bank photo 
        self.button_photo = Label(self.frame, image=self.bank_photo, bg="white")
        
        # Create Labels Information :
        self.bank_information_label = Label(self.frame, text="Bank Management System",width=20, font=('Arial',16,'bold'), bg="white")
        self.account_information_label = Label(self.frame, text="Account Information",width=20, font=('Arial',16,'bold'), bg="white")

        # Craete entries to show data in tables :
        self.account_login_type_label = Entry(self.frame, width=20, fg='grey',font=('Arial',16,'bold'))
        self.account_login_type_label_value = Entry(self.frame, width=20, fg='grey',font=('Arial',16,'bold'))
        
        self.account_id_label = Entry(self.frame, width=20, fg='grey',font=('Arial',16,'bold'))
        self.account_id_label_value = Entry(self.frame, width=20, fg='grey',font=('Arial',16,'bold'))
        
        self.account_name_label = Entry(self.frame, width=20, fg='grey',font=('Arial',16,'bold'))
        self.account_name_label_value = Entry(self.frame, width=20, fg='grey',font=('Arial',16,'bold'))
        
        self.address_label = Entry(self.frame, width=20, fg='grey',font=('Arial',16,'bold'))
        self.address_label_value = Entry(self.frame, width=20, fg='grey',font=('Arial',16,'bold'))
        
        self.phone_number_label = Entry(self.frame, width=20, fg='grey',font=('Arial',16,'bold'))
        self.phone_number_label_value = Entry(self.frame, width=20, fg='grey',font=('Arial',16,'bold'))
        
        self.account_number_label = Entry(self.frame, width=20, fg='grey',font=('Arial',16,'bold'))
        self.account_number_label_value = Entry(self.frame, width=20, fg='grey',font=('Arial',16,'bold'))
        
        self.date_label = Entry(self.frame, width=20, fg='grey',font=('Arial',16,'bold'))
        self.date_label_value = Entry(self.frame, width=20, fg='grey',font=('Arial',16,'bold'))
        
        self.time_created_label = Entry(self.frame, width=20, fg='grey',font=('Arial',16,'bold'))
        self.time_created_label_value = Entry(self.frame, width=20, fg='grey',font=('Arial',16,'bold'))

        self.balanced_label = Entry(self.frame, width=20, fg='grey',font=('Arial',16,'bold'))
        self.balanced_label_value = Entry(self.frame, width=20, fg='grey',font=('Arial',16,'bold'))

        self.saving_balanced_label = Entry(self.frame, width=20, fg='grey',font=('Arial',16,'bold'))
        self.saving_balanced_label_value = Entry(self.frame, width=20, fg='grey',font=('Arial',16,'bold'))

        # Insert values :
        self.account_login_type_label.insert(END, "Account Type : ")
        self.account_login_type_label_value.insert(END, f"{self.account_login_type}")
        self.account_id_label.insert(END, "Customer Id : ")
        self.account_id_label_value.insert(END, f"{self.account.account_id}")
        self.account_name_label.insert(END, "Customer Name : ")
        self.account_name_label_value.insert(END, f"{self.account.account_name}")
        self.address_label.insert(END, "Address : ")
        self.address_label_value.insert(END, f"{self.account.address}")
        self.phone_number_label.insert(END, "Phone Number : ")
        self.phone_number_label_value.insert(END, f"{self.account.phone_number}")
        self.account_number_label.insert(END, "Account Number : ")
        self.account_number_label_value.insert(END, f"{self.account.account_number}")
        self.date_label.insert(END, "Date Created : ")
        self.date_label_value.insert(END, f"{self.account.date_created}")
        self.time_created_label.insert(END, "Time Created : ")
        self.time_created_label_value.insert(END, f"{self.account.time_created}")
        self.balanced_label.insert(END, "Checking Balanced : ")
        self.saving_balanced_label.insert(END, "Saving Balanced : ")

        # Check if the log in is Manager Or not :
        if self.account_login_type == "Manager" :
            # Insert the balance values of manager account :
            self.balanced_label_value.insert(END, f"{self.bank.managers[self.account.account_number].Accounts['checking'].balance}")
            self.saving_balanced_label_value.insert(END, f"{self.bank.managers[self.account.account_number].Accounts['saving'].balance}")
        else :
            # Check on checking and saving account if found put it:
            try : 
                self.balanced_label_value.insert(END, f"{self.bank.tellers[self.account.account_number].Accounts['checking'].balance}")
            except :
                self.balanced_label_value.insert(END, "Not Found")
            try :
                self.saving_balanced_label_value.insert(END, f"{self.bank.tellers[self.account.account_number].Accounts['saving'].balance}")
            except : 
                self.saving_balanced_label_value.insert(END, "Not Found")

        # Placing The Label and enties :
        self.bank_information_label.place(x = 70, y=25)
        self.button_photo.place(x=5, y=10)
        self.account_information_label.place(x = 400, y = 60)
        self.account_login_type_label.place(x = 300, y =100)
        self.account_login_type_label_value.place(x = 545, y =100)
        self.account_id_label.place(x = 300, y =130)
        self.account_id_label_value.place(x = 545, y =130)
        self.account_name_label.place(x = 300, y =160)
        self.account_name_label_value.place(x = 545, y =160)
        self.address_label.place(x = 300, y =190)
        self.address_label_value.place(x = 545, y =190)
        self.phone_number_label.place(x = 300, y =220)
        self.phone_number_label_value.place(x = 545, y =220)
        self.account_number_label.place(x = 300, y =250)
        self.account_number_label_value.place(x = 545, y =250)
        self.date_label.place(x = 300, y =280)
        self.date_label_value.place(x = 545, y =280)
        self.time_created_label.place(x = 300, y =310)
        self.time_created_label_value.place(x = 545, y =310)
        self.balanced_label.place(x = 300, y =340)
        self.balanced_label_value.place(x = 545, y =340)
        self.saving_balanced_label.place(x = 300, y =370)
        self.saving_balanced_label_value.place(x = 545, y =370)

        # Disabled all entries :
        self.setAllWidgetsDisabled()
    def setAllWidgetsDisabled(self):
        """
            Function to disabled the entries :
        """
        self.account_login_type_label.config(state = DISABLED)
        self.account_login_type_label_value.config(state = DISABLED)
        self.account_id_label.config(state = DISABLED)
        self.account_id_label_value.config(state = DISABLED)
        self.account_name_label.config(state = DISABLED)
        self.account_name_label_value.config(state = DISABLED)
        self.address_label.config(state = DISABLED)
        self.address_label_value.config(state = DISABLED)
        self.phone_number_label.config(state = DISABLED)
        self.phone_number_label_value.config(state = DISABLED)
        self.account_number_label.config(state = DISABLED)
        self.account_number_label_value.config(state = DISABLED)
        self.date_label.config(state = DISABLED)
        self.date_label_value.config(state = DISABLED)
        self.time_created_label.config(state = DISABLED)
        self.time_created_label_value.config(state = DISABLED)
        self.balanced_label.config(state = DISABLED)
        self.balanced_label_value.config(state = DISABLED)
        self.saving_balanced_label.config(state = DISABLED)
        self.saving_balanced_label_value.config(state = DISABLED)

    def clearAllInsideFrame(self):
        """
            Function to clear out all widgets inside a frame
        """
        # Iterate through every widget inside the frame and delete it
        for widget in self.frame.winfo_children():
            widget.destroy()  # Safely destroy each widget