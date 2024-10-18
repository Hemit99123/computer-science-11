# Hemit Patel
# 781159
# MR VEERA
# Ex 6
# Oct 17 2024

# Using this syntax so that the only function that we need is returned not all

from random import randint

# Randint produces a random int from a to b which is put as arguments in the function

random_number_1 = randint(1,10)
random_number_2 = randint(1,10)

# Using this to determine which operator to use (randomize selection)
random_operator_number = randint(1,4)

# Initalizing these variables so I can use them GLOBALLY i
operator = ""
correct = 0

if (random_operator_number == 1):
    correct = random_number_1 * random_number_2
    operator = "*"

elif (random_operator_number == 2):
    correct = random_number_1 + random_number_2
    operator = "+"

elif (random_operator_number == 3):
    correct = random_number_1 - random_number_2

    ## BONUS: here we COULD check which one is higher so that the 
    ## user does not need to compute negative values
    ## if (random_number_1 > random_number_2):
    ##    correct = random_number_1 - random_number_2
    ## else:
    ##    correct = random_number_2 - random_number_1

    
    operator = "-"

elif (random_operator_number == 4):
    correct = random_number_1 // random_number_2
    operator = "//"

# We now ask for the answer because we have all the randomized items to create equation
answer = int(input(f"What is {random_number_1} {operator} {random_number_2}?"))

# Here we check if the answer given by user is correct

if (answer == correct):
    print("Correct!")
else:
    print("Wrong!")
