LOGO = r"""
   *********************************************
   *       SIMPLE CALCULATOR (OOP Edition)     *
   *         ~ with Exception Handling ~       *
   *********************************************
"""

class Operation:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def execute(self):
        raise NotImplementedError

class Addition(Operation):
    def execute(self):
        return self.a + self.b

class Subtraction(Operation):
    def execute(self):
        return self.a - self.b

class Multiplication(Operation):
    def execute(self):
        return self.a * self.b

class Division(Operation):
    def execute(self):
        if self.b == 0:
            raise ZeroDivisionError("Cannot divide by zero!")
        return self.a / self.b

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❗ Invalid input. Please enter a number.")

def format_result(result):
    if result == int(result):
        return str(int(result))
    else:
        return f"{result:.5f}"

def calculate(choice, a, b):
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
    print(LOGO)
    while True:
        print("\n--- Available Operations ---")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        try:
            choice = int(input("\nEnter your choice (1-4): "))
            if choice not in [1,2,3,4]:
                print("❗ Please choose 1,2,3, or 4.")
                continue
        except ValueError:
            print("❗ Invalid input. Enter a number.")
            continue

        num1 = get_number("First number: ")
        num2 = get_number("Second number: ")

        try:
            result = calculate(choice, num1, num2)
            print(f"\n✅ RESULT: {format_result(result)}")
        except ZeroDivisionError as e:
            print(f"\n❌ Math error: {e}")
        except Exception as e:
            print(f"\n❌ Unexpected error: {e}")

        again = input("\n🔄 Try again? (y/n): ").lower()
        if again != 'y':
            print("\nThank you for using the calculator! 👋")
            break

if __name__ == "__main__":
    main()