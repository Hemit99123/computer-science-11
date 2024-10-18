# Hemit Patel
# 781159
# ICS3U0-4 (reorged)
# Q11 
# MR VEERA
# 8 oct 2024

from math import sqrt
a = int(input("Enter the value of a:"))
b= int(input("Enter the value of b:"))
c = int(input("Enter the value of c:"))

# First find the root from the equation

root = sqrt(b**2 - 4*a*c)

# Then find the two solutions
# -1 * b is to make the equation negative
b_value = -1*b

# Need 2 solutions since quadartic equation has 2 roots (one from adding)
# one from subtracting


root_solution_1 = (b_value + root) / (2*a)
root_soultion_2 = (b_value - root) / (2*a)

print(f'The roots are {root_solution_1} and {root_soultion_2}')
