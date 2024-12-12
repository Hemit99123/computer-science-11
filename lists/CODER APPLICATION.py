# Hemit Patel
# 781159
# ICS3U0-4
# MR VEERA
# 12 dec 2024
# coder application

word = input("Enter a string:").lower()
coded = ""

# no need for list, strings also have indexes and better for memory
# they are also iterable so we can get each of the letter

alphabet = "abcdefghijklmnopqrstuvwxyz"

for letter in word:
    
    if (letter not in alphabet):
        coded += letter
        continue
    
    index = alphabet.index(letter)
    coded += alphabet[index+2]


print(coded)
