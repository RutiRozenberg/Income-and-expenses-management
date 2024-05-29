from fastapi import APIRouter, HTTPException

from app.models.Expense import Expense
from app.services.expense_service import get_one_expense_service, get_all_expense_service, insert_expense_service, \
    update_expense_service, delete_one_expense_service, delete_all_expense_service, get_expense_by_email
from app.services.visualization_service import group_amounts_by_year

expense_router = APIRouter()


@expense_router.get("/{expense_id}")
async def get_income(expense_id):
    """
    - Description: Retrieves a single expense based on the provided expense_id.
    - Parameters:
        - expense_id: The unique identifier of the expense to retrieve.
    - Returns:
        - The expense object corresponding to the expense_id.
    """
    return await get_one_expense_service(expense_id)


@expense_router.get("s/{email}")
async def get_all_incomes(email: str):
    """
    - Description: Retrieves all expenses associated with the specified email.
    - Parameters:
        - email: The email address associated with the expenses to retrieve.
    - Returns:
        - List of expense objects associated with the provided email.
    """
    return await get_all_expense_service(email)


@expense_router.post("/")
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


@expense_router.put("/{expense_id}")
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


@expense_router.delete('/{income_id}')
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


@expense_router.delete('s/{email}')
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


@expense_router.get("{email}/{year}")
async def show_visualization(email: str, year: int):
    """
       Displays a visualization for expenses grouped by year for a specific user based on the provided email and year.

       Parameters:
       - email (str): The email of the user for whom expenses will be visualized.
       - year (int): The year for which expenses will be grouped and visualized.

       Returns:
       - bool: True if the visualization is successfully displayed.

       Raises:
       - HTTPException: If there is an error processing the request, returns status code 400 with the detail "oops...".
       """
    try:
        await group_amounts_by_year(year, await get_expense_by_email(email))
        return True
    except:
        raise HTTPException(status_code=400, detail="oops...")

