
from app.db_management.connect_db import db
from app.models.Expense import Expense

expenses = db['expense']


# Retrieve all expenses from the database
async def get_all_expenses():
    """
        Retrieve all expenses from the expenses collection.
        Returns:
            List[Expense]: List of Expense objects representing all expenses.
    """
    return [Expense(**expense) for expense in expenses.find()]


# Get the next available ID for a new expense
async def get_next_id():
    """
        Get the next available ID for a new expense.
        Returns:
            int: Next available ID.
    """
    result = await get_all_expenses()
    if result:
        max_id = max(result, key=lambda x: x.id, default=None)
        return max_id.id
    return None


# Insert a new expense into the database
async def insert_expense(newExpense: Expense):
    """
       Insert a new expense into the expenses' collection.
       Args:
           newExpense (Expense): Expense object to insert.
       Returns:
           bool: True if insertion is successful, False otherwise.
       """
    expenses.insert_one(dict(newExpense))
    return True


# Delete all expenses associated with a specific user email
async def delete_all_expense(email: str):
    """
       Delete all expenses associated with a specific user email.
       Args:
           email (str): User email for which expenses should be deleted.
       """
    expenses.delete_many({'user_email': email})


# Delete a specific expense by its ID
async def delete_one_expense(expense_id: int):
    """
      Delete a specific expense by its ID.
      Args:
          expense_id (int): ID of the expense to delete.
      """
    expenses.delete_one({'id': expense_id})


# Update an existing expense in the database
async def update_expense(expense_id: int, updated_expense: Expense):
    """
       Update an existing expense in the expenses' collection.
       Args:
           expense_id (int): ID of the expense to update.
           updated_expense (Expense): Updated Expense object.
       """
    expenses.update_one({'id': expense_id}, {'$set': updated_expense.dict()})
