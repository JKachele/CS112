def getBMI(inputPath, outputPath):
    input = open(inputPath, 'r').readlines()
    output = open(outputPath, 'w')

    input.pop(0)    # Remove first element from list (titles)

    for lineStr in input:
        line = lineStr.split(',')   # Split line into list by commas
        outStr = line[0] + ": "

        # Calculate BMI
        height = float(line[2])
        weight = float(line[3])
        bmi = weight / (height ** 2)

        # Round and format to 2 decimal places
        bmi = (int(round(bmi, 2) * 100)) / 100

        outStr += str(bmi) + "\n"
        output.write(outStr)

    output.close


# getBMI("input1.csv", "output1.txt")
# getBMI("input2.csv", "output2.txt")
# getBMI("input3.csv", "output3.txt")
