import requests
import os.path
import json
import argparse

script_path = os.path.dirname(__file__)
raw_path = os.path.join("scripts", "..", "data", "raw")

def main():

    parse = argparse.ArgumentParser()
    parse.add_argument("author")

    args = parse.parse_args()

    author1 = r"george%20orwell"
    author2 = r"donald%20trump"

    url1 = "https://openlibrary.org/search/authors.json?q=" + author1
    r1 = requests.get(url1)

    url2 = "https://openlibrary.org/search/authors.json?q=" + author2
    r2 = requests.get(url2)

    author1_data = r1.json()
    author2_data = r2.json()

    # write out raw data
    fname = f"author1_theme.json"
    with open(os.path.join(raw_path, fname), "w") as f:
        json.dump(author1_data, f, indent=4)

    fname = f"author2_theme.json"
    with open(os.path.join(raw_path, fname), "w") as f:
        json.dump(author2_data, f, indent=4)

if __name__ == "__main__":
    main()   