# Hemit Patel
# 781159
# ICS3U0-4 (reorged)
# Order
# MR VEERA
# 8 oct 2024

# all the inputs 
burgers = int(input("Enter the number of burgers:"))
fries = int(input("Enter the number of fries:"))
sodas = int(input("Enter the number of sodas:"))


# computation which gets the subtotal before tax and then computes the tax and total
subtotal = (burgers * 1.69) + (fries * 1.09) + (sodas * 0.99)

tax = subtotal * 0.065

total = subtotal + tax

print("Total before tax:{:.2f}".format(subtotal))
print("Tax: {:.2f}".format(tax))
print("Final total: {:.2f}".format(total))