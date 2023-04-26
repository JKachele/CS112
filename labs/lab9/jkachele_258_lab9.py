def sum_even_numbers(numbers):
    # return 0 if the list is empty (exit condition)
    if (len(numbers) == 0):
        return 0
    if (numbers[0] % 2 == 0):
        number = numbers.pop(0)
        return (number + sum_even_numbers(numbers))
    else:
        numbers.pop(0)
        return sum_even_numbers(numbers)


# print(sum_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
# print(sum_even_numbers([12, 31, 22, 41, 142, 551, 768]))
