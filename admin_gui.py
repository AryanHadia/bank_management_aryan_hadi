'''
. khaste nabashid in file edit shode akhare ke ye seri mavader taghir kardan
1- bakhsh management admin ha dare ezafe mishe 
2- bakhsh management customer ha ezafe shode
3- baksh login admin ha dare taghir mikone va be database vasl mishe
4- toye zaher tkinter ye seri taghirat sorat gerefte
5- ye moudel tarahi kardam baraye generate kardane shomare kart

. ye seri bakhsh ha hanoz kamel nashodan baraye mesal bakhshe transaction ha hanoz code nevisi nashode

. icon hayi ke estefade kardam ro ferestadam baraton

!!! dar hale hazer karam gir karede :
    moshkel ine ke be code haye bakhsh Data_base dorost kar nemkone va be data base vasn nemishe
    va error   (line 360, in _open_connection
    raise get_mysql_exception(
    sqlalchemy.exc.ProgrammingError: (mysql.connector.errors.ProgrammingError) 1049 (42000): Unknown database 'bank_management')
    ro mide har kari mikonam dorost nemishe nmidonam chera .
    shaki ham nadaram ke hame etelatesh doroste
'''


# admin gui (tkinter)
from tkinter import *
from tkinter import ttk , messagebox
from turtle import width
from PIL import Image, ImageTk
from datetime import datetime
from core import admin_panel

class admin_gui:
    def __init__(self): # making main page
        self.root = Tk()
        self.root.title("Bank Managment System") # title of page
        self.root.geometry("1000x600") # page size
        self.root.configure(bg="#1E1E2F") # background color
        self.root.resizable(False,False) # not resizable

    
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

    
    def wellcome_page(self):
        self.wellcome_label = Label(self.root, text="Welcome to ........... Managment System", font=("Arial", 20), bg="#1E1E2F", fg="white")
        self.wellcome_label.place(x=285 , y=200)
        self.main_login_button = Button(self.root, text="Login", font=("Arial", 14), bg="#1E1E2F", fg="white", command=self.login_window , width=10)
        self.main_login_button.place(x=455 , y=300)
        self.bank_icon_label = Label(self.root, image=self.wellcome_page_bank_icon, bg="#1E1E2F")
        self.bank_icon_label.place(x=433 , y=163)

    
    def mouse_confiqure(self):
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

    
    def run(self):
        self.root.mainloop()

        

    def login_confirm(self):
        self.username_login = self.username_entry.get().strip()
        self.password_login = self.password_entry.get().strip()
        if not self.username_login or not self.password_login:
            messagebox.showerror("Error", "Please enter both username and password")
            return
        if self.username_login == "admin" and self.password_login == "1234":
            self.login_window.destroy()
            self.dashboard()
        else:
            messagebox.showerror("Error", "Invalid username or password")



    def login_window(self):
        self.login_window = Toplevel(self.root)
        self.login_window.title("Admin Login")
        self.login_window.geometry("400x200")
        self.login_window.configure(bg="#1E1E2F")
        self.login_window.resizable(False, False)
        Label(self.login_window, text="Username:", font=("Arial", 14), bg="#1E1E2F", fg="white").place(x=10, y=30)
        self.username_entry = Entry(self.login_window, font=("Arial", 14), bg="#1E1E2F", fg="white")
        self.username_entry.place(x=120, y=30)
        Label(self.login_window, text="Password:", font=("Arial", 14), bg="#1E1E2F", fg="white").place(x=10, y=70)
        self.password_entry = Entry(self.login_window, font=("Arial", 14), bg="#1E1E2F", fg="white", show="*")
        self.password_entry.place(x=120, y=70)
        self.login_button = Button(self.login_window, text="Login", font=("Arial", 14), bg="#1E1E2F", fg="white",
               command=self.login_confirm)
        self.login_button.place(x=192, y=120)



    def edit_profile_confirm(self):
        new_name = self.name_entry.get().strip()
        if not new_name:
            messagebox.showerror("Error", "Please enter a username")
            return
        if len(new_name) > 8:
            messagebox.showerror("Error", "Username is too long (max 8 characters)")
            return
        self.username = new_name
        self.user_name.config(text=self.username)
        self.edit_profile_window.destroy()



    def edit_profile(self):
        self.edit_profile_window = Toplevel(self.root)
        self.edit_profile_window.title("Edit Profile")
        self.edit_profile_window.geometry("400x200")
        self.edit_profile_window.configure(bg="#1E1E2F")
        self.edit_profile_window.resizable(False, False)

        Label(self.edit_profile_window, text="Name:", font=("Arial", 14), bg="#1E1E2F", fg="white").place(x=30, y=30)
        self.name_entry = Entry(self.edit_profile_window, font=("Arial", 14), bg="#1E1E2F", fg="white")
        self.name_entry.insert(0, self.username_login)
        self.name_entry.place(x=100, y=30)

        Button(self.edit_profile_window, text="Confirm", font=("Arial", 14), bg="#1E1E2F", fg="white",
               command=self.edit_profile_confirm).place(x=100, y=100)
        # next fetures
        '''
        photo labels for admin photo
        '''



    def logout(self): # logout button
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
        self.add_account_window = Toplevel(self.root)
        self.add_account_window.title("Add Account")
        self.add_account_window.geometry("400x300")
        self.add_account_window.configure(bg="#1E1E2F")
        self.add_account_window.resizable(False, False)
        Label(self.add_account_window, text="customer Id:", font=("Arial", 14), bg="#1E1E2F", fg="white").place(x=30, y=30)
        self.customer_id_entry = Entry(self.add_account_window, font=("Arial", 14), bg="#1E1E2F", fg="white")
        self.customer_id_entry.place(x=150, y=30)
        Label(self.add_account_window, text="Initial Balance:", font=("Arial", 14), bg="#1E1E2F", fg="white").place(x=30, y=80)
        self.initial_balance_entry = Entry(self.add_account_window, font=("Arial", 14), bg="#1E1E2F", fg="white")
        self.initial_balance_entry.place(x=150, y=80)
        Button(self.add_account_window, text="Add Account", font=("Arial", 14), bg="#838b8b", fg="white", command=self.add_account_confirm).place(x=150, y=150)
        Label(self.add_account_window, text="Account pin:", font=("Arial", 14), bg="#1E1E2F", fg="white").place(x=30, y=120)
        self.account_pin_entry = Entry(self.add_account_window, font=("Arial", 14), bg="#1E1E2F", fg="white")
        self.account_pin_entry.place(x=150, y=120)



    def add_account_confirm(self):
        customer_id = self.customer_id_entry.get().strip()
        if not customer_id:
            messagebox.showerror("Error", "Please enter a customer ID")
            return
        account_number = admin_panel().make_account_number()
        initial_balance = self.initial_balance_entry.get().strip()
        if not initial_balance:
            messagebox.showerror("Error", "Please enter an initial balance")
            return
        try:
            initial_balance = float(initial_balance)
        except ValueError:
            messagebox.showerror("Error", "Initial balance must be a number")
            return
        self.add_account_window.destroy()
        if account_number:
            messagebox.showinfo("Success", f"Account added successfully with number: {account_number}")
        else:
            messagebox.showerror("Error", "Failed to generate account number. Please try again.")
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
        


    def remove_account(self):
        self.remove_account_window = Toplevel(self.root)
        self.remove_account_window.title("Remove Account")
        self.remove_account_window.geometry("400x200")
        self.remove_account_window.configure(bg="#1E1E2F")
        self.remove_account_window.resizable(False, False)


    def customer_managment(self):
        self.customer_managment_window_ = Toplevel(self.root)
        self.customer_managment_window_.title("Customer Managment")
        self.customer_managment_window_.geometry("300x200")
        self.customer_managment_window_.configure(bg="#1E1E2F")
        self.customer_managment_window_.resizable(False, False)

        # customer add/remove button
        self.add_customer_button = Button(self.customer_managment_window_, text="Add Customer", font=("Arial", 14), bg="#838b8b", fg="white", command=self.add_customer)
        self.add_customer_button.place(x=50, y=45)
        self.remove_customer_button = Button(self.customer_managment_window_, text="Remove Customer", font=("Arial", 14), bg="#838b8b", fg="white", command=self.remove_customer)
        self.remove_customer_button.place(x=50, y=100)

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
        Label(self.remove_customer_window, text="Customer Name:", font=("Arial", 14), bg="#1E1E2F", fg="white").place(x=30, y=30)
        self.remove_name_entry = Entry(self.remove_customer_window, font=("Arial", 14), bg="#1E1E2F", fg="white")
        self.remove_name_entry.place(x=150, y=30)
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



    def dashboard(self): # dashboard page
        # page design
        self.wellcome_label.destroy()
        self.main_login_button.destroy()
        self.header_label = Label(self.root, text="Bank manager", font=("Arial", 20), bg="#1E1E2F", fg="white")
        self.header_label.place(x=72 , y=27)
        self.user_icon = Label(self.root, image=self.user_default_icon, bg="#6e6e6e")
        self.user_icon.place(x=26 , y=80)
        self.user_name = Label(self.root, text=self.username_login, font=("Arial", 14), bg="#1E1E2F", fg="white")
        self.user_name.place(x=23 , y=200)
        self.profile_edit_button = Button(self.root, text="Edit Profile", font=("Arial", 11), bg="#1E1E2F", fg="white" , command=self.edit_profile)
        self.profile_edit_button.place(x=64 , y=559)
        self.logout_button = Button(self.root, image=self.logout_icon, font=("Arial", 14), bg="#8b2500", fg="white" , command=self.logout)
        self.logout_button.place(x=10 , y=545)
        self.bank_icon_label = Label(self.root, image=self.bank_icon, bg="#1E1E2F")
        self.bank_icon_label.place(x=10 , y=10)
        self.transactions_button = Button(self.root, text="Transactions", font=("Arial", 13), bg="#838b8b", fg="white")
        self.transactions_button.place(x=840 , y=420)
        self.transactions_button_icon = Label(self.root, image=self.transaction_icon, bg="#1E1E2F")
        self.transactions_button_icon.place(x=810 , y=420)
        self.add_account_button = Button(self.root, text="Add Account", font=("Arial", 13), bg="#838b8b", fg="white", command=self.add_account)
        self.add_account_button.place(x=840 , y=470)
        self.add_account_button_icon = Label(self.root, image=self.add_account_icon, bg="#1E1E2F")
        self.add_account_button_icon.place(x=810 , y=470)
        self.remove_account_button = Button(self.root, text="Remove Account", font=("Arial", 13), bg="#838b8b", fg="white")
        self.remove_account_button.place(x=840 , y=520)
        self.remove_account_button_icon = Label(self.root, image=self.remove_account_icon, bg="#1E1E2F")
        self.remove_account_button_icon.place(x=810 , y=520)
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
        self.root.after(1000, self.update_clock)
        
        
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
                                  columns=("ID", "Name", "Balance", "Email"),
                                  show="headings",
                                  height=18,
                                  style="Treeview")
        self.table.heading("ID", text="ID")
        self.table.heading("Name", text="Name")
        self.table.heading("Balance", text="Balance")
        self.table.heading("Email", text="Email")
        self.table.column("ID", width=50)
        self.table.column("Name", width=170)
        self.table.column("Balance", width=170)
        self.table.column("Email", width=250)
        self.table.place(x=155, y=80)
        
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
            '''
            try:
                from admin_managment import admin_login
                admin_login().main_page(self.root)
            except Exception as e:
                messagebox.showerror("Error", str(e))
            '''
# running just for test
page = admin_gui()
page.mouse_confiqure()
page.icons()
page.wellcome_page()
page.run()

