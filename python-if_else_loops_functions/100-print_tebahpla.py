#!/usr/bin/python3

def print_tebahpla():
    for i in range(25, -1, -1):
        # Check if i is even (z, x, v,... should be lowercase)
        if i % 2 == 0:
            print(chr(122 - i), end="")
        else:
            print(chr(122 - i).upper(), end="")

