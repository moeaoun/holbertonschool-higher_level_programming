#!/usr/bin/python3
def uppercase(str):
    result = ""
    for char in str:
        # Convert lowercase letters to uppercase by checking their ASCII values
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)  # Convert to uppercase by adjusting ASCII value
        else:
            result += char  # If not lowercase, just add the character as is
    print("{}".format(result))  # Using .format() for the final print

