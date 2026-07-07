# Calculator functions

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

try:
    user_input = input("Enter two numbers and an operator separated by a space: ")

    numbers = user_input.split()

    a = float(numbers[0])
    b = float(numbers[1])
    operator = numbers[2]

    if operator == "+":
        result = add(a, b)
    elif operator == "-":
        result = subtract(a, b)
    elif operator == "*":
        result = multiply(a, b)
    elif operator == "/":
        result = divide(a, b)
    else:
        result = "Error: Invalid operator."

    print(result)

except ValueError:
    print("Error: Please enter valid numbers.")
except IndexError:
    print("Error: Please enter two numbers and an operator.")