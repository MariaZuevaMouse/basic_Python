from random import randint, choice, sample, shuffle

# 1. загадать случайное число от 0 до 100
print(randint(0, 100))

# 2. выбрать победителя из списка players
players = ['Kate', 'Leo', 'Karlo', 'Bill', 'Ron']
print(choice(players))

# 3. выбрать 3-x победителей из списка
print(sample(players, 3))

# 4. перемешать карты в стопке
cards =['1', '2', '3', '4', '5', '6']
print(cards)
shuffle(cards)
print(cards)
# randint - целое случайное число от A до B
# choice - случайный элемент последовательности
# shuffle - перемешивает последовательность
# random - случайное число от 0 до 1
# sample - список длиной k из последовательности ...