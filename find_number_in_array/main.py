def find_number_in_array(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i  # returns the index of the found element
    return -1  # if the number is not found

# Example usage
numbers = [3, 7, 1, 9, 5]
target_number = 9

index = find_number_in_array(numbers, target_number)

if index != -1:
    print(f"The number {target_number} was found at position {index}.")
else:
    print(f"The number {target_number} was not found in the array.")
