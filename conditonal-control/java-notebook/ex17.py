# Hemit Patel
# 781159
# ICS3U0-4
# MR VEERA
# ex 17
# oct 18 2024

import math

angle = int(input("Enter an angle in degrees:"))

angle_radians = math.radians(angle)

arcsin = math.asin(angle_radians)
arccos = math.acos(angle_radians)
arctan = math.atan(angle_radians)


print(f"Arcsin: {arcsin:.2f}")
print(f"Arccos: {arccos:.2f}")
print(f"Arctan: {arctan:.2f}")