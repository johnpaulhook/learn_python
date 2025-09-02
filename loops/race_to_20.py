import random

number = 0
while True:
    roll = random.randint(1, 6)


    if roll == 1:
        print("you lose")
        break
    elif roll == 2:
        print("you rolled a 2")
        number += 2
    elif roll == 3:
        print("you rolled a 3")
        number += 3
    elif roll == 4:
        print("you rolled a 4")
        number += 4
    elif roll == 5:
        print("you rolled a 5")
        number += 5
    elif number >= 20:
        print("you win")
        break
    
print(f"your score was {number}")