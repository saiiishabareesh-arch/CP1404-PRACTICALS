"""
Menu demo: ask for a name; (H)ello, (G)oodbye, (Q)uit.
"""

name = input("Enter name: ")
menu = "(H)ello\n(G)oodbye\n(Q)uit"
print(menu)
choice = input(">>> ").upper()

while choice != "Q":
    if choice == "H":
        print(f"Hello {name}")
    elif choice == "G":
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")
    print(menu)
    choice = input(">>> ").upper()

print("Finished.")

# Pseudocode:
# get name
# display menu
# get choice
# while choice != Q
#     if choice == H
#         display "Hello name"
#     else if choice == G
#         display "Goodbye name"
#     else
#         display "Invalid choice"
#     display menu
#     get choice
# display "Finished."
