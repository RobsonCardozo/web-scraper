import os
import sys
import json
import random
import requests

from bs4 import BeautifulSoup

class DataExtractionError(Exception):
    pass

def extract_data(memory_card):
    url = "https://en.wikipedia.org/wiki/Special:Random"

    with requests.Session() as session:
        try:
            response = session.get(url)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            raise DataExtractionError(f"Request failed: {e}")

        soup = BeautifulSoup(response.content, "html.parser")

        title_element = soup.find("h1", id="firstHeading")
        title = title_element.text.strip() if title_element else ""

        description_element = soup.find("div", class_="lead-section")
        description_paragraph = (description_element.find("p") if description_element else None)
        description = description_paragraph.text.strip() if description_paragraph else ""

        categories_element = soup.find("div", class_="mw-normal-catlinks")
        categories_list = categories_element.find("ul") if categories_element else None
        categories = [li.text for li in categories_list.find_all("li")] if categories_list else []

        images_element = soup.find("div", class_="thumbinner")
        images = [img["src"] for img in images_element.find_all("img")] if images_element else []

        external_links_element = soup.find("div", id="External_links")
        external_links_list = external_links_element.find_next("ul") if external_links_element else None
        external_links = [a["href"] for a in external_links_list.find_all("a")] if external_links_list else []

        data = {
            "title": title,
            "description": description,
            "categories": categories,
            "images": images,
            "external_links": external_links,
        }

        memory_card(data)
        return data
