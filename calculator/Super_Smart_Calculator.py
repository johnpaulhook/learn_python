# 🧮 Super Smart Calculator
# This version uses eval() so you can type full math expressions
# Example:  10 + 5 * 2 - 8 / 4   →   18.0
# Example:  (3 + 2) * 5          →   25

print("Welcome to Super Smart Calculator! Type 'quit' to exit.")  # Greeting message at start

while True:  # Start infinite loop so program keeps running
    # Step 1: Ask user for a math expression
    expression = input("\nEnter a math expression: ")

    # Step 2: Allow quitting
    if expression.lower() == "quit":   # .lower() allows "QUIT", "Quit", etc.
        print("Goodbye! 👋")
        break  # Exit the loop → program ends

    try:
        # Step 3: Evaluate the expression safely
        # eval() takes a string and runs it as Python code
        # Example: "10 + 5 * 2" → eval() → 20
        result = eval(expression)

        # Step 4: Show the result
        print("Result:", result)

    except ZeroDivisionError:
        # Special case → if user tries to divide by zero
        print("❌ Error! Cannot divide by zero.")

    except Exception as e:
        # Catch any other errors (like typing letters or invalid symbols)
        print("❌ Invalid expression!", e)
