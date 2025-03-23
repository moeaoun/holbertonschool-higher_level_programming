#!/usr/bin/python3
import sys

if __name__ == "__main__":
    # Initialize the sum as 0
    total = 0

    # Loop through the arguments (excluding the script name)
    for arg in sys.argv[1:]:
        total += int(arg)  # Convert each argument to an integer and add to the total

    # Print the total sum
    print(total)

