# ✅ 1. try-except (Error Handling)
# Purpose:
# Handle runtime errors gracefully without crashing your program.

try:
    userInput = int(input("Enter a number: "))
    result = 10/userInput
    print(f"Result: {result}")
except ZeroDivisionError:
    print("You can not divide it by Zero")
except ValueError:
    print("This is not a number, please enter valid number")