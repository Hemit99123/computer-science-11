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


print("{:>24}{:>10} {:>10}".format("Tax","Tip", "Pay"))
print("{:<20}{:<10.2f}{:<10.2f}{:<10.2f}".format("Person #1",person_one_tax, split_tip, person_one_pay))
print("{:<20}{:<10.2f}{:<10.2f}{:<10.2f}".format("Person #2",person_two_tax, split_tip, person_two_pay))
print("{:<20}{:<10.2f}{:<10.2f}{:<10.2f}".format("Person #3",person_three_tax, split_tip, person_three_pay))
print("{:<20}{:<10.2f}{:<10.2f}{:<10.2f}".format("Person #4", person_four_tax, split_tip,person_four_pay))
print()

print("{:<20}{:<10.2f}".format("Subtotal", subtotal))
print("{:<20}{:<10.2f}".format("Total Tax", total_tax))
print("{:>25}".format("-----"))
print("{:<20}{:<10.2f}".format("Total Tip", total_tip))
print("{:<20}{:<10.2f}".format("Grand Total", grand_total))

