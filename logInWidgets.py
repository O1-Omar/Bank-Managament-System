from tkinter import *
from tkinter import messagebox
from datetime import datetime

class LogInPage:
    def __init__(self, frame: Frame, logInPage , bank : object, account: object) -> None:
        self.frame = frame
        self.account = account
        self.bank = bank
        self.log_in_func = logInPage
        self.account_login_type = "Customer"

    def createWidgets(self):
        self.createBasicInformation()
        self.createButtons()


    def createButtons(self):
        self.veiw_transaction_button = Button(self.frame, width=30, text="Veiw Transaction Log", command=self.transactionButton, fg="white",font=("Arial", 12, "bold"), background="blue")
        self.veiw_transaction_button.place(x=280, y=420)

        self.withdraw_button = Button(self.frame, width=10, text="Withdraw", command=self.withdrawButton, fg="white", font=("Arial", 12, "bold"), background="#8B0000")
        self.withdraw_button.place(x=160, y=480)

        self.deposite_button = Button(self.frame, width=10, text="Deposite", command=self.depositButton, fg="white", font=("Arial", 12, "bold"), background="green")
        self.deposite_button.place(x=390, y=480)

        self.logout_button = Button(self.frame, width=10, text="Logout", command = self.logout, fg="white", font=("Arial", 12, "bold"), background="red")
        self.logout_button.place(x=620, y=480)

    def transactionButton(self):
        self.transaction_window = Toplevel(self.frame)
        self.transaction_window.geometry("600x450")

        self.transaction_label = Label(self.transaction_window, text="Transaction Log:", font=("Arail", 13, "bold"))
        self.transaction_label.pack(pady=10)

        self.transaction_text_box = Text(self.transaction_window, width=75, height=25)
        self.transaction_text_box.pack()

        for line in self.account.events:
            self.transaction_text_box.insert(END, f"{line}\n")


        self.transaction_window.mainloop()

    def withdrawButton(self):
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

        self.submit_deposit_customer_button = Button(self.withdraw_page, text="Submit Withdraw", bg="green", fg="white", font=("Arial", 10, "bold"), command =lambda : [self.withdrawSubmit(), self.withdraw_page.destroy()])

        self.deposit_account_label.grid(row = 1, column=1)
        self.deposit_account_entry.grid(row = 1, column=2)
        self.deposit_amount_label.grid(row = 2, column=1)
        self.deposit_amount_entry.grid(row = 2, column=2)
        self.withdraw_saving_amount_label.grid(row = 3, column=1)
        self.customer_withdraw_account_type_button.grid(row = 3, column=2)
        self.submit_deposit_customer_button.grid(row=4, column=1, columnspan=20, pady=10)
        self.withdraw_page.mainloop()
        
    def withdrawSubmit(self):
        try:
            account_number = int(self.deposit_account_entry.get())
            amount = int(self.deposit_amount_entry.get())
        except :
            messagebox.showerror("Account Info", "Fields must be filled .")
        is_saving = self.is_withdraw_in_saving_account.get()
        try :
            if self.account.account_number == account_number:
                if amount < self.bank.Customers[self.account.account_number].Accounts['checking'].balance :
                    time = datetime.now().strftime("%I:%M:%S %p")
                    date = datetime.now().strftime("%a %b %Y")
                    if is_saving :
                        self.account.events.append(f"* Withdraw (Saving): -{amount}, New Balance : {self.bank.Customers[self.account.account_number].Accounts['saving'].balance - amount} .\n\t- Date : {date} .\n\t- Time : {time} .\n\tThe process was done by (Customer): {self.account.account_name} .")
                        self.account.withdrawSaving(self.bank, amount)
                        self.saving_balanced_label_value.config(state=NORMAL)
                        self.saving_balanced_label_value.delete(0, END)
                        self.saving_balanced_label_value.insert(0, self.bank.Customers[self.account.account_number].Accounts['saving'].balance)
                        self.saving_balanced_label_value.config(state=DISABLED)
                        messagebox.showinfo("Successful Submit", "Done .")
                    else :
                        self.account.events.append(f"* Withdraw (Checking): -{amount}, New Balance : {self.bank.Customers[self.account.account_number].Accounts['checking'].balance - amount} .\n\t- Date : {date} .\n\t- Time : {time} .\n\tThe process was done by (Customer): {self.account.account_name} .")
                        self.account.withdraw(self.bank, amount)
                        self.checking_balanced_label_value.config(state=NORMAL)
                        self.checking_balanced_label_value.delete(0, END)
                        self.checking_balanced_label_value.insert(0, self.bank.Customers[self.account.account_number].Accounts['checking'].balance)
                        self.checking_balanced_label_value.config(state=DISABLED)
                        messagebox.showinfo("Successful Submit", "Done .")
                else :
                    messagebox.showerror("Error", "Insufficient funds .")
            else :
                messagebox.showerror("Error", "Account Not Found .")
        except:
            messagebox.showerror("Error", "Bank Account Not Found .")
    def depositButton(self):
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

        self.submit_deposit_customer_button = Button(self.deposit_page, text="Submit Despsoit", bg="green", fg="white", font=("Arial", 10, "bold"), command =lambda : [self.depositSubmit(), self.deposit_page.destroy()])

        self.deposit_account_label.grid(row = 1, column=1)
        self.deposit_account_entry.grid(row = 1, column=2)
        self.deposit_amount_label.grid(row = 2, column=1)
        self.deposit_amount_entry.grid(row = 2, column=2)
        self.deposit_saving_amount_label.grid(row = 3, column=1)
        self.customer_account_type_button.grid(row = 3, column=2)
        self.submit_deposit_customer_button.grid(row=4, column=1, columnspan=20, pady=10)
        self.deposit_page.mainloop()


    def depositSubmit(self):
        try:
            account_number = int(self.deposit_account_entry.get())
            amount = int(self.deposit_amount_entry.get())
        except :
            messagebox.showerror("Account Info", "Fields must be filled .")
        is_saving = self.is_deposit_in_saving_account.get()
        try :
            if self.account.account_number == account_number:
                time = datetime.now().strftime("%I:%M:%S %p")
                date = datetime.now().strftime("%a %b %Y")
                if is_saving :
                    self.bank.Customers[account_number].events.append(f"* Diposit (Saving): +{amount}, New Balance : {amount + self.bank.Customers[account_number].Accounts['saving'].balance} .\n\t- Date : {date} .\n\t- Time : {time} .\n\t- The process was done by (Customer): {self.account.account_name} .")
                    self.bank.Customers[account_number].depositSaving(self.bank, amount)
                    self.saving_balanced_label_value.config(state=NORMAL)
                    self.saving_balanced_label_value.delete(0, END)
                    self.saving_balanced_label_value.insert(0, self.bank.Customers[self.account.account_number].Accounts['saving'].balance)
                    self.saving_balanced_label_value.config(state=DISABLED)
                else :
                    self.bank.Customers[account_number].events.append(f"* Diposit (checking): +{amount}, New Balance : {amount + self.bank.Customers[account_number].Accounts['checking'].balance} .\n\t- Date : {date} .\n\t- Time : {time} .\n\t- The process was done by (Customer): {self.account.account_name} .")
                    self.bank.Customers[account_number].deposit(self.bank, amount)
                    self.checking_balanced_label_value.config(state=NORMAL)
                    self.checking_balanced_label_value.delete(0, END)
                    self.checking_balanced_label_value.insert(0, self.bank.Customers[self.account.account_number].Accounts['checking'].balance)
                    self.checking_balanced_label_value.config(state=DISABLED)
                messagebox.showinfo("Successful Submit", "Done .")
            else :
                messagebox.showerror("Error", "Account Not Found .")
        except:
            messagebox.showerror("Error", "Bank Account Not Found .")


    def logout(self):
        self.clearAllInsideFrame()
        self.log_in_func()

    def createBasicInformation(self):
        self.clearAllInsideFrame()  # Clear previous widgets
        self.frame.config(width=850, height=600)
        
        self.bank_photo = PhotoImage(file = "images/bank2.png").subsample(2)
        self.button_photo = Label(self.frame, image=self.bank_photo, bg="white")
        self.bank_information_label = Label(self.frame, text="Bank Management System",width=20, font=('Arial',16,'bold'), bg="white")
        self.account_information_label = Label(self.frame, text="Account Information",width=20, font=('Arial',16,'bold'), bg="white")
        
        self.bank_information_label.place(x = 70, y=25)
        self.button_photo.place(x=5, y=10)

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

        self.checking_balanced_label = Entry(self.frame, width=20, fg='grey',font=('Arial',16,'bold'))
        self.checking_balanced_label_value = Entry(self.frame, width=20, fg='grey',font=('Arial',16,'bold'))

        self.saving_balanced_label = Entry(self.frame, width=20, fg='grey',font=('Arial',16,'bold'))
        self.saving_balanced_label_value = Entry(self.frame, width=20, fg='grey',font=('Arial',16,'bold'))


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
        self.checking_balanced_label.insert(END, "Checking Balanced : ")
        self.saving_balanced_label.insert(END, "Saving Balanced : ")
        try : 
            self.checking_balanced_label_value.insert(END, f"{self.bank.Customers[self.account.account_number].Accounts['checking'].balance}")
        except :
            self.checking_balanced_label_value.insert(END, "Not Found")
        try :
            self.saving_balanced_label_value.insert(END, f"{self.bank.Customers[self.account.account_number].Accounts['saving'].balance}")
        except : 
            self.saving_balanced_label_value.insert(END, "Not Found")
        
        self.account_information_label.place(x = 300, y = 80)
        self.account_login_type_label.place(x = 200, y =110)
        self.account_login_type_label_value.place(x = 445, y =110)
        self.account_id_label.place(x = 200, y =140)
        self.account_id_label_value.place(x = 445, y =140)
        self.account_name_label.place(x = 200, y =170)
        self.account_name_label_value.place(x = 445, y =170)
        self.address_label.place(x = 200, y =200)
        self.address_label_value.place(x = 445, y =200)
        self.phone_number_label.place(x = 200, y =230)
        self.phone_number_label_value.place(x = 445, y =230)
        self.account_number_label.place(x = 200, y =260)
        self.account_number_label_value.place(x = 445, y =260)
        self.date_label.place(x = 200, y =290)
        self.date_label_value.place(x = 445, y =290)
        self.time_created_label.place(x = 200, y =320)
        self.time_created_label_value.place(x = 445, y =320)
        self.checking_balanced_label.place(x = 200, y =350)
        self.checking_balanced_label_value.place(x = 445, y =350)
        self.saving_balanced_label.place(x = 200, y =380)
        self.saving_balanced_label_value.place(x = 445, y =380)

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
        self.checking_balanced_label.config(state = DISABLED)
        self.checking_balanced_label_value.config(state = DISABLED)
        self.saving_balanced_label.config(state = DISABLED)
        self.saving_balanced_label_value.config(state = DISABLED)

    # Function to clear out all widgets inside a frame
    def clearAllInsideFrame(self):
        # Iterate through every widget inside the frame and delete it
        for widget in self.frame.winfo_children():
            widget.destroy()  # Safely destroy each widget