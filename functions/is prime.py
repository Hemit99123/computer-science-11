# Hemit Patel
# 781159
# ICS3U0-4 
# MR VEERA
# is prime
# 9 jan 2025

def is_prime(number):
    # Handle edge cases
    if number <= 1:
        return False
    if number == 2:
        return True
    # Check if number is even
    if number % 2 == 0:
        return False
    
    # Check odd numbers up to the square root
    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            return False
    return True

number = int(input("Enter number:"))
print(is_prime(number))
