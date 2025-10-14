"""
CP1404/CP5632 Practical
Refactored cumulative total income program
Includes:
- f-string input
- refactored variable name (months -> month_count)
- function to print report using enumerate
"""


def main():
    """Display income report for incomes over a given number of months."""
    month_count = int(input("How many months? "))
    incomes = get_incomes(month_count)
    print_income_report(incomes)


def get_incomes(month_count):
    """Get income input for each month and store in a list."""
    incomes = []
    for month in range(1, month_count + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)
    print()  # blank line before report
    return incomes


def print_income_report(incomes):
    """Print formatted income report with cumulative totals."""
    print("Income Report")
    print("-------------")
    total = 0
    for month, income in enumerate(incomes, start=1):
        total += income
        print(f"Month {month:2} - Income: ${income:10.2f}   Total: ${total:10.2f}")


if __name__ == "__main__":
    main()