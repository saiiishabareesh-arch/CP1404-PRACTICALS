"""
CP1404/CP5632 Practical
Random numbers demo and questions
"""
import random

print(random.randint(5, 20))       # inclusive 5–20
print(random.randrange(3, 10, 2))  # 3, 5, 7, 9
print(random.uniform(2.5, 5.5))    # float between 2.5–5.5

# Answers (in comments)
# 1. randint(5, 20): smallest=5, largest=20
# 2. randrange(3, 10, 2): smallest=3, largest=9; cannot be 4
# 3. uniform(2.5, 5.5): smallest≈2.5, largest≈5.5

# Random number 1–100 inclusive
print(random.randint(1, 100))
