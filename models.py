# class ke vasl behshe be soton database
from sqlalchemy.orm import relationship
from sqlalchemy import Column , String , Integer , Float , ForeignKey , DateTime , LargeBinary
from datetime import datetime
from data_base import base

class customer(base): # customer table in database
    __tablename__ = "customer" # table name
    # data
    id = Column(Integer , primary_key=True , autoincrement=True)
    email = Column(String , unique=True)
    name = Column(String , nullable=False)
    age = Column(Integer , nullable=False)
    phone_number = Column(String , nullable=False)
    address = Column(String , nullable=False)
    

    accounts = relationship("Account", back_populates="customer", cascade="all, delete-orphan") # one customer can have many accounts
    
    """ customer data base that can connect to many accounts """

    def __str__(self):
        return f"[{self.email},{self.name}]"
    def __repr__(self):
        return f"<id={self.id} , email={self.email}>"




class Account(base): # account table in database
    __tablename__ = "accounts" # table name
    # data
    id = Column(Integer , primary_key=True , autoincrement=True)
    account_number = Column(String , unique=True)
    account_type = Column(String , nullable=False)
    balance = Column(Float , nullable=False)
    customer_id = Column(Integer , ForeignKey("customer.id"))   
    pin = Column(String , nullable=False)

    # relationships
    customer = relationship("customer", back_populates="accounts", foreign_keys=[customer_id]) # one account can have one customer
    transactions = relationship("Transaction" , back_populates="account")   # one account can have many transactions

    """ account data base that can connect to a customer """




class admin_data(base): # admin table in database
    __tablename__= "admin_data" # table name
    # data
    id = Column(Integer , primary_key=True , autoincrement=True)
    username = Column(String , unique=True)
    password = Column(String , nullable=False)
    email = Column(String , nullable=False)
    gender = Column(String , nullable=False)
    region = Column(String , nullable=False)
    profile_image = Column(LargeBinary , nullable=True)

    """ admin data for login and ... """


class Transaction(base): # transaction table in database
    __tablename__ = "transactions" # table name
    # data
    id = Column(Integer , primary_key=True , autoincrement=True)
    account_id = Column(Integer , ForeignKey("accounts.id") , nullable=False)
    amount = Column(Float , nullable=False)
    created_at = Column(DateTime , default=datetime.now)

    account = relationship("Account" , back_populates="transactions") # one transaction can have one account

    """ transactions betwin to account """
 

    # next features
    #card_number = Column(String , unique=True)
    #card_cvv = Column(String , nullable=False)
    #card_holder_name = Column(String , nullable=False)
    #card_expiration_date = Column(String , nullable=False)
