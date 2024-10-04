# Hemit Patel
# STUDENT NUMBER
# ICS3U0-4 (reorged)
# Spending Calculator
# INSTRUCTOR NAME
# 4 oct 2024

# All the inputs needed 

time_second = int(input("Enter time in seconds:"))

hours = time_second // 3600
remainder = time_second % 3600
minutes = remainder // 60 
seconds = remainder % 60

# Printing the time in hours, minutes, and seconds
# Using the format function to make the time look nice (padded with 0 in sample too)

print("Time is {:02d}:{:02d}:{:02d}".format(hours, minutes, seconds))
