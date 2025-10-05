"""
CP1404/CP5632 Practical
String formatting examples and exercises
"""

# Example
guitar = "Gibson L-5 CES"
year = 1922
cost = 16036
print(f"{year} {guitar} for about ${cost:,.0f}!")

# Powers of 2 table
for exponent in range(0, 11):
    print(f"2 ^{exponent:2d} is {2 ** exponent:4d}")
