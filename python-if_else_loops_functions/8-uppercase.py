#!/usr/bin/python3
def uppercase(str):
    result = ""
    for c in str:
        if ord('a') <= ord(c) <= ord('z'):
            result += chr(ord(c) - 32)  # Convert to uppercase
        else:
            result += c  # Keep non-lowercase characters as is
    print("".join(result))  # Only one print function used here

