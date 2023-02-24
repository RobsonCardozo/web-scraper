import requests
from bs4 import BeautifulSoup
import json


def extract_data_to_json():
    api_endpoint = "https://test.wikipedia.org/w/api.php"
    params = {
        "action": "parse",
        "format": "json",
        "page": "Special:Random",
        "prop": "text|categories|references"
    }
    response = requests.get(api_endpoint, params=params)
    data = {"title": "", "categories": [], "references": []}
    if response.ok:
        try:
            page_data = response.json()["parse"]["text"]["*"]
            soup = BeautifulSoup(page_data, "html.parser")
            categories_list = soup.find_all("div", {"class": "catlinks"})
            if categories_list:
                categories_list = categories_list[0].find_all("li")
                for category in categories_list:
                    data["categories"].append(category.text)
            else:
                print("No categories found on the page.")
            references_list = soup.find_all("ol", {"class": "references"})
            if references_list:
                for reference in references_list:
                    data["references"].append(reference.text)
            else:
                print("No references found on the page.")
            data["title"] = response.json()["parse"]["title"]
            with open("data.json", "w") as f:
                json.dump(data, f, indent=4)
        except KeyError:
            print("Failed to parse data from the Wikipedia API response.")
            print("Response content:")
            print(response.content)
    else:
        print(f"Failed to retrieve data from the Wikipedia API. Status code: {response.status_code}")
