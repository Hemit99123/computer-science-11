# Hemit Patel
# 781159
# ICS3U0
# Mr. Veera
# Leap Year Converter
# 14 oct 2024


'''
How would you design a program that determines whether a year is a leap year, but only if the year is also a multiple of 5, or the century begins with an odd digit? 
'''


year = int(input("Enter the year:"))

# The comparision operators makes these variables boolean values 

multiple_of_four = year % 4 == 0
multiple_of_five = year % 5 == 0

# Assuming that a year only has 4 digits

# This gets all the digits except for the thousands because they were grouped in the int division

century = year % 1000

# This will get the groups of 100s

century_first_digit = century // 100

# Odd digits are never divisable by two, therefore it makes sense to see if 
# remainder produces a non-zero integer
# Will produce boolean value of true if NOT zero

is_odd_century = century_first_digit % 2 != 0


# Using the conditional operators to see if it is the proper year and using connectors 
# of and/or to fit multiple conditions in one if statement

if (multiple_of_four and multiple_of_five or is_odd_century):
  print("This is the year!")

else:
  print("Is NOT the year!")
