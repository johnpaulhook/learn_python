# 🧮 Smarter Calculator
# Lets you type full expressions like:  10 + 5

print("Welcome to Smart Calculator! Type 'quit' to exit.")  # Greeting message

while True:  # Start an infinite loop (will keep running until we 'break')
    # Step 1: Ask user for the full expression
    expression = input("\nEnter calculation (e.g., 10 + 5): ")

    # Step 2: Allow quitting
    if expression.lower() == "quit":   # .lower() makes it case-insensitive ("Quit", "QUIT")
        print("Goodbye! 👋")
        break  # Exit the loop → program ends

    # Step 3: Split input into pieces (number, operator, number)
    parts = expression.split()   # Example: "10 + 5" → ["10", "+", "5"]

    # If user didn't type exactly 3 parts, show error
    # Examples:
    # "7 * 4" → ["7","*","4"] → OK
    # "7 *" → ["7","*"] → WRONG (only 2 parts)
    # "7 * 4 2" → ["7","*","4","2"] → WRONG (4 parts)
    if len(parts) != 3:
        print("❌ Invalid format! Use: number operator number (e.g., 7 * 4)")
        continue  # Skip rest of loop and ask again

    # Step 4: Assign each part to a variable
    num1, operation, num2 = parts  # Example: ["10","+","5"] → num1="10", operation="+", num2="5"

    # Step 5: Convert num1 and num2 into numbers (floats)
    try:
        num1 = float(num1)  # convert first input to a number
        num2 = float(num2)  # convert second input to a number
    except ValueError:
        # If conversion fails (like user typed "ten"), show error
        print("❌ Please enter valid numbers!")
        continue  # Ask again

    # Step 6: Perform the chosen operation
    if operation == "+":        # Addition
        result = num1 + num2
    elif operation == "-":      # Subtraction
        result = num1 - num2
    elif operation == "*":      # Multiplication
        result = num1 * num2
    elif operation == "/":      # Division
        if num2 != 0:           # Prevent dividing by zero
            result = num1 / num2
        else:
            result = "Error! Cannot divide by zero."
    else:
        # If user typed something other than + - * /
        result = "❌ Invalid operator!"

    # Step 7: Show the result
    print("Result:", result)
