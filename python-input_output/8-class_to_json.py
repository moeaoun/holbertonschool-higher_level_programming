#!/usr/bin/python3
"""
This module provides a function that returns the dictionary description
for JSON serialization of a simple object.
"""

def class_to_json(obj):
    """
    Returns the dictionary description for JSON serialization of an object.

    Args:
        obj: An instance of a class with serializable attributes.

    Returns:
        dict: A dictionary representation of the object.
    """
    return obj.__dict__

