"""
Prac 05 – State Names
"""

CODE_TO_NAME = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "SA": "South Australia",
    "TAS": "Tasmania",
    "VIC": "Victoria",
    "ACT": "Australian Capital Territory",
}


def print_all_states():
    """Print all state abbreviations and names neatly aligned."""
    width = max(len(code) for code in CODE_TO_NAME)
    for code, name in sorted(CODE_TO_NAME.items()):
        print(f"{code:<{width}} is {name}")


def main():
    print("Enter short state (blank to quit)")
    while True:
        state_code = input("State: ").strip()
        if not state_code:
            break
        try:
            print(CODE_TO_NAME[state_code.upper()])
        except KeyError:
            print("Invalid short state")
    print("\nAll states:")
    print_all_states()


if __name__ == "__main__":
    main()
