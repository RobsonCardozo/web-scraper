import requests
from bs4 import BeautifulSoup
import random

def extract_data_to_json():
    # Choose a random page from English Wikipedia
    page_id = random.randint(1, 61301906)
    url = f"https://en.wikipedia.org/w/api.php?action=query&prop=extracts|categories|images|links&exintro&explaintext&format=json&pageids={page_id}"

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code != 200:
        print(f"Request failed with status code {response.status_code}")
        return None

    # Parse the JSON content of the response
    json_data = response.json()

    # Check if the required keys exist in the JSON data
    if "query" not in json_data or "pages" not in json_data["query"] or str(page_id) not in json_data["query"]["pages"]:
        print(f"Failed to find required keys in JSON data for page {page_id}")
        return None

    # Extract the HTML content of the page
    html_content = json_data["query"]["pages"][str(page_id)]["extract"]

    # Parse the HTML content of the page
    soup = BeautifulSoup(html_content, "html.parser")

    # Extract the title of the page
    title_element = soup.find("h1", id="firstHeading")
    if title_element is not None:
        title = title_element.text.strip()
    else:
        title = ""

    # Extract the page description
    description_element = soup.find("div", class_="lead-section")
    if description_element is not None:
        description_paragraph = description_element.find("p")
        if description_paragraph is not None:
            description = description_paragraph.text.strip()
        else:
            description = ""
    else:
        description = ""

    # Extract the categories of the page
    categories_element = soup.find("div", class_="mw-normal-catlinks")
    if categories_element is not None:
        categories_list = categories_element.find("ul")
        if categories_list is not None:
            categories = [li.text for li in categories_list.find_all("li")]
        else:
            categories = []
    else:
        categories = []

    # Extract the images on the page
    images_element = soup.find("div", class_="thumbinner")
    if images_element is not None:
        images = [img["src"] for img in images_element.find_all("img")]
    else:
        images = []

    # Extract the external links on the page
    external_links_element = soup.find("div", id="External_links")
    if external_links_element is not None:
        external_links_list = external_links_element.find_next("ul")
        if external_links_list is not None:
            external_links = [a["href"] for a in external_links_list.find_all("a")]
        else:
            external_links = []
    else:
        external_links = []

    # Convert the data to a dictionary
    data = {
        "title": title,
        "description": description,
        "categories": categories,
        "images": images,
        "external_links": external_links,
    }

    return data
