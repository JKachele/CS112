def calculate_balance(withdrawlAmt, initBalance, atmType, location):
    finalBalance = initBalance - withdrawlAmt
    if (location == "Utopia"):
        if (atmType != "NBU"):
            finalBalance -= 10
    else:
        finalBalance -= withdrawlAmt * 0.1

    if (finalBalance < 0):
        finalBalance -= 50

    return finalBalance


# print(calculate_balance(100, 1000, "NBU", "Utopia"))
# print(calculate_balance(100, 1000, "abc", "Utopia"))
# print(calculate_balance(200, 1000, "CDE", "Bangladesh"))
# print(calculate_balance(200, 100, "CDE", "Bangladesh"))
