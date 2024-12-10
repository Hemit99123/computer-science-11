# Hemit Patel
# 781159
# ICS3U0-4
# MR VEERA
# Reverse
# 10 december 2024

from random import randint


# List are very memory intestive so make sure to keep list size LOW AS POSSIBLE (class note)

idx = [0,0,0,0,0,0,0,0,0,0]

for _ in range(500):
    num = randint(0,9)

    idx[num] += 1

print("{:<15}{:<10}".format("Number","Occurance"))

for num in range(0,10):
    print("{:<15}{:<5}".format(num, idx[num]))
          
