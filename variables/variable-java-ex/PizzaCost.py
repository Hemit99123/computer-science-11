# Hemit Patel
# 781159
# ICS3U0-4 (reorged)
# PizzaCost
# INSTRUCTOR NAME
# 5 oct 2024


diameter = int(input("Enter the diameter of the pizza in inches: "))

# Computation which includes a simple math equation that computes 3 costs (labour, materials and rent)

cost = (0.05 * diameter * diameter) + 0.75 + 1.00

# Printing a formatted verison where numbers are rounded to the second decimal place
print("The cost of making the pizza is {:.2f}".format(cost))