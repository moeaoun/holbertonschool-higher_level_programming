#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    # Make a copy of the list
    new_list = my_list[:]
    
    # Check if idx is a valid index, otherwise return the original list
    if idx < 0 or idx >= len(my_list):
        return new_list
    
    # Replace the element in the copied list
    new_list[idx] = element
    return new_list

