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
        return self.a / self.b

def main():
    while True:
        print("\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")
        try:
            choice = int(input("Choose operation (1-4): "))
        except ValueError:
            print("Invalid input. Please enter 1-4.")
            continue

        try:
            num1 = float(input("First number: "))
            num2 = float(input("Second number: "))
        except ValueError:
            print("Invalid number. Please try again.")
            continue

        if choice == 1:
            op = Addition(num1, num2)
        elif choice == 2:
            op = Subtraction(num1, num2)
        elif choice == 3:
            op = Multiplication(num1, num2)
        elif choice == 4:
            op = Division(num1, num2)
        else:
            print("Invalid choice.")
            continue

        result = op.execute()
        print(f"Result: {result}")

        again = input("Try again? (y/n): ").lower()
        if again != 'y':
            break
    print("Thank you!")

if __name__ == "__main__":
    main()