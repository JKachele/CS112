def lunch_plan(income):
    """Returns the title of the lunch plan based on income of family"""
    plan_str = ""
    if (income <= 25000):
        plan_str = "Free Lunch"
    elif (income <= 35000):
        plan_str = "Reduced Price Lunch"
    else:
        plan_str = "No Subsidy"
    return plan_str


def calc_cost(price_list):
    """Returns the total price of the list of items
        with tax and luxury tax included"""
    total_price = 0
    for price in price_list:
        tax = price * 0.04
        total_price = total_price + price
        total_price = total_price + tax
        if (price > 100):
            luxury_tax = price * 0.015
            total_price = total_price + luxury_tax

    # Uncomment to round to 2 decimal places
    # total_price = int(total_price * 100) / 100.0
    return total_price


def count_rolls(roll_list):
    """Returns the numbers of rolls in the given list to reach 50"""
    rolls = 0
    count = 0
    while (count < 50):
        count = count + roll_list[rolls]
        rolls = rolls + 1
    return rolls


# print(lunch_plan(21000.00))
# print(lunch_plan(25025.00))
# print(lunch_plan(38000.00))
# print()
# print(calc_cost([74.99]))
# print(calc_cost([100.00, 100.01]))
# print(calc_cost([9.99, 18.75, 33.50, 209.00]))
# print()
# print(count_rolls([6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]))
# print(count_rolls([6, 5, 6, 3, 3, 1, 5, 3, 5, 5, 5, 2, 1, 1, 4, 5, 6]))
# print(count_rolls([6, 5, 2, 3, 3, 3, 5, 2, 5, 6, 5, 1, 1, 1, 4, 5, 6]))
