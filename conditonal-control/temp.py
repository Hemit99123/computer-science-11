# Hemit Patel
# 781159
# ICS3U0
# Mr. Veera
# 12 oct 2024

temperature = int(input("Enter the temperature?"))

# Ranges are being used to determine the heat/cold

# Using == to determine if the temperature is equal to the range (0)

if (0 == temperature <= 10):
  print("Cold")

# These 3 elif statements use the same format to find in-between values that are inclusive

elif (11 <= temperature <= 20):
  print("Mild")

elif (21 <= temperature <= 30):
  print("Warm")

elif (31 <= temperature <= 40):
  print("Hot")

# Not using = in this range because it is not inclusive but rather below 0 and above 40

elif (0 < temperature > 40 ):
  print("Extereme")
