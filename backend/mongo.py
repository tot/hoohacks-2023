import os
from dotenv import load_dotenv
from pymongo import MongoClient


db_url = os.getenv("DB_URL")
client = MongoClient(db_url)
users = client["users"]
print(users)