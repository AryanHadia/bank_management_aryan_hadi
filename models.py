from sqlalchemy.orm import relationship
from sqlalchemy import Column , String , Integer , Float , ForeignKey , DateTime
from datetime import datetime
from data_base import base


class customer(base):
    __tablename__ = "customers"
    id = Column(Integer , primary_key=True , autoincrement=True)
    email = Column(String , unique=True)
    name = Column(String , nullable=False)
    age = Column(Integer , nullable=False)
    phone_number = Column(String , nullable=False)
    address = Column(String , nullable=False)

    accounts = relationship("account" , back_populates="customer")
    
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
    customer_id = Column(Integer , ForeignKey("customers.id"))
    pin = Column(String , nullable=False)

    # relationships
    customer = relationship("customer" , back_populates="accounts")
    transactions = relationship("transaction" , back_populates="account")


    # next features
    #card_number = Column(String , unique=True)
    #card_cvv = Column(String , nullable=False)
    #card_holder_name = Column(String , nullable=False)

    #card_expiration_date = Column(String , nullable=False)

