# Hemit Patel
# 781159
# ICS3U0-4 (reorged)
# Conditional Control
# MR VEERA
# 12 oct 2024

age = int(input("Enter the age of the person: "))

# Check for Senior Citizen
if age >= 65:
    print("Senior Citizen")


# FOR ELIF STATEMENTS, IT MUST BE IN THE SAME ORDER (EITHER ASC OR DESC)
# I chose ASC order because it is easier to read

# Check for Toddler
elif 0<= age <= 5:  # This covers ages 0-5
    print("Toddler")

# Check for Child
elif 6 <= age <= 12:
    print("Child")

# Check for Teenager
elif 13 <= age <= 17:
    print("Teenager")

# Check for Adult
elif 18 <= age <= 64:
    print("Adult")
