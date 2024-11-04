# Hemit Patel
# 781159
# ICS3U0-4
# MR VEERA 
# 4 nov 2024

amount = int(input("Enter the amount:"))
doubled = amount * 2
rate = float(input("Enter the percentage:")) / 100
year = 0

while True:
    interest = amount * rate
    amount += interest
    year += 1
    if (amount >= doubled):
        break

print(year, "years to reach ${}".format(doubled))
