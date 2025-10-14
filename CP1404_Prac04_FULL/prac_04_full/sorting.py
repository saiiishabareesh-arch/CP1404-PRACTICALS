"""
CP1404/CP5632 Practical
Demo of sorting lists of 'compound' values
"""
from operator import itemgetter

names_with_ages = [['Derek', 7], ['Carrie', 8], ['Bob', 6], ['Aaron', 9]]

# Sort by the first value (name)
names_with_ages.sort()
print(names_with_ages)

# Sort by the second value (age)
names_with_ages.sort(key=itemgetter(1))
print(names_with_ages)

data = [['Derek', 7], ['Carrie', 7], ['Bob', 6], ['Aaron', 6]]
# Sort by age then name
data.sort(key=itemgetter(1, 0))
print(data)

# The following items are in the form: id, first name, last name, age
# TODO: sort the following list of tuples by last name then first name
items = [
    ('123', 'Derek', 'Smith', 7),
    ('124', 'Carrie', 'Brown', 7),
    ('125', 'Bob', 'Smith', 6),
    ('126', 'Aaron', 'Hewitt', 6)
]

# Sort by last name (index 2) then first name (index 1)
items.sort(key=itemgetter(2, 1))
print(items)