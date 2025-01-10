# Hemit Patel
# 781159
# ICS3U0-4 
# MR VEERA
# iso triangle
# 9 jan 2025

# the size of the triangle (how many "bars" there will be)
size = int(input("Enter size:"))

# the size of the bar and space
# these values are changed within iteration done later on

size_bar = 1 

# the initial value is one less than the initial size 
# this was a pattern i noticed

space_bar = size - 1

# functions used to create bars and add spae
def draw_bar(size):
    return "*" * size

def add_space(bar, size):
    return " " * size + bar + " " * size

# here for each of the bars needed to be created, we first draw the bar
# then we add the space to the bar 
# and update our bar attributes (size and space)

for _ in range(size):
    bar = draw_bar(size_bar)
    print(add_space(bar, space_bar))
    size_bar += 2
    space_bar -= 1
