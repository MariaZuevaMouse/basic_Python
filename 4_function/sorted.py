numbers = [1, 4, 54, 55, 66, 72, 1, 4, 3]
print(sorted(numbers))

print(sorted(numbers, reverse=True))

names = ['Max', 'Alex', 'KAte']
print(sorted(names))

cities = [('Млсква', 1000), ('Лас-Вегас', 1500), ('Амстердам', 2000)]
print(sorted(cities))


def by_count(city):
    return city[1]


print(sorted(cities, key=by_count))

print(sorted(cities, key=lambda city: city[1]))
