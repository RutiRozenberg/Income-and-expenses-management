from fastapi import APIRouter, HTTPException

from app.models.Expense import Expense
from app.services.expense_service import get_one_expense_service, get_all_expense_service, insert_expense_service, \
    update_expense_service, delete_one_expense_service, delete_all_expense_service

expense_router = APIRouter()


@expense_router.get("/getOne/{expense_id}")
async def get_income(expense_id):
    """
    - Description: Retrieves a single expense based on the provided expense_id.
    - Parameters:
        - expense_id: The unique identifier of the expense to retrieve.
    - Returns:
        - The expense object corresponding to the expense_id.
    """
    return await get_one_expense_service(expense_id)


@expense_router.get("/getAll/{email}")
async def get_all_incomes(email: str):
    """
    - Description: Retrieves all expenses associated with the specified email.
    - Parameters:
        - email: The email address associated with the expenses to retrieve.
    - Returns:
        - List of expense objects associated with the provided email.
    """
    return await get_all_expense_service(email)


@expense_router.post("/insert")
async def signUp(expense: Expense):
    """
    - Description: Inserts a new expense into the database.
    - Parameters:
        - expense: The expense object to insert.
    - Returns:
        - True if the insertion is successful, raises HTTPException with status_code 400 if insertion fails.
     """
    if not await insert_expense_service(expense):
        raise HTTPException(status_code=400, detail="oops... invalid parameters")
    return True


@expense_router.put("/put/{expense_id}")
async def update_income(expense_id: int, expense: Expense):
    """
    - Description: Updates an existing expense identified by the expense_id.
    - Parameters:
        - expense_id: The unique identifier of the expense to update.
        - expense: The updated expense object.
    - Returns:
        - True if the update is successful, raises HTTPException with status_code 404 if update fails.
    """
    if await update_expense_service(expense_id, expense):
        return True
    raise HTTPException(status_code=404, detail="oops...")


@expense_router.delete('/deleteOne/{income_id}')
async def delete_income(expense_id: int):
    """
    - Description: Deletes a specific expense by the income_id.
    - Parameters:
        - expense_id: The unique identifier of the expense to delete.
    - Returns:
        - True if the deletion is successful, raises HTTPException with status_code 404 if deletion fails.
    """
    if await delete_one_expense_service(expense_id):
        return True
    raise HTTPException(status_code=404, detail="oops...")


@expense_router.delete('/deleteAll/{email}')
async def delete_all_income(email: str):
    """
    - Description: Deletes all expenses associated with the provided email.
    - Parameters:
        - email: The email address associated with the expenses to delete.
    - Returns:
        - True if all deletions are successful, raises HTTPException with status_code 404 if deletion fails.
    """
    if await delete_all_expense_service(email):
        return True
    raise HTTPException(status_code=404, detail="oops...")
