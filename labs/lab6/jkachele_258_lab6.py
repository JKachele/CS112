def trace(matrix):
    traceValue = 0
    matrixY = len(matrix)
    matrixX = len(matrix[0])
    for i in range(matrixX if matrixX <= matrixY else matrixY):
        traceValue += matrix[i][i]
    return traceValue


"""
Explinaion: There is no need to check if the matrix is square.
    If it isnt square, just conting the diagonal until it reaches the end of
    is the same as padding the matrix with zeros to make it square.
    So, the program just loops through the square indices
    until it reaches the smaller dimension
    ("matrixX if matrixX <= matrixY else matrixY" selects the minimum
    of the 2 numbers)
"""

# print(trace([[2, 4], [4, 6]]))
# print(trace([[6, 2, 3], [5, 6, 7], [8, 9, 5]]))
# print(trace([[2, 6, 10, 9], [9, 11, 0, 39], [35, 22, 1, 21]]))
# print(trace([[2, 6, 10, 9], [9, 11, 0, 39],
#             [35, 22, 1, 21], [32, 15, 76, 9]]))
