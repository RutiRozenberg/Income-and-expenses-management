from app.db_management.connect_db import db
from app.models.User import User

users = db['users']


async def get_all_users():
    return [User(**user) for user in users.find()]


async def save_user_db(user: User):
    users.insert_one(dict(user))


async def delete_user_db(email: str):
    users.delete_one({'email': email})


async def update_user_db(email: str, user: User):
    users.update_one({'email': email}, {'$set': dict(user)})
