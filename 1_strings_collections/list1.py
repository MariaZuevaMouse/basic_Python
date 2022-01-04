

some_list = ['hello', 123, True]
print(some_list)

empty_list = []

friends = ['Max', 'Leo', 'Kate']
print(type(friends))  #<class 'list'>

# index begining from 0
print('My friends', friends)
print("Второй друг: ", friends[1])
print("Первый друг с конца: ", friends[-1])

#  sublist
print('friends[1:2]', friends[1:2])
print('friends[:2]', friends[:2])
print('friends[1:]', friends[1:])

# len(friends) - длина списка (сколько в нем элементов)
# friends.append(‘Ron’) - добавление нового элемента
# friends.pop() - удаляем последний элемент и возвращаем его
# friends.clear() - очищаем весь список
# friends.remove(‘Ron’) - удаление объекта из списка
# del friends[0] - удаление элемента по индексу

print('len(friends)', len(friends))

friends.append('Ron')
print(friends)
print('len(friends)', len(friends))

print('friends.pop()',friends.pop())
print(friends)

friends.clear()
print(friends)

friends =  ['Max', 'Leo', 'Kate']
friends.remove('Kate')
print(friends, 'after friends.remove("Kate")')

del friends[0]
print(friends, 'after del friends[0]')
