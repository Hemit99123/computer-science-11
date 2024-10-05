# String formatting with spaces


percent_design=28.5673

# left align
print("{:<15}{:<10}".format("Task","% Time"))

# right align
print("{:>15}{:<10}".format("Task","% Time"))

# center align
print("{:^15}{:<10}".format("Task","% Time"))



print("{:<15}{:<5.2f}{:2}".format("Designing",percent_design,"%"))




# Formatted with spaces so it resembles a table-like structure
print("{:<15}{:>10.2f}%".format("Designing", percentage_designing))
print("{:<15}{:>10.2f}%".format("Coding", percentage_coding))
print("{:<15}{:>10.2f}%".format("Debugging", percentage_debugging))
print("{:<15}{:>10.2f}%".format("Testing", percentage_testing))



## CHANGE THE SPACING DEPENDING ON UR LARGEST TEXT
