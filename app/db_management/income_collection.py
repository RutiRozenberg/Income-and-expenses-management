import asyncio

from app.db_management.connect_db import db
from app.models.Income import Income

incomes = db['income']


async def get_all_income():
    return [Income(**income) for income in incomes.find()]


# async def get_next_id():
#     result = await get_all_income().sort([('id', -1)]).limit(1)
#     if result:
#         return result[0]['id']
#     else:
#         return None
async def get_next_id():
    result = await get_all_income()
    if result:
        result = result.sort([('id', -1)]).limit(1).to_list(1)
        if result:
            return result[0]['id']
    return None


async def insert_income(newIncome: Income):
    incomes.insert_one(dict(newIncome))
    return True


async def delete_all_income(email: str):
    incomes.delete_many({'user_email': email})


async def delete_one_income(income_id: int):
    incomes.delete_one({'id': income_id})


async def update_income(income_id: int, updated_income: Income):
    incomes.update_one({'id': income_id}, {'$set': updated_income.dict()})
