# Hemit Patel
# MR VEERA 
# ICS3U0-4 
# 20 oct 2024
# extra functions notes 
# LAMBDA 
# creates a function in ONE LINE of code 
# good for quick/short functions to save lines of code
x_input = 1

# the x: is the inputs whilst x % 2 == 0 is the computation being done. it will return the value from that operation
is_even = lambda x: x % 2 == 0
is_even(x)

# Ternary Operator
# kinda the same thing as lamada but for if-else statements
# only use for simple if else, for complex write it out in proper form
# show this as an ALT to the regular simple if else

# ten
result = "Even" if x % 2 == 0 else "Odd"

# reg 

if (x%2 == 0):
  result = "Event"
else:
  result = "Odd"
