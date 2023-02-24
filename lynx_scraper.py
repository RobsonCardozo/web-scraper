import requests
from bs4 import BeautifulSoup
import json
import random
import tkinter as tk

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
        
    # Create a Tkinter window to display the data
    window = tk.Tk()
    window.title("Wikipedia Categories")
    window.geometry("600x400")
    
    # Create labels to display the data
    title_label = tk.Label(window, text=f"Title: {data['title']}", font=("Arial", 14))
    title_label.pack(pady=10)
    
    description_label = tk.Label(window, text=f"Description: {data['description']}", font=("Arial", 12), wraplength=500, justify="left")
    description_label.pack(pady=10)
    
    categories_label = tk.Label(window, text=f"Categories: {', '.join(data['categories'])}", font=("Arial", 12), wraplength=500, justify="left")
    categories_label.pack(pady=10)
    
    images_label = tk.Label(window, text=f"Images: {', '.join(data['images'])}", font=("Arial", 12), wraplength=500, justify="left")
    images_label.pack(pady=10)
    
    external_links_label = tk.Label(window, text=f"External Links: {', '.join(data['external_links'])}", font=("Arial", 12), wraplength=500, justify="left")
    external_links_label.pack(pady=10)
    
    # Create a button to close the window
    close_button = tk.Button(window, text="Close", command=window.destroy)
    close_button.pack(pady=10)
    
    window.mainloop()

extract_data_to_json()
