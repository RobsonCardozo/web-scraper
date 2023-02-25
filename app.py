from pymongo import MongoClient
from dotenv import load_dotenv
from data_extractor import extract_data_to_json
from gui import display_data_in_gui

import os

load_dotenv()

MONGODB_URI = os.environ.get("MONGODB_URI")
MONGODB_DB_NAME = os.environ.get("MONGODB_DB_NAME")
MONGODB_COLLECTION_NAME = os.environ.get("MONGODB_COLLECTION_NAME")

client = MongoClient(MONGODB_URI)
db = client[MONGODB_DB_NAME]
collection = db[MONGODB_COLLECTION_NAME]

try:
    data = extract_data_to_json()
    if data:
        result = collection.insert_one(data)
        print(
            f"Inserted data with ID {result.inserted_id} into collection {MONGODB_COLLECTION_NAME}"
        )
        display_data_in_gui(data)
    else:
        print("Data is empty, cannot display in GUI.")
except Exception as e:
    print(f"Failed to insert data into collection {MONGODB_COLLECTION_NAME}: {e}")
