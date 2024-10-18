# Hemit Patel
# 781159
# MR VEERA
# Ex 2
# Oct 17 2024

weight = int(input("Enter the weight in kg:"))
length = int(input("Enter the length in cm:"))
width = int(input("Enter the width in cm:"))
height = int(input("Enter the height in cm:"))


# Employing lwh to find cubic cm as length,width and height are all in cm

size = length * width * height

if (weight > 27 and size > 100000):
    print("Too heavy and too large");

elif (weight > 27):
    print("Too heavy");

elif (size > 100000):
    print("Too large")

## BONUS: added an output for if the box meet the requirements

else:
    print("Box is accepted")
