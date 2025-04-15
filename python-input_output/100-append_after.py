#!/usr/bin/python3
"""
Function to append a line after each line containing a specific string.
"""

def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text (new_string) after each line containing the search_string.
    """
    # Open the file for reading and writing (read mode to check content, write mode to update it)
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Open the file again in write mode to overwrite it with the updated content
    with open(filename, 'w') as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)

