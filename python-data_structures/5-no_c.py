#!/usr/bin/python3

def no_c(my_string):
    # Initialize an empty list to collect characters that are not 'c' or 'C'
    result = []
    
    # Loop through each character in the string
    for char in my_string:
        # If the character is not 'c' or 'C', add it to the result list
        if char != 'c' and char != 'C':
            result.append(char)
    
    # Join the result list into a new string and return it
    return ''.join(result)

