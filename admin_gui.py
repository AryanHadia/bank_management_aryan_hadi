'''
.dashbord taghriban camel shode lotfan barresi konid bebinid khobe (user=admin , pass=1234)

.bishtare tamarkozam ro gozashtam ro zaher barname ke khob dar biyad masalan az icon estefade mikonam va mikham ui/ux khobi dashte bashe
shoma ham age pishnhadi darid mamnon misham benevisid baram

.toye vasl kardane link kardane in file ha be ham yekam moshkel daram ye tozih midid ?
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
        self.bank_icon = ImageTk.PhotoImage(Image.open("assets/icons8-bank-96 (1).png").resize((55,55)))
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

    def login(self):
        self.username = self.entry_username.get()
        password = self.entry_password.get()
        if self.username == "" or password == "":
            messagebox.showerror("Error", "Please enter username and password")
            return
        if self.username == "admin" and password == "1234":
            self.login_frame.destroy()
            self.dashboard()
        else:
            messagebox.showerror("Error", "Invalid username or password")

    def login_window(self):
        self.login_frame = Toplevel(self.root)
        self.login_frame.title("Login")
        self.login_frame.geometry("300x200")
        self.login_frame.configure(bg="#1E1E2F")
        self.login_frame.resizable(False,False)
        self.entry_username = Entry(self.login_frame, font=("Arial", 14), bg="#1E1E2F", fg="white")
        self.entry_username.place(x=30 , y=50)
        self.entry_password = Entry(self.login_frame, font=("Arial", 14), bg="#1E1E2F", fg="white")
        self.entry_password.place(x=30 , y=100)
        self.login_button = Button(self.login_frame, text="Login", font=("Arial", 14), bg="#1E1E2F", fg="white", command=self.login)
        self.login_button.place(x=100 , y=150)

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
        self.name_entry.insert(0, self.username)
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
        Label(self.add_account_window, text="Initial Balance:", font=("Arial", 14), bg="#1E1E2F", fg="white").place(x=30, y=80)
        self.initial_balance_entry = Entry(self.add_account_window, font=("Arial", 14), bg="#1E1E2F", fg="white")
        self.initial_balance_entry.place(x=150, y=80)
        Button(self.add_account_window, text="Add Account", font=("Arial", 14), bg="#838b8b", fg="white", command=self.add_account_confirm).place(x=150, y=150)
        Label(self.add_account_window, text="Account pin:", font=("Arial", 14), bg="#1E1E2F", fg="white").place(x=30, y=120)
        self.account_pin_entry = Entry(self.add_account_window, font=("Arial", 14), bg="#1E1E2F", fg="white")
        self.account_pin_entry.place(x=150, y=120)
    
    def add_account_confirm(self):
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
        


    def remove_account(self):
        self.remove_account_window = Toplevel(self.root)
        self.remove_account_window.title("Remove Account")
        self.remove_account_window.geometry("400x200")
        self.remove_account_window.configure(bg="#1E1E2F")
        self.remove_account_window.resizable(False, False)

    def dashboard(self): # dashboard page
        # page design
        self.wellcome_label.destroy()
        self.main_login_button.destroy()
        self.header_label = Label(self.root, text="Bank manager", font=("Arial", 20), bg="#1E1E2F", fg="white")
        self.header_label.place(x=75 , y=10)
        self.user_icon = Label(self.root, image=self.user_default_icon, bg="#6e6e6e")
        self.user_icon.place(x=30 , y=80)
        self.user_name = Label(self.root, text=self.username, font=("Arial", 14), bg="#1E1E2F", fg="white")
        self.user_name.place(x=20 , y=200)
        self.profile_edit_button = Button(self.root, text="Edit Profile", font=("Arial", 11), bg="#1E1E2F", fg="white" , command=self.edit_profile)
        self.profile_edit_button.place(x=64 , y=559)
        self.logout_button = Button(self.root, image=self.logout_icon, font=("Arial", 14), bg="#8b2500", fg="white" , command=self.logout)
        self.logout_button.place(x=10 , y=545)
        self.bank_icon_label = Label(self.root, image=self.bank_icon, bg="#1E1E2F")
        self.bank_icon_label.place(x=10 , y=5)
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
        self.customer_management_button = Button(self.root, text="Customer Management", font=("Arial", 12), bg="#1E1E2F", fg="white")
        self.customer_management_button.place(x=800 , y=30)


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

# running just for test
page = admin_gui()
page.mouse_confiqure()
page.icons()
page.wellcome_page()
page.run()
