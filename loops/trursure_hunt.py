import random


computer_x = random.randint(1,20)
computer_y = random.randint(1,20)

while True:
    while True:
        guess1 = input("type your height:")
        guess1 = int(guess1)
        if guess1 == computer_x:
            print ("you got the height correct")
            break
        elif guess1 > computer_x:
            print("too high")
        else:
            print ("too low")
    while True:
        guess2 = int(input("type your width:"))
        if guess2 == computer_y:
            print ("you got the width correct")
            break
        elif guess2 > computer_y:
            print("too high")
        else:
            print ("too low")
    
    if guess1 == computer_x and guess2 == computer_y:
        break


print ("you got it")