# Hemit Patel
# 781159
# ICS3U0-4
# MR VEERA
# random walk
# 17 nov 2024

from random import randint

length = 7
person_length = 3.5
steps = 0

for num in range(50):
    determining_num  = randint(0,1)

    if (determining_num == 0):
        person_length += 1
    else:
        person_length -= 1
    
    if (person_length != -0.5 and person_length != 7.5):
        steps += 1
