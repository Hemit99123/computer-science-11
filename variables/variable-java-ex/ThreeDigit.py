# Hemit Patel
# 781158
# ICS3U0-4 (reorged)
# Digit Calculator
# MR VEERA
# 5 oct 2024

# Input needed as a paramter for computation
number = int(input("Enter a three digit number:"))

# The computation which includes grouping the number into hundreds, tens and ones using int div
# Using % to find the remainder after the division operators

hundreths = number // 100
remainder_1 = number % 100
tenths = remainder_1 // 10
units = remainder_1 % 10

# Printing an empty line to create space between input and output
print()

print("The hundreds-place digit is:", hundreths)
print("The tens-place digit is:", tenths)
print("The ones-place digit is:", units)