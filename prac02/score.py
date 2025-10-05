"""Score classifier with pure decision function."""

# CONSTANTS
MIN_SCORE = 0
MAX_SCORE = 100
EXCELLENT_CUTOFF = 90
PASSABLE_CUTOFF = 50

def main():
    """Ask for a score, classify it, then classify a random score."""
    from random import randint

    score = get_valid_score(MIN_SCORE, MAX_SCORE)
    result = classify_score(score)
    print(f"Your score: {score} -> {result}")

    random_score = randint(MIN_SCORE, MAX_SCORE)
    random_result = classify_score(random_score)
    print(f"Random score: {random_score} -> {random_result}")

def get_valid_score(min_score: int, max_score: int) -> float:
    """Get a valid score within the inclusive range."""
    score = float(input(f"Enter score ({min_score}-{max_score}): "))
    while score < min_score or score > max_score:
        print("Invalid score.")
        score = float(input(f"Enter score ({min_score}-{max_score}): "))
    return score

def classify_score(score: float) -> str:
    """
    Return a label for the given score.
    Decision structure only returns a label (no printing).
    """
    if score >= EXCELLENT_CUTOFF:
        return "Excellent"
    elif score >= PASSABLE_CUTOFF:
        return "Passable"
    else:
        return "Bad"

if __name__ == "__main__":
    main()
