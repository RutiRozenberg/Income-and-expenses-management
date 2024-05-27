from fastapi import HTTPException
from app.db_management.income_collection import get_next_id, insert_income, delete_all_income, delete_one_income, update_income, get_all_income
from app.models.Income import Income


async def get_Income_by_email(email: str):
    """
    Retrieves a list of incomes based on the provided email.
    Parameters:
        - email: The email address to filter incomes by.
    Returns:
        - List of incomes matching the provided email.
    """
    return [income for income in await get_all_income() if email == income.user_email]


async def get_income_by_id(income_id: int):
    """
    Retrieves a single income based on the provided income_id.
    Parameters:
        - income_id: The unique identifier of the income to retrieve.
    Returns:
        - The income object corresponding to the income_id if found, raises HTTPException with status_code 404 if not found.
    """
    try:
        income_id = int(income_id)
    except:
        raise HTTPException(status_code=400, detail="oops... invalid id ")
    income = [income for income in await get_all_income() if income_id == income.id]
    if income:
        return income[0]
    raise HTTPException(status_code=404, detail="oops... income didn't find")


async def get_all_Income_service(email: str):
    """
    Retrieves all incomes associated with the specified email.
    Parameters:
        - email: The email address associated with the incomes to retrieve.
    Returns:
        - List of incomes associated with the provided email if found, raises HTTPException with status_code 404 if not found.
    """
    incomes = await get_Income_by_email(email)
    if incomes:
        return incomes
    raise HTTPException(status_code=404, detail="oops... incomes didn't find")


async def get_one_income_service(income_id: int):
    """
    Retrieve a single income based on the provided income_id.
    Parameters:
        - income_id: The unique identifier of the income to retrieve.
    Returns:
        - The income object corresponding to the income_id.
    """
    return await get_income_by_id(income_id)


async def insert_income_service(newIncome: Income):
    """
    Inserts a new income into the database.
    Parameters:
        - newIncome: The Income object to insert.
    Returns:
        - True if the insertion is successful.
    """
    max_id = await get_next_id()
    if max_id is None:
        max_id = -1
    newIncome.id = max_id + 1
    await insert_income(newIncome)
    return True


async def delete_all_income_service(email: str):
    """
    Deletes all incomes associated with the provided email.
    Parameters:
        - email: The email address associated with the incomes to delete.
    Returns:
        - True if all deletions are successful.
    """
    await delete_all_income(email)
    return True


async def delete_one_income_service(income_id: int):
    """
    Deletes a specific income based on the provided income_id.
    Parameters:
        - income_id: The unique identifier of the income to delete.
    Returns:
        - True if the deletion is successful.
    """
    await delete_one_income(income_id)
    return True


async def update_income_service(income_id: int, updated_income: Income):
    """
    Updates an existing income based on the provided income_id and updated_income.
    Parameters:
        - income_id: The unique identifier of the income to update.
        - updated_income: The updated Income object with new information.
    Returns:
        - True if the update is successful, raises HTTPException with status_code 400 if the ID does not match.
    """
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
