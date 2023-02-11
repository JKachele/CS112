'''
Honor Code Statement
Name: Justin Kachele
Assignment: PA 1
Due Date: February 13, 2023
Honor Code Statement: I received no assistance on this assignment that
violates the ethical guidelines set forth by professor and class syllabus.

Comments and Assumptions:

NOTE:  width of source code should be <=80 characters to be readable on-screen.
12345678901234567890123456789012345678901234567890123456789012345678901234567890
'''


def pounds_to_kg(pounds):
    # function to convert lbs to kg
    kg = pounds/2.2046
    return kg


# START
print("Welcome to Mael's Calculator")
# Mass is in Kg unless otherwise stated
aLbs = float(input("Total Coffee A Pounds: "))
bLbs = float(input("Total Coffee B Pounds: "))
cLbs = float(input("Total Coffee C Pounds: "))
aPrice = float(input("Coffee A Price/Kg: "))
bPrice = float(input("Coffee B Price/Kg: "))
cPrice = float(input("Coffee C Price/Kg: "))
aAmmount = pounds_to_kg(aLbs)
bAmmount = pounds_to_kg(bLbs)
cAmmount = pounds_to_kg(cLbs)
