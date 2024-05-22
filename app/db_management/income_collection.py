
from app.db_management.connect_db import db
from app.models.Income import Income

incomes = db['income']


async def get_all_Income(email: str):
    return [Income(**income) for income in incomes.find() if email == income.get('user_email')]


async def insert_income(newIncome: Income):
    incomes.insert_one(dict(newIncome))
    return newIncome


async def get_next_id():
    return incomes.find().sort([('id', -1)]).limit(1)[0]['id']
