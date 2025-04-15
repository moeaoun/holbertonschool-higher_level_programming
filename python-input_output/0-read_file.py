#!/usr/bin/python3
"""
This module provides a function to read and print the contents of a UTF-8 text file to stdout.
"""

def read_file(filename=""):
    """
    Reads a text file (UTF-8) and prints its contents to stdout.

    Args:
        filename (str): The path to the file to read. Defaults to an empty string.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end="")

