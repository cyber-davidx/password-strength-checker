print("Welcome to the upgraded calculator!")
print("Type 'quit' at any time to exit.\n")

while True:
    # Get user input
    first = input("Enter the first number: ")
    if first.lower() == "quit":
        break

    operator = input("Enter an operator (+, -, *, /, ^, %): ")
    if operator.lower() == "quit":
        break

    second = input("Enter the second number: ")
    if second.lower() == "quit":
        break

    # Try to convert input to numbers
    try:
        num1 = float(first)
        num2 = float(second)

        # Perform the operation
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                result = "Error! Cannot divide by zero."
            else:
                result = num1 / num2
        elif operator == "^":
            result = num1 ** num2
        elif operator == "%":
            result = num1 % num2
        else:
            result = "Invalid operator."

    except ValueError:
        result = "Invalid number input."

    # Show the result
    print("Result:", result, "\n")

print("Thanks for using the calculator. Goodbye!")


