
friends =  ['Max', 'Leo', 'Kate']
print(friends)
print(type(friends))
friend = friends[0]
print(friend)
print(type(friend))

#  dict / add age
friend = {
    'name': 'Max',
    'age': 23
}
print(friend)
print(type(friend))

# получение элемента по ключу friend['name']
# Добавление значения friend['has_car'] = False
# Изменение значения friend['has_car'] = True
# удаление значения removr friend['age']
# оператор in 'age' in friend

print(friend['age'])
friend['has_car'] = False
print(friend)

friend['has_car'] = True
print(friend)

del friend['age']
print(friend)

if 'age' in friend:
    print('Есть возраст')

if 'has_car' in friend:
    print('Есть машина')

friend = {
    'name': 'Max',
    'has_car': True,
    'age': 23
}

# по ключам
for key in friend.keys():
    print(key)

for key in friend:
    print('key: ', key)
    print('friend[key]: ',friend[key])

# по значениям
for value in friend.values():
    print(value)

# пары ключ значение
# кортежи
for item in friend.items():
    print(item)

for key, val in friend.items():
    print('key', key)
    print('val', val)


