import asyncio

from app.db_management.user_collection import *
from app.models.User import User


async def get_by_email(email: str):
    user =  [user for user in await get_all_users() if user.email == email]
    return user[0]


async def inset_user(name :str , password: str, email: str):
    newUser = User(name =name, password=password, email=email)
    asyncio.run((save_user_db(newUser)))


async def delete_user(email:str):
    await (delete_user_db({'email':email}))
