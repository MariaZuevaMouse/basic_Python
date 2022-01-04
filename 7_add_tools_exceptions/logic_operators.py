#       Приведение типов к bool в Python
# Все встроенные типы данных в Python приводятся к
# логическому типу bool по определенным правилам:
#    -   Истина: ‘abc’, [1], (1,), {1:’a’}, 10, 1.1, ...
#    -   Ложь: ‘’, [], (), {}, 0, None, ...

#       Стиль записи логических выражений
# Из-за данного преобразования типов в Python желательно использовать
# лаконичный стиль записи логических выражений:
#  - Вместо if len(str_var) > 0: ...
#  - Пишем: if str_var: ...
# Это ускоряет разработку и делает код более читаемым.

#       Как работает and
# Оператор and не проверяет следующее логическое выражение если текущее False (ленивый).
# Оператор and возвращает первый ложный элемент или последний истинный.

#       Как работает or
# Оператор or не проверяет следующее логическое выражение если текущее True (ленивый).
# Оператор or возвращает первый истинный элемент или последний ложный.

s = 'abc'

# classic approach
if len(s) != 0:
    print('String is not empty')
else:
    print('String is empty')

# python useful syntax
if s:
    print('String is not empty')
else:
    print('String is empty')
# ----------------------------------
list = [1, 2, 3]
dict = {1: 'a'}

# classic
if len(list) != 0 and len(dict) != 0:
    print('List and dictionary are not empty')
else:
    print('List and dictionary are empty')

# python approach
if list and dict:
    print('List and dictionary are not empty')
else:
    print('List and dictionary are empty')

# ____________________________________________________
import math

if 1 > 2 and math.sqrt(-1):
    print('Ошибки не будет так как первое условие ложь')
print('Двигаемся дальше')

# вернется первая ложь
false = [1] and [] and '' and 1
print(false)
print([1] and [] and '' and 1)

# вернется последняя истина
print([1] and 1 and 20 and 1.1)

# ________________
if 2 > 1 or math.sqrt(-1):
    print('Ошибки не будет так как первое условие истина')

# вернется первая истина
print(0 or [] or 8 or 5)

# вернется последняя ложь
print(0 or [] or () or {})

# example: and: извлечение квадратного корня из отрицательного числа
import math

numbers = [4, 1, 2, 3, -4, -2, 7, 16]

result = []

# usual method
for number in numbers:
    if number > 0:
        sqrt = math.sqrt(number)
        if sqrt < 2:
            result.append(number)
print(result)

result = []
# through lazy AND
for number in numbers:
    if number > 0 and math.sqrt(number) < 2:
        result.append(number)
print(result)

# through generator
result = [number for number in numbers if number > 0 and math.sqrt(number) < 2]
print(result)


# example: or: сохранение в переменную одного из 2-х значений

# classic method
def add_to_list(input_list=None):
    if input_list is None:
        input_list = []
    input_list.append(2)
    return input_list


result = add_to_list([0, 1])
print(result)

result = add_to_list()
print(result)


# through operator OR
def add_to_list2(input_list=None):
    input_list = input_list or []
    input_list.append(2)
    return  input_list

result = add_to_list2([0, 1])
print(result)

result = add_to_list2()
print(result)


