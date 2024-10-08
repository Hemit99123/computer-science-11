# Hemit Patel
# STUDENT NUMBER
# ICS3U0-4 (reorged)
# Project Time Manager
# INSTRUCTOR NAME
# 4 oct 2024

# All the inputs needed 
designing_mins = int(input())
coding_mins = int(input())
debugging_mins = int(input())
testing_mins = int(input())

# Getting the total time from the inputs
total_time = designing_mins + coding_mins + debugging_mins + testing_mins

# Using that to find out how much percentage each task takes up
designing_percentage = (designing_mins / total_time) * 100
coding_percentage = (coding_mins / total_time) * 100
debugging_percentage = (debugging_mins / total_time) * 100
testing_percentage = (testing_mins / total_time) * 100

# Outputting a formatted table using the formatted output for string (adds spaces)
# Also added numerical formatting to the table for rounding 2 decimal places

print("{:<15}{:>10}".format("Task","% Time"))
print("{:<15}{:>10}".format("Designing","{:.2f} %".format(designing_percentage)))
print("{:<15}{:>10}".format("Coding","{:.2f} %".format(coding_percentage)))
print("{:<15}{:>10}".format("Debugging","{:.2f} %".format(debugging_percentage)))
print("{:<15}{:>10}".format("Testing","{:.2f} %".format(testing_percentage)))
