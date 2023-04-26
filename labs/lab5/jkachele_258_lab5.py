def numToLetterGrade(numGrade):
    grade = ""
    if numGrade >= 95:
        grade = "A+"
    elif numGrade >= 91:
        grade = "A"
    elif numGrade >= 80:
        grade = "B+"
    else:
        grade += "F"
    return grade


def calculate_grades(scores):
    grades = []
    total = 0
    for score in scores:
        total += score
        grades += [numToLetterGrade(score)]

    average = total / len(grades)
    grades += [numToLetterGrade(average)]

    return grades


# print(calculate_grades([79, 80, 92, 96]))
# print(calculate_grades([99, 100, 92, 96]))
# print(calculate_grades([80, 80.5, 91.7, 96.9]))
