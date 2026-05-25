# Simple 2-digit Calculator in Python

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

# Take input
#num1 = int(input("Enter first 2-digit number: "))
#num2 = int(input("Enter second 2-digit number: "))

# Check if inputs are 2-digit
if 10 <= num1 <= 99 and 10 <= num2 <= 99:
    print("Select operation: +, -, *, /")
    choice = input("Enter choice: ")

    if choice == '+':
        print("Result:", add(num1, num2))
    elif choice == '-':
        print("Result:", subtract(num1, num2))
    elif choice == '*':
        print("Result:", multiply(num1, num2))
    elif choice == '/':
        print("Result:", divide(num1, num2))
    else:
        print("Invalid operation")
else:
    print("Please enter valid 2-digit numbers only.")

