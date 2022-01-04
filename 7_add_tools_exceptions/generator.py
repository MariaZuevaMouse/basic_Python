#       Определение
#  - В Python существует специальная синтаксическая конструкция,
# которая позволяет по определенным правилам создавать заполненные списки.
# Такие конструкции называются генераторами списков.
#  - Генераторы словарей можно определить по аналогии.
#       Синтаксис
# [ number for number in numbers if number > 0 ]
#       Преимущества
#  - компактный и читаемый код
#  - скорость
#       Недостатки
#  - Нельзя заменить очень сложные конструкции.
#  - При неправильном использовании могут ухудшить читаемость.

# выбрть из списка только положительные числа  !!!list generator
numbers = [1, 2, 3, 4, 5, -1, -8, -7]
result = []

# classic \
for number in numbers:
    if number >= 0:
        result.append(number)

print(result)

# through function filter
result = filter(lambda number: number >= 0, numbers)
print(list(result))

# through list generator
result = [number for number in numbers if number >= 0]
print(result)

# !!! dictionary generator
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]

# classic method
result = {}
for pair in pairs:
    key = pair[0]
    val = pair[1]
    result[key] = val

print(result)
# through dict generator
result = {pair[0]: pair[1] for pair in pairs}
print(result)

# Создать список из случайных чисел от 1 до 100.
import random

numbers = [random.randint(1, 100) for i in range(10)]
print(numbers)

# Создать список квадратов чисел.
numbers = [1, 2, 3, -4]

numbers = [number ** 2 for number in numbers]
print(numbers)

# Создать список имен на букву А.
names = ['Руслан', 'Дмитрий', 'Алексей', 'Андрей']

names = [name for name in names if name.startswith('А')]
print(names)
