# abs - модуль числа
# min, max - минимальное, максимальное значение
# round - округление числа
# sum - сумма элементов последовательности
# enumerate - нумерация последовательности
#

print(abs(-7))

numbers = [5, 10, 11, 13]
print(max(numbers))
print(min(numbers))

print(round(19.76785, 2))

print(sum(numbers))

winners = ['Mari', 'Karlo', 'Elis']
for number, winner in enumerate(winners, 1):
    print(number, winner)

# ------------------------
# Пользователь вводит 3 числа.
# Найти минимальное из них, максимальное из них,
# их сумму и вывести результат на экран.

numbers = []

for i in range(3):
    number = int(input('Введите число: '))
    numbers.append(number)

print(f'max = {max(numbers)}')
print(f'min = {min(numbers)}')
print(f'sum = {sum(numbers)}')

