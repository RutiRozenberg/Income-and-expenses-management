
from app.db_management.connect_db import db
from app.models.Income import Income

incomes = db['income']


async def get_all_Income(email: str):
    return [Income(**income) for income in incomes.find() if email == income.user_email]


async def insert_income(newIncome: Income):
    max_id = incomes.find().sort([('id', -1)]).limit(1)[0]['id']
    if max_id is None:
        max_id = -1
    newIncome.id = max_id + 1
    incomes.insert_one(dict(newIncome))
    return newIncome
