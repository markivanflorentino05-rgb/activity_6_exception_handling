"""
Simple Calculator with OOP and Exception Handling
Author: [Mark Ivan Florentino]
Date: 2026-05-01
"""

LOGO = r"""
   *********************************************
   *       SIMPLE CALCULATOR (OOP Edition)     *
   *         ~ with Exception Handling ~       *
   *********************************************
"""

class Operation:
    """Base class for all arithmetic operations."""
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        """Perform the operation. Must be overridden by subclasses."""
        raise NotImplementedError("Subclasses must implement execute()")


class Addition(Operation):
    """Addition of two numbers."""
    def execute(self):
        return self.a + self.b


class Subtraction(Operation):
    """Subtraction of two numbers."""
    def execute(self):
        return self.a - self.b


class Multiplication(Operation):
    """Multiplication of two numbers."""
    def execute(self):
        return self.a * self.b


class Division(Operation):
    """Division of two numbers, with zero-division check."""
    def execute(self):
        if self.b == 0:
            raise ZeroDivisionError("Cannot divide by zero!")
        return self.a / self.b


def get_number(prompt):
    """
    Ask the user for a number, repeat until valid input.
    Handles ValueError (non-numeric input).
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❗ Invalid input. Please enter a number (e.g., 5, 3.14).")


def format_result(result):
    """
    Format the result: show as integer if it's a whole number,
    otherwise show with up to 5 decimal places.
    """
    if result == int(result):
        return str(int(result))
    else:
        return f"{result:.5f}"


def calculate(choice, a, b):
    """
    Factory-like function that returns the result of the chosen operation.
    """
    if choice == 1:
        return Addition(a, b).execute()
    elif choice == 2:
        return Subtraction(a, b).execute()
    elif choice == 3:
        return Multiplication(a, b).execute()
    elif choice == 4:
        return Division(a, b).execute()
    else:
        raise ValueError("Invalid operation choice")


def main():
    """Main program loop."""
    print(LOGO)
    while True:
        # Show menu and get user choice
        print("\n--- Available Operations ---")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        try:
            choice = int(input("\nEnter your choice (1-4): "))
            if choice not in [1, 2, 3, 4]:
                print("❗ Please choose a number between 1 and 4.")
                continue
        except ValueError:
            print("❗ Invalid input. Enter a number (1, 2, 3, or 4).")
            continue

        # Get the two numbers
        num1 = get_number("First number: ")
        num2 = get_number("Second number: ")

        # Perform calculation with error handling
        try:
            result = calculate(choice, num1, num2)
            print(f"\n✅ RESULT: {format_result(result)}")
        except ZeroDivisionError as e:
            print(f"\n❌ Math Error: {e}")
        except Exception as e:
            # Catch any other unforeseen error
            print(f"\n❌ An unexpected error occurred: {e}")

        # Ask to repeat
        again = input("\n🔄 Try again? (y/n): ").lower()
        if again != 'y':
            print("\nThank you for using the calculator! 👋")
            break


if __name__ == "__main__":
    main()