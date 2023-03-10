import os
import sys
import json
import logging

from pymongo import MongoClient
from dotenv import load_dotenv
from data_extractor import extract_data
from gui import display_data

sys.stdout.reconfigure(encoding='utf-8')

load_dotenv()

MONGODB_URI = os.environ.get("MONGODB_URI")
MONGODB_DB_NAME = os.environ.get("MONGODB_DB_NAME")
MONGODB_COLLECTION_NAME = os.environ.get("MONGODB_COLLECTION_NAME")

client = MongoClient(MONGODB_URI)
db = client[MONGODB_DB_NAME]
collection = db[MONGODB_COLLECTION_NAME]

logging.basicConfig(level=logging.INFO)

def memory_card(data):
    with open("data.json", "w") as f:
        json.dump(data, f)

try:
    data = extract_data(memory_card)
    if data:
        result = collection.insert_one(data)
        logging.info(f"Inserted data with ID {result.inserted_id} into collection {MONGODB_COLLECTION_NAME}")
        display_data(data)
    else:
        logging.warning("Data is empty, cannot display in GUI.")
except Exception as e:
    logging.error(f"Failed to insert data into collection {MONGODB_COLLECTION_NAME}: {e}")
finally:
    client.close()
