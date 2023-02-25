import os
import sys
import json
import pymongo

from pymongo.errors import ConnectionFailure
from dotenv import load_dotenv

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")
DB_NAME = os.getenv("MONGODB_DB_NAME")
COLLECTION_NAME = os.getenv("MONGODB_COLLECTION_NAME")


def get_collection():
    try:
        client = pymongo.MongoClient(
            MONGODB_URI,
            serverSelectionTimeoutMS=5000,
            maxPoolSize=10
        )
        db = client[DB_NAME]
        collection = db[COLLECTION_NAME]
        return collection
    except ConnectionFailure:
        print("Failed to connect to MongoDB")
        sys.exit(1)


def insert_data(data):
    collection = get_collection()
    try:
        result = collection.insert_one(data)
        print(
            f"Inserted data with ID {result.inserted_id} into collection {COLLECTION_NAME}"
        )
    except Exception as e:
        print(f"Error inserting data: {e}")


def get_data():
    collection = get_collection()
    try:
        data = collection.find_one()
        return data
    except Exception as e:
        print(f"Error retrieving data: {e}")
        return None
