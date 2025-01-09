# Hemit Patel
# 781159
# ICS3U0-4
# Mr. Veera
# 9 jan 2025

def find_spanish_number(number):
  if (number == 1):
    return "uno"
  elif (number == 2):
    return "dos"
  elif (number == 3):
    return "tres"
  elif (number == 4):
    return "cuatro"
  elif (number == 5):
    return "cinco"
  elif (number == 6):
    return "seis"
  elif (number == 7):
    return "siete"
  elif (number == 8):
    return "ocho"
  elif (number == 9):
    return "neuve" 
  elif (number == 10):
    return "diez"

number = int(input("Enter number:"))

print(find_spanish_number(number))
