"""
CP1404 - Practical 04
File: quick_picks.py
Generate "quick pick" lottery lines.
Constraints:
- 6 numbers per line
- Each between 1 and 45 inclusive
- No duplicates within a line
- Sorted ascending
- Nicely aligned output
- Do NOT use random.sample
"""
from random import randint

MIN = 1
MAX = 45
NUMBERS_PER_PICK = 6


def main():
    count = get_positive_int("How many quick picks? ")
    for _ in range(count):
        line = generate_quick_pick()
        line.sort()
        print(" ".join(f"{n:2d}" for n in line))


def generate_quick_pick() -> list[int]:
    pick: list[int] = []
    while len(pick) < NUMBERS_PER_PICK:
        n = randint(MIN, MAX)
        if n not in pick:
            pick.append(n)
    return pick


def get_positive_int(prompt: str) -> int:
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Please enter a positive integer.")
        except ValueError:
            print("Please enter a valid integer.")


if __name__ == "__main__":
    main()