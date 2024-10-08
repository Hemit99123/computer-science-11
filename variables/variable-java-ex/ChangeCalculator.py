# Hemit Patel
# 781159
# ICS3U0-4 (reorged)
# Change Calculator
# MR VEERA
# 5 oct 2024

# Input needed as a paramter for computation
change_cents = int(input("Enter the change in cents:"))

# Computation which includes grouping of the change into quarters, dimes, nickels (int div)
# Using % to find remaining change after the division operators
quarters = change_cents // 25 
remainder_1 = change_cents % 25
dimes = remainder_1 // 10
remainder_2 = remainder_1 % 10
nickels = remainder_2 // 5

# No need to use the remainder_3 variable because pennies do not need to be grouped into a speific number

pennies = remainder_2 % 5

# Printing an empty statement to create a space between the input and the output
print()
print("The minimum number of coins is:")

# Using tab (\t) to create even spacing between the coins as all coins are spaced away from the initial cursor position

print("\t Quarters:", quarters)
print("\t Dimes:", dimes)
print("\t Nickels:", nickels)
print("\t Pennies:", pennies)