# Hemit Patel
# 781159
# ICS3U0-4 
# 10 dec 2024 
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
  
print("Average:", mean(nums))
print("Max:", max(nums))
print("Range:", max(nums) - min(nums))
print("Median:", median(nums_sorted))
print("Mode:", mode(nums_sorted))
