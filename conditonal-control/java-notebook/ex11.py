# Hemit Patel
# MR VEERA
# ICS3UO-4
# Ex 11 - Quadratic Equation
# 781159
# 18 oct 2024

import math

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))

# First find the discriminant
discriminant = b**2 - 4*a*c

# Check if discriminant is non-negative (meaning there are 2 solutions)
# and therefore can be used in this equation as this equation produces
# 2 REAL numbers

if discriminant >= 0:
    # If non-negative, find the square root
    root = math.sqrt(discriminant)
    
    # Find the two solutions
    root_solution_1 = (-b + root) / (2*a)
    root_solution_2 = (-b - root) / (2*a)
    
    print(f'The roots are {root_solution_1:.1f} and {root_solution_2:.1f}')
else:
    print("This equation has complex roots.")
