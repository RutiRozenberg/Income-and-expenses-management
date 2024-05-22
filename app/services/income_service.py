
from app.db_management.income_collection import get_next_id, insert_income
from app.models.Income import Income


async def insert_income_service(newIncome: Income):
    max_id = await get_next_id()
    if max_id is None:
        max_id = -1
    newIncome.id = max_id + 1
    return await insert_income(newIncome)

