# Hemit Patel
# 781159
# ICS3U0-4 
# MR VEERA
# pythagorean triple
# 9 jan 2025

def is_perfect_square(number):
    root = int(number ** 0.5)
    return root * root == number

def find_pythagorean_triples():
    triples = []
    # getting all possible values of a (1, 100)

    for a in range(1, 100):
        # for each "a" variable, we need to check every combination it can have with a "b" variable
        # this is why we start the range at a because a itself should not be included
        
        for b in range(a, 100):  
            c_squared = a*a + b*b
            if is_perfect_square(c_squared):
                c = int(c_squared ** 0.5)
                # adding as a tuple so these values are immutable 
                triples.append((a, b, c))
    return triples

res = " ,".join(map(str, find_pythagorean_triples()))

print(res)