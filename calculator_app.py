class Calculator:
    # Method for addition
    def add(self, a, b):
        return a + b

    # Method for subtraction
    def subtract(self, a, b):
        return a - b

    # Method for multiplication
    def multiply(self, a, b):
        return a * b

    # Method for division
    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero is undefined."
        return a / b


# Main function to interact with the user
def main():
    calc = Calculator()  # Create an instance of the Calculator class

    print("Welcome to the Python Calculator!")
    print("Available operations: + (add), - (subtract), * (multiply), / (divide)")

    # Await user input
    operation = input("Enter the operation (+, -, *, /): ").strip()
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Error: Please enter valid numeric values.")
        return

    # Execute the desired operation
    if operation == '+':
        result = calc.add(num1, num2)
    elif operation == '-':
        result = calc.subtract(num1, num2)
    elif operation == '*':
        result = calc.multiply(num1, num2)
    elif operation == '/':
        result = calc.divide(num1, num2)
    else:
        print("Error: Invalid operation entered.")
        return

    print(f"The result is: {result}")


# Run the program
if __name__ == "__main__":
    main()