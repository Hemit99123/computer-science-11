# Hemit Patel
# 781159
# ICS3U0-4
# MR VEERA 
# 15 nov 2024

starting_hour = int(input("Enter the starting hour (1-12): "))
am_or_pm = input("Enter am or pm: ").lower()
elapsed_time = int(input("Enter the elapsed time in hours: "))

# Initialize the hour to the starting hour
current_hour = starting_hour

# Use a loop to increment the hour by each elapsed hour
for _ in range(elapsed_time):
    # Increment the hour
    current_hour += 1
    
    # Handle the 12-hour cycle
    if current_hour == 13:
        current_hour = 1  # Reset to 1 if it goes beyond 12
        
        # Switch between am and pm
        if am_or_pm == "am":
            am_or_pm = "pm"
        else:
            am_or_pm = "am"

# Print the result
print(f"The new time is {current_hour} {am_or_pm}")
