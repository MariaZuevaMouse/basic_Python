# 1. В этой игре человек загадывает число, а компьютер пытается его угадать.
# В начале игры человек загадывает число от 1 до 100 в уме или
# записывает его на листок бумаги. Компьютер начинает его отгадывать
# предлагая игроку варианты чисел. Если компьютер угадал число,
# игрок выбирает “победа”. Если компьютер назвал число меньше загаданного,
# игрок должен выбрать “загаданное число больше”.
# Если компьютер назвал число больше, игрок должен выбрать “загаданное число меньше”.
# Игра продолжается до тех пор пока компьютер не отгадает число.
# Пример игры:
# Допустим, пользователь загадал число 42
#
#     Примечание: Знаки “=”, “>” и “<” пользователь вводит с клавиатуры
#     для общения с компьютером.
#     Вы можете использовать этот способ или придумать свой.

import random

min_number = 1
max_number = 100
result = None

while result != '=':
    number = random.randint(min_number, max_number)
    print(number)
    result = input('Выберете результат испрользуя знаки: \n  '
                   ' =  - загаданное число угадано, \n'
                   ' >  - загаданное число больше преположения компьютера, \n'
                   ' <  - загаданное число меньше предположения компьютера:   ')
    if result == '>':
        min_number = number + 1
    elif result == '<':
        max_number = number -1

print('Победа')