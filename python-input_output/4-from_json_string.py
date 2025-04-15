#!/usr/bin/python3
"""
This module provides a function that returns a Python object represented by a JSON string.
"""

import json

def from_json_string(my_str):
    """
    Converts a JSON string to a Python object.

    Args:
        my_str (str): The JSON string to convert.

    Returns:
        object: The corresponding Python object (dict, list, etc.).
    """
    return json.loads(my_str)

