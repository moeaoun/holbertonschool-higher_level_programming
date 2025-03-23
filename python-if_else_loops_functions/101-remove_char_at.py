#!/usr/bin/python3

def remove_char_at(str, n):
    if n < 0:
        n = len(str) + n  # Convert negative index to positive equivalent
    if n < 0 or n >= len(str):  # If the index is out of bounds
        return str
    return str[:n] + str[n+1:]
 
