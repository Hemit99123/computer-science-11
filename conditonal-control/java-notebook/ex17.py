# Hemit Patel
# 781159
# ICS3U0-4
# MR VEERA
# ex 17
# oct 18 2024

## BIG QUESTION IS: THIS GIVES CORRECT OUTPUT BUT ISNT ASIN ACOS AND ATAN SUPPOSED TO TAKE THE VALUE OF SIN, COS, TAN AND OUTPUT ANGLE THETA?!?
## HERE WE ARE INPUTTING AN ANGLE TO THESE INVERSE FUNCTIONS WHICH MAKES NO SENSE TO ME

import math

angle = int(input("Enter an angle in degrees:"))

angle_radians = math.radians(angle)

arcsin = math.asin(angle_radians)
arccos = math.acos(angle_radians)
arctan = math.atan(angle_radians)


print(f"Arcsin: {arcsin:.2f}")
print(f"Arccos: {arccos:.2f}")
print(f"Arctan: {arctan:.2f}")
