import requests
from bs4 import BeautifulSoup
import json
import random

def extract_data_to_json():
    api_endpoint = "https://en.wikipedia.org/w/api.php"
    random_title = random.choice(requests.get(api_endpoint, params={
        "action": "query",
        "format": "json",
        "list": "random",
        "rnnamespace": "0",
        "rnlimit": "1"
    }).json()["query"]["random"])["title"]
    params = {
        "action": "query",
        "format": "json",
        "titles": random_title,
        "prop": "categories|images|extlinks|extracts",
        "cllimit": "max",
        "imlimit": "max",
        "ellimit": "max",
        "exintro": "1",
        "explaintext": "1"
    }
    response = requests.get(api_endpoint, params=params)
    data = {"title": "", "categories": [], "images": [], "external_links": [], "description": ""}
    if response.ok:
        try:
            page_data = response.json()["query"]["pages"]
            for _, page in page_data.items():
                data["categories"] = [category["title"] for category in page.get("categories", [])]
                data["images"] = [image["title"] for image in page.get("images", [])]
                data["external_links"] = [link["*"] for link in page.get("extlinks", [])]
                data["title"] = page.get("title", "")
                data["description"] = page.get("extract", "")
            with open("data.json", "w") as f:
                json.dump(data, f, indent=4)
        except KeyError:
            print("Failed to parse data from the Wikipedia API response.")
            print("Response content:")
            print(response.content)
    else:
        print(f"Failed to retrieve data from the Wikipedia API. Status code: {response.status_code}")

extract_data_to_json()
