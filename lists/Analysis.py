# Hemit Patel
# 781159
# ICS3U0-4 
# 11 dec 2024 
# Analysis (numbers)

from statistics import median, mean, mode

nums = []
total = 0

while (True):
     num = int(input())

     # sential of the infinte loop (will END it)
     if (num == 0):
         break

        
     nums.append(num)
     total += num

one_to_five = ""
six_to_ten = ""
eleven_to_fifteen = ""
sixteen_to_twenty = ""
twenty_one_to_twenty_five = ""
twenty_six_to_thirty = ""
thirty_one_to_thirty_five = ""
thirty_six_to_forty = ""
forty_one_to_forty_five = ""
forty_six_to_fifty = ""

for num in nums:
    if (1 <= num <= 5):
        one_to_five += "*"
    elif (6 <= num <= 10):
        six_to_ten += "*"
    elif (11 <= num <= 15):
        eleven_to_fifteen += "*"
    elif (16 <= num <= 20):
        sixteen_to_twenty += "*"
    elif (21 <= num <= 25):
        twenty_one_to_twenty_five += "*"
    elif (26 <= num <= 30):
        twenty_six_to_thirty += "*"
    elif (31 <= num <= 35):
        thirty_one_to_thirty_five += "*"
    elif (36 <= num <= 40):
        thirty_six_to_forty += "*"
    elif (41 <= num <= 45):
        forty_one_to_forty_five += "*"
    elif (46 <= num <= 50):
        forty_six_to_fifty += "*"

# Print the distribution
print("1-5:    " + one_to_five)
print("6-10:   " + six_to_ten)
print("11-15:  " + eleven_to_fifteen)
print("16-20:  " + sixteen_to_twenty)
print("21-25:  " + twenty_one_to_twenty_five)
print("26-30:  " + twenty_six_to_thirty)
print("31-35:  " + thirty_one_to_thirty_five)
print("36-40:  " + thirty_six_to_forty)
print("41-45:  " + forty_one_to_forty_five)
print("46-50:  " + forty_six_to_fifty)


nums_sorted = sorted(nums)

print("Average:", mean(nums))
print("Max:", max(nums))
print("Range:", max(nums) - min(nums))
print("Median:", median(nums_sorted))
print("Mode:", mode(nums_sorted))
