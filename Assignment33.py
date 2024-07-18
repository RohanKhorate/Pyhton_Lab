# Function to calculate the mean of dictionary values
def calculate_mean(dictionary):
    # Get the sum of all values in the dictionary
    total_sum = 0
    for value in dictionary.values():
        total_sum += value
    
    # Calculate the mean by dividing the total sum by the number of items
    mean = total_sum / len(dictionary)
    
    return mean

# Example dictionary
test_dict = {"A": 6, "B": 9, "C": 5, "D": 7, "E": 4}

# Calculate and print the mean
mean_value = calculate_mean(test_dict)
print(f"The mean of the dictionary values is: {mean_value:.1f}")
#Output
#The mean of the dictionary values is: 6.2
