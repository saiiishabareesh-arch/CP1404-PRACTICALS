"""
Word Occurrences
Estimate: 20 minutes
Actual:   __ minutes
"""

def main():
    text = input("Text: ").strip()
    words = text.split()
    counts = {}
    for w in words:
        w = w.lower()
        counts[w] = counts.get(w, 0) + 1

    longest = max((len(w) for w in counts), default=0)
    for word in sorted(counts):
        print(f"{word:{longest}} : {counts[word]}")


if __name__ == "__main__":
    main()
