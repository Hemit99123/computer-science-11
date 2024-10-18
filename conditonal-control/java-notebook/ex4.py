# Hemit Patel
# 781159
# MR VEERA
# Ex 4
# Oct 17 2024

model = int(input("Enter the car's model number:"))

if (model == 119 or model == 179 or 189 <= model <= 195 or model == 221 or model == 789):
    print("Your car is defective. It must be repaired")
else:
    print("Your car is not defective")


## BONUS, alternatively (this way looks better and is more easier to read)

# Put all defective models in an list which allows us to store a collection of things
# For the range of 189 to 195, I have simply manually written it out

defective_models = [119, 179, 189, 190, 191, 192, 193, 194, 195, 221, 780]

# This syntax will go through each one of these models in linear time 
# O(n) and check if it is == to the model input given by user
# If so it will output True otherwise it'll be false

if (model in defective_models):
    print("Your car is defective. It must be repaired")
else:
    print("Your car is not defective")
