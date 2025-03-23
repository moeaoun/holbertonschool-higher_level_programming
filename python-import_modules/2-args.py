#!/usr/bin/python3
import sys

if __name__ == "__main__":
    # Get the number of arguments
    num_arguments = len(sys.argv) - 1  # Exclude the script name

    if num_arguments == 0:
        print("0 arguments.")
    elif num_arguments == 1:
        print("1 argument:")
    else:
        print(f"{num_arguments} arguments:")

    # Print each argument with its position
    for i in range(1, num_arguments + 1):
        print(f"{i}: {sys.argv[i]}")

