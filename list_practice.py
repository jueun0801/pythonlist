# two separate list of toppings and prices:
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
prices = [2, 6, 1, 3, 2, 7, 2]

#count how many 2 dollar slices there are
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)
#how many toppings there are
num_pizzas = len(toppings)
#same outputs
print("we sell",num_pizzas, "different kinds of pizza!")
print("we sell " + str(num_pizzas) + " different kinds of pizza!")

#2D List of toppings and prices combined
pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausages"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]
#sort to ascending by price
pizza_and_prices.sort()
print(pizza_and_prices)
#first pizza on sorted list is cheapest
cheapest_pizza = pizza_and_prices[0]
print(cheapest_pizza)
#last pizza on sorted list is cheapest
priciest_pizza = pizza_and_prices[-1]
print(priciest_pizza)

#remove a pizza from list 
sold_pizza = pizza_and_prices.pop()
print(sold_pizza)

#insert new pizza by index to keep it sorted
pizza_and_prices.insert(4, [2.5, "peppers"] )
print(pizza_and_prices)

#print the cheapest pizzas, first three list items
three_cheapest = pizza_and_prices[:3]
print(three_cheapest)