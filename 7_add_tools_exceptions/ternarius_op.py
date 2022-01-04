#       Определение
# тернарный (ternarius — «тройной») оператор — операция,
# возвращающая свой первый или третий операнд в зависимости от
# значения логического выражения, заданного вторым операндом
#
# результат 1 если выражение_истинно, иначе результат 2

#       Синтаксис
# name = ‘Max’ if is_has_name else ‘Empty’
# number = 1 if is_one else 2
# print(‘Привет’ if is_russian else ‘Hello’)
# в общем виде: результат1 если условие иначе результат2

is_has_name = True
name = 'Max' if is_has_name else 'Empty'
print(name)

is_one = False
number = 1 if is_one else 2
print(number)

is_russian = True
print('Привет' if is_russian else 'Hello')


# ------------- слово -> СлОвО
word = 'слово'

result = []

for i in range(len(word)):
    # if i%2 != 0:
    #     letter = word[i].lower()
    # else:
    #     letter = word[i].upper()
    letter = word[i].lower() if i%2 != 0 else word[i].upper()
    result.append(letter)

result = ''.join(result)
print(result)


# password
password = input('Enter password: ')

print('Вы вошли в систему ' if password =='secret' else 'Вход запрещен')


