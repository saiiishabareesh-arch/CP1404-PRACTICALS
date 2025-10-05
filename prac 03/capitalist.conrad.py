"""
CP1404/CP5632 Practical
Capitalist Conrad - stock price simulator
"""
import random

MAX_INCREASE = 0.175  # up to 17.5%
MAX_DECREASE = 0.05   # up to 5%
MIN_PRICE = 1.0
MAX_PRICE = 100.0
INITIAL_PRICE = 10.0
FILENAME = "conrad_prices.txt"

price = INITIAL_PRICE
number_of_days = 0

out_file = open(FILENAME, 'w')
print(f"Starting price: ${price:,.2f}", file=out_file)

while MIN_PRICE <= price <= MAX_PRICE:
    number_of_days += 1
    if random.randint(1, 2) == 1:
        price *= (1 + random.uniform(0, MAX_INCREASE))
    else:
        price *= (1 - random.uniform(0, MAX_DECREASE))
    print(f"On day {number_of_days} price is: ${price:,.2f}", file=out_file)

out_file.close()
