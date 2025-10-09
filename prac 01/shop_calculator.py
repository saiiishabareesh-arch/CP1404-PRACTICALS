"""
Ask for the number of items, then each price;
sum total; apply 10% discount if total > $100.
"""

number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))

total_price = 0
for i in range(number_of_items):
    price = float(input("Price of item: "))
    total_price += price

if total_price > 100:
    total_price *= 0.9

print(f"Total price for {number_of_items} items is ${total_price:.2f}")

# Pseudocode:
# get number_of_items
# while number_of_items < 0
#     display "Invalid number of items!"
#     get number_of_items
# total_price = 0
# for each item in number_of_items
#     get price
#     add price to total_price
# if total_price > 100
#     total_price = total_price * 0.9
# display "Total price for n items is $<total_price>"
