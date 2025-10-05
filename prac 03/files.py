"""
CP1404/CP5632 Practical
Files exercises
"""

# 1. Ask for name and write it to file
name = input("Name: ")
out_file = open("name.txt", "w")
print(name, file=out_file)
out_file.close()

# 2. Read name from file and greet
in_file = open("name.txt", "r")
read_name = in_file.read().strip()
in_file.close()
print(f"Hi {read_name}!")

# 3. Read first two numbers and print total (expect 59)
with open("numbers.txt") as f:
    first = int(f.readline())
    second = int(f.readline())
print(first + second)

# 4. Sum all numbers in numbers.txt
total = 0
with open("numbers.txt") as f:
    for line in f:
        total += int(line.strip())
print(total)
