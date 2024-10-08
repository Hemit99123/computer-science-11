# Hemit Patel
# 781159
# ICS3U0-4 (reorged)
# Energy    
# INSTRUCTOR NAME
# 5 oct 2024

# The mass needed for our program to work
mass = int(input("Enter the mass in kilograms: "))

# The mathemtical equation of e=mc2 to find out energy produced 
speed_light = 3 * 10 ** 8
energy = mass * speed_light ** 2

# Calculating the amount of 100 watt lightbulbs that can be powered (360000 joules needed for one)
amount_100watt = energy / 360000

# Printing a formatted verison where numbers are shown with scienctific notation
print("The energy produced in joules is = {:.1E}".format(energy))
print("The number of 100 watt lightbulb powered is = {:.1E}".format(amount_100watt))