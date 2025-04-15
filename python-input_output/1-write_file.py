#!/usr/bin/python3
"""
This module provides a function to write a string to a UTF-8 text file and return the number of characters written.
"""

def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF-8) and returns the number of characters written.

    Args:
        filename (str): The name of the file.
        text (str): The text to write to the file.

    Returns:
        int: The number of characters written.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)

