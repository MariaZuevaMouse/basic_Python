friend = 'Mari'

# type str
print(friend)
print(type(friend))

friend = "Mari"
print(type(friend))

say = 'say "Hello"'
print(say)
say = "say 'Hello'"
print(say)

first_letter = friend[0]
print("Первая буква имени друга: ", first_letter)
print("Тип для одного символа слова", type(first_letter))

# indexing can be from the end of world e.g [-1]
print("Последняя буква имени друга: ", friend[-1])

#  substrings / first index included / last is not included to substring
print(friend[1:3])
print(friend[:2])
print(friend[1:])
print("substring friend[0:4] :", friend[0:4])
print(type(friend[1:3]))

# functions
# length
friends = "Максим Леонид"
print(friends)
print('длина строки: ', len(friends))

# friend.find('a') look fo the symbol  - >return index
print("индекс подстроки 'Лео'", friends.find('Лео'))

print("friends.split()", friends.split())
friends = "Максим;Леонид"
print("friends.split(';')", friends.split(';'))

number = '123'
print("number = ", number, "number.isdigit()", number.isdigit())

print('friends.upper()', friends.upper())
print('friends.lower()', friends.lower())

