# a. count in 10s from 0 to 100
for i in range(0, 101, 10):
    print(i, end=" ")
print()

# b. count down from 20 to 1
for i in range(20, 0, -1):
    print(i, end=" ")
print()

# c. print a number of stars
number_of_stars = int(input("Number of stars: "))
print("*" * number_of_stars)

# d. print lines of increasing stars
n = int(input("Number of lines: "))
for i in range(1, n + 1):
    print("*" * i)

# Pseudocode:

# a.
# for i from 0 to 100 step 10
#     display i

# b.
# for i from 20 down to 1 step -1
#     display i

# c.
# get number_of_stars
# display "*" repeated number_of_stars times

# d.
# get number_of_lines
# for i from 1 to number_of_lines
#     display "*" repeated i times
