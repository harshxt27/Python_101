# Arrays
# This file contains functions to manipulate arrays

def print_array(arr):
    for i in arr:
        print(i)

def add_element(arr, element):
    arr.append(element)
    return arr

def remove_element(arr, element):
    arr.remove(element)
    return arr

# Example usage
if __name__ == "__main__":
    my_array = [1, 2, 3]
    print("Original array:")
    print_array(my_array)

    print("Array after adding an element:")
    add_element(my_array, 4)
    print_array(my_array)

    print("Array after removing an element:")
    remove_element(my_array, 2)
    print_array(my_array)

