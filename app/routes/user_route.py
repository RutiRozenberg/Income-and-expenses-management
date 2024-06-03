from fastapi import APIRouter, HTTPException

from app.models.User import User
from app.services.user_service import update_user_service, sign_in_service, sign_up_service

user_router = APIRouter()


@user_router.get("/{email}/{password}")
async def sign_in(email, password):
    """
    - Description: Validates user sign-in credentials by checking the provided email and password.
    - Parameters:
        - email: The user's email address.
        - password: The user's password.
    - Returns:
    - The user object if sign-in is successful, raises HTTPException with status_code 404 if user not found.
    """
    user = await sign_in_service(email, password)
    if not user:
        raise HTTPException(status_code=404, detail="oops... user didn't find")
    return user


@user_router.post("")
async def sign_up(user: User):
    """
    - Description: Registers a new user by creating their account with the provided details.
    - Parameters:
        - user: The user object containing sign-up details.
    - Returns:
    - True if sign-up is successful, raises HTTPException with status_code 400 if parameters are invalid.
    """
    if not await sign_up_service(user):
        raise HTTPException(status_code=400, detail="oops... invalid parameters")
    return True


@user_router.put("/{email}")
async def update_user(email: str, user_from_body: User):
    """- Description: Updates an existing user's information based on the provided email.
    - Parameters:
        - email: The user's email address.
        - user_from_body: The updated user object with new information.
    - Returns:
    - True if the update is successful, raises HTTPException with status_code 404 if user update fails.
    """
    if await update_user_service(email, user_from_body):
        return True
    raise HTTPException(status_code=404, detail="oops...")
