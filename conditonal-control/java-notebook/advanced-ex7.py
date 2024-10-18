# Hemit Patel
# MR VEERA
# ICS3U0-4
# Ex 7 -> Equivalent fraction quiz
# 17 oct 2024

from random import randint

# Generate random fractions
fractions = []
for _ in range(8):
    numerator = randint(1, 200)
    denominator = randint(1, 200)
    fractions.append([numerator, denominator])

print("Equivalent Fractions Quiz:")
print()

# Display fractions to the user
for iterator, fraction_list in enumerate(fractions):
    print(f"\t{iterator + 1}. {fraction_list[0]}/{fraction_list[1]}")

# Select a random fraction number to check for equivalence
random_fraction_number = randint(0, 7)  # Changed to 0-7 to match list indices
print(f"Which fraction number is equivalent to fraction #{random_fraction_number + 1}?")
fraction_number_answer = int(input("Your answer: "))

# Get the randomly selected fraction
random_fraction = fractions[random_fraction_number]
random_fraction_numerator, random_fraction_denominator = random_fraction

# Store correct equivalent fraction numbers
correct = []

# Check for equivalent fractions using cross multiplication
for i, fraction_items in enumerate(fractions):
    # breaking down the sublist instead of fractions
    current_numerator, current_denominator = fraction_items
    # Using cross multiplacation to find out if the fraction is equivalent
    if (random_fraction_numerator * current_denominator == 
        random_fraction_denominator * current_numerator):
        correct.append(i + 1)

# Determine if the user's answer is correct
if fraction_number_answer in correct:
    if fraction_number_answer != random_fraction_number + 1:
        print("Correct!")
    else:
        print("That's the same fraction, not an equivalent one.")
elif len(correct) == 1:
    print("Wrong. There are no other equivalent fractions.")
else:
    print("Wrong")
