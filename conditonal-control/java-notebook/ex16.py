# Hemit Patel
# 781159
# ICS3U0-4
# MR VEERA
# ex 16
# 18 oct 2024

import math

angle = int(input("Enter an angle in degrees:"))

# Need to convert angles to radian because the trig functions only accept radian not DEGREES

angle_radian = math.radians(angle)

# The trig functions being computed
sine = math.sin(angle_radian)
cosine = math.cos(angle_radian)
tangent = math.tan(angle_radian)

# Rounding 2 decimal places like question looks like
print(f"Sine: {sine:.2f}")
print(f"Cosine: {cosine:.2f}")
print(f"Tangent: {tangent:.2f}")
