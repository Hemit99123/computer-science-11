# Hemit Patel
# 781159
# ICS3U0-4
# Surfers Application
# MR VEERA
# 10 oct 2024

waves = int(input("Enter the amount of waves:"))


if (waves > 6):
    print("Great day for surfing")

# If waves are not above 6 feet, then we must check for ranges

# GOING IN ASC order because its much easier to read!

# We assume that the boundries (ranges) are exlusive unless explicity stated otherwise (since we are using mathemitcal logic
elif (3 <= waves < 6):
        print("Go body boarding!")
elif (0 <= waves < 3):
        print("Go for a swim.")

# If waves in feet don't make it to any of these ranges, output the following (otherwise)
else:
    print("Whoa! What kind of a surf is that?")
