from fastapi import APIRouter, HTTPException

from app.models.Income import Income
from app.services.income_service import get_one_income_service, insert_income_service, \
    update_income_service, delete_one_income_service, delete_all_income_service, get_all_income_service
from app.services.visualization_service import group_amounts_by_year

income_router = APIRouter()


@income_router.get("/{income_id}")
async def get_income(income_id):
    """
    - Description: Retrieves a single income based on the provided income_id.
- Parameters:
    - income_id: The unique identifier of the income to retrieve.
- Returns:
    - The income object corresponding to the income_id.
    :param income_id:
    :return:
    """
    return await get_one_income_service(income_id)


@income_router.get("s/{email}")
async def get_all_incomes(email: str):
    """
    - Description: Retrieves all incomes associated with the specified email.
    - Parameters:
        - email: The email address associated with the incomes to retrieve.
    - Returns:
        - List of income objects associated with the provided email.
    """
    return await get_all_income_service(email)


@income_router.post("")
async def insert_income(income: Income):
    """
    - Description: Inserts a new income into the database.
    - Parameters:
        - income: The income object to insert.
    - Returns:
        - True if the insertion is successful, raises HTTPException with status_code 400 if insertion fails.
    """
    if not await insert_income_service(income):
        raise HTTPException(status_code=400, detail="oops... invalid parameters")
    return True


@income_router.put("/{income_id}")
async def update_income(income_id: int, income: Income):
    """
    - Description: Updates an existing income identified by the income_id.
    - Parameters:
        - income_id: The unique identifier of the income to update.
        - income: The updated income object.
    - Returns:
        - True if the update is successful, raises HTTPException with status_code 404 if update fails.
    """
    if await update_income_service(income_id, income):
        return True
    raise HTTPException(status_code=404, detail="oops...")


@income_router.delete('/{income_id}')
async def delete_income(income_id: int):
    """
    - Description: Deletes a specific income by the income_id.
    - Parameters:
        - income_id: The unique identifier of the income to delete.
    - Returns:
        - True if the deletion is successful, raises HTTPException with status_code 404 if deletion fails.
    """
    if await delete_one_income_service(income_id):
        return True
    raise HTTPException(status_code=404, detail="oops...")


@income_router.delete('s/{email}')
async def delete_all_income(email: str):
    """
    - Description: Deletes all incomes associated with the provided email.
    - Parameters:
        - email: The email address associated with the incomes to delete.
    - Returns:
    - True if all deletions are successful, raises HTTPException with status_code 404 if deletion fails.
    """
    if await delete_all_income_service(email):
        return True
    raise HTTPException(status_code=404, detail="oops...")


@income_router.get("/{email}/{year}")
async def show_visualization(email: str, year: int):
    """
       Retrieves income data for a specific user based on the provided email and year and displays a visualization.

       Parameters:
       - email (str): The email of the user for whom income data will be visualized.
       - year (int): The year for which income data will be grouped and visualized.

       Returns:
       - bool: True if the visualization of income data is successfully displayed.

       Raises:
       - HTTPException: If there is an error processing the request, returns status code 400 with the detail "oops...".
       """
    try:
        await group_amounts_by_year(year, await get_all_Income_service(email))
        return True
    except:
        raise HTTPException(status_code=400, detail="oops...")
