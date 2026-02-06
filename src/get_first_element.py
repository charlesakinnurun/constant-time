def get_first_element(data_list):
    """
    Example 1: Accessing an element in array/list

    This is O(1) because python list are implemented as contigous arrays
    To find the first element, the computer simply looks at the memory address
    of the start of the array. It doesn't matter if the list has 10
    elements or 10000000 elements; the jump to index 0 is instantenous
    """ 

    if not data_list:
        return None
    
    # This single operation is Constant Time

    return data_list[0]


small_list = [i for i in range(44,66)]
large_list = [i for i in list((565,77,738,898392,66272,83383))]

# Accessing the first element of the small list
print(f"Small list first item: {get_first_element(small_list)}")

# Accessing the first element of the large lits
# Notice that logically, this take the exact same amount of work for the CPU
print(f"Large list first item: {get_first_element(large_list)}")