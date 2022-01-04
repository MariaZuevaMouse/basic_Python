#       json. Основные функции
# dump — сохранение объекта в формате json в файл
# dumps — преобразование объекта в json (в текст)
# load — загрузка объекта из файла
# loads — загрузка объекта из формата json (строки)

import json

friends = [
    {'name': 'Max', 'phones': [123, 345], 'age': 20},
    {'name': 'Leo', 'age': 33}
]

print(type(friends))

json_friends = json.dumps(friends)

print(type(json_friends))
print(json_friends)

friends = json.loads(json_friends)

print(type(friends))
print(friends)


# json to file

with open('friends.json', 'w') as f:
    json_friends = json.dump(friends, f)

with open('friends.json', 'r') as f:
    friends = json.load(f)

