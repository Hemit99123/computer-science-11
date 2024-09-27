# Hemit Patel
# 781159
# ICS3U0-1
# Pizza Cost Calculator
# Mr Veera
# 25 sep 2024

# The input which is the diameter of the pizza

diameter = int(input("Enter your diameter in inches:"));


# The computation which is stored in an output of cost.
# It is the mathemtical model which takes into account the labour, materials and rent costs


rent = 1.00
labour = 0.75
materials = 0.05 * diameter * diameter

# Added () around materials because I want it to calculate before the addition
cost = rent + labour + (materials)

# Formatted it for rounding it 2 decimal places
print('The cost of making the pizza is {:.2f}'.format(cost))
