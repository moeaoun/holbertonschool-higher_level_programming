#!/usr/bin/python3

# Function to check if a character is lowercase
def islower(c):
    if ord('a') <= ord(c) <= ord('z'):
        return True
    return False

# Function to convert string to uppercase
def uppercase(str):
    for c in str:
        # If the character is lowercase, convert it to uppercase
        if islower(c):
            print(chr(ord(c) - 32), end="")  # Convert to uppercase
        else:
            print(c, end="")  # Print the character as it is
    print()  # Print a newline after the string


