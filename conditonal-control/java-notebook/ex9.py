# Hemit Patel
# 781159
# MR VEERA
# ICS3U0-4
# 18 oct 2024
# guess game

from random import randint

guess = int(input("Enter a number between 1 and 20:"))

# BETWEEN 1 and 20 means the range is exclusive because it only includes the values in-between
# using this range to ensure that the number really is between 1 and 20 (BONUS WORK)

if (1 < guess < 20):

    # performing all logic instead this if statement so that it does not execute if number is not between 1-20
    
    # randint function's arguments are inclusive but we need values from 2 to 19 so we include those limits instead of 1
    # and 20
    secret_num = randint(2,19)

    if (guess == secret_num):
        print("You won!")
    else:
        print("Better luck next time!")

# IF NOT IN RANGE, let us print an error to warn user to change their ways

else:
    print("Not between 1 and 20, try again")
