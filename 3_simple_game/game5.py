# Добавить в игру выбор количества пользователей.
# Добавить возможность ввода имен пользователей.
# Добавить систему поочередного хода.
# Добавить объявление победителя.

import random

number = random.randint(1, 100)
print(number)

count = 0
user_input = None
levels = {1: 10, 2: 5, 3: 3}

level = int(input('выберете уровень сложности от 1 до 3: '))
max_count = levels[level]

user_count = int(input('Введите количество пользователей: '))
users = []

for i in range(user_count):
    user_index = i+1
    user_name = input(f'Введите имя пользователя {user_index}: ')
    users.append(user_name)

print('users: ', users)

is_winner = False
winner_name = None
while not is_winner:
    count +=1
    if count > max_count:
        print('Все пользователи проиграли')
        break
    print(f'Попытка № {count}')
    for user in users:
        print(f'Ход пользователя {user}')
        user_input = int(input('Введите число: '))
        if user_input == number:
            is_winner = True
            winner_name = user
            break
        if number < user_input:
            print('Ваше число больше загаданного')
        elif number > user_input:
            print('Ваше число меньше загаданного')

else:  # выполняется если выход происходит по условию, но не выполняется,если по Brake
    print(f'Победа! Победитель {winner_name}')



