# 1. Suppose you have a dataset containing daily temperature readings for a city, and you want to identify days with extreme temperature conditions. Find days where the temperature either exceeded 35 degrees Celsius (hot day) or dropped below 5 degrees Celsius (cold day). 

# Input: temperatures = np.array([32.5, 34.2, 36.8, 29.3, 31.0, 38.7, 23.1, 18.5, 22.8, 37.2])

import numpy as np

# This is input Values
temperatures = np.array([32.5, 34.2, 36.8, 29.3, 31.0, 38.7, 23.1, 18.5, 22.8, 37.2, -2.0, 3, 4])

# Identifying hot days where temperature > 35 degrees Celsius
hot_Temp = np.where(temperatures>35)

# Printing the results in the desired format
print("Hot Days :")
print("Day \t Temperature  (°C)")

for i in hot_Temp[0]:
  print(f"{i+1}\t{temperatures[i]}")

# Identifying cold days where temperature < 5 degrees Celsius
cold_Temp = np.where(temperatures < 5)

# Printing the results in the desired format
print("Cold Days:")
print("Day\t Temperature  (°C)")

# Iterating over the indices of cold days and printing the day and temperature
for i in cold_Temp[0]:
  print(f"{i+1}\t{temperatures[i]}")


'''
Hot Days :
Day      Temperature  (°C)
3       36.8
6       38.7
10      37.2
Cold Days:
Day      Temperature  (°C)
11      -2.0
12      3.0
13      4.0

'''