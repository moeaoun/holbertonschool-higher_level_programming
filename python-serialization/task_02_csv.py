#!/usr/bin/env python3
import csv
import json

def convert_csv_to_json(csv_filename):
    """Convert CSV data to JSON format and save it to a file."""
    try:
        # Open the CSV file and read the data
        with open(csv_filename, mode='r', newline='') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = [row for row in csv_reader]  # List of dictionaries
            
        # Write the JSON data to data.json
        with open('data.json', mode='w') as json_file:
            json.dump(data, json_file, indent=4)
        
        return True
    except FileNotFoundError:
        print(f"The file {csv_filename} was not found.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

