#!/usr/bin/python3

def best_score(a_dictionary):
    # Check if the dictionary is None or empty
    if not a_dictionary:
        return None
    
    # Use max to find the key with the highest value
    return max(a_dictionary, key=a_dictionary.get)

