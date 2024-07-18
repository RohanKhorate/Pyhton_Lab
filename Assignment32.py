def find_largest_and_smallest(numbers):
    if not numbers:
        return None, None  # Return None if the list is empty
    
    # Initialize largest and smallest with the first element of the list
    largest = numbers[0]
    smallest = numbers[0]

    # Iterate through the list starting from the second element
    for num in numbers[1:]:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num

    return largest, smallest

# Example usage
my_list = [5, 3, 8, 1, 9, 2]
largest, smallest = find_largest_and_smallest(my_list)
print(f"The largest number in the list is: {largest}")
print(f"The smallest number in the list is: {smallest}")
#Output
#The largest number in the list is: 9
#The smallest number in the list is: 1
