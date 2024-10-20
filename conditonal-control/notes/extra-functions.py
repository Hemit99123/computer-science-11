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

# assert (produces an error) 
# good to use when you want to check for a condition that is troublesome and it will cause an error if that condition is meet
# it raises an assertionerror
# assertion is a condition that you expect to be True

assert age >= 0, "Age must be non-negative"

# here we are checking if age is a negative. if so we assert the error of "Age must be non-negative"
