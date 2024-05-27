from fastapi import HTTPException

from app.db_management.expense_collection import get_all_expenses, get_next_id, insert_expense, delete_all_expense, \
    delete_one_expense, update_expense
from app.models.Expense import Expense


async def get_expense_by_email(email: str):
    """
    Retrieves a list of expenses based on the provided email.
    Parameters:
        - email: The email address to filter expenses by.
    Returns:
        - List of expenses matching the provided email.
    """
    return [expense for expense in await get_all_expenses() if email == expense.user_email]


async def get_expense_by_id(expense_id: int):
    """
    Retrieves a single expense based on the provided expense_id.
    Parameters:
        - expense_id: The unique identifier of the expense to retrieve.
    Returns:
        - The expense object corresponding to the expense_id if found, raises HTTPException with status_code 404 if not found.
    """
    try:
        expense_id = int(expense_id)
    except:
        raise HTTPException(status_code=400, detail="oops... invalid id ")
    expense = [expense for expense in await get_all_expenses() if expense_id == expense.id]
    if expense:
        return expense[0]
    raise HTTPException(status_code=404, detail="oops... income didn't find")


async def get_all_expense_service(email: str):
    """
    Retrieves all expenses associated with the specified email.
    Parameters:
        - email: The email address associated with the expenses to retrieve.
    Returns:
        - List of expenses associated with the provided email if found, raises HTTPException with status_code 404 if not found.
    """
    expenses = await get_expense_by_email(email)
    if expenses:
        return expenses
    raise HTTPException(status_code=404, detail="oops... incomes didn't find")


async def get_one_expense_service(expense_id: int):
    """
    Retrieve a single expense based on the provided expense_id.
    Parameters:
        - expense_id: The unique identifier of the expense to retrieve.
    Returns:
        - The expense object corresponding to the expense_id.
    """
    return await get_expense_by_id(expense_id)


async def insert_expense_service(newExpense: Expense):
    """
    Inserts a new expense into the database.
    Parameters:
        - newExpense: The Expense object to insert.
    Returns:
        - True if the insertion is successful.
    """
    max_id = await get_next_id()
    if max_id is None:
        max_id = -1
    newExpense.id = max_id + 1
    await insert_expense(newExpense)
    return True


async def delete_all_expense_service(email: str):
    """
    Deletes all expenses associated with the provided email.
    Parameters:
        - email: The email address associated with the expenses to delete.
    Returns:
        - True if all deletions are successful.
    """
    await delete_all_expense(email)
    return True


async def delete_one_expense_service(income_id: int):
    """
    Deletes a specific expense based on the provided expense_id.
    Parameters:
        - expense_id: The unique identifier of the expense to delete.
    Returns:
        - True if the deletion is successful.
    """
    await delete_one_expense(income_id)
    return True


async def update_expense_service(expense_id: int, updated_expense: Expense):
    """
    Updates an existing expense based on the provided expense_id and updated_expense.
    Parameters:
        - expense_id: The unique identifier of the expense to update.
        - updated_expense: The updated Expense object with new information.
    Returns:
        - True if the update is successful, raises HTTPException with status_code 400 if the ID does not match.
    """
    if expense_id != updated_expense.id:
        raise HTTPException(status_code=400, detail="oops... invalid id")
    expense: Expense = await get_expense_by_id(expense_id)
    if updated_expense.amount is not None:
        expense.amount = updated_expense.amount
    if updated_expense.description is not None:
        expense.description = updated_expense.description
    if updated_expense.target is not None:
        expense.target = updated_expense.target
    if updated_expense.date is not None:
        expense.date = updated_expense.date
    await update_expense(expense_id, updated_expense)
    return True
