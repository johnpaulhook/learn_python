import time
import random

print("🎮 Countdown Game 🎮")
print("Try to press ENTER exactly when the timer hits 0!\n")

rounds = 3
score = 0
high_score = 0

for round_num in range(1, rounds + 1):
    print(f"--- Round {round_num} ---")

    start = random.randint(5, 10)
    print(f"Countdown will start from {start}...\n")
    time.sleep(1)

    for i in range(start, -1, -1):
        print(i)
        time.sleep(1)

    # Tell player it's time
    print("⏰ PRESS ENTER NOW!")

    input_time = time.time()           # mark the time when countdown ends
    input()                            # wait for player to press Enter
    end_time = time.time()             # mark when they actually pressed

    reaction_time = end_time - input_time
    print(f"⏱ You pressed Enter {reaction_time:.2f} seconds after 0.")

    # Scoring
    if reaction_time < 0.2:
        points = 100
        print("🔥 Perfect timing! +100 points")
    elif reaction_time < 0.5:
        points = 70
        print("⚡ Great job! +70 points")
    elif reaction_time < 1:
        points = 50
        print("👍 Not bad! +50 points")
    else:
        points = 10
        print("😅 Too slow! +10 points")

    score += points
    high_score = max(high_score, points)
    print(f"Your score this round: {points}\n")

print("=== GAME OVER ===")
print(f"🏆 Total Score: {score}")
print(f"⭐ Best Round Score: {high_score}")
