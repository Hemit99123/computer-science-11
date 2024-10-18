# Hemit Patel
# 781159
# MR VEERA
# Ex 5
# Oct 17 2024

percentage_mark = int(input("Enter the percentage:"))

# No need to initalize this variable here, but I did so for readability purposes
# Will use this variable to determine the letter grade
grade = ""
# Going in DESC order (greatest to least) to maintain consistency with the elif statemen

if (90 <= percentage_mark <= 100):
    grade = "A"

elif (80 <= percentage_mark <= 89):
    grade = "B"

elif (70 <= percentage_mark <= 79):
    grade = "C"

elif (60 <= percentage_mark <= 69):
    grade = "D"

else:
    grade = "F"

print(f"The corresponding letter grade is {grade}")
