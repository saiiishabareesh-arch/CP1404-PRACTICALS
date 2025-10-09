"""
Menu-driven number sequence generator:
1. Even numbers from x to y
2. Odd numbers from x to y
3. Squares from x to y (prints n^2)
4. Exit
"""

# Gather x and y once
x = int(input("Enter x: "))
y = int(input("Enter y: "))
if x > y:
    x, y = y, x  # normalise so x <= y

MENU = (
    "1. Show the even numbers from x to y\n"
    "2. Show the odd numbers from x to y\n"
    "3. Show the squares of the numbers from x to y\n"
    "4. Exit"
)

print(MENU)
choice = input(">>> ").strip()

while choice != "4":
    if choice == "1":
        for i in range(x + (x % 2), y + 1, 2):  # start at first even >= x
            print(i, end=" ")
        print()
    elif choice == "2":
        start = x if x % 2 == 1 else x + 1      # first odd >= x
        for i in range(start, y + 1, 2):
            print(i, end=" ")
        print()
    elif choice == "3":
        for i in range(x, y + 1):
            print(i * i, end=" ")
        print()
    else:
        print("Invalid choice")

    print(MENU)
    choice = input(">>> ").strip()

print("Finished.")

# Pseudocode:
# get x
# get y
# if x > y
#     swap x and y
#
# display menu
# get choice
# while choice != "4"
#     if choice == "1"
#         for i from first even between x..y
#             display i
#     else if choice == "2"
#         for i from first odd between x..y
#             display i
#     else if choice == "3"
#         for i from x to y
#             display i squared
#     else
#         display "Invalid choice"
#     display menu
#     get choice
# display "Finished."
