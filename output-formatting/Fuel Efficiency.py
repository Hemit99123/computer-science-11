# Hemit Patel
# STUDENT NUMBER
# ICS3U0-4 (reorged)
# Spending Calculator
# INSTRUCTOR NAME
# 4 oct 2024

# The inputs that are cascaded with float type

driven_km = float(input("Enter the number of kilometers driven: "))
fuel_liters = float(input("Enter the amount of fuels used in liters"))

# Mathemtical model put into use to find fuel efficiency

efficiency = driven_km / fuel_liters

# Printing the results but with formatting so efficiency only shows one decimal place (rouding)

print("Fuel efficiency is {:.1f} km per liter.".format(efficiency))
