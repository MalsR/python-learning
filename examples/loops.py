# basic iterating a list and adding up values
list_prices = [2, 2.55, 3.75, 9.99]
total_price = 0
for price in list_prices:
    print(price)
    total_price += price
print("Average price", total_price/len(list_prices))

# dynamically creates a list containing 10 items under the hood for iteration
for number in range(10):
    print(number)

# another example of range with a start value, stop and step (print every other year)
for number in range(2005, 2016, 2):
    print("The year ", number)
