#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    # Create a copy of the list to avoid modifying the original list
    new_list = my_list[:]
    
    # If idx is out of range (negative or beyond the length of the list)
    if idx < 0 or idx >= len(new_list):
        return new_list
    
    # Remove the item at the given index by slicing
    return new_list[:idx] + new_list[idx + 1:]

