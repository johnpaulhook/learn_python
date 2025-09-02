# Upgraded Calculator - Keeps running until you quit

while True: 
    # Step 1: Ask the user if they want to quit
    print("\n--- Simple Calculator ---")  # makes newline then prints -- Simple Calculator --
    print("Type 'quit' anytime to exit.")  # prints "Type 'quit' anytime to exit." bellow the -- Simple Calculator --

    # Step 2: Get first number
    num1 = input("Enter the first number: ") # whatever number You put gets stored in the num1
    if num1.lower() == "quit": # if you type quit 
        break  # turn off calculator
    num1 = float(num1)  # turn num1 into a decimal number

    # Step 3: Get second number
    num2 = input("Enter the second number: ")# whatever number You put gets stored in the num2
    if num2.lower() == "quit":# if you type quit 
        break # turn off calculator
    num2 = float(num2)# turn num2 into a decimal number

    # Step 4: Get operation
    print("Choose operation: +, -, *, /")  #prints ("Choose operation: +, -, *, /")
    operation = input("Enter your choice: ") # witch ever you put gets stored in operation 
    if operation.lower() == "quit":# if you type quit 
        break# turn off calculator

    # Step 5: Do the calculation
    if operation == "+":# if you type +
        result = num1 + num2# add the numbers
    elif operation == "-":# if you type -
        result = num1 - num2# subtract the numbers
    elif operation == "*":# if you type *
        result = num1 * num2# multiply the numbers 
    elif operation == "/":# if you type /
        if num2 != 0: # if a number not 0
            result = num1 / num2# divide
        else:# if not 
            result = "Error! Cannot divide by zero."# print "Error! Cannot divide by zero."
    else:# if niether
        result = "Invalid operation." # print "Invalid operation."

    # Step 6: Show result
    print("Result:", result) # show the result 

print("Goodbye! 👋") # if you said quit it says good bye
