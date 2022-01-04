def my_filter(numbers, funcion):
    res = []
    for number in numbers:
        if funcion(number):
            res.append(number)
    return res


def is_even(number):
    return number % 2 == 0


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(my_filter(numbers, is_even))

print(my_filter(numbers, lambda number: number % 2 == 0))

print(my_filter(numbers, lambda number: number % 2 != 0))

print(my_filter(numbers, lambda number: number > 4))
