# Hemit Patel
# STUDENT NUMBER
# ICS3U0-1
# 3 digit finder
# INSTRUCTOR NAME
# 30 sep 2024

number = int(input("Enter a three digit number:"))

hundreds = number // 100

tens_units = number % 100

tens = tens_units // 10

ones = tens_units % 10

print("The hundreds-place digit is:", hundreds)
print("The tens-place digit is:", tens)
print("The unit-place digit is:", ones)
