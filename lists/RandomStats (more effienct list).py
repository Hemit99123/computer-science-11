# Hemit Patel
# 781159
# ICS3U0-4
# MR VEERA
# Reverse
# 10 december 2024

from random import randint


# List are very memory intestive so make sure to keep list size LOW AS POSSIBLE 

idx = [0,0,0,0,0,0,0,0,0,0]


for _ in range(500):
    num = randint(0,9)

    idx[num] += 1


for num in range(0,10):
    print("Number: {} Occurances: {}".format(num, idx[num]))
          
