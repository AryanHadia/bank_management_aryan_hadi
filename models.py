# class ke vasl behshe be soton database
from sqlalchemy.orm import relationship
from sqlalchemy import Column , String , Integer , Float , ForeignKey , DateTime , LargeBinary
from datetime import datetime
from data_base import base

class customer(base):
    __tablename__ = "customer"
    id = Column(Integer , primary_key=True , autoincrement=True)
    email = Column(String , unique=True)
    name = Column(String , nullable=False)
    age = Column(Integer , nullable=False)
    phone_number = Column(String , nullable=False)
    address = Column(String , nullable=False)
    

    accounts = relationship("Account", back_populates="customer", cascade="all, delete-orphan")
    
    """ customer data base """

    def __str__(self):
        return f"[{self.email},{self.name}]"
    def __repr__(self):
        return f"<id={self.id} , email={self.email}>"




class Account(base):
    __tablename__ = "accounts"
    id = Column(Integer , primary_key=True , autoincrement=True)
    account_number = Column(String , unique=True)
    account_type = Column(String , nullable=False)
    balance = Column(Float , nullable=False)
    customer_id = Column(Integer , ForeignKey("customer.id"))   
    pin = Column(String , nullable=False)

    # relationships
    customer = relationship("customer", back_populates="accounts", foreign_keys=[customer_id])
    transactions = relationship("Transaction" , back_populates="account")





class admin_data(base):
    __tablename__= "admin_data"
    id = Column(Integer , primary_key=True , autoincrement=True)
    username = Column(String , unique=True)
    password = Column(String , nullable=False)
    profile_image = Column(LargeBinary , nullable=True)




class Transaction(base):
    __tablename__ = "transactions"
    id = Column(Integer , primary_key=True , autoincrement=True)
    account_id = Column(Integer , ForeignKey("accounts.id") , nullable=False)
    amount = Column(Float , nullable=False)
    created_at = Column(DateTime , default=datetime.now)

    account = relationship("Account" , back_populates="transactions")


    # next features
    #card_number = Column(String , unique=True)
    #card_cvv = Column(String , nullable=False)
    #card_holder_name = Column(String , nullable=False)
    #card_expiration_date = Column(String , nullable=False)
