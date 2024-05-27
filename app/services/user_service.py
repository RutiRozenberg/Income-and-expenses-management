import bcrypt
from fastapi import HTTPException
from pydantic import ValidationError
from app.db_management.user_collection import *
from app.models.User import User

salt = bcrypt.gensalt(rounds=20)


async def get_by_email(email: str):
    """
    Retrieves a user by the provided email.
    Parameters:
        - email: The email address associated with the user.
    Returns:
        - The user object corresponding to the email if found, None if not found due to ValidationError.
    """
    try:
        user = [user for user in await get_all_users() if user.email == email]
    except ValidationError as error:
        user = None
        print(error)
    if not user:
        return None
    return user[0]


async def delete_user(email: str):
    """
    Deletes a user by the specified email.
    Parameters:
        - email: The email address of the user to delete.
    Returns:
        - True if the deletion is successful.
    """
    await delete_user_db(email)
    return True


async def update_user_service(email: str, user_from_body: User):
    """
    Updates user information based on the provided email and user object from the request body.
    Parameters:
        - email: The email address of the user to update.
        - user_from_body: The updated User object with new information.
    Returns:
        - True if the update is successful, raises HTTPException with status_code 400 if the provided email does not match.
    """
    if user_from_body.email != email:
        raise HTTPException(status_code=400, detail="oops... try another email")
    user: User = await get_by_email(email)
    if user_from_body.name is not None:
        user.name = user_from_body.name
    await update_user_db(email, user)
    return True


async def signIn_service(email: str, password: str):
    """
    Validates user sign-in credentials based on the provided email and password.
    Parameters:
      - email: The user's email address.
      - password: The user's password.
    Returns:
      - The user object if sign-in is successful, None if not found or password does not match.
    """
    user = await get_by_email(email)
    if user:
        bytes_password = password.encode('utf-8')
        hashed_password = user.password.encode('utf-8')
        if bcrypt.checkpw(bytes_password, hashed_password):
            return user
    return None


async def signUp_service(newUser: User):
    """
    Registers a new user with the provided details.
    Parameters:
        - newUser: The User object with the details of the new user.
    Returns:
        - True if the registration is successful, False if there is a ValidationError during the process.
    """
    oldUser = await get_by_email(newUser.email)
    if oldUser:
        raise HTTPException(status_code=400, detail="oops... invalid email")
    try:
        newUser.password = hashPassword(newUser.password)
        await save_user_db(newUser)
        return True
    except ValidationError:
        return False


def hashPassword(password: str):
    """
    Hashes the provided password using bcrypt with the preset salt value.
    Parameters:
        - password: The password to hash.
    Returns:
        - The hashed password.
    """
    return bcrypt.hashpw(password.encode('utf-8'), salt)
