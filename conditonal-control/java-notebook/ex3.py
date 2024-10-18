# Hemit Patel
# 781159
# MR VEERA
# Ex 3
# Oct 17 2024

eggs = int(input("Enter the number of eggs purchased:"))

dozens = eggs // 12 
leftover = eggs % 12

# Must initalize it before so that it is a global variable that can be accessed outside
# of the if clause

price_per_dozen = 0

if (0 <= dozens < 4):
    price_per_dozen = 0.5

elif (4 <= dozens < 6):
    price_per_dozen = 0.45

elif (6 <= dozens < 11):
    price_per_dozen = 0.40

elif (dozens >= 11):
    price_per_dozen = 0.35

bill_dozens = dozens * price_per_dozen
price_leftover = price_per_dozen * 1/12
bill_leftover = leftover * price_leftover
bill = bill_dozens + bill_leftover

# Using f string so i can get the $ sign near the bill
# allows the mixing of strings and variables of different data types

print(f"The bill is equal to ${bill}")
