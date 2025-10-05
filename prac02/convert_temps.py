"""Convert Fahrenheit values in temps_input.txt to Celsius in temps_output.txt."""

INPUT_FILE = "temps_input.txt"
OUTPUT_FILE = "temps_output.txt"

def main():
    """Read Fahrenheit temps from file, write Celsius temps to file."""
    with open(INPUT_FILE, "r", encoding="utf-8") as in_file, \
         open(OUTPUT_FILE, "w", encoding="utf-8") as out_file:
        for line in in_file:
            fahrenheit = float(line.strip())
            celsius = fahrenheit_to_celsius(fahrenheit)
            out_file.write(f"{celsius}\n")
    print(f"Converted to {OUTPUT_FILE}")

def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Return Celsius from Fahrenheit."""
    return (fahrenheit - 32) * 5 / 9

if __name__ == "__main__":
    main()
