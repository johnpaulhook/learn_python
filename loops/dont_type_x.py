import random

score = 0
computer = random.choice("abcdefghijklmnopqrstuvwxyz")

while True:
    type = input("put a leter: ")
    
    if type == computer:
        print ("you lose")
        print (f"score={score}")
        break
    else:
        print ("keep going")
        score += 1
    
        
        