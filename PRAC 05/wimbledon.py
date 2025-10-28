"""
Wimbledon
Estimate: 35 minutes
Actual:   __ minutes
"""

FILENAME = "wimbledon.csv"


def load_data(filename):
    rows = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        header = in_file.readline()  # discard header
        for line in in_file:
            parts = [p.strip() for p in line.strip().split(",")]
            if len(parts) >= 3:
                rows.append(parts)
    return rows


def count_champions(rows):
    # Assuming columns: year, champion, country
    wins = {}
    for row in rows:
        champion = row[1]
        wins[champion] = wins.get(champion, 0) + 1
    return wins


def collect_countries(rows):
    countries = set()
    for row in rows:
        country = row[2]
        countries.add(country)
    return countries


def print_champions(wins):
    print("Wimbledon Champions:")
    for champion, count in sorted(wins.items(), key=lambda kv: (kv[0].split()[-1], kv[0])):
        print(champion, count)


def print_countries(countries):
    country_list = sorted(countries)
    print(f"\nThese {len(country_list)} countries have won Wimbledon:")
    print(", ".join(country_list))


def main():
    rows = load_data(FILENAME)
    wins = count_champions(rows)
    countries = collect_countries(rows)
    print_champions(wins)
    print_countries(countries)


if __name__ == "__main__":
    main()
