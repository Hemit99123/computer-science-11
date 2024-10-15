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

elif (3 < wave_height < 6):
    print("Go body boarding!")

elif (0 <= wave_height <= 3):
    print("Go swimming")

else:
    print("Whoa! What kind of surf is that?")
