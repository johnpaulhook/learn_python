import random

score = 0

while True:
    computer = random.choice([1, 2, 3, 4, 5, 6,])
    
    print(f"computer chose {computer}")
    
    if computer == 6:
        break
    elif computer == 5:
        score += 1
    elif computer == 4:
        score += 1
    elif computer == 3:
        score += 1
    elif computer == 2:
        score += 1
    elif computer == 1:
        score += 1
        
    print("Your score:", score)

# -------- ASK PLAYER FOR INITIALS --------
name = input("Enter your initials or name: ")

# -------- SAVE SCORE WITH NAME --------
with open("scores.txt", "a") as file: 
    file.write(f"{name}:{score}\n")   # format: Name:Score

# -------- LOAD ALL SCORES --------
with open("scores.txt", "r") as file:
    lines = file.readlines()

# -------- PARSE INTO (NAME, SCORE) PAIRS --------
scores = []
for line in lines:
    line = line.strip()   # remove spaces/newlines
    if ":" in line:       # only process valid lines
        n, s = line.split(":")   # split "Name:Score"
        scores.append((n, int(s)))

# -------- SORT SCORES BY HIGHEST --------
scores.sort(key=lambda x: x[1], reverse=True)  # sort by score

# -------- DISPLAY TOP 3 --------
print("\n🏆 Top 3 Scores:")
for i, (n, s) in enumerate(scores[:3], start=1):
    print(f"{i}. {n} - {s}")