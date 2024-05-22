from fastapi import HTTPException

from app.db_management.income_collection import get_next_id, insert_income, delete_all_income, delete_one_income, \
    update_income, get_all_income
from app.models.Income import Income


async def get_Income_by_email(email: str):
    return [income for income in await get_all_income() if email == income.user_email]


async def get_income_by_id(income_id: int):
    try:
        income_id = int(income_id)
    except:
        raise HTTPException(status_code=400, detail="oops... invalid id ")
    income = [income for income in await get_all_income() if income_id == income.id]
    if income:
        return income[0]
    raise HTTPException(status_code=404, detail="oops... income didn't find")


async def get_all_Income_service(email: str):
    incomes = await get_Income_by_email(email)
    if incomes:
        return incomes
    raise HTTPException(status_code=404, detail="oops... incomes didn't find")


async def get_one_income_service(income_id: int):
    return await get_income_by_id(income_id)


async def insert_income_service(newIncome: Income):
    max_id = await get_next_id()
    if max_id is None:
        max_id = -1
    newIncome.id = max_id + 1
    await insert_income(newIncome)
    return True


async def delete_all_income_service(email: str):
    await delete_all_income(email)
    return True


async def delete_one_income_service(income_id: int):
    await delete_one_income(income_id)
    return True


async def update_income_service(income_id: int, updated_income: Income):
    if income_id != updated_income.id:
        raise HTTPException(status_code=400, detail="oops... invalid id")
    income: Income = await get_income_by_id(income_id)
    if updated_income.amount is not None:
        income.amount = updated_income.amount
    if updated_income.description is not None:
        income.description = updated_income.description
    if updated_income.source is not None:
        income.source = updated_income.source
    if updated_income.date is not None:
        income.date = updated_income.date
    await update_income(income_id, updated_income)
    return True
