def delete_at(my_list=[], idx=0):
    # Check if the index is valid (within the list's range)
    if idx < 0 or idx >= len(my_list):
        return my_list
    
    # If index is valid, delete the element at that position
    return my_list[:idx] + my_list[idx+1:]

