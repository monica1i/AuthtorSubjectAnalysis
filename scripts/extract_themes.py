import requests
import json
import os.path
import argparse

def main():
    # Directory setup
    script_dir = os.path.dirname(__file__)
    raw_path = os.path.join(script_dir, "..", "data")

    # Argument parsing
    parser = argparse.ArgumentParser(description="Extract author details from a JSON file and save first two entries formatted into a new JSON file")
    parser.add_argument("filename", help="The JSON file containing author data")
    args = parser.parse_args()

    # Full path of the input JSON file
    json_file = os.path.join(raw_path, args.filename)

    # Load JSON data
    try:
        with open(json_file, 'r') as file:
            parsed_data = json.load(file)
    except FileNotFoundError:
        print(f"File not found: {json_file}")
        return
    except json.JSONDecodeError:
        print("Error decoding JSON.")
        return

    # Ensure there are at least two entries in the file
    if not parsed_data.get('docs') or len(parsed_data['docs']) < 2:
        print("Not enough entries found in the JSON file (need at least two).")
        return

    # Extract first two entries
    first_entry = parsed_data['docs'][0]
    second_entry = parsed_data['docs'][1]

    # Format extracted data
    formatted_data = [
        {
            "key": first_entry.get('key'),
            "name": first_entry.get('name'),
            "top_subjects": first_entry.get('top_subjects', [])
        },
        {
            "key": second_entry.get('key'),
            "name": second_entry.get('name'),
            "top_subjects": second_entry.get('top_subjects', [])
        }
    ]

    # Define output path for formatted data
    output_file = os.path.join(raw_path, f"{args.filename}_themes.json")


    # Save formatted data to JSON file
    try:
        with open(output_file, 'w', encoding='utf-8') as outfile:
            json.dump(formatted_data, outfile, indent=4, ensure_ascii=False)
        print(f"Formatted data successfully saved to: {output_file}")
    except Exception as e:
        print(f"Error saving formatted JSON: {e}")

if __name__ == "__main__":
    main()
