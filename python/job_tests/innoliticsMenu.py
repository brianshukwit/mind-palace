# Increase Satisfaction Challenge
# Brian Shukwit | 9/29/2020

# User Inputs
price_range = float(input("What is your budget: $"))
calorie_min = int(input("What is your minimum calorie intake? : "))
calorie_max = int(input("What is your maximum calorie intake? : "))


class MenuClass:
    def __init__(self, item, price, calorie):
        self.item = item
        self.price = price
        self.calorie = calorie


# Innolitics Restaurant Menu List
items = [MenuClass("Bottled Water", 1.00, 0),
         MenuClass("Soda", 1.00, 100),
         MenuClass("Cheese Pizza Slice", 4.00, 700),
         MenuClass("House Salad", 8.50, 100),
         MenuClass("Beef Brisket", 12.50, 400),
         MenuClass("Grilled Shrimp", 15.00, 400)
         ]

# Begin Loop
for i in items:
    how_many = 0
    how_many_price = 0
    how_many_calorie = 0
    total_price = 0
    if price_range >= i.price and calorie_min >= i.calorie <= calorie_max:
        how_many_price = price_range / i.price
        if i.calorie == 0:
            how_many_calorie = calorie_max / 0.1
        else:
            how_many_calorie = calorie_max / i.calorie
        if how_many_price < how_many_calorie:
            how_many = how_many_price
        else:
            how_many = how_many_calorie
        total_price = how_many * i.price

    # Print out Menu Items they can afford with prices
    if how_many == 0:
        print("Sorry, you can't afford " + i.item)
    elif how_many == 1:
        print("You can buy " + str(int(how_many)) + " " + i.item + " for $" + str(float(total_price)))
    else:
        print("You can buy " + str(int(how_many)) + " " + i.item + "s for $" + str(total_price))
