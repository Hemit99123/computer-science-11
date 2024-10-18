# Hemit Patel
# 781159
# ICS3U0-4
# Ex 10
# 18 oct 2024
# MR VEERA

import math

# Assigning this variable to avoid reduncy in the code of repeating the same string of text in the code
# which can cause problems later on when you want to change said piece of text to something else

output_text = "The volume is:"

# Dimensions for rectanglular prism
print("Rectangular Prism")
length_rectangular = int(input("Enter the length:"))
width_rectangular = int(input("Enter the width:"))
height_rectangular = int(input("Enter the height:"))

volume_rectangular = length_rectangular * width_rectangular * height_rectangular

print(f"{output_text} {volume_rectangular:.2f}")
print()
# Dimensions for sphere
print("Sphere")
radius_sphere = int(input("Enter the radius:"))

# Need diameter in the formula so assigning a variable for that (no need too but reads better)

diameter_sphere = radius_sphere * 2
volume_sphere = (math.pi * diameter_sphere ** 3) / (6)

print(f"{output_text} {volume_sphere:.2f}")
print()

# Dimensions for cube

print("Cube")
length_cube = int(input("Enter the length of each side:"))
volume_cube = length_cube ** 3
print(f"{output_text} {volume_cube:.2f}")
