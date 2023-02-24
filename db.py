import pymongo
from dotenv import load_dotenv
import os

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")
DB_NAME = os.getenv("DB_NAME")
COLLECTION_NAME = "random"

def get_collection():
    client = pymongo.MongoClient(MONGODB_URI)
    db = client[DB_NAME]
    collection = db[COLLECTION_NAME]
    return collection

def insert_data(data):
    collection = get_collection()
    collection.insert_one(data)

def get_data():
    collection = get_collection()
    data = collection.find_one()
    return data
