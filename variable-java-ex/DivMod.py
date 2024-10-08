# Hemit Patel
# 781159
# ICS3U0-4 (reorged)
# DivAndMod
# MR. VEERA
# 5 oct 2024

first = int(input("Enter an integer:"))
second = int(input("Enter a second integer:"))

# Int division operations (//)
first_int_second = first // second 
second_int_first = second // first

# Mod division operation (%)
first_mod_second = first % second
second_mod_first = second % first

# Printing an empty statement to create a space between the input
print()

# Printing operators from first to second

# Used / instead of // because sample input is using /
print(first, "/", second, "=", first_int_second)
print(first, "%", second, "=", first_mod_second)

# Seperating to the next print statements using empty statement
print()

print(second, "/", first, "=", second_int_first)
print(second, "%", first, "=", second_mod_first)