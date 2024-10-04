# String formatting with spaces


percent_design=28.5673

# left align
print("{:<15}{:<10}".format("Task","% Time"))

# right align
print("{:>15}{:<10}".format("Task","% Time"))

# center align
print("{:^15}{:<10}".format("Task","% Time"))



print("{:<15}{:<5.2f}{:2}".format("Designing",percent_design,"%"))
