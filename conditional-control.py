#Example for if statement
#Mr Veera
#ICS3U0
# 09 OCT 2024

SECRET_NUM = 5 

guess=int(input("Guess a number less than 10: "))

# Double checking if guess is under 10                                                 
if (guess>10):
    print("Higher than 10, try again sorry")


if (guess == SECRET_NUM): 
    
    print("You guessed it!")


# THE ELSE STATEMENT IS PART OF THE IF BLOCK AND THEREFORE THE IF STATEMENT CANNOT BE EXITED BEFORE ELSE

else: 
    print("Sorry wrong. Try again!")
