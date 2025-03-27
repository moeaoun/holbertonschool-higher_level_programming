#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:  # If the list is empty
        return None
    
    max_val = my_list[0]  # Assume the first element is the maximum initially
    
    for num in my_list:
        if num > max_val:  # If we find a larger number, update max_val
            max_val = num
    
    return max_val  # Return the largest value found

