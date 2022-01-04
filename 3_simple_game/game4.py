
# Добавить в игру уровни сложности.
# Чем выше уровень сложности, тем меньше попыток дается пользователю,
# чтобы угадать число.

import random

number = random.randint(1, 100)
print(number)

count = 0
user_input = None
levels = {1: 10, 2: 5, 3: 3}

level = int(input('выберете уровень сложности от 1 до 3: '))
max_count = levels[level]

while number !=  user_input:
    count +=1
    if count > max_count:
        print('Вы проиграли')
        break
    print(f'Попытка № {count}')
    user_input = int(input('Введите число: '))
    if number < user_input:
        print('Ваше число больше загаданного')
    elif number > user_input:
        print('Ваше число меньше загаданного')

else:  # выполняется если выход происходит по условию, но не выполняется,если по Brake
    print('Победа')