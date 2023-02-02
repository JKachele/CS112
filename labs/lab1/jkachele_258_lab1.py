freq = float(input("Enter the frequency in GHz "))
lambdaIn = 3E8 / freq
Gt = 4
Gr = 1
Pt = 1
R = 100
lambdaSquared = lambdaIn ** 2
power = (Pt * Gt * Gr * lambdaSquared) / ((4 * 3.14 * R) ** 2)

print("The received power is", str(power), "Watt")
