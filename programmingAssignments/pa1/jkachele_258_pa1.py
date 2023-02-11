'''
Honor Code Statement
Name: Justin Kachele
Assignment: PA 1
Due Date: February 13, 2023
Honor Code Statement: I received no assistance on this assignment that
violates the ethical guidelines set forth by professor and class syllabus.
'''


def pounds_to_kg(pounds):
    # function to convert lbs to kg
    kg = pounds/2.2046
    return kg


def allCoffeePrice(kgs, price):
    return kgs * price


def addTax(price, tax):
    return price + (price * tax)


def priceForSpecial(aLbs, bLbs, cLbs, aPrice, bPrice, cPrice):
    """Calculates the price for a single order of a special coffee"""
    # Convert the total coffee from lbs to kg
    aKgs = pounds_to_kg(aLbs)
    bKgs = pounds_to_kg(bLbs)
    cKgs = pounds_to_kg(cLbs)
    price = aKgs * aPrice + bKgs * bPrice + cKgs * cPrice
    return addTax(price, 0.1)


# START
print("Welcome to Mael's Calculator")
# Mass is in Kg unless otherwise stated
aLbs = float(input("Total Coffee A Pounds: "))
bLbs = float(input("Total Coffee B Pounds: "))
cLbs = float(input("Total Coffee C Pounds: "))
aPrice = float(input("Coffee A Price/Kg: "))
bPrice = float(input("Coffee B Price/Kg: "))
cPrice = float(input("Coffee C Price/Kg: "))
# Convert the total coffee from lbs to kg
aKgs = pounds_to_kg(aLbs)
bKgs = pounds_to_kg(bLbs)
cKgs = pounds_to_kg(cLbs)
# Calculate the total price for the coffees
aTotal = allCoffeePrice(aKgs, aPrice)
bTotal = allCoffeePrice(bKgs, bPrice)
cTotal = allCoffeePrice(cKgs, cPrice)
total = aTotal + bTotal + cTotal
print("Selling all of Coffee A makes: $", round(aTotal, 2), sep="")
print("Selling all of Coffee B makes: $", round(bTotal, 2), sep="")
print("Selling all of Coffee C makes: $", round(cTotal, 2), sep="")
print("Selling all of the Coffee makes: $", round(total, 2), sep="")

print("***Valentine's Day Special***")
numOrders = int(input("Enter total orders: "))
# Calculate price and ammount of coffee if sold all Red Velvet Mocha
priceForRVM = priceForSpecial(2, 1, 0, aPrice, bPrice, cPrice) * numOrders
priceForRVM = round(priceForRVM, 2)
aForRVM = round(pounds_to_kg(2) * numOrders, 2)
bForRVM = round(pounds_to_kg(1) * numOrders, 2)
# Calculate price and ammount of coffee if sold all Valentine's Day Frapp
priceForVDF = priceForSpecial(0, 2.5, 1.5, aPrice, bPrice, cPrice) * numOrders
priceForVDF = round(priceForVDF, 2)
bForVDF = round(pounds_to_kg(2.5) * numOrders, 2)
cForVDF = round(pounds_to_kg(1.5) * numOrders, 2)
# Calculate price and ammount of coffee if sold all Lover's Spice
priceForLS = priceForSpecial(0.45, 0, 2.16, aPrice, bPrice, cPrice) * numOrders
priceForLS = round(priceForLS, 2)
aForLS = round(pounds_to_kg(0.45) * numOrders, 2)
cForLS = round(pounds_to_kg(2.16) * numOrders, 2)
# calculate packages of cups and any additional cups needed to fill all orders
cupPackages = numOrders // 50
cupAdditional = numOrders % 50

print("Charge $", priceForRVM, " for Red Velvet Mocha", sep="")
print("Need ", aForRVM, "kg of Coffee A and ",
      bForRVM, "kg of Coffee B", sep="")
print("Charge $", priceForVDF, " for Valentine's Day Frapp", sep="")
print("Need ", bForVDF, "kg of Coffee B and ",
      cForVDF, "kg of Coffee C", sep="")
print("Charge $", priceForLS, " for Lover's Spice", sep="")
print("Need ", aForLS, "kg of Coffee A and ",
      cForLS, "kg of Coffee C", sep="")
print("Need", cupPackages, "packages of cups and",
      cupAdditional, "additional cup(s)")
