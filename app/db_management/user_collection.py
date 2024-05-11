import asyncio

from app.db_management.connect_db import db
from app.models.User import User

users = db['users']

async def get_all_users():
    return [User(**user) for user in users.find()]

async def save_user(user:User):
    users.insert_one(dict(user))
