# Basic Calculator

line01 = "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$" # header / footer
line02 = "$                                $" # re-use
line03 = "$ welcome to my basic calculator $" 

# show sign
print('')
print(line01)
print(line02)
print(line03)
print(line02)
print(line01)

while True:
    # GET NUMBER 1 FROM USER
    num1 = int((input("Enter the first number: "))) # INTEGER
    if not num1:
        print('Error, num1 cannot be empty!\n')
        continue

    # SELECT OPERATOR
    operator = input("Enter an operator (+, -, *, /): ")
    if not operator:
        print('Error, an opeartion must be done!\n')
        continue

    # GET NUMBER 2 FROM USER  
    num2 = int((input("Enter the second number: "))) # INTEGER
    if not num2:
        print('Error, cannot be left empty')
        continue

    # Do the calculation
    try:
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                result = "Error! Division by zero."
            else:
                result = num1 / num2
    except ValueError:
        print('Error: invalid input. Try again.\n')

    # Show the result
    print("Result:", result, "\n" " Hacker2.o!", '\n') 

