# Hemit Patel
# STUDENT NUMBER
# ICS3U0-4 (reorged)
# Spending Calculator
# INSTRUCTOR NAME
# 4 oct 2024

# Asking for the equipment information needed
total = int(input("Enter the total amount of equipment:"))
volleyballs = int(input("Enter the amount of volleyballs:"))

# Computing the amount of basketballs and soccerballs
basket_soccer = total - volleyballs

# Grouping the amounts to their respective bags amount
bags = basket_soccer // 10
volley_bags = volleyballs // 3

# The leftover amounts which couldn't be grouped sadly
remainder_bags = basket_soccer % 10
remainder_volley = volleyballs % 3

# The sum of those leftovers so it accurately portrays all types of equipment
leftover = remainder_bags + remainder_volley

# Printing it to shell for user to view
print("The amount of bags is", bags)
print("The amount of volleyball bags is", volley_bags)
print("The amount of leftover is", leftover)
