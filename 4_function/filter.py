# фильтрация последовательности
# filter(function, iterable)
# аргументы: функция фильтрации, последовательность

numbers = (1, 3, 4, 77, 6, 4, 5, 8)


def is_even(number):
    return number % 2 == 0


result = filter(is_even, numbers)
print(result)

result = list(result)
print(result)

names = ['Max', 'Alex', 'Kate', 'Leo']
print(list(filter(lambda x: len(x) > 3, names)))
