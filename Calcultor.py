def add(x, y):
    """
    This function adds two numbers.
    """
    return x + y

def subtract(x, y):
    """
    This function subtracts the second number from the first.
    """
    return x - y

def multiply(x, y):
    """
    This function multiplies two numbers.
    """
    return x * y

def divide(x, y):
    """
    This function divides the first number by the second.
    """
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def calculator():
    """
    This function performs the basic calculator operations.
    """
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        # Take input from the user
        choice = input("Enter choice (1/2/3/4): ")

        # Check if choice is one of the four options
        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"The result of addition is: {add(num1, num2)}")
            elif choice == '2':
                print(f"The result of subtraction is: {subtract(num1, num2)}")
            elif choice == '3':
                print(f"The result of multiplication is: {multiply(num1, num2)}")
            elif choice == '4':
                print(f"The result of division is: {divide(num1, num2)}")
            
            # Check if the user wants to perform another calculation
            next_calculation = input("Do you want to perform another calculation? (yes/no): ")
            if next_calculation.lower() != 'yes':
                break
        else:
            print("Invalid input. Please enter a number between 1 and 4.")

# Run the calculator
if __name__ == "__main__":
    calculator()
