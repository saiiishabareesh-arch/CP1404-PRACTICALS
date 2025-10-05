"""Menu-driven score program that reuses classification and shows stars."""

# IMPORT your classify function or copy it in this file.
from random import randint

# CONSTANTS
MIN_SCORE = 0
MAX_SCORE = 100
EXCELLENT_CUTOFF = 90
PASSABLE_CUTOFF = 50

MENU_TEXT = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit\n"

def main():
    """Run the score menu program."""
    print("Score Menu")
    score = get_valid_score(MIN_SCORE, MAX_SCORE)  # pre-get as required
    choice = input(MENU_TEXT).strip().upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score(MIN_SCORE, MAX_SCORE)
        elif choice == "P":
            print(classify_score(score))
        elif choice == "S":
            show_stars(score)
        else:
            print("Invalid option")
        choice = input(MENU_TEXT).strip().upper()
    print("Farewell.")

def get_valid_score(min_score: int, max_score: int) -> int:
    """Get a valid score within the inclusive range."""
    value = int(input(f"Enter score ({min_score}-{max_score}): "))
    while value < min_score or value > max_score:
        print("Invalid score.")
        value = int(input(f"Enter score ({min_score}-{max_score}): "))
    return value

def classify_score(score: float) -> str:
    """Return a label for the score (pure decision)."""
    if score >= EXCELLENT_CUTOFF:
        return "Excellent"
    elif score >= PASSABLE_CUTOFF:
        return "Passable"
    else:
        return "Bad"

def show_stars(score: int, symbol: str = "*") -> None:
    """Print stars equal to the score value."""
    print(symbol * score)

if __name__ == "__main__":
    main()
