
from app.db_management.connect_db import db
from app.models.Expense import Expense

expenses = db['expense']


async def get_all_expenses():
    return [Expense(**expense) for expense in expenses.find()]


async def get_next_id():
    result = await get_all_expenses()
    if result:
        max_id = max(result, key=lambda x: x.id, default=None)
        return max_id.id
    return None


async def insert_expense(newExpense: Expense):
    expenses.insert_one(dict(newExpense))
    return True


async def delete_all_expense(email: str):
    expenses.delete_many({'user_email': email})


async def delete_one_expense(expense_id: int):
    expenses.delete_one({'id': expense_id})


async def update_expense(expense_id: int, updated_expense: Expense):
    expenses.update_one({'id': expense_id}, {'$set': updated_expense.dict()})
