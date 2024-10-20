# Lesson on Math functions Library
# ICS3U0
# Mr Veera
# 17 Oct 2024

import math

angle=float(input("Give an angle: ")) 

# Converts angle from deg to radians   
angle_rad=math.radians(angle)
                                      

# gets sine from radian 
sine_value=math.sin(angle_rad)

# gets tan 
tan_value = math.tan(angle_rad) 

# gets cops
cos_value = math.cos(angle_rad) 

# rounded value
print(" Sine of {:.2f} Deg = {:.2f}".format(angle,sine_value))

# asin, atan and acos find the original angle theta based on the sin,cos,tan value

original_angle_rad = math.asin(sine_value)
original_angle_rad = math.acos(tan_value)
original_angle_rad = math.atan(cos_value)

# converts from radians to deg
original_angle_deg=math.degrees(original_angle_rad) 

# in trig, go to decimal places up to 4
print('Given angle is {:.4f} rad'.format(original_angle_rad))
print('Given angle is {:.2f} deg'.format(original_angle_deg))

print(math.pi) # gets pi constant
print(math.e) # gets euler constant

logarithm_value = math.log(1000) # calculates logarithms
print(logarithm_value)
