def calculate_hypotenuse(a, b):
    cSquared = a ** 2 + b ** 2
    c = cSquared ** 0.5
    return c


print("Hypoenuse Calculator!")
a = float(input("Input the lengthe of leg a of the right triangle: "))
b = float(input("Input the lengthe of leg b of the right triangle: "))
print("The length of the hypotenuse is:", calculate_hypotenuse(a, b))
