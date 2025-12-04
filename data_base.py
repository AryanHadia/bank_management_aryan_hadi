from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base


engine = create_engine("mysql+mysqlconnector://aryan:pythonint12@localhost:3306", echo=False, future=True)


with engine.begin() as conn:
    conn.execute(text("CREATE DATABASE IF NOT EXISTS bank_db"))


engine = create_engine("mysql+mysqlconnector://aryan:pythonint12@localhost:3306/bank_db", echo=False, future=True)

base = declarative_base()
SessionLocal = sessionmaker(bind=engine, autoflush=False, future=True)
session = SessionLocal()
