# Hemit Patel
# STUDENT NUMBER
# ICS3U0-1
# Dice Game
# INSTRUCTOR NAME
# 30 sep 2024
import random

roll = 10
score = 0

# This means as long as we have above 10 rolls we can run the while loop

while roll > 0:
    continue_play = input("Continue the play?")

    # Break out of the while loop if given value of no (no case senstivity)
    
    if continue_play.lower() == "no":
        break;

    # The two rolls providing random values
    
    die_1 = random.randint(1,6)
    die_2 = random.randint(1,6)

    # The sum of both of them within a variable
    
    total_sum = die_1 + die_2

    # The conditional logic that determines the score given
    
    if total_sum == 7 or total_sum == 11:
        score = 0
    else:
        if die_1 > die_2:
            score += die_1
        else:
            score += die_2
    print("You rolled a", die_1, ",", die_2, "Your current score is", score)
    roll -= 1
print("Final score", score)
