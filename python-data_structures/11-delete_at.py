#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if 0 <= idx < len(my_list):
        return my_list[:idx] + my_list[idx + 1:]
    return my_list

# Main code to print after modification
my_list = [1, 2, 3, 4, 5]
idx = 3
new_list = delete_at(my_list, idx)

# Ensure that only these two prints happen
print(new_list)  # Expected: [1, 2, 3, 5]
print(my_list)   # Expected: [1, 2, 3, 4, 5]

