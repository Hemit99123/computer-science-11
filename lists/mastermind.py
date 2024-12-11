# Hemit Patel
# 781159
# ICS3U0-4
# MR VEERA
# 12 december 2024
# mastermind game python

from random import randint

# Get game parameters
pegs = int(input("Enter amount of pegs: "))
colors = int(input("Enter amount of colors: "))

# Generate secret code
correct_order = []
for _ in range(pegs):
    random_color = randint(1, colors)
    correct_order.append(random_color)
    
print(correct_order)
    
# Game loop
while True:
    correct_place = 0
    correct_colors = 0
    
    # Get player's guess
    attempted_order = []
    for iteration in range(pegs):
        color = int(input(f"Enter for peg {iteration + 1}: "))
        attempted_order.append(color)
    
    # Create copies to mark used pegs
    correct_copy = correct_order.copy()
    attempt_copy = attempted_order.copy()
    
    # Check for correct positions
    for i in range(pegs):
        if attempted_order[i] == correct_order[i]:
            correct_place += 1
            # Mark these positions as used
            correct_copy[i] = -1
            attempt_copy[i] = -2
            correct_colors += 1  # Add to correct colors when position is correct
    
    # Check for correct colors in wrong positions
    for i in range(pegs):
        if attempt_copy[i] != -2:  # If not already counted
            for j in range(pegs):
                if correct_copy[j] == attempt_copy[i]:
                    correct_colors += 1
                    correct_copy[j] = -1  # Mark as used
                    break
    
    print(f"You have {correct_place} peg(s) correct and {correct_colors} color(s) correct")
    
    # Check for win
    if correct_place == pegs:
        print("Congratulations! You've won!")
        break
