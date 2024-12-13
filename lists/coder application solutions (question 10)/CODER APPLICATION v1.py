# Hemit Patel
# 781159
# ICS3U0-4
# MR VEERA
# 12 dec 2024
# coder application

word = input("Enter a string:")
shift = int(input("Enter the amount of shift:"))
coded = ""

# no need for list, strings also have indexes and better for memory
# they are also iterable so we can get each of the letter

lower_alphabet = "abcdefghijklmnopqrstuvwxyz"
upper_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# this is for when you have shifts that go beyond z, so
# you have to wrap back starting from a again
# it is in a function because this same logic is used for both
# upper and lower cases so adding it into one function and using it 2 times
# is better for maintaibuility because you only have to modify this function
# not the 2 different sets of logic which are identical

def compute_extra_distance(index):
    distance_to_z = 25 - index
    distance = (shift - distance_to_z) - 1

    return distance

for letter in word:

    upper = letter.isupper()
    lower = letter.islower()

    # not encrypting non alphabetical character (in v2 we will through unicode conversion)
    if (letter not in upper_alphabet and letter not in lower_alphabet):
        coded += letter
    
    elif (upper == True):
        index = upper_alphabet.index(letter) 
        if (index + shift > 25):
            distance = compute_extra_distance(index)
            coded += upper_alphabet[distance]
        else:
            coded += upper_alphabet[index+shift]

    elif (lower== True):
        index = lower_alphabet.index(letter)
        if (index + shift > 25):
            distance = compute_extra_distance(index)
            coded += lower_alphabet[distance]
        else:
            coded += lower_alphabet[index+shift]
        
print(coded)
