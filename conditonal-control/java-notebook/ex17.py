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

# Hemit Patel
# MR VEERA 
# ICS3U0-4
# Oct 20 2024
# java notebook corrected question 17

from math import asin, acos, atan, degrees

# the sine, cosine and tangent values must be a float because they represent a fractional value (ratio of the diff sides of a right triangle)

sine = float(input("Enter sin value:"))
cosine = float(input("Enter cosine value:"))
tangent = float(input("Enter tangent value:"))

# assert is a function we use to throw an error if the condition is FALSE
# in our case, sine and cosine can only be between -1 and 1, so we reflect that 
# with our ranges and outputting an error if they are not
# the next part of the keyword is the error text which is seperated with a ,

assert -1 <= sine <= 1, "Sine value must be between 0 and 1"
assert -1 <= cosine <= 1, "Cosine value must be between 0 and 1"

# arcsin, arccos and arctan is inverse function of the trignometric functions of 
# sine, cosine and tangent
# this means they will do the opposite of the trig functions so input a ratio value and return the corresponding angle theta
# commonly denoted as the greek letter theta 
# this is why, we input the sine, cosine and tangent values into these functions

arcsine = asin(sine)
arccosine = acos(cosine)
arctangent = atan(tangent)

# the output of the angle theta is in radians, so we need to convert it to degrees

arcsine_deg = degrees(arcsine)
arccosine = degrees(arccosine)
arctangent = degrees(arctangent)

# in trig we mostly round to the 4 digit so i am reflecting that here with the syntax :.4f which is similar to the syntax of the .format()
# this looks more cleaner and easier to read hence why i choose this syntax

print(f"The arcsine of {sine} is {arcsine_deg:.4f}")
print(f"The arccosine of {cosine} is {arccosine:.4f}")
print(f"The arctangent of {tangent} is {arctangent:.4f}")
