"""
CP1404/CP5632 Practical
Exceptions demo with Q&A
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        print("Cannot divide by zero.")
    else:
        print(numerator / denominator)
except ValueError:
    print("Please enter valid integers.")

# Q1: ValueError -> when non-integer entered
# Q2: ZeroDivisionError -> when denominator = 0
# Q3: Avoid ZeroDivisionError by checking denominator before dividing
print("Finished.")
