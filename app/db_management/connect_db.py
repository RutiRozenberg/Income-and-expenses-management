from pymongo import MongoClient


# Create a MongoClient instance to connect to the MongoDB database
client = MongoClient('mongodb://localhost:27017/')


# Access the 'Income_and_expenses_management' database within the MongoClient
db = client['Income_and_expenses_management']


"""
This Python script establishes a connection to a MongoDB database using the pymongo library.
The MongoClient class is initialized with the connection string 'mongodb://localhost:27017/' 
to connect to a MongoDB server running on the local machine on port 27017.

The 'Income_and_expenses_management' database is accessed within the client using db = client['Income_and_expenses_management'].
This database will be used for storing data related to income and expenses management.
"""

