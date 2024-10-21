# import Files :
from tkinter import *
from GUI import BankSystem

# check if the file is run or the file is imported in another file :
if __name__ == '__main__':
    # Creat Page From the tkinter :
    main_page = Tk()

    # Create Object Frome the Bank :
    my_bank = BankSystem(main_page)

    # Run the Bank App :
    my_bank.runApp()