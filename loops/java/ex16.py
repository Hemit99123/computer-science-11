from random import randint

total_steps = 0
steps = 1
distance = 3.5

distance_list = []

while (steps <= 50):
    operation = randint(0,1)

    # negative int 
    if (operation == 0):
        distance -= 1

    # postive int
    else:
        distance += 1

    # user is now outside of the bridge
    if (distance == -0.5 or distance == 7.5):
        distance_list.append(steps)
        
    steps += 1
    
sorted_list = sorted(distance_list, reverse=True)

print(sorted_list[0])

