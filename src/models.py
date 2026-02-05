from sqlalchemy import Column, Date, Float, String, Integer
from .database import Base


class Expenses(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key= True, index= True)
    date = Column(Date, index= True)
    amount = Column(Float, index=True)
    category = Column(String(100), index= True)
    note = Column(String(300), index= True)
