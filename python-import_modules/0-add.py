#!/usr/bin/python3
from add_0 import add

if __name__ == "__main__":
    a = 1
    b = 2
    print(f"{a} + {b} = {add(a, b)}")

    a = 10
    b = 30
    print(f"{a} + {b} = {add(a, b)}")

    a = -10
    b = 30
    print(f"{a} + {b} = {add(a, b)}")

    a = -10
    b = -30
    print(f"{a} + {b} = {add(a, b)}")

    a = 5
    b = "H"
    print(f"{a} + {b} = {add(a, b)}")

