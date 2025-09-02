import random
import time
coins = 200000
while True:
    computer1 = random.randint(1, 20)
    computer2 = random.randint(1, 20)
    computer3 = random.randint(1, 20)
    time.sleep(0.25)
    print(computer1, computer2, computer3)
    if coins == 0:
            break
    if computer1 == computer2 == computer3:
        print("you got the jackpot")
        coins += 20000000000000000000000
        break
    else:
        print("no jackpot")
        coins -= 1
        continue
