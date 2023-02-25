import os
import sys
import json
import pymongo

from dotenv import load_dotenv

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")
DB_NAME = os.getenv("MONGODB_DB_NAME")
COLLECTION_NAME = os.getenv("MONGODB_COLLECTION_NAME")


def get_collection():
    client = pymongo.MongoClient(MONGODB_URI)
    db = client[DB_NAME]
    collection = db[COLLECTION_NAME]
    return collection


def insert_data(data):
    collection = get_collection()
    result = collection.insert_one(data)
    print(
        f"Inserted data with ID {result.inserted_id} into collection {COLLECTION_NAME}"
    )


def get_data():
    collection = get_collection()
    data = collection.find_one()
    return data
