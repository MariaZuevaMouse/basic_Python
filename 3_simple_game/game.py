# Компьютер загадывает случайное число от 1 до 100.
# Пользователю предлагается его угадать.
# Если пользователь угадал, программа сообщает о победе.
# Если пользователь ввел неверно число, программа дает ему подсказку:
# введенное число больше или меньше загаданного.


# Программа загадывает случайное число.
import random

number = random.randint(1, 100)
print(number)

while True:
    user_input = int(input('Введите число: '))

    if number == user_input:
        print('Победа')
        break
    elif number > user_input:
        print('Ваше число меньше загаданного')
    else:
        print('Ваше число больше загаданного')







