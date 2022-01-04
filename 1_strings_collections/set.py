
cities = ['Las Vegas', 'Paris', 'Spb', 'Paris', 'Spb']

print(type(cities))
print(cities)

cities = set(cities)
print(type(cities))
print(cities)

# declare
cities = {'Las Vegas', 'Paris', 'Spb', 'Paris', 'Spb'}
print(cities)

# Добавление элемента cities.add('Burma')
# удалеие элемента cities.remove('Spb')
# длина множества len
# оператор in, цикл for
# работа с несколькими множествами(обединение, пересечение, и тд)

cities.add('Burma')
print(cities)
cities.add('Spb')
print(cities)
print(len(cities))

print('Paris' in cities)

for city in cities:
    print(city)

# Обединение |
# Пересечение &
# разность (вычитание) -

max_things = {'Телефон', 'Бритва', 'Рубашка', 'Шорты'}
kate_thins = {'Телефон', 'Шорты', 'Зонтик', 'Помада'}

# все вещи
print(max_things | kate_thins)

# повторяющиеся вещи
print(max_things & kate_thins)

# уникальные в max_things
print(max_things -kate_thins)

# уникальные в kate_thins
print(kate_thins - max_things)