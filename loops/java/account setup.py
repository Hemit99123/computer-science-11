# Hemit Patel
# 781159
# ICS3U0-4
# MR VEERA
# 17 nov 2024
# accountsetup


username = input("Enter a user name:")

password = ""

while (len(password) < 8):
    
    password = input("Enter a password that is at least 8 characters:")

print(f"Your user name is {username.lower()} and your password is {password.lower()}")
