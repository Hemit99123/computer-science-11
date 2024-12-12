# Hemit Patel
# 781159
# ICS3U0-4 
# 11 dec 2024 
# Analysis (numbers)

from statistics import median, mean, mode

nums = []

while (True):
     num = int(input())

     # sential of the infinte loop (will END it)
     if (num == 0):
         break

        
     nums.append(num)
     
ranges = [0,0,0,0,0,0,0,0,0,0]
ranges_name = ["1-5", "6-10", "11-15", "16-20", "21-25", "26-30", "31-35", "36-40", "41-45", "45-50"]

for num in nums:
    if (1 <= num <= 5):
        ranges[0] += 1
    elif (6 <= num <= 10):
        ranges[1] += 1
    elif (11 <= num <= 15):
        ranges[2] += 1
    elif (16 <= num <= 20):
        ranges[3] += 1
    elif (21 <= num <= 25):
        ranges[4] += 1
    elif (26 <= num <= 30):
        ranges[5] += 1
    elif (31 <= num <= 35):
        ranges[6] += 1
    elif (36 <= num <= 40):
        ranges[7] += 1
    elif (41 <= num <= 45):
        ranges[8] += 1
    elif (46 <= num <= 50):
        ranges[9] += 1

# Build histogram
# Ensure both ranges_name and ranges are both the same length because both are referenced based on their pos 

for idx in range(len(ranges)):
     print("{:>6} {}".format(ranges_name[idx], ranges[idx])
           
print("Average:", mean(nums))
print("Max:", max(nums))
print("Range:", max(nums) - min(nums))
print("Median:", median(nums))
print("Mode:", mode(nums))
