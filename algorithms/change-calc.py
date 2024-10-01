# Hemit Patel
# STUDENT NUMBER
# ICS3U0-4
# Change Calculator
# INSTRUTOR NAME
# 1 oct 2024


change = int(input("Eneter the change in cents:"))

quarters = change // 25

remainder = change % 25

dimes = remainder // 10

remainder_2 = remainder % 10

nickels = remainer_2 // 5

pennies = remainder_2 % 5

print("The minimum number of coins is:")

print("Quarters", quarters)
print("Dimes", dimes)
print("Nickels", nickels)
print("Pennies", pennies)
