# Hemit Patel
# 781159
# ICS3U0-4
# MR VEERA
# 12 dec 2024
# coder application

word = input("Enter a string:")
coded = ""

# no need for list, strings also have indexes and better for memory
# they are also iterable so we can get each of the letter

lower_alphabet = "abcdefghijklmnopqrstuvwxyz"
upper_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for letter in word:
    
    if (letter not in upper_alphabet and letter not in lower_alphabet):
        coded += letter
        continue

    elif (letter.isupper() == True):
        index = upper_alphabet.index(letter)
        coded += upper_alphabet[index+2]

    elif (letter.islower() == True):
        index = lower_alphabet.index(letter)
        coded += lower_alphabet[index+2]
        
print(coded)
