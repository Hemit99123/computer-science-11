# Hemit Patel
# 781159
# ICS3U0
# Mr Veera
# Vending Machine 
# 14 oct 2024 

price_item = int(input("Enter the price of the item:"))

number_items = int(input("Enter the amount of items:"))

temperature = int(input("Enter the current temperature:"))

balance = int(input("Enter the user's balance:"))

is_valid_code = input("Is there a valid discount code? (Yes or No):")

# Checking if correct inputs were put into is_valid_code (yes or no ONLY)

if (is_valid_code.lower() != "yes" and is_valid_code.lower() != "no"):
    print("Invalid input for the valid discount code. Only can put YES or NO!")

# Otherwise if inputs are okay, run the program in the else block
else:

  # Checking for the multiple conditions using connectors of or and
  # A range is also present hence the <= syntax for temperature
  
  if (number_items > 0 and 10 <= temperature <= 35 and balance >= price_item or is_valid_code.lower() == "yes"):
    print("dispense")
  
  # If these conditions are not meant then run the else block
  
  else:
    print("no dispense")
  
