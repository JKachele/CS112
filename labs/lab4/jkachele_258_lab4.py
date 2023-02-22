def calc_years(initial_balance, rate, target):
    balance = initial_balance
    years = 0
    while (balance < target):
        balance += balance * rate
        years += 1

    return years


# years = calc_years(5000, 0.15, 10000)
# print("years: ", years)
