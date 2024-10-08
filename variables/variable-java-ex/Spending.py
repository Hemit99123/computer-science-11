# Hemit Patel
# 781159
# ICS3U0-4 (reorged)
# Spending
# MR VEERA
# 8 oct 2024

print("Enter the amount spent last month on the following items:")
print()

food_money = int(input("Food:"))
clothing_money = int(input("Clothing:"))
entertainment_money = int(input("Entertainment:"))
rent_money = int(input("Rent:"))

total = food_money + clothing_money + entertainment_money + rent_money

food_percent = (food_money / total) * 100
clothing_percent = (clothing_money / total) * 100
entertainment_percent = (entertainment_money / total) * 100
rent_percent = (rent_money / total) * 100

print()
print("{:<25}{:<10}".format("Category","Budget"))
print("{:<25}{:<5.2f}%".format("Food",food_percent))
print("{:<25}{:<5.2f}%".format("Clothing",clothing_percent))
print("{:<25}{:<5.2f}%".format("Entertainment",entertainment_percent))
print("{:<25}{:<5.2f}%".format("Rent",rent_percent))
