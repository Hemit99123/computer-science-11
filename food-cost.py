# Hemit Patel
# STUDENT NUMBER
# ICS3U0-4 (reorged)
# Cost of food Calculator
# INSTRUCTOR NAME
# 4 oct 2024

burgers = int(input("Enter the amount of burgers:"))

fries = int(input("Enter the amount of fries"))

sodas = int(input("Enter the amount of sodas"))

tax = 0.065

burgers_cost = burgers * 1.69
fries_cost = fries * 1.09
sodas_cost = sodas * 0.99

subtotal = burgers_cost + fries_cost + sodas_cost

tax = subtotal * tax

total = subtotal + tax

print("Total before tax {:.2f}".format(subtotal))
print("Tax: {:.2f}".format(tax))
print("Final total: {:.2f}".format(total))
