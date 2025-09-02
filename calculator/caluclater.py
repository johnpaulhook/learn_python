# Simple Calculator

# Step 1: Get numbers
num1 = float(input("Enter the first number: "))  # ask for 1st number
num2 = float(input("Enter the second number: "))  # ask for 2nd number

# Step 2: Get operation
print("Choose operation: +, -, *, /") # ask for operation  +, -, *, /
operation = input("Enter your choice: ") # store your choice in operation 

# Step 3: Do the calculation
if operation == "+": # if we type +
    result = num1 + num2  # it will add
elif operation == "-":  # if we type - 
    result = num1 - num2  # it will subtract 
elif operation == "*":  # if we type *
    result = num1 * num2  # it will multipy
elif operation == "/":  #if we type /
    if num2 != 0:  # if num2 is not 0
        result = num1 / num2  # it will divide normaly
    else:  # if not 
        result = "Error! Cannot divide by zero."  # print  "Error! Cannot divide by zero."
else:  # if not either 
    result = "Invalid operation."  # print "Invalid operation."

# Step 4: Show result
print("Result:", result)  # show the result to the operation
