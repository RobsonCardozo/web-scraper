import json
from extract_wikipedia import extract_data_to_json

def main():
    extract_data_to_json()
    with open("data.json") as f:
        data = json.load(f)
        if data["categories"] is None:
            print("No categories found on the page.")
        else:
            print(data["categories"])

if __name__ == "__main__":
    main()
