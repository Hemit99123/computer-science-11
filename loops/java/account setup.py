# Hemit Patel
# 781159
# ICS3U0-4
# MR VEERA
# 17 nov 2024
# accountsetup


username = input("Enter a user name:")

password = ""

while (True):
    password = input("Enter a password that is at least 8 characters:")

    if (len(password) > 8):
        break

print(f"Your user name is {username.lower()} and your password is {password.lower()}")
