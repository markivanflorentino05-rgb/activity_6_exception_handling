class Operation:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def execute(self):
        raise NotImplementedError

def main():
    while True:
        num1 = input("First number: ")
        num2 = input("Second number: ")
        print(f"You entered {num1} and {num2}")
        again = input("Try again? (y/n): ").lower()
        if again != 'y':
            break
    print("Thank you!")

if __name__ == "__main__":
    main()