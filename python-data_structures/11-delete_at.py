#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    # Check if the index is valid (not negative and within bounds)
    if 0 <= idx < len(my_list):
        # Delete the element by slicing before and after the index
        return my_list[:idx] + my_list[idx + 1:]
    return my_list  # Return the list unchanged if idx is invalid

