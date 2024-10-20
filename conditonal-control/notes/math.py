# Lesson on Math functions Library
# ICS3U0
# Mr Veera
# 17 Oct 2024

from math import sin, tan, cos, atan, acos, asin, pi, e as euler, degrees, radians, log

angle=float(input("Give an angle: ")) 

# Converts angle from deg to radians   
angle_rad= radians(angle)
                                      

# gets sine from radian 
sine_value= sin(angle_rad)

# gets tan 
tan_value = tan(angle_rad) 

# gets cops
cos_value = cos(angle_rad) 

# rounded value
print(" Sine of {:.2f} Deg = {:.2f}".format(angle,sine_value))

# asin, atan and acos find the original angle theta based on the sin,cos,tan value

original_angle_rad = asin(sine_value)
original_angle_rad = acos(tan_value)
original_angle_rad = atan(cos_value)

# converts from radians to deg
original_angle_deg= degrees(original_angle_rad) 

# in trig, go to decimal places up to 4
print('Given angle is {:.4f} rad'.format(original_angle_rad))
print('Given angle is {:.2f} deg'.format(original_angle_deg))

print(pi) # gets pi constant
print(euler) # gets euler constant

logarithm_value = log(1000) # calculates logarithms
print(logarithm_value)


# Example of importing One function form tyhe math library
#ICS3U0
#Mr Veera
# 17 Oct 2024

# added an alias for e so it is more descriptive

from math import pi, e as euler

print(pi)
print(euler)
