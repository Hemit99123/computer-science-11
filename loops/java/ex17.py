# Hemit Patel
# 781159
# ICS3U0-4
# MR VEERA
# 17 nov 2024
# ex 17

pwd = "hemit1212"

is_denied = True

attempts = 0

while (attempts >= 3):
    guess = input("Enter the password:")

    if (guess == pwd):
        print("Welcome")
        is_denied = False
        break
    else:
        print("The password you typed is incorrect.")

if (is_denied == True):
    print("Access denied.")
