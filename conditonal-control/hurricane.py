# Hemit Patel
# 781159
# ICS3U0-4
# Hurricane Classifer
# MR VEERA
# 13 oct 2024

speed = int(input("Enter the speed of the hurricane:"))

# No need for any type casting as input is str by default
unit = input("Enter the unit of speed (mph or km or kt):")

# The outputs are all in variables to avoid redundancy with the code
category_1 = "Category 1: 74-95 mph or 64-82 kt or 119-153 km/hr"
category_2 = "Category 2: 96-110 mph or 83-95 kt or 154-177 km/hr"
category_3 = "Category 3: 111-130 mph or 96-113 kt or 178-209 km/hr"
category_4 = "Category 4: 131-155 mph or 114-135 kt or 210-249 km/hr"
category_5 = "Category 5: greater than 155 mph or 135 kt or 249 km/hr"

# The category is determined based on the type of unit being used as ranges differ
# For each unit, we run nested if statements to find the category for the speific speed entered by the user
# Going in ASC order for elifs because it is much better to read
if (unit == "km"):
  if (119 <= speed <= 153):
    print(category_1)
  elif (154 <= speed <= 177):
    print(category_2)
  elif (178 <= speed <= 209):
    print(category_3)
  elif (210 <= speed <= 249):
    print(category_4)
  else:
    print(category_5)

elif (unit == "kt"):
  if (64 <= speed <= 82):
    print(category_1)
  elif (83 <= speed <= 95):
    print(category_2)
  elif (96 <= speed <= 113):
    print(category_3)
  elif (114 <= speed <= 135):
    print(category_4)
  else:
    print(category_5)

elif (unit == "mph"):
  if (74 <= speed <= 95):
    print(category_1)
  elif (96 <= speed <= 110):
    print(category_2)
  elif (111 <= speed <= 130):
    print(category_3)
  elif (131 <= speed <= 155):
    print(category_4)
  else:
    print(category_5)


# If none of these units are used, output the following to let user know and to allow fixes to occur to their inputs (error handling)

else:
  print("This is not a recognized unit of speed.")
  print()
  print("Please enter either mph, kt, or km.")
