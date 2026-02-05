import datetime
from . import  models
from . import schemas 
from sqlalchemy.orm import Session
from sqlalchemy import func, desc
 



def fetch_expense_for_date(db: Session, date: datetime.date):

    expenses = (db.query(models.Expenses)
              .filter(models.Expenses.date == date)
              .all() 

            )
    
    return expenses




def list_expenses(db: Session, start_date: datetime.date, end_date: datetime.date):
    
    expenses = (db.query(models.Expenses)
                .filter(models.Expenses.date.between(start_date, end_date))
                .all()

             )
    
    return expenses



def add_expenses(db:Session, expenses: schemas.ExpenseCreate):

    db_expenses = [
        models.Expenses(
            date = expense.date,
            amount = expense.amount,
            category = expense.category,
            note = expense.note       
            
        )
        for expense in expenses
    ]

    db.add_all(db_expenses)
    db.commit()
    
    
    return {'message': 'successfully added!'}

    


def summarize_expense_categorywise(db: Session, start_date: datetime.date, end_date: datetime.date):
    
    total = db.query(func.sum(models.Expenses.amount)).filter(
        models.Expenses.date.between(start_date, end_date)
    ).scalar()
    
    # If no expenses, return empty list
    if not total:
        return []
    
    summary = (
        db.query(
            models.Expenses.category,
            func.sum(models.Expenses.amount).label("Total"),
            (func.sum(models.Expenses.amount) / total * 100).label("Percentage")
        )
        .filter(models.Expenses.date.between(start_date, end_date))
        .group_by(models.Expenses.category)
        .order_by(desc("Total"))
        .all()
    )
    
    
    return [
        {
            "category": row.category, 
            "total": row.Total, 
            "percentage": round(row.Percentage, 2)
        } 
        for row in summary
    ]

    


