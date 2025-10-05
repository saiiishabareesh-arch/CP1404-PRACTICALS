"""
CP1404/CP5632 Practical
Exceptions to complete - input validation
"""

while True:
    try:
        result = int(input("Enter a valid integer: "))
        break
    except ValueError:
        print("Invalid input; enter an integer.")
print(f"You entered: {result}")
