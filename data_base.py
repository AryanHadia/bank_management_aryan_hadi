from sqlalchemy import False_, create_engine
from sqlalchemy.orm import sessionmaker,declarative_base

engine = create_engine("mysql+mysqlconnector://root:root1234@localhost",echo=False ,future=True)
base = declarative_base()
session = sessionmaker(bind=engine ,autoflush=False , future=True)
def get_session():
    return session()



