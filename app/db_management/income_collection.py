
from app.db_management.connect_db import db
from app.models.Income import Income

incomes = db['income']


# Retrieve all income entries from the database
async def get_all_income():
    """
       Retrieve all income entries from the 'income' collection.
       Returns:
           List[Income]: List of Income objects representing all income entries.
       """
    return [Income(**income) for income in incomes.find()]


# Get the next available ID for a new income entry
async def get_next_id():
    """
       Get the next available ID for a new income entry.
       Returns:
           int: Next available ID.
       """
    result = await get_all_income()
    if result:
        max_id = max(result, key=lambda x: x.id, default=None)
        return max_id.id
    return None


# Insert a new income entry into the database
async def insert_income(newIncome: Income):
    """
       Insert a new income entry into the 'income' collection.
       Args:
           newIncome (Income): Income object to insert.
       Returns:
           bool: True if insertion is successful, False otherwise.
       """
    incomes.insert_one(dict(newIncome))
    return True


# Delete all income entries associated with a specific user email
async def delete_all_income(email: str):
    """
       Delete all income entries associated with a specific user email.
       Args:
           email (str): User email for which income entries should be deleted.
       """
    incomes.delete_many({'user_email': email})


# Delete a specific income entry by its ID
async def delete_one_income(income_id: int):
    """
       Delete a specific income entry by its ID.
       Args:
           income_id (int): ID of the income entry to delete.
       """
    incomes.delete_one({'id': income_id})


# Update an existing income entry in the database
async def update_income(income_id: int, updated_income: Income):
    """
        Update an existing income entry in the 'income' collection.
        Args:
            income_id (int): ID of the income entry to update.
            updated_income (Income): Updated Income object.
        """
    incomes.update_one({'id': income_id}, {'$set': updated_income.dict()})
