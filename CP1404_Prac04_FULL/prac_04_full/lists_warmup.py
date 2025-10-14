# CP1404 - Practical 04
# File: lists_warmup.py
# Start value:
numbers = [3, 1, 4, 1, 5, 9, 2]

# === Without running the code, predicted answers ===
# numbers[0]              -> 3
# numbers[-1]             -> 2
# numbers[3]              -> 1
# numbers[:-1]            -> [3, 1, 4, 1, 5, 9]
# numbers[3:4]            -> [1]
# 5 in numbers            -> True
# 7 in numbers            -> False
# "3" in numbers          -> False
# numbers + [6, 5, 3]     -> [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# === Now perform the requested statements ===
numbers[0] = "ten"            # Change the first element to string "ten"
numbers[-1] = 1               # Change the last element to 1
print(numbers[2:])            # Print all elements except the first two
print(9 in numbers)           # Print whether 9 is an element