import random

# Randomly pick "heads" or "tails"
computer = random.choice(["heads", "tails"])

# Track score
score = 0

# Ask player for their guess
guess = input("Heads or Tails: ").lower()   # <-- need () to actually call .lower()

# Compare guess with computer's choice
if guess == computer:
    score += 1
    print(f"Computer flipped {computer}")
    print("🎉 YOU WIN!")
else:
    print(f"Computer flipped {computer}")
    print("❌ YOU LOSE")

print("Your score:", score)
