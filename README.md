# 🧮 Simple Calculator (OOP + Exception Handling)

A **feature-rich calculator** built with Python that demonstrates **Object-Oriented Programming (OOP)**, **inheritance**, and **robust exception handling**. The program repeatedly asks the user to choose an arithmetic operation, input two numbers, and displays the result – with cool emojis, formatted output, and a friendly loop.

## 🚀 Features

- ➕ Addition  
- ➖ Subtraction  
- ✖️ Multiplication  
- ➗ Division (with zero-division check)  
- 🔁 "Try again?" loop  
- ❗ Handles non‑numeric input (e.g., letters) and division by zero  
- 📦 **OOP design** – base `Operation` class + 4 child classes  
- 🧹 Clean result formatting (shows integers without `.0`)  
- 😎 ASCII logo and emoji feedback ("maangas" touch)  
- 📝 Full docstrings and comments for readability  

## 🧪 Requirements

- Python 3.6 or higher (uses f‑strings)

## 🏃 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/oop-calculator.git
   cd oop-calculator
   
2. Run the calculator:
   python calculator.py

## 📸 Demo
A demo video is available at: [Insert YouTube / Google Drive link here]

The video shows:

All four operations working correctly

Division by zero error message

Entering letters instead of numbers

The "Try again?" loop and exit message

## 🧱OOP Structure (Inheritance)
 Operation (abstract base)
    ├── Addition
    ├── Subtraction
    ├── Multiplication
    └── Division
    
Operation defines __init__(self, a, b) and an execute() method that must be overridden.

Each child class implements its own execute() logic.

The calculate() function acts as a simple factory that returns the result using the appropriate class

## ⚠️ Exception Handling
ValueError – Caught when the user enters something that isn't a number or a valid menu choice.

ZeroDivisionError – Raised in Division.execute() and caught in the main loop.

Exception – A final catch‑all prevents any crash.

## 📝 Git Commit Milestones (10 commits)
The commit history shows a work‑in‑progress evolution:

Initial skeleton: main loop and basic input

Add base Operation class with inheritance structure

Implement Addition and Subtraction classes

Implement Multiplication and Division classes

Add exception handling for division by zero and non-numeric input

Integrate OOP calculator logic into main flow

Add 'Try again?' loop and proper exit message

Improve result formatting: show integers without decimal

Add ASCII logo and emojis for a polished user experience

Final polish: docstrings, comments, and catch-all exception handler
