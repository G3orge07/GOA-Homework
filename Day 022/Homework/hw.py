def display_menu():
    print("\nSimple Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

def main():
    while True:
        display_menu()
        choice = input("Please select an operation (1-5): ")

        if choice == '1':
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                result = num1 + num2
                print(f"The result of {num1} + {num2} is {result}")
            except ValueError:
                print("Invalid input. Please enter numeric values.")

        elif choice == '2':
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                result = num1 - num2
                print(f"The result of {num1} - {num2} is {result}")
            except ValueError:
                print("Invalid input. Please enter numeric values.")

        elif choice == '3':
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                result = num1 * num2
                print(f"The result of {num1} * {num2} is {result}")
            except ValueError:
                print("Invalid input. Please enter numeric values.")

        elif choice == '4':
            try:
                num1 = float(input("Enter the numerator: "))
                num2 = float(input("Enter the denominator: "))
                if num2 != 0:
                    result = num1 / num2
                    print(f"The result of {num1} / {num2} is {result}")
                else:
                    print("Error: Division by zero is not allowed.")
            except ValueError:
                print("Invalid input. Please enter numeric values.")
        
        elif choice == '5':
            print("Exiting the calculator. Goodbye!")
            break

        else:
            print("Invalid option. Please choose a number between 1 and 5.")

if __name__ == "__main__":
    main()