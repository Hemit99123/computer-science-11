# Hemit Patel
# 781159
# ICS3U0-4
# MR VEERA
# prime number checking 1.b.
# 5 nov 2024

## FOR LOOP METHOD
lower_limit = int(input())

if (lower_limit == 1):
    lower_limit = 2
    
higher_limit = int(input())

print()
print("FOR LOOP")
print()

for number in range(lower_limit, higher_limit + 1):
    is_prime = True
    for divisor in range(2, number - 1):
        if (number % divisor == 0):
            is_prime = False

    if (is_prime == True):
        print(number)



## WHILE LOOP METHOD

number = lower_limit

print()
print("WHILE LOOP")
print()

while (number <= higher_limit):
    is_prime = True
    divisor = 2
    while (divisor < number):
        if number % divisor == 0:
            is_prime = False
            break
        divisor += 1
    if is_prime:
        print(number)
    number += 1
