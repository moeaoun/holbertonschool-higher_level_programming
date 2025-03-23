#!/usr/bin/python3

def print_tebahpla():
    print("".join([chr(122 - i) if i % 2 == 0 else chr(122 - i).upper() for i in range(26)]), end="")

