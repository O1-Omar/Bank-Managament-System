# import libraries and files : 
from tkinter import *                           # tkinter library for GUI
from tkinter import messagebox                  # import message box for show errors, warning and info                  
from Bank import Bank                           # Bank user Class 
from logInWidgets import LogInPage              # Log in Page As Customer
from logInASTeller import LogInAsTellerPage     # Log in Page As Teller, Manager

# create the main class in Gui :
class BankSystem:
    # Init the class :
    def __init__(self, root : Tk) -> None:
        
        self.root = root                            # set main page of app
        self.root.geometry("850x600")               # set the geometry of app
        self.root.title("Bank Managmenet System")   # set the title of app 
        self.root.iconbitmap("images/bank.ico")     # set icon of app
        
        # Create frame in main app :
        self.log_in_frame = Frame(self.root, width=850, height=600, bg="white")

        # Packing of the frame :
        self.log_in_frame.pack()
        
        # Create and packing log in Page :
        self.addLogInPage()

        # Init the accounts in Bank :
        self.initBank()
        
    def addLogInPage(self):
        """
            Function to show main log in page (buttons, entries) .
        """
        # Set flag to show the password is hide or appearance
        self.is_password_show = False

        # Stor the bank image variable : 
        self.log_img = PhotoImage(file = "images/1.png")

        # Set the log in button image in variable :
        self.bank_logo = PhotoImage(file= "images/2.png")

        # Create Label to store photo in it :
        self.bank_logo_label = Label(self.log_in_frame, image = self.bank_logo, bg="white")

        # Create log in body :
        self.user_name_label = Label(self.log_in_frame, text="Username : ", font=("Arial", 15, "bold"), bg="white")
        
        self.user_name_entry = Entry(self.log_in_frame, width=50)
        
        self.password_label = Label(self.log_in_frame, text="Password : ", font=("Arial", 15, "bold"), bg="white")
        
        self.password_entry = Entry(self.log_in_frame, width=50, show='*') # show = '*' to show entry data like *
        
        # Check button to make the password hide or not :
        self.check_bottun = Checkbutton(self.log_in_frame, text="Show Passsword", command=self.toggelPassword, bg="white")
        
        # Submit button to log in
        self.submit_button = Button(self.log_in_frame, image=self.log_img, bd=0, bg='#ffffff',activebackground='#ffffff', command=self.logIn)
        
        # Grid the Labels and buttons:
        self.bank_logo_label.place(x = 380, y = 140)
        self.user_name_label.place(x = 150, y =300)
        self.user_name_entry.place(x = 280, y =307)
        self.password_label.place(x = 150, y =350)
        self.password_entry.place(x = 280, y =357)
        self.check_bottun.place(x = 590, y =357)
        self.submit_button.place(x = 400, y =400)

    def logIn(self):
        """
            this Function will run when i press on log in button .
        """
        # Get the data from user_name feild :
        user_name = self.user_name_entry.get()

        # Get the data from password feild :
        password = self.password_entry.get()

        # Set flage to check if user found or not after him press log in button :
        is_not_found = True

        # if the user_name and password equal Manager user_name and password :
        if self.bank.managers[1020].account_name == user_name and self.bank.managers[1020].password == password :
            LogInAsTellerPage(self.log_in_frame,  self.addLogInPage, "Manager", self.bank, self.bank.managers[1020]).createWidgetsAsManager()
            is_not_found = False # set is not fond flag false .

        else :
            # Search about account in Customers :
            for account_number in self.bank.Customers:
                if self.bank.Customers[account_number].account_name == user_name and self.bank.Customers[account_number].password == password : 
                    LogInPage(self.log_in_frame,  self.addLogInPage, self.bank, self.bank.Customers[account_number]).createWidgets()
                    is_not_found = False # set is not fond flag false .
                    break

            # Search about account in Tellers :
            for account_number in self.bank.tellers:
                if self.bank.tellers[account_number].account_name == user_name and self.bank.tellers[account_number].password == password : 
                    LogInAsTellerPage(self.log_in_frame, self.addLogInPage, "Teller",self.bank, self.bank.tellers[account_number]).createWidgets()
                    is_not_found = False # set is not fond flag false .
                    break
        
        # if the account is not found raise error message :
        if is_not_found :
            messagebox.showerror("User Info", "User not Found .")

    def initBank(self):
        """
            Function To create the Base Accounts in Bank .
        """

        # Craete Bank Object : 
        self.bank = Bank("CIB", "Egypt, Cairo", "212689")

        # Craete Tellers Objects :
        self.bank.createTeller(1120, "Mohammed", "mohammed_123", "Egypt, Cairo", "01032115654", 1010)
        self.bank.createTeller(1145, "Ahmed", "ahmed_123", "Egypt, Giza", "01032115654", 1030)
        
        # Craete accounts for Teller :
        self.bank.create_teller_account(1010, "checking", 10000)
        self.bank.create_teller_account(1010, "saving", 15000)

        # Account Two :
        self.bank.create_teller_account(1030, "checking", 5000)
        self.bank.create_teller_account(1030, "saving", 20000)

        # Create Customers :
        self.bank.create_customer(359, "Ahmed Ibrahim", "14015016", "Egypt, Mansoura", "01236548985", 1219)
        self.bank.create_customer(409, "Abdo Ibrahim", "522522", "Egypt, Alexandria", "01531048685", 1211)
        
        # Craete accounts for Customer :
        self.bank.create_account(1219, "checking", 5000)
        self.bank.create_account(1219, "saving", 1000)

        # Craete checking account for Customer 2 :
        self.bank.create_account(1211, "checking", 5000)
        
    def toggelPassword(self):
        """
            Function to Toogle is password show or not flag .
        """
        # if the is password appearance and user press on button change to hide 
        if self.is_password_show :
            self.password_entry.config(show = '*')
            self.is_password_show = False
        else:
            self.password_entry.config(show = '')
            self.is_password_show = True

    def runApp(self):
        """
            Function To Run The Main App .
        """
        # run main page (self.root) .
        self.root.mainloop() 

