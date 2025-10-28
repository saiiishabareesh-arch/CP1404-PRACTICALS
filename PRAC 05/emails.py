"""
Emails
Estimate: 20 minutes
Actual:   __ minutes
"""

def extract_name(email: str) -> str:
    local = email.split("@", 1)[0]
    local = local.replace(".", " ").replace("_", " ")
    parts = [p for p in local.split() if p]
    return " ".join(p.title() for p in parts) if parts else ""


def main():
    email_to_name = {}
    while True:
        email = input("Email: ").strip()
        if email == "":
            break
        suggested = extract_name(email)
        choice = input(f"Is your name {suggested}? (Y/n) ").strip().lower()
        if choice not in ("", "y", "yes"):
            suggested = input("Name: ").strip()
        email_to_name[email] = suggested

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


if __name__ == "__main__":
    main()
