#!/usr/bin/python3

# Open the file and read its contents
file_content = '''#!/usr/bin/python3
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
    print(f"{a} + {b} = {add(a, b)}")'''

# Count occurrences
number_of_add_0 = file_content.count("add_0")
number_of_print = file_content.count("print")
number_of_a = file_content.count("a =")
number_of_b = file_content.count("b =")
number_of_add = file_content.count("add(a, b)")

# Print results
print(f"Number of occurrences of 'add_0': {number_of_add_0}")
print(f"Number of occurrences of 'print': {number_of_print}")
print(f"Number of occurrences of 'a =': {number_of_a}")
print(f"Number of occurrences of 'b =': {number_of_b}")
print(f"Number of occurrences of 'add(a, b)': {number_of_add}")

