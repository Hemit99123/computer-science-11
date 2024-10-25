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

elif (51 <= data <= 150):
    price = 50 * 0.5  + (data-50) * 1

elif (151 <= data <= 300):
    price = 50 * 0.5 + 100 * 1 + (data-150) * 2

elif (data > 300):
    price = 50 * 0.5 + 100 * 1 + 150 * 2 + (data - 300) * 3

price += 20

print(price)
