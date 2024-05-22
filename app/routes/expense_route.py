from fastapi import APIRouter, HTTPException

from app.models.Expense import Expense
from app.services.expense_service import get_one_expense_service, get_all_expense_service, insert_expense_service, \
    update_expense_service, delete_one_expense_service, delete_all_expense_service

expense_router = APIRouter()


@expense_router.get("/getOne/{expense_id}")
async def get_income(expense_id):
    return await get_one_expense_service(expense_id)


@expense_router.get("/getAll/{email}")
async def get_all_incomes(email: str):
    return await get_all_expense_service(email)


@expense_router.post("/insert")
async def signUp(expense: Expense):
    if not await insert_expense_service(expense):
        raise HTTPException(status_code=400, detail="oops... invalid parameters")
    return True


@expense_router.put("/put/{expense_id}")
async def update_income(expense_id: int, expense: Expense):
    if await update_expense_service(expense_id, expense):
        return True
    raise HTTPException(status_code=404, detail="oops...")


@expense_router.delete('/deleteOne/{income_id}')
async def delete_income(expense_id: int):
    if await delete_one_expense_service(expense_id):
        return True
    raise HTTPException(status_code=404, detail="oops...")


@expense_router.delete('/deleteAll/{email}')
async def delete_all_income(email: str):
    if await delete_all_expense_service(email):
        return True
    raise HTTPException(status_code=404, detail="oops...")
