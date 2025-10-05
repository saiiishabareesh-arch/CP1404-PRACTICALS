"""
CP1404/CP5632 Practical
Password checker program
"""

MIN_LENGTH = 5
MAX_LENGTH = 15
REQUIRE_SPECIAL_CHARS = True
SPECIAL_CHARS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"

def is_valid_password(password: str) -> bool:
    """Validate password to meet all rules."""
    if not (MIN_LENGTH <= len(password) <= MAX_LENGTH):
        return False
    has_lower = has_upper = has_digit = has_special = False
    for char in password:
        if char.islower():
            has_lower = True
        elif char.isupper():
            has_upper = True
        elif char.isdigit():
            has_digit = True
        elif char in SPECIAL_CHARS:
            has_special = True
    if REQUIRE_SPECIAL_CHARS:
        return has_lower and has_upper and has_digit and has_special
    return has_lower and has_upper and has_digit


print("Please enter a valid password")
print(f"Your password must be between {MIN_LENGTH} and {MAX_LENGTH} characters, and contain:")
print("    1 or more uppercase characters")
print("    1 or more lowercase characters")
print("    1 or more numbers")
if REQUIRE_SPECIAL_CHARS:
    print(f"    and 1 or more special characters:  {SPECIAL_CHARS}")

while True:
    password = input("> ")
    if is_valid_password(password):
        print(f"Your {len(password)} character password is valid: {password}")
        break
    else:
        print("Invalid password!")
