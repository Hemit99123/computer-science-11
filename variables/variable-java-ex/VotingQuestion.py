# Hemit Patel
# 781159
# ICS3U0-4 (reorged)
# The Voting Machine 
# MR VEERA
# 6 oct 2024

# Getting the 3 states name so each input for votes is more clear
state_one = input("Enter the first state name:")
state_two = input("Enter the second state name:")
state_three = input("Enter the third state name:")

# Getting the 2 candidates name for the same purpose
first_candidate = input("Enter the first candidate name:")
second_candidate = input("Enter the second candidate name:")

# Using f"" to add the state and candidate variable to make it clear where each vote go
# First means the first candiate and second means the second candidate which are used as prefixes for my code

first_vote_firststate = int(input(f"Enter the number of votes for the {first_candidate} in the {state_one} state:"))

first_vote_secondstate = int(input(f"Enter the number of votes for the {first_candidate} in the {state_two} state:"))

first_vote_thirdstate = int(input(f"Enter the number of votes for the {first_candidate} in the {state_three} state:"))

second_vote_firststate = int(input(f"Enter the number of votes for the {second_candidate} in the {state_one} state:"))

second_vote_secondstate = int(input(f"Enter the number of votes for the {second_candidate} in the {state_two} state:"))

second_vote_thirdstate = int(input(f"Enter the number of votes for the {second_candidate} in the {state_three} state:"))

# Getting the two candidates totaled votes accross all 3 states
first_votes = first_vote_firststate + first_vote_secondstate + first_vote_thirdstate

second_votes = second_vote_firststate + second_vote_secondstate + second_vote_thirdstate

# Getting total for output and further computation
total = first_votes + second_votes

# Getting the percentage of votes for each candidate
first_percent = (first_votes / total) * 100
second_percent = (second_votes / total) * 100

print()

# Making a table by formatting strings + using numerical formatting to round numbers to the second decimal place
print("{:<15}{:>10}{:>21}".format("Candidate", "Votes", "Percentage"))
print("{:<15}{:>10}{:>20.2f}%".format(first_candidate, first_votes, first_percent))
print("{:<15}{:>10}{:>20.2f}%".format(second_candidate, second_votes, second_percent))

print()

print("TOTAL VOTES:", total)