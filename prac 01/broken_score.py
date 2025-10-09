"""
Read a score and print the result:
Invalid (if <0 or >100)
Excellent (>=90)
Passable (>=50)
Bad (<50)
"""

score = float(input("Enter score: "))
if score < 0 or score > 100:
    print("Invalid score")
elif score >= 90:
    print("Excellent")
elif score >= 50:
    print("Passable")
else:
    print("Bad")

# Pseudocode:
# get score
# if score < 0 or score > 100
#     display "Invalid score"
# else if score >= 90
#     display "Excellent"
# else if score >= 50
#     display "Passable"
# else
#     display "Bad"
