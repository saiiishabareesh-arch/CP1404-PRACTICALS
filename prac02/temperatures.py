"""Temperature converter with pure calculation functions."""

# CONSTANTS
MENU_PROMPT = "(C)elsius to Fahrenheit\n(F)ahrenheit to Celsius\n(Q)uit\n"
CELSIUS_OPTION = "C"
FAHRENHEIT_OPTION = "F"
QUIT_OPTION = "Q"

def main():
    """Show a menu and convert temperatures."""
    print("Temperature Converter")
    choice = input(MENU_PROMPT).strip().upper()
    while choice != QUIT_OPTION:
        if choice == CELSIUS_OPTION:
            celsius = float(input("Celsius: "))
            print(f"Fahrenheit: {celsius_to_fahrenheit(celsius):.2f}")
        elif choice == FAHRENHEIT_OPTION:
            fahrenheit = float(input("Fahrenheit: "))
            print(f"Celsius: {fahrenheit_to_celsius(fahrenheit):.2f}")
        else:
            print("Invalid option")
        choice = input(MENU_PROMPT).strip().upper()
    print("Goodbye.")

def celsius_to_fahrenheit(celsius: float) -> float:
    """Return Fahrenheit from Celsius."""
    return celsius * 9 / 5 + 32

def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Return Celsius from Fahrenheit."""
    return (fahrenheit - 32) * 5 / 9

if __name__ == "__main__":
    main()
