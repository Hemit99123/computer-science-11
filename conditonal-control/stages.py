# Hemit Patel
# 781159
# ICS3U0-4 (reorged)
# Conditional Control
# MR VEERA
# 12 oct 2024


age = int(input("Enter the age of the child:"))

# First checking if age is above 18
if age > 18:
  print("Adult")


# The elif statements are in asc order because we are checking for < (less than)
# these comparision operators would be true for a larger number in a small input
# e.g. if age <=12 was first and input was 4 it would be true 
# but 4 != to preteen 

# If not true, then checking if age is below/equal to 5

elif age <= 5:
  print("Toddler")

# If not true, checking if age is below/equal to 10

elif age <= 10:
  print("Child")

# If not true, checking if age is below/equal to 12

elif age <= 12:
  print("Preteen")

# If none of these are true, the age range is 13-17 which is teenager

else:
  print("Teen")
