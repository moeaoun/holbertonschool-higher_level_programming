#!/usr/bin/env python3
import json

def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary and save it to a file.
    
    Args:
        data (dict): The Python dictionary to be serialized.
        filename (str): The name of the file to save the serialized data.
    """
    with open(filename, 'w') as file:
        # Serialize the dictionary to a JSON formatted string and write to the file
        json.dump(data, file)

def load_and_deserialize(filename):
    """
    Load a JSON file and deserialize its content into a Python dictionary.
    
    Args:
        filename (str): The name of the file to load and deserialize from.
    
    Returns:
        dict: The deserialized Python dictionary.
    """
    with open(filename, 'r') as file:
        # Deserialize the JSON data from the file and return the resulting Python dictionary
        return json.load(file)

