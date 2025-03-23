#!/usr/bin/python3

def print_last_digit(number):
    last_digit = abs(number) % 10  # Get the last digit (positive number)
    print(last_digit, end="")       # Print the last digit without newline
    return last_digit               # Return the last digit

