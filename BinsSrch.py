# Example usage

my_list = [1, 3, 5, 7, 9, 11]
target_value = 7

def binary_search(my_list, target_value):
    low = 0
    high = len(my_list) - 1

    while low <= high:
        mid = (low + high) // 2
        if my_list[mid] == target_value:
            return mid  # Target found, return its index
        elif my_list[mid] < target_value:
            low = mid + 1  # Target is in the upper half
        else:
            high = mid - 1  # Target is in the lower half

    return -1  # Target not found

# Perform binary search and print the result
index = binary_search(my_list, target_value)
if index != -1:
    print(f"Target {target_value} found at index {index}.")
else:
    print(f"Target {target_value} not found in the list.")
