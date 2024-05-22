from app.db_management.connect_db import db
from app.models.User import User

users = db['users']


# Retrieve all users from the 'users' collection
async def get_all_users():
    """
       Get all users from the 'users' collection.

       Returns:
           list: List of User objects representing all users.
       """
    return [User(**user) for user in users.find()]


# Save a user to the database
async def save_user_db(user: User):
    """
       Save a user to the 'users' collection in the database.

       Args:
           user (User): User object to be saved.
       """
    users.insert_one(dict(user))


# Delete a user from the database by email
async def delete_user_db(email: str):
    """
        Delete a user from the 'users' collection based on the provided email.

        Args:
            email (str): Email of the user to be deleted.
        """
    users.delete_one({'email': email})


# Update a user in the database by email
async def update_user_db(email: str, user: User):
    """
       Update a user in the 'users' collection based on the provided email.

       Args:
           email (str): Email of the user to be updated.
           user (User): Updated User object.
       """
    users.update_one({'email': email}, {'$set': dict(user)})
