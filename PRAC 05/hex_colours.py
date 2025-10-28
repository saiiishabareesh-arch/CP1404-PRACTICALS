"""
Hex Colour Lookup
"""

COLOUR_TO_HEX = {
    "aliceblue": "#f0f8ff",
    "antiquewhite": "#faebd7",
    "aqua": "#00ffff",
    "aquamarine": "#7fffd4",
    "azure": "#f0ffff",
    "beige": "#f5f5dc",
    "bisque": "#ffe4c4",
    "black": "#000000",
    "blue": "#0000ff",
    "blueviolet": "#8a2be2",
    "brown": "#a52a2a",
}


def main():
    while True:
        colour = input("Colour name: ").strip()
        if not colour:
            break
        print(COLOUR_TO_HEX.get(colour.lower(), "Invalid colour name"))


if __name__ == "__main__":
    main()
