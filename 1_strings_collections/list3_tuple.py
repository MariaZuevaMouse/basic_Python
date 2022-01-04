# Кортеж (tuple)
# список, который нельзя изменять
# записывается в круглых скобках
# roles = (‘user’, ‘manager’, ‘admin’)
# служит для защиты от изменений


# Программа winners, интерактивное награждение победителей соревнований по Python
print('Соревнование по Python')
count = int (input('Введите количество участников: '))
i = count
members = []
while i > 0:
    name = input('Кто занял {} место: '.format(i))
    members.append(name)
    i-=1
print('В соревновании участвовали: ', sorted(members))
# мы записывали с конца
members.reverse()


winners = members[:3]
result = 'Победители: {}. Поздравляем!'.format(winners)
print(result)

