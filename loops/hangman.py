import random 

print ("Welcome to hangman") # greeting

computer = random.choice(["apple", "banana", "orange", "grape", "peach", "melon", "cherry", "mango",
    "kiwi", "lemon", "tiger", "lion", "zebra", "panda", "monkey", "giraffe",
    "dolphin", "whale", "eagle", "snake", "chair", "table", "desk", "couch",
    "bed", "pillow", "blanket", "lamp", "door", "window", "car", "bus",
    "train", "plane", "boat", "bike", "truck", "scooter", "subway", "rocket",
    "red", "blue", "green", "yellow", "purple", "black", "white", "gray",
    "pink", "orange", "happy", "sad", "angry", "tired", "excited", "nervous",
    "calm", "silly", "brave", "shy", "book", "pen", "pencil", "paper",
    "ruler", "eraser", "marker", "chalk", "notebook", "folder", "pizza",
    "burger", "fries", "taco", "salad", "soup", "sandwich", "pasta", "rice",
    "cake", "robot", "computer", "phone", "camera", "radio", "clock", "watch",
    "light", "fan", "TV", "music", "dance", "sing", "laugh", "cry", "jump",
    "run", "walk", "swim", "play"])
letters = list(computer)
misses = 0
hidden = ["_"] * len(computer)

while True:
    guess = input("put a letter: ")  
    if guess in letters:
        print("Correct! That letter is in the word.")
        
        for i in range(len(letters)):
            if letters[i] == guess:
                hidden[i] = guess
    else:
        print("Nope, not in the word.")
        misses += 1
    print("Word so far:", " ".join(hidden))
    print(f"misses so far={misses}")
    
    if misses == 6:
        break