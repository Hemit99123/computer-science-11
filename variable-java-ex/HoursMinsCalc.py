# Hemit Patel
# 781159
# ICS3U0-4 (reorged)
# Time in hours and minutes Calculator
# Mr Veera
# 5 oct 2024

times_mins = int(input("Enter the time in minutes:"))

# Grouping the time into hours using int div
hours = times_mins // 60

# Finding any minutes that were not able to be grouped into hours using %
leftover_mins = times_mins % 60

# The f"" is the same as the format function with different syntax

#The leftover minutes is getting a padding of 00 (2 digits) 
# so that single digits look like 2 digit numerals like 01,04,03 etc..

print(f"The time is: {hours}:{leftover_mins:02d}")