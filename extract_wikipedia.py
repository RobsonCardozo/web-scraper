import requests
import json


def extract_data_to_json():
    api_endpoint = "https://www.mediawiki.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "titles": "MediaWiki",
        "prop": "categories|images|extlinks",
        "cllimit": "max",
        "imlimit": "max",
        "ellimit": "max",
    }
    response = requests.get(api_endpoint, params=params)
    data = {"title": "", "categories": [], "images": [], "external_links": []}
    if response.ok:
        try:
            page_data = response.json()["query"]["pages"]
            for _, page in page_data.items():
                data["categories"] += [
                    category["title"] for category in page.get("categories", [])
                ]
                data["images"] += [image["title"] for image in page.get("images", [])]
                data["external_links"] += [
                    link["*"] for link in page.get("extlinks", [])
                ]
                data["title"] = page.get("title", "")
            with open("data.json", "w") as f:
                json.dump(data, f, indent=4)
        except KeyError:
            print("Failed to parse data from the MediaWiki API response.")
            print("Response content:")
            print(response.content)
    else:
        print(
            f"Failed to retrieve data from the MediaWiki API. Status code: {response.status_code}"
        )
    return data


if __name__ == "__main__":
    data = extract_data_to_json()
    print(data["categories"])
