# Hemit Patel
# 781159
# ICS3U0
# MR VEERA
# Time Converter App
# 6 jan 2025

def hours_to_minutes(hours):
    minutes = hours * 60
    print(minutes) 

def days_to_hours(days):
    hours = days * 24
    print(hours) 

def minutes_to_hours(minutes):
    hours = minutes / 60
    print(hours) 

def hours_to_days(hours):
    days = hours / 24
    print(days) 

print("Type: HM for hours to minutes, DH for days to hours, MH for minutes to hours, HD for hours to days")
print()

type_time = input("What time conversion?:")
time = int(input("Enter time amount (number):"))

if (type_time == "HM"):
    hours_to_minutes(time)
elif (type_time == "DH"):
    days_to_hours(time)
elif(type_time == "MH"):
    minutes_to_hours(time)
elif(hours_to_days == "HD"):
    hours_to_days(time)
else:
    print("invalid")