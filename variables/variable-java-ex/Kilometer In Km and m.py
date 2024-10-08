# Hemit Patel
# 781159
# ICS3U0-4 (reorged)
# Kilometer Converter
# MR VEERA
# 8 oct 2024

kilometer_decimal = float(input("Enter the distance in kilometers:"))

# Kilometers turned into integer because it is going to be float due to kilometer_decimal being float
kilometers = int(kilometer_decimal // 1)

# The leftover kilometers (decimal value of the kilometer_decimal)
leftover_kilometers = kilometer_decimal % 1

# Left in float format to round to nearest whole number for better accuracy
meters = leftover_kilometers * 1000

# Rounding to meters to the 0 decimal place so it is a whole number and therefore a integer when outputted
print(f"The distance is: {kilometers} km {meters:.0f} m")
