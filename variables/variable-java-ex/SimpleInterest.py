# Hemit Patel
# 781159
# ICS3U0-4 (reorged)
# Simple Interest
# MR VEERA 
# 8 oct 2024

# Ask the user for the principal, rate and time

principal = int(input("Enter the principal amount:"))

years = int(input("Enter the number of years:"))

rate = float(input("Enter the interest rate:"))

# Calculate the simple interest
simple_interest = principal * (1 + years * rate)

total = simple_interest + principal
print("The value after the term is: $", simple_interest)