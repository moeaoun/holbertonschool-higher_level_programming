#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if 0 <= idx < len(my_list):
        return my_list[:idx] + my_list[idx + 1:]
    return my_list

# Main code
my_list = [1, 2, 3, 4, 5]
idx = 3
new_list = delete_at(my_list, idx)

print(new_list)  # This should print the list after deletion
print(my_list)   # This should print the original list unchanged

