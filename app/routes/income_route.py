from fastapi import APIRouter, HTTPException

from app.models.Income import Income
from app.services.income_service import get_one_income_service, get_all_Income_service, insert_income_service, \
    update_income_service, delete_one_income_service, delete_all_income_service

income_router = APIRouter()


@income_router.get("/getOne/{income_id}")
async def get_income(income_id):
    return await get_one_income_service(income_id)


@income_router.get("/getAll/{email}")
async def get_all_incomes(email: str):
    return await get_all_Income_service(email)


@income_router.post("/insert")
async def signUp(income: Income):
    if not await insert_income_service(income):
        raise HTTPException(status_code=400, detail="oops... invalid parameters")
    return True


@income_router.put("/put/{income_id}")
async def update_income(income_id: int, income: Income):
    if await update_income_service(income_id, income):
        return True
    raise HTTPException(status_code=404, detail="oops...")


@income_router.delete('/deleteOne/{income_id}')
async def delete_income(income_id: int):
    if await delete_one_income_service(income_id):
        return True
    raise HTTPException(status_code=404, detail="oops...")


@income_router.delete('/deleteAll/{email}')
async def delete_all_income(email: str):
    if await delete_all_income_service(email):
        return True
    raise HTTPException(status_code=404, detail="oops...")
