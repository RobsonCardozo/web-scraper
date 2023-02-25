import json
import os
import requests
from bs4 import BeautifulSoup
import pymongo
import random


def extract_data_to_json():
    # random page from Wikipedia
    url = "https://en.wikipedia.org/wiki/Special:Random"

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Request failed for page {page_id}: {e}")
        return None

    soup = BeautifulSoup(response.content, "html.parser")
    title_element = soup.find("h1", id="firstHeading")
    title = title_element.text.strip() if title_element else ""
    description_element = soup.find("div", class_="lead-section")
    description_paragraph = (
        description_element.find("p") if description_element else None
    )
    description = description_paragraph.text.strip() if description_paragraph else ""
    categories_element = soup.find("div", class_="mw-normal-catlinks")
    categories_list = categories_element.find("ul") if categories_element else None
    categories = (
        [li.text for li in categories_list.find_all("li")] if categories_list else []
    )
    images_element = soup.find("div", class_="thumbinner")
    images = (
        [img["src"] for img in images_element.find_all("img")] if images_element else []
    )
    external_links_element = soup.find("div", id="External_links")
    external_links_list = (
        external_links_element.find_next("ul") if external_links_element else None
    )
    external_links = (
        [a["href"] for a in external_links_list.find_all("a")]
        if external_links_list
        else []
    )
    data = {
        "title": title,
        "description": description,
        "categories": categories,
        "images": images,
        "external_links": external_links,
    }
    json_data = json.dumps(data)
    try:
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["mydatabase"]
        collection = db["random"]

        result = collection.insert_one(json.loads(json_data))
        print(result.inserted_id)
    except pymongo.errors.PyMongoError as e:
        print(f"Failed to insert data into collection random: {e}")
        return None

    return data


if __name__ == "__main__":
    extract_data_to_json()
