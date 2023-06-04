def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def divide(a, b):
    if b != 0:
        return a / b


def multiply(a, b):
    return a * b


def calculator():
    num1 = float(input('Enter first number: '))
    num2 = float(input('Enter second number: '))
    operation = input('Enter the operation(+,-,*,/): ')
    result = 0

    if operation == '+':
        result = add(num1, num2)
    elif operation == '-':
        result = subtract(num1, num2)
    elif operation == '*':
        result = multiply(num1, num2)
    elif operation == '/':
        result = divide(num1, num2)
    else:
        return 'Error:Invalid operation'

    return f'Result: {result}'


print(calculator())
