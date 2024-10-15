# Hemit Patel
# 781159
# ICS3U0-4
# Wave surfer conditonal logic
# MR VEERA
# 9 oct 2024


wave_height = int(input("Enter the amount of wave height:"))

# If wave is higher than 6 feet print an output

if (wave_height >= 6):
    print("Great day for surfing!")
# The wave must be BETWEEN 3 and 6 feet which means that 3 and 6 are not included 

elif (3 < wave_height < 6):
    print("Go body boarding!")

# It was worded from 0 to 3, the from means that the limits are counted
elif (0 <= wave_height <= 3):
    print("Go swimming")

else:
    print("Whoa! What kind of surf is that?")
