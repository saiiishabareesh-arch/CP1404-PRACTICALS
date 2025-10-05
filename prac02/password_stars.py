"""Password check with functions and constants."""

# CONSTANTS
MIN_PASSWORD_LENGTH = 8  # Avoid magic numbers

def main():
    """Run the password check program."""
    password = get_password(min_length=MIN_PASSWORD_LENGTH)
    print_stars(text=password)

def get_password(min_length: int) -> str:
    """Get a valid password that meets the minimum length."""
    password = input("Enter password: ")
    while len(password) < min_length:
        print(f"Password must be at least {min_length} characters.")
        password = input("Enter password: ")
    return password

def print_stars(text: str, symbol: str = "*") -> None:
    """Print stars equal to the length of the given text."""
    print(symbol * len(text))

if __name__ == "__main__":
    main()
