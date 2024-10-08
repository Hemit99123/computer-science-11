# Hemit Patel
# 781159
# ICS3U0-4 (reorged)
# Sleep Calculator
# MR VEERA
# 5 oct 2024

print("Enter your birthdate:")
birth_year = int(input("Year:"))
birth_month = int(input("Month:"))
birth_day = int(input("Day:"))
print("Enter today's date:")
current_year = int(input("Year:"))
current_month = int(input("Month:"))
current_day = int(input("Day:"))


years_elapased = (current_year - birth_year) * 365
months_elapased = (current_month - birth_month) * 30
days_elapased = (current_day - birth_day)

alive = years_elapased + months_elapased + days_elapased

slept = alive * 8

print("You have been alive for", alive, "days.")
print("You have slept for", slept, "hours.")