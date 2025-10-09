"""
Temperature conversion program:
Convert Celsius to  Fahrenheit.
"""

MENU = "(C)elsius to Fahrenheit\n(F)ahrenheit to Celsius\n(Q)uit"
print(MENU)
choice = input(">>> ").strip().upper()


def c_to_f(celsius: float) -> float:
    """Convert Celsius to Fahrenheit."""
    return celsius * 9 / 5 + 32


def f_to_c(fahrenheit: float) -> float:
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5 / 9


while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = c_to_f(celsius)
        print(f"Result: {fahrenheit:.2f} F")
    elif choice == "F":
        fahrenheit = float(input("Fahrenheit: "))
        celsius = f_to_c(fahrenheit)
        print(f"Result: {celsius:.2f} C")
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").strip().upper()


# Pseudocode:
# display menu
# get choice
# while choice != Q
#     if choice == C
#         get Celsius
#         convert to Fahrenheit
#         display result
#     else if choice == F
#         get Fahrenheit
#         convert to Celsius
#         display result
#     else
#         display "Invalid option"
#     display menu
#     get choice
# display "Thank you."



