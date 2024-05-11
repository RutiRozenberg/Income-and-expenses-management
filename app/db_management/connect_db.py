from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['Income_and_expenses_management']
