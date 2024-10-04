# Hemit Patel
# STUDENT NUMBER
# ICS3U0-4 (reorged)
# Spending Calculator
# INSTRUCTOR NAME
# 4 oct 2024

# All the inputs needed 
print("Entire the amount spent in the last month on the following items:")
print()
food_cost = int(input("Enter the amount spent on food:"))
clothing_cost = int(input("Enter the amount spent on clothing:"))
entertainment_cost = int(input("Enter the amount spent on entertainment:"))
rent_cost = int(input("Enter the amount spent on rent:"))

# Getting the total amount of money spent
total = food_cost + clothing_cost + entertainment_cost + rent_cost

# Using that to find out how much percentage each item is of the total

food_percentage = (food_cost / total) * 100
clothing_percentage = (clothing_cost / total) * 100
entertainment_percentage = (entertainment_cost / total) * 100
rent_percentage = (rent_cost / total) * 100

# Outputting a formatted table using the formatted output for string (adds spaces)
# Also added numerical formatting to the table for rounding 2 decimal places
print()
print("{:<20}{:>10}".format("Task","% Time"))
print("{:<20}{:>10}".format("Food","{:.2f} %".format(food_percentage)))
print("{:<20}{:>10}".format("Clothing","{:.2f} %".format(clothing_percentage)))
print("{:<20}{:>10}".format("Entertainment","{:.2f} %".format(entertainment_percentage)))
print("{:<20}{:>10}".format("Rent","{:.2f} %".format(rent_percentage)))
