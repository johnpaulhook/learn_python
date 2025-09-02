import random   # Import random module so we can generate random numbers

print("🎲 Welcome to Number Guessing Game!")  # Greeting message

# Pick a random secret number between 1 and 1000
secret = random.randint(1, 1000)

# Start an infinite loop → keeps running until player guesses correctly
while True:
    # Ask the player for a guess
    guess = int(input("Guess a number (1-1000): "))

    # If the guess is correct
    if guess == secret:
        print("🎉 Correct! You win!")
        break   # Exit the loop → game ends

    # If the guess is too low
    elif guess < secret:
        print("Too low ⬇️")

    # If the guess is too high
    else:
        print("Too high ⬆️")
