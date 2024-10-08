# Hemit Patel
# 781159
# ICS3U0-4 (reorged)
# Project Time
# MR VEERA
# 8 oct 2024

print("Enter the amount of minutes spent on each of the following project tasks:")
print()

designing_mins = int(input("Designing:"))
coding_mins = int(input("Coding:"))
debugging_mins = int(input("Debugging:"))
testing_mins = int(input("Testing:"))

total = designing_mins + coding_mins + debugging_mins + testing_mins

designing_percent = (designing_mins / total) * 100
coding_percent = (coding_mins / total) * 100
debugging_percent = (debugging_mins / total) * 100
testing_percent = (testing_mins / total) * 100

print()

# Added one extra space for "% Time" because it is one space off from the other numbers
print("{:<15}{:>11}".format("Task", "% Time"))
print("{:<15}{:>10.2f}%".format("Designing", designing_percent))
print("{:<15}{:>10.2f}%".format("Coding", coding_percent))
print("{:<15}{:>10.2f}%".format("Debugging", debugging_percent))
print("{:<15}{:>10.2f}%".format("Testing", testing_percent))