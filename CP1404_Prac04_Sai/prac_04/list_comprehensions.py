"""
CP1404 - Practical 04
File: list_comprehensions.py
Practice a variety of list comprehensions.
"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
names = ["Bob", "Alice", "Chad", "Diana", "Eleanor"]

# Examples
squares = [n ** 2 for n in numbers]
evens = [n for n in numbers if n % 2 == 0]
name_lengths = [len(name) for name in names]

print("squares:", squares)
print("evens:", evens)
print("name_lengths:", name_lengths)

# TODOs (completed):
# 1) numbers greater than 9
gt_nine = [n for n in numbers if n > 9]
print("greater than 9:", gt_nine)

# 2) first letters of each name
first_letters = [name[0] for name in names]
print("first letters:", first_letters)

# 3) names of length >= 4 (lowercased)
long_lower = [name.lower() for name in names if len(name) >= 4]
print("lowercase long names:", long_lower)

# 4) numbers as strings with leading zeros width=2 (e.g., '01')
two_digit_strings = [f"{n:02d}" for n in numbers]
print("two-digit strings:", two_digit_strings)