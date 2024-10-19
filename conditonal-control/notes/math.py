# Lesson on Math functions Library
# ICS3U0
# Mr Veera
# 17 Oct 2024

import math

angle=float(input("Give an angle: ")) 

angle_rad=math.radians(angle)    # Converts angle from deg to radians   
                                      

sine_value=math.sin(angle_rad)   # gets sine from radian CAN ONLY BE RADIAN
tan_value = math.tan(angle_rad) # gets tan 
cos_value = math.cos(angle_rad) # gets cops

print(" Sine of {:.2f} Deg = {:.2f}".format(angle,sine_value))

original_angle_rad = math.asin(sine_value)
original_angle_rad = math.atan(tan_value)
original_angle_rad = math.atan(cos_value)

# Inverse Trig( Inverse sine function)
# gets angle theta based on trig function (sin, cos or tan)

original_angle_deg=math.degrees(original_angle_rad) # converts from radians to deg

print('Given angle is {:.4f} rad'.format(original_angle_rad))
print('Given angle is {:.2f} deg'.format(original_angle_deg))

print(math.pi) # gets pi constant
print(math.e) # gets euler constant

logarithm_value = math.log(1000) # calculates logarithms
print(logarithm_value)
