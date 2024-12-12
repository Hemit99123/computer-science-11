# Hemit Patel
# 781159
# ICS3U0-4
# MR VEERA
# 12 dec 2024
# count constant

text = input("Enter word:")
consonants = 0

for char in text:
    # The spring of characters is all the consonants in the english language
    if (char.lower() in "bcdfghgklmnpqrstvwxyz"):
        consonants += 1

print("The number of consonants in {} is {}".format(text, consonants))
