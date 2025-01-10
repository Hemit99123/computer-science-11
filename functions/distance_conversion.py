# Hemit Patel
# 781159
# ICS3U0-4 
# MR VEERA
# distance conversion
# 9 jan 2025

def inches_to_centimeters(inches):
    """Convert inches to centimeters"""
    return f"{inches} inches equals ${inches * 2.54:.1f} centimeter"

def cm_to_inches(cm):
    """Convert centimeters to inches"""
    return f"{cm} centimeters equals ${cm / 2.54:.1f} inches"


def feet_to_centimeters(feet):
    """Convert feet to centimeters"""
    return f"{feet} feet equals ${feet * 30} centimeters"

def cm_to_feet(cm):
    """Convert centimeters to feet"""
    return f"{cm} centimeters equals ${cm / 30:.1f} feet"

def yards_to_meters(yards):
    """Convert yards to meters"""
    return f"{yards} yards equals ${yards * 0.91:.1f} meters"

def meters_to_yards(meters):
    """Convert meters to yards"""
    return f"{meters} meters equals ${yards / 0.91:.1f} yards"

def miles_to_kilometers(miles):
    """Convert miles to kilometers"""
    return f"{miles} miles equals ${miles * 1.6:.1f} kilometers"

def km_to_miles(km):
    """Convert kilometers to miles"""
    return f"{km} kilometers equals ${km / 1.6:.1f} miles"

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

    print (centimeters)


elif (type_of_conversion == 2):

    centimeters = feet_to_centimeters (number)

    print (centimeters)


elif (type_of_conversion == 3):

    meters = yards_to_meters (number)

    print (meters)


elif (type_of_conversion == 4):

    kilometers = miles_to_kilometers (number)

    print (kilometers)

    

elif (type_of_conversion == 5):

    inches = centimeters_to_inches (number)

    print (inches)


elif (type_of_conversion== 6):

    feet = centimeters_to_feet (number)

    print (feet)


elif (type_of_conversion == 7):

    yards = meters_to_yards (number)

    print (yards)


elif (type_of_conversion == 8):

    miles = kilometers_to_miles(number)

    print (miles)


else:

    print ("Invalid input, try again!")