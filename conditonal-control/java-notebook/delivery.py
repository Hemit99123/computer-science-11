# Hemit Patel
# 781159
# ICS3U0-4
# Delivery
# MR VEERA
# 16 oct 2024


length = int(input("Enter the length:"))
width = int(input("Enter the width:"))
height = int(input("Enter the height:"))

# The most strictest (precise) cretria should be first followed by more
# leniant cretria that accepts more scenarios

if (length <= 10 and width <= 10 and height <= 10):
    print("Accept")

else:
    print("Reject")
