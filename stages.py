# Hemit Patel
# 781159
# ICS3U0-4
# Stages Application
# MR VEERA
# 10 oct 2024

# Integer variable because age is always a whole number
age = int(input("Enter the age"))

# Checking if user is an adult
if age > 18:
    print("adult")

# If not over 18, then we run the conditional statements for under 18s

# We need to run the elif statements in asc (smallest to greatest age range) 
# order because the statements are
# lesser than so smaller inputs don't become true for larger age ranges

elif age <= 5:
    print("toddler")
elif age <= 10:
    print("child")
elif age <= 12:
    print("preteen")
else:
    print("teen")
