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

    author_name = args.author.replace(" ", "%20")

    author1 = r"george%20orwell"
    author2 = r"donald%20trump"

    url1 = "https://openlibrary.org/search/authors.json?q=" + author1
    r1 = requests.get(query_url)

    url2 = "https://openlibrary.org/search/authors.json?q=" + author2
    r2 = requests.get(query_url)

    author_data = r.json()
    author_key = author_data["docs"][0]["key"]

    # write out raw data
    fname = f"author_{author_key}_works.json"
    with open(os.path.join(raw_path, fname), "w") as f:
        json.dump(books_data, f, indent=4)

if __name__ == "__main__":
    main()   