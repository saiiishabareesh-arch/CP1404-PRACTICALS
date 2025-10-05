"""Generate random scores and write classifications to a file."""

from random import randint

# CONSTANTS
MIN_SCORE = 0
MAX_SCORE = 100
OUTPUT_FILE = "results.txt"
EXCELLENT_CUTOFF = 90
PASSABLE_CUTOFF = 50

def main():
    """Write N random score classifications to a file."""
    count = get_positive_integer("How many scores? ")
    with open(OUTPUT_FILE, "w", encoding="utf-8") as out_file:
        for _ in range(count):
            score = randint(MIN_SCORE, MAX_SCORE)
            label = classify_score(score)
            out_file.write(f"{score} is {label}\n")
    print(f"Wrote {count} results to {OUTPUT_FILE}")

def get_positive_integer(prompt: str) -> int:
    """Return a positive integer from user input."""
    value = int(input(prompt))
    while value <= 0:
        print("Enter a positive number.")
        value = int(input(prompt))
    return value

def classify_score(score: float) -> str:
    """Return label for a score (reused logic)."""
    if score >= EXCELLENT_CUTOFF:
        return "Excellent"
    elif score >= PASSABLE_CUTOFF:
        return "Passable"
    else:
        return "Bad"

if __name__ == "__main__":
    main()
