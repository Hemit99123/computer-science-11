# Hemit Patel
# 781159
# ICS3U0-4 (reorged)
# Project Time Budgeter
# MR. VEERA
# 5 oct 2024

# Instructions to be printed to the end user about inputs
print("Enter the amount spent last month on the following items:")

# Empty line needed to seperate the instruction from input
print()

money_food = int(input("Food:"))
money_clothing = int(input("Clothing:"))
money_entertainment = int(input("Entertainment:"))
money_rent = int(input("Rent:"))

# Total that is needed for computation

total_spent = money_food + money_clothing + money_entertainment + money_rent

# Getting percentages of each item's money spent
percent_food = (money_food / total_spent) * 100
percent_clothing = (money_clothing / total_spent) * 100
percent_entertainment = (money_entertainment / total_spent) * 100
percent_rent = (money_rent / total_spent) * 100

# Empty line to seperate the input and output

print()

# Formatted with spaces so it resembles a table-like structure
print("{:<20}{:>11}".format("Category", "Budget"))
print("{:<20}{:>10.2f}%".format("Food", percent_food))
print("{:<20}{:>10.2f}%".format("Clothing", percent_clothing))
print("{:<20}{:>10.2f}%".format("Entertainment", percent_entertainment))
print("{:<20}{:>10.2f}%".format("Rent", percent_rent))