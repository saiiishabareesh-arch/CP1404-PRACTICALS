"""
CP1404 - Practical 04
File: list_exercises.py
- Prompt user for 5 numbers, store in list, print stats
- Then perform a simple username access check
"""
AUTH_USERNAMES = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye',
                   'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
                   'Command', 'ExecState', 'InteractiveConsole',
                   'InterpreterInterface', 'StartServer', 'bob']


def main():
    numbers = []
    for _ in range(5):
        number = get_float("Number: ")
        numbers.append(number)

    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {sum(numbers) / len(numbers)}")

    print()  # blank line
    username = input("Username: ")
    if username in AUTH_USERNAMES:
        print("Access granted")
    else:
        print("Access denied")


def get_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


if __name__ == "__main__":
    main()