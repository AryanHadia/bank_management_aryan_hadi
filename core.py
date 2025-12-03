from models import customer, Account , admin_data
from utils import hash_password, check_password
from data_base import get_session
import random


class admin_panel:
    def __init__(self):
        self.session=get_session()

    def create_customer(self, name, email, age , phone_number , address):
        # built a row in database
        new_customer = customer(name=name, email=email, age=age, phone_number=phone_number, address=address)
        self.session.add(new_customer)
        self.session.commit()
        print(f"Customer {name} created successfully")
        print(f"Customer ID: {new_customer.id}")
        print(f"Customer Email: {new_customer.email}")
        print(f"Customer Age: {new_customer.age}")
        print(f"Customer Phone Number: {new_customer.phone_number}")
        print(f"Customer Address: {new_customer.address}")
        return new_customer
    
    
    def create_account(self, customer_id, account_number , account_type, account_balance , pin):
        db_customer = self.session.get(customer, customer_id)
        if not db_customer:
            raise ValueError("Customer not found")
        hashed_pin = hash_password(pin)
        account = Account(customer_id=db_customer.id, account_number=account_number, account_type=account_type, balance=account_balance, pin=hashed_pin)
        self.session.add(account)
        self.session.commit()
        print(f"Account {account_number} created successfully")
        print(f"Account ID: {account.id}")
        print(f"Account Type: {account.account_type}")
        print(f"Account Balance: {account.balance}")
        return account

    
    def delete_account(self,account_id):
        account=self.session.get(Account, account_id)
        if not account:
            raise ValueError("Account not found")
        self.session.delete(account)
        self.session.commit()
        print(f"Account {account_id} deleted successfully")
        return account
    
    
    def show_balance(self,account_id):
        account=self.session.get(Account, account_id)
        if not account:
            raise ValueError("Account not found")
        print(f"Account Balance: {account.balance}")
        return account
    
    
    def deposit(self,account_id, amount):
        account=self.session.get(Account, account_id)
        if not account:
            raise ValueError("Account not found")
        account.balance += amount
        self.session.commit()
        return account
    
    
    def withdraw(self,account_id, amount):
        account=self.session.get(Account, account_id)
        if not account:
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
        
    def remove_customer(self, name):
        customer=self.session.query(customer).filter_by(name=name).first()
        if not customer:
            raise ValueError("Customer not found")
        self.session.delete(customer)
        self.session.commit()
        print(f"Customer {name} deleted successfully")
        return customer

    def create_admin(self, ad_username, ad_password):
        hashed_password = hash_password(ad_password)
        admin = admin_data(username=ad_username, password=hashed_password)
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

