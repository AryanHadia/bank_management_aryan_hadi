# admin gui (tkinter)
from cProfile import label
from tkinter import *
from tkinter import ttk , messagebox
from turtle import width
from PIL import Image, ImageTk
from datetime import datetime
from core import admin_panel

class admin_gui:
    def __init__(self): # making main page
        self.root = Tk() # tkinter main page
        self.root.title("Bank Managment System") # title of page
        self.root.geometry("1000x600") # page size
        self.root.configure(bg="#1E1E2F") # background color
        self.root.resizable(False,False) # not resizable

        """ making main page """



    def icons(self): # addin icons for design
        self.user_default_icon = ImageTk.PhotoImage(Image.open("assets/icons8-user-96.png")) 
        self.logout_icon = ImageTk.PhotoImage(Image.open("assets/icons8-logout-100.png").resize((40,40)))
        self.bank_icon = ImageTk.PhotoImage(Image.open("assets/icons8-bank-96 (1).png").resize((59,59)))
        self.username_icon = ImageTk.PhotoImage(Image.open("assets/icons8-username-100.png").resize((20,20)))
        self.password_icon = ImageTk.PhotoImage(Image.open("assets/icons8-password-100.png").resize((20,20)))
        self.wellcome_page_bank_icon = ImageTk.PhotoImage(Image.open("assets/icons8-bank-100.png"))
        self.transaction_icon = ImageTk.PhotoImage(Image.open("assets/icons8-transaction-64.png").resize((20,20)))
        self.add_account_icon = ImageTk.PhotoImage(Image.open("assets/icons8-add-male-user-64.png").resize((20,20)))
        self.remove_account_icon = ImageTk.PhotoImage(Image.open("assets/icons8-denied-64.png").resize((20,20)))
        self.cutomer_Add_icon = ImageTk.PhotoImage(Image.open("assets/icons8-add-administrator-100.png").resize((90,90)))
        self.cutomer_remove_icon = ImageTk.PhotoImage(Image.open("assets/icons8-remove-64.png").resize((50,50)))
        self.cutomer_edit_icon = ImageTk.PhotoImage(Image.open("assets/icons8-edit-100.png").resize((50,50)))

        """ importing icons for design """



    def wellcome_page(self):
        self.wellcome_label = Label(self.root, text="Welcome to ........... Managment System", font=("Arial", 20), bg="#1E1E2F", fg="white") # wellcome label
        self.wellcome_label.place(x=285 , y=200)
        self.main_login_button = Button(self.root, text="Login", font=("Arial", 14), bg="#1E1E2F", fg="white", command=self.login_window , width=10) # login page button
        self.main_login_button.place(x=455 , y=300)
        self.bank_icon_label = Label(self.root, image=self.wellcome_page_bank_icon, bg="#1E1E2F") # bank logo
        self.bank_icon_label.place(x=433 , y=163)

        """ first page (login button) """



    def mouse_confiqure(self): # cursor configure
        def enter(event):
            self.root.config(cursor="hand2")
        def leave(event):
            self.root.config(cursor="arrow")

        self.root.bind("<Enter>" , enter)
        self.root.bind("<Leave>" , leave)
        def apply_cursor_to_all_entries(cursor_type="xterm"):
            for widget in self.root.winfo_children():
                if isinstance(widget, tk.Entry):
                    widget.config(cursor=cursor_type)

        apply_cursor_to_all_entries()

        """ confiquring cursor for all entries """



    def run(self):
        self.root.mainloop() # main program running

        

    def login_confirm(self):
        self.username_login = self.username_entry.get().strip() # get username from entry
        self.password_login = self.password_entry.get().strip() # get password from entry
        if not self.username_login or not self.password_login: # check if username or password is empty
            messagebox.showerror("Error", "Please enter both username and password")
            return
        try:
            admin_panel().admin_login(self.username_login, self.password_login) # check login credentials
            self.login_window.destroy() # close login window
            self.dashboard() # go to dashboard
        except Exception as e:
            messagebox.showerror("Error", str(e))

        """ login confirm """



    def login_window(self):
        self.login_window = Toplevel(self.root) # login page (toplevel)
        self.login_window.title("Admin Login")
        self.login_window.geometry("400x200")
        self.login_window.configure(bg="#1E1E2F")
        self.login_window.resizable(False, False)

        # entries and labels
        Label(self.login_window, text="Username:", font=("Arial", 14), bg="#1E1E2F", fg="white").place(x=10, y=30)
        self.username_entry = Entry(self.login_window, font=("Arial", 14), bg="#1E1E2F", fg="white")
        self.username_entry.place(x=120, y=30)
        Label(self.login_window, text="Password:", font=("Arial", 14), bg="#1E1E2F", fg="white").place(x=10, y=70)
        self.password_entry = Entry(self.login_window, font=("Arial", 14), bg="#1E1E2F", fg="white", show="*")
        self.password_entry.place(x=120, y=70)

        # login button
        self.login_button = Button(self.login_window, text="Login", font=("Arial", 14), bg="#1E1E2F", fg="white",
               command=self.login_confirm)
        self.login_button.place(x=192, y=120)



    def logout(self): # logout button
        # stop clock update loop
        try:
            self.root.after_cancel(self.clock_job)
        except:
            pass

        for widget in self.root.winfo_children():
            widget.destroy()
        self.wellcome_page()



    def transactions(self):
        self.transactions_window = Toplevel(self.root)
        self.transactions_window.title("Transactions")
        self.transactions_window.geometry("800x600")
        self.transactions_window.configure(bg="#1E1E2F")
        self.transactions_window.resizable(False, False)



    def add_account(self):
        # main page
        self.add_account_window = Toplevel(self.root)
        self.add_account_window.title("Add Account")
        self.add_account_window.geometry("400x300")
        self.add_account_window.configure(bg="#1E1E2F")
        self.add_account_window.resizable(False, False)

        # entries and labels
        Label(self.add_account_window, text="Account Type:", font=("Arial", 14), bg="#1E1E2F", fg="white").place(x=30, y=30)
        self.account_type_entry = Entry(self.add_account_window, font=("Arial", 14), bg="#1E1E2F", fg="white")
        self.account_type_entry.place(x=150, y=30)
        Label(self.add_account_window, text="customer Id:", font=("Arial", 14), bg="#1E1E2F", fg="white").place(x=30, y=70)
        self.customer_id_entry = Entry(self.add_account_window, font=("Arial", 14), bg="#1E1E2F", fg="white")
        self.customer_id_entry.place(x=150, y=70)
        Label(self.add_account_window, text="Initial Balance:", font=("Arial", 14), bg="#1E1E2F", fg="white").place(x=30, y=110)
        self.initial_balance_entry = Entry(self.add_account_window, font=("Arial", 14), bg="#1E1E2F", fg="white")
        self.initial_balance_entry.place(x=150, y=110)
        Button(self.add_account_window, text="Add Account", font=("Arial", 14), bg="#838b8b", fg="white", command=self.add_account_confirm).place(x=150, y=200)
        Label(self.add_account_window, text="Account pin:", font=("Arial", 14), bg="#1E1E2F", fg="white").place(x=30, y=160)
        self.account_pin_entry = Entry(self.add_account_window, font=("Arial", 14), bg="#1E1E2F", fg="white")
        self.account_pin_entry.place(x=150, y=160)



    def add_account_confirm(self):
        # cutomer id
        customer_id = self.customer_id_entry.get().strip()
        if not customer_id:
            messagebox.showerror("Error", "Please enter a customer ID")
            return

        # initial balance
        initial_balance = self.initial_balance_entry.get().strip()
        if not initial_balance:
            messagebox.showerror("Error", "Please enter an initial balance")
            return
        try:
            initial_balance = float(initial_balance)
        except ValueError:
            messagebox.showerror("Error", "Initial balance must be a number")
            return

        # 4 digit account pin
        account_pin = self.account_pin_entry.get().strip()
        if not account_pin:
            messagebox.showerror("Error", "Please enter an account pin")
            return
        if len(account_pin) != 4:
            messagebox.showerror("Error", "Account pin must be 4 digits")
            return
        try:
            int(account_pin)
        except ValueError:
            messagebox.showerror("Error", "Account pin must be a number")
            return

        # account type
        account_type = self.account_type_entry.get().strip()
        if not account_type:
            messagebox.showerror("Error", "Please enter an account type")
            return

        # account number
        account_number = admin_panel().make_account_number()

        # final add account
        admin_panel().create_account(customer_id, account_number, account_type, initial_balance, account_pin)
        messagebox.showinfo("Success", f"Account added successfully\nAccount Number: {account_number}")

        self.add_account_window.destroy()
        


    def remove_account_confirm(self):
        account_id = self.remove_account_entry.get().strip()
        if not account_id:
            messagebox.showerror("Error", "Please enter an account ID")
            return
        try:
            int(account_id)
        except ValueError:
            messagebox.showerror("Error", "Account ID must be a number")
            return
        admin_panel().delete_account(account_id)
        messagebox.showinfo("Success", f"Account {account_id} removed successfully")
        self.remove_account_window.destroy()



    def remove_account(self):
        self.remove_account_window = Toplevel(self.root)
        self.remove_account_window.title("Remove Account")
        self.remove_account_window.geometry("400x200")
        self.remove_account_window.configure(bg="#1E1E2F")
        self.remove_account_window.resizable(False, False)
        # account number
        Label(self.remove_account_window, text="Account Id:", font=("Arial", 14), bg="#1E1E2F", fg="white").place(x=30, y=30)
        self.remove_account_entry = Entry(self.remove_account_window, font=("Arial", 14), bg="#1E1E2F", fg="white")
        self.remove_account_entry.place(x=150, y=30)
        Button(self.remove_account_window, text="Remove Account", font=("Arial", 14), bg="#838b8b", fg="white", command=self.remove_account_confirm).place(x=150, y=100)



    def customer_managment(self):
        self.customer_managment_window_ = Toplevel(self.root)
        self.customer_managment_window_.title("Customer Managment")
        self.customer_managment_window_.geometry("300x200")
        self.customer_managment_window_.configure(bg="#1E1E2F")
        self.customer_managment_window_.resizable(False, False)

        # cutomer page design
        Label(self.customer_managment_window_, text="Customer Managment", font=("Arial", 11), bg="#1E1E2F", fg="white").place(x=138, y=5)

        # customer add/remove button
        self.cutomer_edit_button = Button(self.customer_managment_window_,bg="#1e1e2f", bd=False , image=self.cutomer_edit_icon , font=("Arial", 14), fg="white", command=self.edit_customer)
        self.cutomer_edit_button.place(x=160, y=140)
        self.add_customer_button = Button(self.customer_managment_window_,bg="#1e1e2f", bd=False , image=self.cutomer_Add_icon , font=("Arial", 14), fg="white", command=self.add_customer)
        self.add_customer_button.place(x=30, y=107)
        self.remove_customer_button = Button(self.customer_managment_window_,bg="#1e1e2f", bd=False , image=self.cutomer_remove_icon , font=("Arial", 14), fg="white", command=self.remove_customer)
        self.remove_customer_button.place(x=240, y=140)



    def edit_customer_confirm(self):
        customer_id = self.id_entry.get().strip()
        if not customer_id:
            messagebox.showerror("Error", "Please enter a customer ID")
            return
        name = self.name_entry.get().strip()
        if not name:
            messagebox.showerror("Error", "Please enter a name")
            return
        email = self.email_entry.get().strip()
        if not email:
            messagebox.showerror("Error", "Please enter an email")
            return
        age = self.age_entry.get().strip()
        if not age:
            messagebox.showerror("Error", "Please enter an age")
            return
        try:
            age = int(age)
        except ValueError:
            messagebox.showerror("Error", "Age must be a number")
            return
        phone_number = self.phone_entry.get().strip()
        if not phone_number:
            messagebox.showerror("Error", "Please enter a phone number")
            return
        address = self.address_entry.get().strip()
        if not address:
            messagebox.showerror("Error", "Please enter an address")
            return
        admin_panel().cutomer_edit(customer_id, name, email, age , phone_number , address)
        messagebox.showinfo("Success", "Customer updated successfully")
        self.edit_customer_window.destroy()



    def edit_customer(self):
        self.edit_customer_window = Toplevel(self.customer_managment_window_)
        self.edit_customer_window.title("Edit Customer")
        self.edit_customer_window.geometry("400x300")
        self.edit_customer_window.configure(bg="#1E1E2F")
        self.edit_customer_window.resizable(False, False)
        self.id_entry = Entry(self.edit_customer_window, font=("Arial", 14), bg="#1E1E2F", fg="white")
        self.id_entry.place(x=150, y=20)
        self.name_entry = Entry(self.edit_customer_window, font=("Arial", 14), bg="#1E1E2F", fg="white")
        self.name_entry.place(x=150, y=60)
        self.age_entry = Entry(self.edit_customer_window, font=("Arial", 14), bg="#1E1E2F", fg="white")
        self.age_entry.place(x=150, y=100)
        self.email_entry = Entry(self.edit_customer_window, font=("Arial", 14), bg="#1E1E2F", fg="white")
        self.email_entry.place(x=150, y=140)
        self.phone_entry = Entry(self.edit_customer_window, font=("Arial", 14), bg="#1E1E2F", fg="white")
        self.phone_entry.place(x=150, y=180)
        self.address_entry = Entry(self.edit_customer_window, font=("Arial", 14), bg="#1E1E2F", fg="white")
        self.address_entry.place(x=150, y=220)
        self.edit_button = Button(self.edit_customer_window, text="Edit Customer", font=("Arial", 12), bg="#838b8b", fg="white", command=self.edit_customer_confirm)
        self.edit_button.place(x=150, y=260)
        self.id_label = Label(self.edit_customer_window, text="ID:", font=("Arial", 14), bg="#1E1E2F", fg="white")
        self.id_label.place(x=30, y=20)
        self.name_label = Label(self.edit_customer_window, text="Name:", font=("Arial", 14), bg="#1E1E2F", fg="white")
        self.name_label.place(x=30, y=60)
        self.age_label = Label(self.edit_customer_window, text="Age:", font=("Arial", 14), bg="#1E1E2F", fg="white")
        self.age_label.place(x=30, y=100)
        self.email_label = Label(self.edit_customer_window, text="Email:", font=("Arial", 14), bg="#1E1E2F", fg="white")
        self.email_label.place(x=30, y=140)
        self.phone_label = Label(self.edit_customer_window, text="Phone:", font=("Arial", 14), bg="#1E1E2F", fg="white")
        self.phone_label.place(x=30, y=180)
        self.address_label = Label(self.edit_customer_window, text="Address:", font=("Arial", 14), bg="#1E1E2F", fg="white")
        self.address_label.place(x=30, y=220)
    
    

    def add_customer(self):
        self.add_customer_window = Toplevel(self.customer_managment_window_)
        self.add_customer_window.title("Add Customer")
        self.add_customer_window.geometry("400x300")
        self.add_customer_window.configure(bg="#1E1E2F")
        self.add_customer_window.resizable(False, False)
        Label(self.add_customer_window, text="Name:", font=("Arial", 14), bg="#1E1E2F", fg="white").place(x=30, y=30)
        self.name_entry = Entry(self.add_customer_window, font=("Arial", 14), bg="#1E1E2F", fg="white")
        self.name_entry.place(x=115, y=30)
        Label(self.add_customer_window, text="Phone:", font=("Arial", 14), bg="#1E1E2F", fg="white").place(x=30, y=70)
        self.phone_entry = Entry(self.add_customer_window, font=("Arial", 14), bg="#1E1E2F", fg="white")
        self.phone_entry.place(x=115, y=70)
        Label(self.add_customer_window, text="Email:", font=("Arial", 14), bg="#1E1E2F", fg="white").place(x=30, y=110)
        self.email_entry = Entry(self.add_customer_window, font=("Arial", 14), bg="#1E1E2F", fg="white")
        self.email_entry.place(x=115, y=110)
        Label(self.add_customer_window, text="Address:", font=("Arial", 14), bg="#1E1E2F", fg="white").place(x=30, y=150)
        self.address_entry = Entry(self.add_customer_window, font=("Arial", 14), bg="#1E1E2F", fg="white")
        self.address_entry.place(x=115, y=150)
        Label(self.add_customer_window, text="Age:", font=("Arial", 14), bg="#1E1E2F", fg="white").place(x=30, y=190)
        self.age_entry = Entry(self.add_customer_window, font=("Arial", 14), bg="#1E1E2F", fg="white")
        self.age_entry.place(x=115, y=190)
        Button(self.add_customer_window, text="Add Customer", font=("Arial", 14), bg="#838b8b", fg="white", command=self.add_customer_confirm).place(x=150, y=255)
    


    def add_customer_confirm(self): # adding customer to database
        name = self.name_entry.get().strip() # getting name from entry
        email = self.email_entry.get().strip()
        age = self.age_entry.get().strip()
        phone = self.phone_entry.get().strip()
        address = self.address_entry.get().strip()

        if not name:
            messagebox.showerror("Error", "Please enter a name")
            return
        customer_add = admin_panel().create_customer(name, email, age, phone, address)
        if customer_add:
            messagebox.showinfo("Success", f"Customer added successfully with name: {name}")
            self.add_customer_window.destroy()
            self.customer_managment_window_.destroy()
        else:
            messagebox.showerror("Error", "Failed to add customer. Please try again.")
        """ adding customer to database """
    

    # remove customer
    def remove_customer(self):
        self.remove_customer_window = Toplevel(self.customer_managment_window_)
        self.remove_customer_window.title("Remove Customer")
        self.remove_customer_window.geometry("400x200")
        self.remove_customer_window.configure(bg="#1E1E2F")
        self.remove_customer_window.resizable(False, False)
        Label(self.remove_customer_window, text="Customer Name:", font=("Arial", 14), bg="#1E1E2F", fg="white").place(x=10, y=30)
        self.remove_name_entry = Entry(self.remove_customer_window, font=("Arial", 14), bg="#1E1E2F", fg="white")
        self.remove_name_entry.place(x=160, y=30)
        Button(self.remove_customer_window, text="Remove Customer", font=("Arial", 14), bg="#838b8b", fg="white", command=self.remove_customer_confirm).place(x=150, y=100)
    


    def remove_customer_confirm(self):
        name = self.remove_name_entry.get().strip()
        if not name:
            messagebox.showerror("Error", "Please enter a name")
            return
        customer_remove = admin_panel().remove_customer(name)
        if customer_remove:
            messagebox.showinfo("Success", f"Customer removed successfully with name: {name}")
            self.remove_customer_window.destroy()
            self.customer_managment_window_.destroy()
        else:
            messagebox.showerror("Error", "Failed to remove customer. Please try again.")
        """ removing customer from database """



    def transaction_confirm(self): # confirm transaction
        account_from = self.transaction_from_account.get().strip()
        account_to = self.transaction_to_account.get().strip()
        amount = self.amount_entry.get().strip()
        balance = admin_panel().show_balance(account_from)
        try:
            amount = float(amount)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount")
            return
        if amount > balance:
            messagebox.showerror("Error", "Insufficient balance")
        if not account_from or not account_to or not amount:
            messagebox.showerror("Error", "Please fill all fields")
            return
        transaction = admin_panel().transfer(account_from, account_to, amount)
        if  transaction:
            messagebox.showinfo("Success", f"Transaction successful: from {account_from} to {account_to} for amount {amount}")
            self.tc_page.destroy()
        else:
            messagebox.showerror("Error", "Failed to perform transaction. Please try again.")



    def transaction_page(self):
        self.tc_page = Toplevel(self.root)
        self.tc_page.configure(bg="#1E1E2f")
        self.tc_page.geometry("450x300")
        self.tc_page.title("Transaction")
        self.tc_page.resizable(False, False)
        Label(self.tc_page, text="Transaction", font=("Arial", 20), bg="#1E1E2f", fg="white").place(x=150, y=20)
        # first account
        Label(self.tc_page, text="From(id)", font=("Arial", 14), bg="#1E1E2f", fg="white").place(x=30, y=70)
        self.transaction_from_account = Entry(self.tc_page, font=("Arial", 14), bg="#1E1E2F", fg="white")
        self.transaction_from_account.place(x=150, y=70)
        # second account
        Label(self.tc_page, text="To(id)", font=("Arial", 14), bg="#1E1E2f", fg="white").place(x=30, y=110)
        self.transaction_to_account = Entry(self.tc_page, font=("Arial", 14), bg="#1E1E2F", fg="white")
        self.transaction_to_account.place(x=150, y=110)
        # amount
        Label(self.tc_page, text="Amount:", font=("Arial", 14), bg="#1E1E2f", fg="white").place(x=30, y=150)
        self.amount_entry = Entry(self.tc_page, font=("Arial", 14), bg="#1E1E2F", fg="white")
        self.amount_entry.place(x=150, y=150)
        # transaction button
        Button(self.tc_page, text="Transaction", font=("Arial", 14), bg="#838b8b", fg="white", command=self.transaction_confirm).place(x=150, y=190)



    def dashboard(self): # dashboard page
        # page design
        self.wellcome_label.destroy() # closing wellcome page
        self.main_login_button.destroy() # closing wellcome page
        self.bank_icon_label.destroy() # closing wellcome page

        # dashboard design
        self.header_label = Label(self.root, text="Bank manager", font=("Arial", 20), bg="#1E1E2F", fg="white") # just for sesign 
        self.header_label.place(x=72 , y=27)
        self.user_icon = Label(self.root, image=self.user_default_icon, bg="#6e6e6e")
        self.user_icon.place(x=26 , y=80)
        self.user_name = Label(self.root, text=self.username_login, font=("Arial", 14), bg="#1E1E2F", fg="white")
        self.user_name.place(x=23 , y=200)
        self.logout_button = Button(self.root, image=self.logout_icon, font=("Arial", 14), bg="#8b2500", fg="white" , command=self.logout) # logout button
        self.logout_button.place(x=10 , y=545)
        self.bank_icon_label = Label(self.root, image=self.bank_icon, bg="#1E1E2F") # just for design
        self.bank_icon_label.place(x=10 , y=10)
        
        # transaction menu
        self.transactions_button = Button(self.root, text="Transactions", font=("Arial", 13), bg="#838b8b", fg="white", command=self.transaction_page)
        self.transactions_button.place(x=840 , y=420)
        self.transactions_button_icon = Label(self.root, image=self.transaction_icon, bg="#1E1E2F")
        self.transactions_button_icon.place(x=810 , y=420)
        
        # account add/managment
        self.add_account_button = Button(self.root, text="Add Account", font=("Arial", 13), bg="#838b8b", fg="white", command=self.add_account)
        self.add_account_button.place(x=840 , y=470)
        self.add_account_button_icon = Label(self.root, image=self.add_account_icon, bg="#1E1E2F")
        self.add_account_button_icon.place(x=810 , y=470)
      
       # account remove/managment
        self.remove_account_button = Button(self.root, text="Remove Account", font=("Arial", 13), bg="#838b8b", fg="white", command=self.remove_account)
        self.remove_account_button.place(x=840 , y=520)
        self.remove_account_button_icon = Label(self.root, image=self.remove_account_icon, bg="#1E1E2F")
        self.remove_account_button_icon.place(x=810 , y=520)
      
        # management menu
        self.management_choice = StringVar(value="...")
        self.management_menu = OptionMenu(
            self.root,
            self.management_choice,
            "Customer Management",
            "Admin Management",
            command=self.on_management_select,
        )
        self.management_menu.config(bg="#6e6e6e" , activebackground="#6e6e6e" , bd=False)
        self.management_menu.place(x=940, y=20)
        self.design_label = Label(self.root, font=("Arial", 8), bg="#6e6e6e", fg="black",width=300 , bd=5)
        self.design_label.place(x=0 , y=-13)



        # Clock label below remove account button
        self.clock_label = Label(self.root, font=("Arial", 12), bg="#1E1E2F", fg="white")
        self.clock_label.place(x=890, y=570)
        self.update_clock()



    def update_clock(self):
        now = datetime.now().strftime("%H:%M:%S")
        self.clock_label.config(text=now)
        self.clock_job = self.root.after(1000, self.update_clock)
        
        # makin table
        # Configure Treeview style
        self.table_color = ttk.Style()
        self.table_color.theme_use("clam")  # Use a theme that supports color changes
        self.table_color.configure("Treeview",
                                   background="#6e6e6e",
                                   foreground="white",
                                   fieldbackground="#6e6e6e",
                                   rowheight=25)
        self.table_color.map("Treeview", background=[("selected", "#4a4a4a")])

        # Create Treeview with the custom style
        self.table = ttk.Treeview(self.root,
                                  columns=("ID", "Account Number", "Balance", "Account Type"),
                                  show="headings",
                                  height=18,
                                  style="Treeview")
        self.table.heading("ID", text="ID")
        self.table.heading("Account Number", text="Account Number")
        self.table.heading("Balance", text="Balance")
        self.table.heading("Account Type", text="Account Type")
        self.table.column("ID", width=50)
        self.table.column("Account Number", width=180)
        self.table.column("Balance", width=180)
        self.table.column("Account Type", width=225)
        self.table.place(x=155, y=80)
        admin_panel().show_accounts(self.table)
        
        # data table
        def show_data(name, age, customer, balance, email, customer_id):
            self.name = Label(self.root, text=f"name={name}", font=("Arial", 8), bg="#6e6e6e", fg="white")
            self.name.place(x=830, y=110)
            self.age = Label(self.root, text=f"age={age}", font=("Arial", 8), bg="#6e6e6e", fg="white")
            self.age.place(x=830, y=140)
            self.customer = Label(self.root, text=f"customer={customer}", font=("Arial", 8), bg="#6e6e6e", fg="white")
            self.customer.place(x=830, y=170)
            self.balance = Label(self.root, text=f"balance={balance}", font=("Arial", 8), bg="#6e6e6e", fg="white")
            self.balance.place(x=830, y=200)
            self.email = Label(self.root, text=f"email={email}", font=("Arial", 8), bg="#6e6e6e", fg="white")
            self.email.place(x=830, y=230)
            self.customer_id = Label(self.root, text=f"customer_id={customer_id}", font=("Arial", 8), bg="#6e6e6e", fg="white")
            self.customer_id.place(x=830, y=260)



    def on_management_select(self, choice):
        if choice == "Customer Management":
            self.customer_managment()
            self.management_choice.set("...")
        elif choice == "Admin Management":
            self.management_choice.set("...")
            self.admin_data_page()



    def admin_data_page (self):
        # admin data page and configuration
        self.page = Toplevel(self.root)
        self.page.title("Admin Data")
        self.page.geometry("1000x600")
        self.page.resizable(False, False)
        self.page.configure(bg="#1E1E2F")

        # admin show data in the treeview
        self.admin_treeview = ttk.Treeview(
            self.page,
            columns=("ID", "Username","Email" , "Gender"),
            show="headings",
            height=18,
            style="Treeview",) # the treeview
        
        # admin treeview headings
        self.admin_treeview.heading("ID", text="ID")
        self.admin_treeview.heading("Username", text="Username")
        self.admin_treeview.heading("Email", text="Email")
        self.admin_treeview.heading("Gender" , text="Gender")

        # admin treeview columns
        self.admin_treeview.column("ID", width=50)
        self.admin_treeview.column("Username", width=170)
        self.admin_treeview.column("Email", width=250)
        self.admin_treeview.column("Gender" , width=100)
        self.admin_treeview.place(x=30, y=50, width=700, height=520)

        admin_panel().show_admin_data(self.admin_treeview)

        # scrollbar for the admin treeview
        self.scrollbar = ttk.Scrollbar(self.page, orient="vertical", command=self.admin_treeview.yview) # the scrollbar
        self.scrollbar.place(x=710, y=80, height=460)
        self.admin_treeview.configure(yscrollcommand=self.scrollbar.set)

        # admin remove
        self.delete_button = Button(self.page, text="Delete", command=self.delete_admin, bg="#4a4a4a", fg="white")
        self.delete_button.place(x=410, y=500) 

        # admin update
        self.update_button = Button(self.page, text="Update", command=self.update_admin, bg="#4a4a4a", fg="white")
        self.update_button.place(x=330, y=500)
        
        # admin add
        self.add_button = Button(self.page, text="Add", command=self.add_admin, bg="#4a4a4a", fg="white")
        self.add_button.place(x=260, y=500)

        def admin_data_show(self): # showing data in the admin info widgets
            selection = self.admin_treeview.selection()
            if not selection:
                return None
            selected_item = selection[0]
            values = self.admin_treeview.item(selected_item, "values")
            admin = admin_panel().show_admin_data_once(values[0])
            if not admin:
                return None
            for widget in getattr(self, "admin_info_widgets", []):
                widget.destroy()
            labels = []

            # admin name 
            name_admin = Label(self.page, text="Admin Name:", font=("Arial", 10),
                            bg="#6e6e6e", fg="white") # name label
            name_admin.place(x=730, y=100)
            labels.append(name_admin)
            name_admin_value = Label(self.page, text=admin.username, font=("Arial", 10),
                                    bg="#6e6e6e", fg="white") # name value
            name_admin_value.place(x=830, y=100)
            labels.append(name_admin_value) # adding to labels

            # admin email
            email_admin = Label(self.page, text="Admin Email:", font=("Arial", 10),
                            bg="#6e6e6e", fg="white") # email label
            email_admin.place(x=730, y=150)
            labels.append(email_admin)
            email_admin_value = Label(self.page, text=admin.email, font=("Arial", 10),
                                    bg="#6e6e6e", fg="white") # email value
            email_admin_value.place(x=830, y=150)
            labels.append(email_admin_value)

            # admin gender
            gender_admin = Label(self.page, text="Admin Gender:", font=("Arial", 10),
                            bg="#6e6e6e", fg="white") # gender label    
            gender_admin.place(x=730, y=200)
            labels.append(gender_admin)
            gender_admin_value = Label(self.page, text=admin.gender, font=("Arial", 10),
                                    bg="#6e6e6e", fg="white") # gender value
            gender_admin_value.place(x=830, y=200)
            labels.append(gender_admin_value) # adding to labels

            # admin region
            region_admin = Label(self.page, text="Admin Region:", font=("Arial", 10),
                            bg="#6e6e6e", fg="white") # region label
            region_admin.place(x=730, y=250)
            labels.append(region_admin) 
            region_admin_value = Label(self.page, text=admin.region, font=("Arial", 10),
                                    bg="#6e6e6e", fg="white") # region value
            region_admin_value.place(x=830, y=250)
            labels.append(region_admin_value) # adding to labels    
            
            self.admin_info_widgets = labels
            print(values)
            return labels

            """ showing the admin data in the admin info widgets """
        
        self.admin_treeview.bind("<<TreeviewSelect>>", lambda e: admin_data_show(self))

    
    def delete_admin(self):
        selected_item = self.admin_treeview.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Please select an admin to delete.")
            return
        values = self.admin_treeview.item(selected_item, "values")
        username = values[1]
        admin_panel().remove_admin(username)
        self.admin_treeview.delete(selected_item)
        messagebox.showinfo("Success", "Admin deleted successfully.")



    def update_admin(self):
        def update_admin_button(value):
            username = self.update_username_entry.get()
            email = self.update_email_entry.get()
            gender = self.update_gender_entry.get()
            admin_panel().update_admin(admin_id=value[0], username=username, email=email, gender=gender)
            messagebox.showinfo("Success", "Admin updated successfully.")
            self.update_page.destroy()
        
        def update_page(self , value):
            # update page design
            self.update_page = Toplevel(self.root)
            self.update_page.title("Update Admin")
            self.update_page.geometry("400x200")
            self.update_page.resizable(False, False)
            self.update_page.configure(bg="#1E1E2F")
            self.update_username = Label(self.update_page, text="Username:", font=("Arial", 10), bg="#1E1E2F", fg="white")
            self.update_username.place(x=30, y=30)
            self.update_username_entry = Entry(self.update_page,textvariable=value[1] ,font=("Arial", 10), bg="#333333", fg="white")
            self.update_username_entry.place(x=100, y=30)
            self.update_email = Label(self.update_page, text="Email", font=("Arial", 10), bg="#1E1E2F", fg="white")
            self.update_email.place(x=30, y=70)
            self.update_email_entry = Entry(self.update_page,textvariable=value[2] ,font=("Arial", 10), bg="#333333", fg="white")
            self.update_email_entry.place(x=100, y=70)
            self.update_gender = Label(self.update_page, text="Gender:", font=("Arial", 10), bg="#1E1E2F", fg="white")
            self.update_gender.place(x=30, y=110)
            self.update_gender_entry = Entry(self.update_page,textvariable=value[3] ,font=("Arial", 10), bg="#333333", fg="white")
            self.update_gender_entry.place(x=100, y=110)
            self.update_button = Button(self.update_page , text="Update", command=lambda: update_admin_button(value), bg="#4a4a4a", fg="white")
            self.update_button.place(x=260, y=150)

        selected_item = self.admin_treeview.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Please select an admin to update.")
            return
        values = self.admin_treeview.item(selected_item, "values")
        update_page(self , value=values)
    
    
    
    def add_admin(self):
        self.add_admin_page = Toplevel(self.root)
        self.add_admin_page.title("Add Admin")
        self.add_admin_page.geometry("400x200")
        self.add_admin_page.resizable(False, False)
        self.add_admin_page.configure(bg="#1E1E2F")
        self.add_admin_username = Label(self.add_admin_page, text="Username:", font=("Arial", 10), bg="#1E1E2F", fg="white")
        self.add_admin_username.place(x=30, y=30)
        self.add_admin_username_entry = Entry(self.add_admin_page,font=("Arial", 10), bg="#333333", fg="white")
        self.add_admin_username_entry.place(x=100, y=30)
        self.add_admin_email = Label(self.add_admin_page, text="Email", font=("Arial", 10), bg="#1E1E2F", fg="white")
        self.add_admin_email.place(x=30, y=70)
        self.add_admin_email_entry = Entry(self.add_admin_page,font=("Arial", 10), bg="#333333", fg="white")
        self.add_admin_email_entry.place(x=100, y=70)
        self.add_admin_gender = Label(self.add_admin_page, text="Gender:", font=("Arial", 10), bg="#1E1E2F", fg="white")
        self.add_admin_gender.place(x=30, y=110)
        self.add_admin_gender_entry = Entry(self.add_admin_page,font=("Arial", 10), bg="#333333", fg="white")
        self.add_admin_gender_entry.place(x=100, y=110)
        self.add_admin_password = Label(self.add_admin_page, text="Password:", font=("Arial", 10), bg="#1E1E2F", fg="white")
        self.add_admin_password.place(x=30, y=150)
        self.add_admin_password_entry = Entry(self.add_admin_page,font=("Arial", 10), bg="#333333", fg="white")
        self.add_admin_password_entry.place(x=100, y=150)
        self.add_admin_button = Button(self.add_admin_page , text="Add", command=self.add_admin_button, bg="#4a4a4a", fg="white")
        self.add_admin_button.place(x=260, y=150)



    def add_admin_button(self):
        username = self.add_admin_username_entry.get()
        email = self.add_admin_email_entry.get()
        gender = self.add_admin_gender_entry.get()
        password = self.add_admin_password_entry.get()
        admin_panel().create_admin(ad_username=username, ad_password=password, ad_email=email, ad_gender=gender)
        messagebox.showinfo("Success", "Admin added successfully.")
        admin_panel().show_admin_data_by_name(admin_name=username, table__=self.admin_treeview)
        self.add_admin_page.destroy()



    def admin_data(self):
        self.admin_data_page()


# running just for test
page = admin_gui() 
page.mouse_confiqure()
page.icons()
page.wellcome_page()
page.run()
