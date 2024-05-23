
"""
Expense Model

Attributes:
    id (int): The unique identifier for the expense.
    user_email (str): The email address of the user associated with the expense.
    amount (int): The amount of the expense.
    description (str): The description of the expense.
    target (str): The target or purpose of the expense.
    date (str): The date of the expense.

Custom Validators:
    - date_format(cls, date): A custom validator function to validate the format of the 'date' field using the 'validate_date_format' function from 'app.validators.string_validator' module.

Usage Example:
    expense = Expense(id=1, user_email='john@example.com', amount=100, description='Groceries', target='Food', date='2022-12-31')
"""

from pydantic import BaseModel, field_validator

from app.validators.string_validator import validate_date_format


class Expense(BaseModel):
    id: int
    user_email: str
    amount: int
    description: str
    target: str
    date: str

    @field_validator('date')
    def date_format(cls, date):
        """
              Validate the format of the 'date' field using the 'validate_date_format' function.

              Args:
                  date (str): The date string to validate.

              Returns:
                  str: The validated date string.

              Raises:
                  ValueError: If the date format validation fails.
              """
        return validate_date_format(cls, date)

