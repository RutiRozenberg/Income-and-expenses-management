import bcrypt
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


async def update_user(email: str, user: User):
    await update_user_db(email, user)


async def signIn_service(email: str, password: str):
    user = await get_by_email(email)
    if user:
        bytes_password = password.encode('utf-8')
        hashed_password = user.password.encode('utf-8')
        if bcrypt.checkpw(bytes_password, hashed_password):
            return user
    return None


async def signUp_service(newUser: User):
    try:
        newUser.password = hashPassword(newUser.password)
        await save_user_db(newUser)
        return True
    except ValidationError as error:
        return False


def hashPassword(password: str):
    return bcrypt.hashpw(password.encode('utf-8'), salt)
