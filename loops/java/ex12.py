# Hemit Patel
# 781159
# ICS3U0-4
# ex 12
# 17 nov 2024
# MR VEERA

start_1 = int(input("Enter the first starting number:"))
start_2 = int(input("Enter the second starting number:"))

print(f"{start_1} {start_2}", end="")

first_num = start_1
second_num = start_2

while True:
    sum_val = (first_num + second_num) % 10
    print(f" {sum_val}", end="")

    # Update the numbers
    first_num = second_num
    second_num = sum_val

    # Check if we've returned to the starting pair
    if first_num == start_1 and second_num == start_2:
        break
