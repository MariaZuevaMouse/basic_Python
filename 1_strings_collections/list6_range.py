#  simple
winners =  ['Max', 'Leo', 'Kate']
for winner in winners:
    print(winner)
#  simple
numbers = [1, 3, 5]
for number in numbers:
    print(number)

#  range
numbers = range(10)
print(numbers)
print(type(numbers))

print(list(numbers))


# use range
for i in range(len(winners)):
    # print(i)
    print(i+1, ')',winners[i])

# range params
# range(start_or_stop, stop[, step])
# start_or_stop - начало или конец последовательности
# stop - конец
# step - шаг

numbers = [1, 3, 5]

print(list(range(1, 100, 2)))

for number in range(1, 100, 2):
    print(number)

winners =  ['Max', 'Leo', 'Kate']
for i in range(1, len(winners) +1):
    print(i, ')', winners[i-1])

# for vs range vs while
# for  - перебор последовательности. Индекс не нужен
# for range  - перебор последовательностию. Индекс нужен
# for range - необходимо пропустить некоторые элементы последовательности
#           или идти  с конца в начало
# while  - цикл связан с условием, но не с последовательностью
