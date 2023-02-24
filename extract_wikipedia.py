import requests
from bs4 import BeautifulSoup
import json


def get_categories(soup):
    categories = []
    categories_list = soup.find_all("div", {"class": "catlinks"})
    if categories_list:
        categories_list = categories_list[0].find_all("li")
        categories = [category.text for category in categories_list]
    return categories


def extract_data_to_json():
    api_endpoint = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "titles": "Python_(programming_language)",
        "prop": "info|extracts|categories|images|extlinks",
        "cllimit": "max",
        "imlimit": "max",
        "ellimit": "max"
    }
    response = requests.get(api_endpoint, params=params)
    data = {"title": "", "categories": []}
    if response.ok:
        try:
            page_data = response.json()["query"]["pages"]
            for _, page in page_data.items():
                soup = BeautifulSoup(page["extract"], "html.parser")
                data["title"] = page.get("title", "")
                data["categories"] = get_categories(soup)
                data["images"] = [image["title"] for image in page.get("images", [])]
                data["external_links"] = [link["*"] for link in page.get("extlinks", [])]
            with open("data.json", "w") as f:
                json.dump(data, f, indent=4)
        except KeyError:
            print("Failed to parse data from the Wikipedia API response.")
            print("Response content:")
            print(response.content)
    else:
        print(f"Failed to retrieve data from the Wikipedia API. Status code: {response.status_code}")
