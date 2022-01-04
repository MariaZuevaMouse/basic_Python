# применение функции к каждому элементу последовательности
# map(func, iterable, ...)
# аргументы: функция, последовательность
#
numbers = [5, 6, 7, 3, 4, 8]
print(list(map(lambda x: x**2, numbers)))

print(list(map(lambda x: str(x), numbers)))
