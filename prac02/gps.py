"""Gopher Population Simulator over 10 years."""

from random import randint

# CONSTANTS
STARTING_POPULATION = 1000
YEARS = 10
BIRTH_MIN_PERCENT = 10
BIRTH_MAX_PERCENT = 20
DEATH_MIN_PERCENT = 5
DEATH_MAX_PERCENT = 25

def main():
    """Run the population simulation and print each year's result."""
    print("Welcome to the Gopher Population Simulator!")
    population = STARTING_POPULATION
    print(f"Starting population: {population}")
    for year in range(1, YEARS + 1):
        print(f"Year {year}")
        births = percentage_of(population, randint(BIRTH_MIN_PERCENT, BIRTH_MAX_PERCENT))
        deaths = percentage_of(population, randint(DEATH_MIN_PERCENT, DEATH_MAX_PERCENT))
        population = population + births - deaths
        print(f"{births} gophers were born. {deaths} died.")
        print(f"Population: {population}")

def percentage_of(base: int, percent: int) -> int:
    """Return an integer that is `percent` % of base."""
    return int(base * percent / 100)

if __name__ == "__main__":
    main()
