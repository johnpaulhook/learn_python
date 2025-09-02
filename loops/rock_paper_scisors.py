import random   # Import random so the computer can choose randomly

print("🎮 Welcome to Rock, Paper, Scissors! Type 'quit' to stop.")  # Greeting message

# Start an infinite loop → game keeps running until the player quits
while True:
    # Ask player for their choice (convert to lowercase so case doesn’t matter)
    player = input("\nChoose Rock, Paper, or Scissors: ").lower()

    # If player types "quit", end the game
    if player == "quit":
        print("👋 Thanks for playing!")  # Goodbye message
        break  # Exit the loop → game ends

    # Check if player typed something valid
    if player not in ["rock", "paper", "scissors"]:
        print("❌ Invalid choice! Try again.")  # Warn player
        continue  # Go back to the top of the loop and ask again

    # Computer randomly picks Rock, Paper, or Scissors
    computer = random.choice(["rock", "paper", "scissors"])
    print("Computer chose:", computer)

    # Decide the result
    if player == computer:
        print("🤝 It's a tie!")  # Same choice → tie
    elif (player == "rock" and computer == "scissors") \
         or (player == "paper" and computer == "rock") \
         or (player == "scissors" and computer == "paper"):
        print("🎉 You win!")  # Player beats computer
    else:
        print("💻 Computer wins!")  # Computer beats player
