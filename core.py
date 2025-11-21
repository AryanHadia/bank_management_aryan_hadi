from models import customer, Account
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
        customer=self.session.get(customer, customer_id)
        if not customer:
            raise exception("Customer not found")
        hashed_pin = hash_password(pin)
        account=Account(customer_id=customer.id, account_number=account_number, account_type=account_type, account_balance=account_balance, pin=hashed_pin)
        self.session.add(account)
        self.session.commit()
        print(f"Account {account_number} created successfully")
        print(f"Account ID: {account.id}")
        print(f"Account Type: {account.account_type}")
        print(f"Account Balance: {account.account_balance}")
        return account

    def delete_account(self,account_id):
        account=self.session.get(Account, account_id)
        if not account:
            raise exception("Account not found")
        self.session.delete(account)
        self.session.commit()
        print(f"Account {account_id} deleted successfully")
        return account
    
    def show_balance(self,account_id):
        account=self.session.get(Account, account_id)
        if not account:
            raise exception("Account not found")
        print(f"Account Balance: {account.account_balance}")
        return account
    
    def deposit(self,account_id, amount):
        account=self.session.get(Account, account_id)
        if not account:
            raise exception("Account not found")
        acount.balance += amount
        self.session.commit()
        return account
    
    def withdraw(self,account_id, amount):
        account=self.session.get(Account, account_id)
        if not account:
            raise exception("Account not found")
        if account.balance < amount:
            raise exception("Insufficient balance")
        account.balance -= amount
        self.session.commit()
        return account
        
    
    def transfer(self,account_id,to_account_id, amount): # transfer from account_id to to_account_id (one account to another account)
        account1=self.session.get(Account, account_id)
        if not account1:
            raise exception("Account not found")
        account2=self.session.get(Account, to_account_id)
        if not account2:
            raise exception("Account not found")
        if account1.balance < amount:
            raise exception("Insufficient balance")
        account1.balance -= amount
        account2.balance += amount
        self.session.commit()
        return account1

    def show_transactions(self,account_id):
        account=self.session.get(Account, account_id)
        if not account:
            raise exception("Account not found")
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