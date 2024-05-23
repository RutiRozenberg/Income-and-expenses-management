"""
User Model

Attributes:
    name (str): The name of the user. It should only contain alphabetic characters and underscores (_).
    email (str): The email address of the user, validated using a regular expression pattern.
    password (str): The password of the user, not subjected to any specific pattern validation.

Usage Example:
    user = User(name='John_Doe', email='john.doe@example.com', password='secure-password123')

Validation:
    - name: Should only contain alphabetic characters and underscores.
    - email: Should match the specified email pattern regex.
    - password: No specific validation applied.

Exceptions:
    - ValidationError: Raised by Pydantic if validation fails for any of the attributes.

Note: Ensure that valid values are provided for 'name' and 'email' attributes to pass the pattern validations.

"""

from pydantic import BaseModel, constr, ValidationError


class User(BaseModel):
    name: constr(pattern=r"^[a-zA-Z_]+$")
    email: constr(pattern=r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b')
    password: str
