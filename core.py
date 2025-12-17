from models import customer, Account , admin_data
from utils import hash_password, check_password
from data_base import session   
import random

class admin_panel:
    def __init__(self):
        self.session=session

    # cutomer managment

    def create_customer(self, name, email, age , phone_number , address):
        # built a row in database
        new_customer = customer(name=name, email=email, age=age, phone_number=phone_number, address=address)
        self.session.add(new_customer) 
        self.session.commit()
        # printint data
        print(f"Customer {name} created successfully")
        print(f"Customer ID: {new_customer.id}")
        print(f"Customer Email: {new_customer.email}")
        print(f"Customer Age: {new_customer.age}")
        print(f"Customer Phone Number: {new_customer.phone_number}")
        print(f"Customer Address: {new_customer.address}")
        return new_customer
    
    def cutomer_edit(self, customer_id, name, email, age , phone_number , address):
        # check if customer exists
        db_customer = self.session.get(customer, customer_id)
        if not db_customer:
            raise ValueError("Customer not found")
        # update data
        db_customer.name = name
        db_customer.email = email
        db_customer.age = age
        db_customer.phone_number = phone_number
        db_customer.address = address
        self.session.commit()
        print(f"Customer {customer_id} updated successfully")
        print(f"Customer Name: {db_customer.name}")
        print(f"Customer Email: {db_customer.email}")
        print(f"Customer Age: {db_customer.age}")
        print(f"Customer Phone Number: {db_customer.phone_number}")
        print(f"Customer Address: {db_customer.address}")
        return db_customer

    def remove_customer(self, customer_id): # removing a customer and all his accounts
        customerـ=self.session.get(customer, customer_id) # finding cutomer 
        if not customerـ: # if not found :
            raise ValueError("Customer not found")

        # and if found :
        self.delete_customer_accounts(customerـ.id) 
        self.session.delete(customerـ) # delete it
        self.session.commit()
        print(f"Customer {customer_id} deleted successfully")
        return customer


    # account managment
   
    def create_account(self, customer_id, account_number , account_type, account_balance , pin): # creating account in database
        db_customer = self.session.get(customer, customer_id) # finding customer
        if not db_customer: # if not found:
            raise ValueError("Customer not found")

        # and if found
        hashed_pin = hash_password(pin) # hash the pin
        account = Account(customer_id=db_customer.id, account_number=account_number, account_type=account_type, balance=account_balance, pin=hashed_pin)
        self.session.add(account) # add the account to database
        self.session.commit()
        print(f"Account {account_number} created successfully")
        print(f"Account ID: {account.id}")
        print(f"Account Type: {account.account_type}")
        print(f"Account Balance: {account.balance}")
        return account
    

    def show_accounts(self , treeview): # show data in treeview
        accounts = self.session.query(Account).all() # get all accounts
        # for every account in data base create a coulumn and write the data
        for _ in accounts:
            treeview.insert("", "end", values=(_.id, _.account_number, _.balance, _.account_type))

        
    def show_account_once(self, account_number , table__): # inserting a single account in table
        account = self.session.query(Account).filter(Account.account_number == account_number).first()  # find the account
        if not account: # if not found: (error)
            raise ValueError("Account not found")
        # and if found:
        table__.insert("", "end", values=(account.id, account.account_number, account.balance, account.account_type))

    
    def delete_account(self,account_id): # deleting account from database
        account=self.session.get(Account, account_id)
        if not account: # if not found: (error)
            raise ValueError("Account not found")
        # and if found:
        self.session.delete(account)
        self.session.commit()
        print(f"Account {account_id} deleted successfully")
        return account


    def delete_customer_accounts (self,customer_id): # deleting all accounts of a customer
        db_customer = self.session.get(customer, customer_id)
        if not db_customer: # if not found: (error)
            raise ValueError("Customer not found")
        # and if found:
        accounts = db_customer.accounts
        for account in accounts:
            self.session.delete(account)
        self.session.commit()
        print(f"All accounts of customer {customer_id} deleted successfully")
        return accounts

    

    def show_balance(self,account_id): # showing balance of an account
        account=self.session.get(Account, account_id)
        if not account: # if not found: (error)
            raise ValueError("Account not found")
        return account.balance
    
    
    def deposit(self,account_id, amount): # deposit money in account
        account=self.session.get(Account, account_id)
        if not account: # if not found: (error)
            raise ValueError("Account not found")
        amount = float(amount)
        account.balance += amount
        self.session.commit()
        return account
    
    
    def withdraw(self,account_id, amount):
        account=self.session.get(Account, account_id)
        amount = float(amount)
        if not account: # if not found: (error)
            raise exception("Account not found")
        if account.balance < amount:
            raise ValueError("Insufficient balance")
        account.balance -= amount
        self.session.commit()
        return account
        
    
    
    def transfer(self,account_id,to_account_id, amount): # transfer from account_id to to_account_id (one account to another account)
        account1=self.session.get(Account, account_id)
        if not account1:
            raise ValueError("Account not found")
        account2=self.session.get(Account, to_account_id)
        if not account2:
            raise ValueError("Account not found")
        amount = float(amount)
        if account1.balance < amount:
            raise ValueError("Insufficient balance")
        account1.balance -= amount
        account2.balance += amount
        self.session.commit()
        return account1

    
    def show_transactions(self,account_id):
        account=self.session.get(Account, account_id)
        if not account:
            raise ValueError("Account not found")
        transactions=account.transactions
        for transaction in transactions:
            print(transaction)
        return transactions

    
    def make_account_number(self):
        num = random.randint(1000000000, 9999999999)
        exists = self.session.query(Account).filter_by(account_number=num).first()
        if exists:
            return False
        else:
            return num
    
    

    # admin managment
    
    def create_admin(self, ad_username, ad_password , ad_email , ad_gender):
        hashed_password = hash_password(ad_password)
        admin = admin_data(username=ad_username, password=hashed_password, email=ad_email, gender=ad_gender)
        self.session.add(admin)
        self.session.commit()
        print(f"Admin {ad_username} created successfully")
        return admin

    def remove_admin(self, ad_username):
        admin=self.session.query(admin_data).filter_by(username=ad_username).first()
        if not admin:
            raise ValueError("Admin not found")
        self.session.delete(admin)
        self.session.commit()
        print(f"Admin {ad_username} deleted successfully")
        return admin

    def admin_login(self, ad_username_login, ad_password_login):
        admin=self.session.query(admin_data).filter_by(username=ad_username_login).first()
        if not admin:
            raise ValueError("Admin not found")
        if check_password(admin.password, ad_password_login) == False:
            raise ValueError("Invalid password")
        elif check_password(admin.password, ad_password_login) == True: 
            return admin
        print(f"Admin {ad_username_login} logged in successfully")

    def set_admin_image(admin_id, image_path):
        db_admin = session.get(admin_data, admin_id)
        if not db_admin:
            raise ValueError("Admin not found")
        with open(image_path, "rb") as f:
            db_admin.profile_image = f.read()
        session.commit()
        return db_admin

    def get_admin_image(self, admin_id):
        db_admin = self.session.get(admin_data, admin_id)
        if not db_admin:
            raise ValueError("Admin not found")
        return db_admin.profile_image

    def show_admin_data(self , table_):
        admins = self.session.query(admin_data).all()
        for admin in admins:
            table_.insert("", "end", values=(admin.id, admin.username, admin.email, admin.gender))
        return admins

    
    def show_admin_data_once(self ,admin_id):
        admin = self.session.query(admin_data).filter_by(id=admin_id).first()
        if not admin:
            raise ValueError("Admin not found")
        return admin


    def show_admin_data_by_name(self, admin_name , table__):
        admin = self.session.query(admin_data).filter_by(username=admin_name).first()
        if not admin:
            raise ValueError("Admin not found")
        table__.insert("", "end", values=(admin.id, admin.username, admin.email, admin.gender))
        return admin

    def update_admin(self, admin_id, username, email, gender):
        db_admin = self.session.query(admin_data).filter_by(id=admin_id).first()
        if not db_admin:
            raise ValueError("Admin not found")
        db_admin.username = username
        db_admin.email = email
        db_admin.gender = gender
        self.session.commit()
        return db_admin
