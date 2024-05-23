"""
Income Model

Attributes:
    id (int): The unique identifier for the income.
    user_email (str): The email address of the user associated with the income.
    amount (int): The amount of the income.
    description (str): The description of the income.
    source (str): The source of the income.
    date (str): The date of the income.

Custom Validation:
    - date_format(cls, date): A custom validator function applied to the 'date' field using the 'validate_date_format' function.

Usage Example:
    income = Income(id=1, user_email='jane@example.com', amount=500, description='Salary', source='Job', date='2022-01-31')
"""
from pydantic import BaseModel, field_validator

from app.validators.string_validator import validate_date_format


class Income(BaseModel):
    id: int
    user_email: str
    amount: int
    description: str
    source: str
    date: str

    @field_validator('date')
    def date_format(cls, date):
        """
          Validate the format of the 'date' field using the 'validate_date_format' function.

          Args:
             date (str): The date string to validate.

          Returns:
            str: The validated date string.
        """
        return validate_date_format(cls, date)
