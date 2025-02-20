# Make a list pizza_orders
pizza_orders = ["Margherita", "Pepperoni", "BBQ Chicken", "Vodka", "Hawaiian"]

# Make an empty list finished_pizzas
finished_pizzas = []

# Pizza loop and print
for pizza in pizza_orders:
	print(f"Your {pizza} pie was finished!")
	finished_pizzas.append(pizza)
	
# Finished pizza loop
for pizza in finished_pizzas:
	print(f"The {pizza} pizza was made.")

