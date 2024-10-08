# Hemit Patel
# STUDENT NUMBER
# ICS3U0-4 (reorged)
# Spending Calculator
# INSTRUCTOR NAME
# 4 oct 2024

# The input of the program 
chocolate_total = int(input("Enter the amount of chocolate produced:"))

# The computation bit which calculates the amount of chocolate produced in different boxes
regular = chocolate_total // 15
remainder_regular = chocolate_total % 15
gift = remainder_regular // 5
leftover = remainder_regular % 5

# Making a space between the input and the output
print()

# Printing out the results
print("Full regular boxes:", regular)
print("Gift boxes:", gift)
print("Leftover chocolate:", leftover)
