def calculate(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero is not allowed."
    else:
        return "Invalid operation."
print("Welcome to the simple calculator!")
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    print("Choose an operation (add, subtract, multiply, divide): ")
    operation = input().lower()
    result = calculate(num1, num2, operation)
    print(f"The result of {operation}ing {num1} and {num2} is: {result}")
except ValueError:
    print("Invalid input! Please enter numerical values.")
