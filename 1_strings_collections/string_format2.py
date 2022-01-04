name = 'Leo'
age = 30
# 1. concat
hello_str = 'Привет, ' + name + ' тебе ' + str(age) + ' лет'
print(hello_str)
# 2. %
hello_str = 'Привет %s тебе %d лет '%(name, age)
print(hello_str)
# 3. format
hello_str = 'Привет {} тебе {} лет'.format(name, age)
print(hello_str)

# --------------
top5 = 'Первые пять мест на соревнованиях: 1. Иванов 2.Петров 3. Сидоров 4.Орлов 5. Соколов'
# Поздравляем 1. Иванов 2.Петров 3. Сидоров  с успехом!
start = top5.find('1')
end = top5.find('4')

top3 = top5[start:end]
print('top3', top3)
result = 'Поздравляем {}  с успехом!'.format(top3.upper())
print(result)