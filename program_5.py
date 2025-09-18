# There are two kinds of hot dogs sold:  
# Hot Dog ($3.50), Chili Dog ($4.50).  
# Additionally a person can order cheese ($0.50), peppers ($0.75), or grilled onions ($1.00).  
# Also tax is 7%. 
# Write a program the inputs the type of hot dog wanted and optional toppings.  
# The program then displays the hot dog cost, tax and total cost. 

 hotdog_type = input('What kind of hot dog would you like:').lower()
if hotdog_type == 'hotdog' or hotdog_type == 'hot dog':
    hotdog_price = float(3.50) 
elif hotdog_type == 'chilidog' or hotdog_type == 'chili dog': 
    hotdog_price = float(4.50) 
cheese = input("Add cheese? (yes/no): ").lower()
if cheese == "yes":
    hotdog_price = hotdog_price + 0.50

peppers = input("Add peppers? (yes/no): ").lower()
if peppers == "yes":
    hotdog_price = hotdog_price + 0.75

onions = input("Add grilled onions? (yes/no): ").lower()
if onions == "yes":
    hotdog_price = hotdog_price + 1.00
tax_amount = float(hotdog_price * 0.07)
hotdog_total_cost = tax_amount + hotdog_price
print('Your subtotal is:' , hotdog_price)
print('Your total is:' , hotdog_total_cost)





