# Hemit Patel
# 781159
# ICS3U0-4
# MR VEERA
# internet data usage bill
# 25 oct 2024

'''

first 50 gb - 0.5 per gb
next 51 to 150 gb - 1 per gb
next 151 to 300 gb - 2 per gb
above 300 gb - 3 per gb

'''

data = int(input())

if (data <= 50):
    price = data * 0.5

# here the last range of up to 50 is accounted for because 51
# is larger than the highest limit so it can be fully accounted
# whatever is leftover is being multiplied by

elif (51 <= data <= 150):
    price = 50 * 0.5  + (data-50) * 1

# here the up to 50 range is accounted for and also the last range of 51 - 150
# the amount of gbs in between that range is 100 gbs, so we account for that because
# we want to account for ALL data used in that range.
# whatever is above 150 (starting of 151) will be accounted for with the pricing for 151-300
elif (151 <= data <= 300):
    price = 50 * 0.5 + 100 * 1 + (data-150) * 2

# same logic here but with one extra range to FULLY account for

elif (data > 300):
    price = 50 * 0.5 + 100 * 1 + 150 * 2 + (data - 300) * 3

# add 20 to the final price because this is the base pricing
# which remains the same regardless of other conditions

price += 20

print(price)


# Hemit Patel
# 781159
# ICS3U0-4 
# MR VEERA
# 25 oct 2024 

'''

first 30 cubic meters - 0.25 
next 100 - 0.5
next 100 - 0.7
above 230 - 0.96
peak hour doubles the rate

'''


usage = int(input("Enter the usage amount:"))
peak_hours = input("Is it peak hours?:")


if (usage <= 30):
    cost = usage * 0.25

# range is from 31 to 130 to account for the 30 units in the prior range (100+30)

elif (31 <= usage <= 130):
    # the remaining usage is from 31 to current so we subtract by 30 so that 31 can be accounted for and does it result in a negative (usage-30)
    cost = 30 * 0.25 + (usage-30) * 0.5

elif (131 <= usage <= 230):
    cost = 30 * 0.25 + 100 * 0.5 + (usage-130) * 0.7 

else:
    cost = 30 * 0.25 + 100 * 0.5 + 100 * 0.7 + (usage-230) * 0.96

# this is an independant decision that is not affected by the pricing of the usage

if (peak_hours == "True"):
    cost = cost * 2 
