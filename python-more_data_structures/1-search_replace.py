#!/usr/bin/python3

def search_replace(my_list, search, replace):
    # Use a list comprehension to replace all occurrences of 'search' with 'replace'
    return [replace if x == search else x for x in my_list]

