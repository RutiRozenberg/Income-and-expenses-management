import bcrypt
from fastapi import HTTPException
from pydantic import ValidationError

from app.db_management.user_collection import *
from app.models.User import User

salt = bcrypt.gensalt(rounds=20)


async def get_by_email(email: str):
    try:
        user = [user for user in await get_all_users() if user.email == email]
    except ValidationError as error:
        user = None
        print(error)
    if not user:
        return None
    return user[0]


async def delete_user(email: str):
    await delete_user_db(email)


async def update_user_service(email: str, user_from_body: User):
    if user_from_body.email != email:
        raise HTTPException(status_code=400, detail="oops... try another email")
    user: User = await get_by_email(email)
    if user.name != user_from_body.name:
        user.name = user_from_body.name
    if user.password != hashPassword(user_from_body.password):
        user.password = user_from_body.password
    return await update_user_db(email, user)


async def signIn_service(email: str, password: str):
    user = await get_by_email(email)
    if user:
        bytes_password = password.encode('utf-8')
        hashed_password = user.password.encode('utf-8')
        if bcrypt.checkpw(bytes_password, hashed_password):
            return user
    return None


async def signUp_service(newUser: User):
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
    return bcrypt.hashpw(password.encode('utf-8'), salt)
