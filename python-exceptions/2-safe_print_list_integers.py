#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            if isinstance(my_list[i], int):  # Check if it's an integer
                print("{:d}".format(my_list[i]), end="")
                count += 1
        except IndexError:
            break  # Stop if we reach an index out of range
    print()  # Ensure a newline after printing all integers
    return count

