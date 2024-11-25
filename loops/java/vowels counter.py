# Hemit Patel
# 781159
# ICS3U0-4
# MR VEERA
# 25 nov 2024
# vowel counter

word_input = input("Enter text:")
number_vowels = 0

for letter in word_input:
    if (letter.lower() in "aeiou"):
        number_vowels += 1

print("The vowels in", word_input, "are", number_vowels)
