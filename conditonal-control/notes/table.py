# Create a header
header = "{:<12} {:<5} {:<6}".format("Name", "Age", "Grade")

# Create rows
# the numbers are based on the highest character in
# each row

row1 = "{:<12} {:<5} {:}".format("John", 15, 10)
row2 = "{:<12} {:<5} {:}".format("Hemit Patel", 16, 10)
row3 = "{:<12} {:<5} {:}".format("Sarah", 14, 9)
row4 = "{:<12} {:<5} {:}".format("Mike", 17, 11)

# Print the table
print(header)
print("-" * 23)  # Line separator
print(row1)
print(row2)
print(row3)
print(row4)
