# Hemit Patel
# 781159
# MR VEERA
# ICS3U0-4
# 29 oct 2024
# percentage passing

number_of_scores = int(input("Enter the amount of scores")) # stores the total number of scores entered

total_above_70=0 # counts the scores above 70
count = 1

while(count<=number_of_scores): # permits scores to be entered until the user desires.

    score=int(input("Enter score: "))

    if( score>=70): # Check for score above 70
        total_above_70 += 1 # count of score above 70
    
    count += 1 # count of all score entered
    
# Calculate percent of score above 70
percent= total_above_70/number_of_scores    

print(f"The percentage is {percent * 100:.2f}%") # Output the calculated percentage
