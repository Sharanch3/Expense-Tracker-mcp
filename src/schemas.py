import datetime
from pydantic import BaseModel, ConfigDict
from typing import Literal


class ExpenseBase(BaseModel):

    date: datetime.date
    
    amount: float
    
    category: Literal["Food", "Transport", "Rent", "Shopping","Entertainment", "Other"]
    
    note: str


class ExpenseCreate(ExpenseBase):
    pass



class ExpenseUpdate(ExpenseBase):
    pass




class ExpenseSummary(BaseModel):
    category: str
    total: float
    percentage: float

    model_config = ConfigDict(from_attributes = True)




class ExpenseOut(ExpenseBase):

    id: int

    model_config = ConfigDict(from_attributes = True)