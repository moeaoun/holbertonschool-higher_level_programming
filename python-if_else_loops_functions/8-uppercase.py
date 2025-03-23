#!/usr/bin/python3

def islower(c):
    # Check if the character is lowercase by its ASCII value
    return ord('a') <= ord(c) <= ord('z')

def uppercase(str):
    result = ""
    for c in str:
        if islower(c):
            result += chr(ord(c) - 32)  # Convert lowercase to uppercase
        else:
            result += c  # Keep non-lowercase characters unchanged
    
    # Print the final result
    print(result)

