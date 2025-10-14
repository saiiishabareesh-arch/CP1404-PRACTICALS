"""
CP1404 - Practical 04
File: total_income.py
- Ask for number of months, then incomes for each month.
- Print a formatted income report with cumulative totals.
Refactors included:
- Use an f-string for input prompt
- Rename 'months' (ambiguous) to 'month_count' via refactor
- Move report printing into its own function using enumerate
"""
def main():
    month_count = get_positive_int("How many months? ")
    incomes = collect_incomes(month_count)
    print_income_report(incomes)


def get_positive_int(prompt: str) -> int:
    """Prompt until a positive integer is entered; return it."""
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Please enter a positive integer.")
        except ValueError:
            print("Please enter a valid integer.")


def collect_incomes(month_count: int) -> list[float]:
    """Read month_count incomes and return them as a list of floats."""
    incomes = []
    for month in range(1, month_count + 1):
        while True:
            try:
                income = float(input(f"Enter income for month {month}: "))
                break
            except ValueError:
                print("Please enter a valid number.")
        incomes.append(income)
    print()  # blank line before report
    return incomes


def print_income_report(incomes: list[float]) -> None:
    """Print a nicely formatted Income Report with cumulative totals."""
    print("Income Report")
    print("-------------")
    running_total = 0.0
    for month_index, income in enumerate(incomes, start=1):
        running_total += income
        print(f"Month {month_index:2d} - Income: ${income:10.2f}   Total: ${running_total:10.2f}")


if __name__ == "__main__":
    main()