import asyncio
import bcrypt

from app.db_management.user_collection import *
from app.models.User import User

salt = bcrypt.gensalt(rounds=20)


async def get_by_email(email: str):
    user = [user for user in await get_all_users() if user.email == email]
    if not user:
        return False
    return user[0]


async def inset_user(name: str, password: str, email: str):
    newUser = User(name=name, password=hashPassword(password), email=email)
    await save_user_db(newUser)


async def delete_user(email: str):
    await delete_user_db({'email': email})


async def update_user(email: str, user: User):
    await update_user_db(email, user)


async def signIn(email: str, password: str):
    user = await get_by_email(email)
    if user:
        bytes_password = password.encode('utf-8')
        hashed_password = user.password.encode('utf-8')
        if bcrypt.checkpw(bytes_password, hashed_password):
            return user
    return None


def hashPassword(password: str):
    return bcrypt.hashpw(password.encode('utf-8'), salt)
