# Hemit Patel
# 781159
# ICS3U0-4
# MR VEERA
# prime number checking
# 5 nov 2024

number = int(input())
divisor = 2

# flag which is set to false once number is found out not to be prime 
is_prime = True

while (divisor <= number - 1):
    if (number % divisor == 0):
        # no need to continue loop because the number is divisable by more than one and itself

        is_prime = False
        break
    divisor += 1

# using the flag to output the proper prompts

if (is_prime == True):
    print("Number is prime")
else:
    print("Number not prime")
