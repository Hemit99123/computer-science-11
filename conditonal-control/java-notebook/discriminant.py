# Hemit Patel
# 781159
# ICS3U0-4
# MR VEERA
# Discriminant
# 14 oct 2024

a_value = int(input("Enter the value for a:"))
b_value = int(input("Enter the value for b:"))
c_value = int(input("Enter the value for c:"))

# The discriminant which uses the mathematical formula of 
# b to the power of 2 - 4ac

discriminant = b_value ** 2 - 4*a_value*c_value

# Going in ASC order (least to greatest)
# <0 means lower than 0 which is negative
# >0 means higher than 0 which is postive
# == 0 means that the discriminant is equal to the actual number of 0

if (discriminant < 0):
    print("No roots")

elif (discriminant == 0):
    print("One root")

# It must be a postive integer if it isnt negative or 0 (so this is when discriminant 
# is a postive value)

else:
    print("Two roots")
