# Hemit Patel
# 781159
# ICS3U0-4 
# MR VEERA
# distance conversion
# 9 jan 2025

def inches_to_centimeters(inches):
    """Convert inches to centimeters"""
    return inches * 2.54

def cm_to_inches(cm):
    """Convert centimeters to inches"""
    return cm / 2.54

def feet_to_centimeters(feet):
    """Convert feet to centimeters"""
    return feet * 30

def cm_to_feet(cm):
    """Convert centimeters to feet"""
    return cm / 30

def yards_to_meters(yards):
    """Convert yards to meters"""
    return yards * 0.91

def meters_to_yards(meters):
    """Convert meters to yards"""
    return meters / 0.91

def miles_to_kilometers(miles):
    """Convert miles to kilometers"""
    return miles * 1.6

def km_to_miles(km):
    """Convert kilometers to miles"""
    return km / 1.6

def display_menu():
    """Display the conversion menu"""
    print("\nMetric Conversion Calculator")
    print("1. Inches to Centimeters")
    print("2. Centimeters to Inches")
    print("3. Feet to Centimeters")
    print("4. Centimeters to Feet")
    print("5. Yards to Meters")
    print("6. Meters to Yards")
    print("7. Miles to Kilometers")
    print("8. Kilometers to Miles")

display_menu()

type_of_conversion = int(input("What type?"))
number = int(input("Amount:"))

if (type_of_conversion == 1):

    centimeters = inches_to_centimeters(number)

    print (number, "inches equals", centimeters, "centimeters")


elif (type_of_conversion == 2):

    centimeters = feet_to_centimeters (number)

    print (number, "feet equals", centimeters, "centimeters")


elif (type_of_conversion == 3):

    meters = yards_to_meters (number)

    print (number, "yards equals", meters, "meters")


elif (type_of_conversion == 4):

    kilometers = miles_to_kilometers (number)

    print (number, "miles equals", kilometers, "kilometers")

    

elif (type_of_conversion == 5):

    inches = centimeters_to_inches (number)

    print (number, "centimeters equals", inches, "inches")


elif (type_of_conversion== 6):

    feet = centimeters_to_feet (number)

    print (number, "centimeters equals", feet, "feet")


elif (type_of_conversion == 7):

    yards = meters_to_yards (number)

    print (number, "meters equals", yards, "yards")


elif (type_of_conversion == 8):

    miles = kilometers_to_miles(number)

    print (number, "kilometers equals", miles, "miles")


else:

    print ("null")