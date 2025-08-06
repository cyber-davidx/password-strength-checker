print("🧠 Welcome to the Super Calculator!")
print("Choose a mode: '1' for step-by-step, '2' for expression mode, or 'quit' to exit.\n")

while True:
    mode = input("Select mode (1 / 2 / quit): ")

    if mode.lower() == "quit":
        print("Goodbye! 👋")
        break

    elif mode == "1":
        print("\n🔢 Step-by-Step Mode (Supports +, -, *, /, ^, %)\n")
        first = input("Enter the first number: ")
        if first.lower() == "quit":
            break

        operator = input("Enter an operator (+, -, *, /, ^, %): ")
        if operator.lower() == "quit":
            break

        second = input("Enter the second number: ")
        if second.lower() == "quit":
            break

        try:
            num1 = float(first)
            num2 = float(second)

            if operator == "+":
                result = num1 + num2
            elif operator == "-":
                result = num1 - num2
            elif operator == "*":
                result = num1 * num2
            elif operator == "/":
                result = "Error! Division by zero." if num2 == 0 else num1 / num2
            elif operator == "^":
                result = num1 ** num2
            elif operator == "%":
                result = num1 % num2
            else:
                result = "Invalid operator."

        except ValueError:
            result = "Invalid number input."

        print("Result:", result, "\n")

    elif mode == "2":
        print("\n🧮 Expression Mode (Example: 2 + 3 * (4 - 1))\n")
        expression = input("Enter your full expression: ")

        if expression.lower() == "quit":
            break

        try:
            result = eval(expression)
            print("Result:", result, "\n")
        except ZeroDivisionError:
            print("Error! Division by zero.\n")
        except Exception as e:
            print("Invalid input:", e, "\n")

    else:
        print("❌ Invalid mode. Please choose 1, 2, or 'quit'.\n")
