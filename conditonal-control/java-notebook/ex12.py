# Hemit Patel
# 781159
# ICS3U0-4
# MR VEERA
# Ex 12
# 18 oct 2024

import math

x = int(input("Enter a value for x:"))
y = int(input("Enter a value for y:"))

# Get the irrelational number from the math lib so that it is the most accurately represented!

euler = math.e

# calculates x ^ y
result_math_model = euler ** (y*math.log(x))

# This is what the above does but without a mathemtical model doing the calculator
result_exp_operator = x ** y

print(f"{result_math_model:.11f}")

# This is already an integer so no need to round or anything of the sorts
print(result_exp_operator)
