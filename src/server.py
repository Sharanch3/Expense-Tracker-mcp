import uvicorn
import datetime
from fastapi import FastAPI, HTTPException, Depends
from .database import Base, engine, SessionLocal
from sqlalchemy.orm import Session
from . import schemas
from typing import List
from .crud import (
    add_expenses,
    fetch_expense_for_date,
    list_expenses,
    summarize_expense_categorywise
)


Base.metadata.create_all(bind= engine)


app = FastAPI(
    title="Expense-Tracking-System",
    version="1.0.0"
)


# dependency with the DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()




#CREATE-
@app.post("/add_expense", response_model= dict)
def create_expenses(expenses: List[schemas.ExpenseCreate], db: Session = Depends(get_db)):
    
    add_expenses(db, expenses)

    return {'message': 'successfully added!'}



#READ-
@app.get("/expenses/{expense_date}", response_model= List[schemas.ExpenseOut])
def get_expense_for_date(expense_date: datetime.date, db:Session = Depends(get_db)):

    expenses = fetch_expense_for_date(db, expense_date)

    if expenses:
        return expenses
    
    raise HTTPException(status_code=400, detail="No expenses found.")



#READ-
@app.get("/expenses", response_model= List[schemas.ExpenseOut])
def get_all_expense(start_date: datetime.date, end_date:datetime.date, db:Session = Depends(get_db)):

    expenses = list_expenses(db, start_date, end_date)

    if expenses:
        return expenses
    
    raise HTTPException(status_code=404, detail="No expenses found.")




@app.get("/summary", response_model= List[schemas.ExpenseSummary])
def summarize(start_date: datetime.date, end_date: datetime.date, db: Session = Depends(get_db)):

    return summarize_expense_categorywise(db, start_date, end_date)





if __name__ == "__main__":
    
    uvicorn.run(
        app= "server:app",
        host="127.0.0.1",
        port= 8000,
        reload= True,
        log_level="info"
    )